import os
import time
from base64 import b64encode
from datetime import datetime
from secrets import token_bytes

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from jose import jwt, ExpiredSignatureError, JWTError
from sqladmin import Admin
from redis import asyncio as aioredis

from starlette.requests import Request

from app.achievement.router import router as router_achievements
from app.admin.auth import authentication_backend
from app.admin.views import *
from app.calculation.router import router as router_calculations
from app.client.router import router as router_clients
from app.company.router import router as router_companies
from app.config import settings
from app.database import engine
from app.direction.router import router as router_directions
from app.employee.router import router as router_employees
from app.feature.router import router as router_features
from app.feedback.router import router as router_feedbacks
from app.lang.router import router as router_langs
from app.link.router import router as router_links
from app.middleware.https import set_new_cookie
from app.project.router import router as router_projects
from app.service.router import router as router_services
from app.technology.router import router as router_technologies
from app.user.router import router as router_users
from app.statistic.router import router as router_statistics
from app.consideration.router import router as router_consideration


from app.visitor.dao import VisitorDAO

app = FastAPI()

app.include_router(router_achievements)
app.include_router(router_calculations)
app.include_router(router_clients)
app.include_router(router_companies)
app.include_router(router_directions)
app.include_router(router_employees)
app.include_router(router_features)
app.include_router(router_feedbacks)
app.include_router(router_langs)
app.include_router(router_links)
app.include_router(router_projects)
app.include_router(router_services)
app.include_router(router_technologies)
app.include_router(router_statistics)
app.include_router(router_consideration)
#app.include_router(router_users)

admin = Admin(app, engine, authentication_backend=authentication_backend,
              base_url="/admin", title="AI Development Generation",
              logo_url="https://api.ai-softdev.com/media/logo_full.svg")


admin.add_view(AchievementsAdmin)
admin.add_view(CalculationsAdmin)
admin.add_view(ClientsAdmin)
admin.add_view(CompaniesAdmin)
admin.add_view(DirectionsAdmin)
admin.add_view(EmployeesAdmin)
admin.add_view(FeaturesAdmin)
admin.add_view(FeedbacksAdmin)
admin.add_view(LangsAdmin)
admin.add_view(LinksAdmin)
admin.add_view(ProjectsAdmin)
admin.add_view(ProjectImageAdmin)
admin.add_view(ServicesAdmin)
admin.add_view(TechnologiesAdmin)
admin.add_view(UserAdmin)
admin.add_view(VisitorAdmin)
admin.add_view(StatisticAdmin)
admin.add_view(ConsiderationAdmin)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.middleware("https")
async def add_count(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    end_time = time.time()
    execution_time = end_time - start_time
    response.headers["X-Response-Time"] = f"{execution_time:.6f} seconds"

    return response


@app.on_event("startup")
async def on_start():
    redis = aioredis.from_url("redis://localhost:6379", encodings="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")



