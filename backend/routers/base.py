from fastapi import APIRouter
from backend.routers import user_route, login_route

api_router = APIRouter()


api_router.include_router(user_route.router,  prefix="/auth",tags=["auths"])
api_router.include_router(login_route.router,  prefix="/login",tags=["login"])