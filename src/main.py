from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routes import resources

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="DevOpsWiki API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost", "http://35.157.173.174"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resources.router, prefix="/api")