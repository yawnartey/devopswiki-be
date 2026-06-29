from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine
import models
from routes import resources
from scheduler import scheduler

@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    scheduler.start()
    yield
    scheduler.shutdown()

app = FastAPI(
    title="DevOpsWiki API",
    description="REST API for searching and managing DevOps learning resources",
    version="1.0.0",
    lifespan=lifespan,
)
app.include_router(resources.router, prefix="/api")
