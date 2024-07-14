from datetime import date, datetime
from fastapi import APIRouter, Response, Request
from fastapi_cache.decorator import cache
from jose import jwt, JWTError
from urllib3 import request
import pytz
from app.config import settings
from app.middleware.https import set_new_cookie
from app.statistic.dao import StatisticDAO
from app.visitor.dao import VisitorDAO

router = APIRouter(
    prefix="/statistics",
    tags=["Статистика"]
)


@router.get("/daily/{date}")
#@cache(expire=30)
async def get_daily_statistic(request: Request, response: Response, date: date):
    japan_timezone = pytz.timezone('Asia/Tokyo')

    date_str_as_string = date.strftime("%Y-%m-%d")
    target_date = japan_timezone.localize(datetime.strptime(date_str_as_string, "%Y-%m-%d"))
    current_date_japan = datetime.now(japan_timezone)

    if current_date_japan < target_date:
        return {"detail": "Такая дата еще не наступила"}

    result = await StatisticDAO.get_statistic_by_day(statistic_date=date)

    cookie = request.headers.get("visitor")
    
    if not cookie:
        secret = await set_new_cookie(request, response)
        
        await VisitorDAO.add_record(ip_address=request.client.host, cookie=secret)
        if request.headers.get("Origin") == "https://ai-softdev.com":
            result = await StatisticDAO.update_count(date=date)
    else:
        
        try:
            payload = jwt.decode(cookie, settings.KEY, settings.ALGORITHM)
            
        except:
            
            await set_new_cookie(request, response)
            result = await StatisticDAO.update_count(date=date)
            return result

        expire: str = payload.get("exp")
        
        if not expire or int(expire) < datetime.utcnow().timestamp():
            await set_new_cookie(request, response)
            
            result = await StatisticDAO.update_count(date=date)
        
        visitor_cookie: str = payload.get("visitor")
        if not visitor_cookie:
            
            await set_new_cookie(request, response)

            result = await StatisticDAO.update_count()

        res = await VisitorDAO.find_one_or_none(cookie=visitor_cookie)
        
        if not res:
            
            secret = await set_new_cookie(request, response)
            await VisitorDAO.add_record(ip_address=request.client.host, cookie=secret)
            result = await StatisticDAO.update_count(date=date)
        else:
            response.headers["visitor"] = request.headers.get("visitor")

    
    if not result:
        
        result = await StatisticDAO.update_count(date=date)

    return result
