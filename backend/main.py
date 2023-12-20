from fastapi import FastAPI
from backend.core.config import settings
from backend.db.session import engine
from backend.db.models import Base
from backend.routers.base import api_router


def include_router(app):
    app.include_router(api_router, prefix="/api/v1")
    
    
def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app 


app = start_application()
