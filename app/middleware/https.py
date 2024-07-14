from base64 import b64encode
from secrets import token_bytes

from app.statistic.dao import StatisticDAO
from app.user.auth import create_access_token
from app.visitor.dao import VisitorDAO


async def set_new_cookie(request, response):
    secret = b64encode(token_bytes(32)).decode()
    access_token = create_access_token({"visitor": secret})

    
    # response.set_cookie("visitor_session", access_token)
    response.headers["visitor"] = access_token

    

    return secret




