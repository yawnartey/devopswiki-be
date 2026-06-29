from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_, String, cast
from sqlalchemy.dialects.postgresql import ARRAY
from typing import List, Optional
from database import get_db
import models, schema

router = APIRouter()

# Search for a resource
@router.get("/search", response_model=List[schema.ResourceOut])
def search_resources(
    q:   Optional[str] = Query(None, description="Search by keyword. Matches title and description"),
    tag: Optional[str] = Query(None, description="Filter by tag e.g. docker, kubernetes, terraform"),
    db:  Session = Depends(get_db)
):
    query = db.query(models.Resource)

    if q:
        query = query.filter(
            or_(
                models.Resource.title.ilike(f"%{q}%"),
                models.Resource.description.ilike(f"%{q}%")
            )
        )
    if tag:
        query = query.filter(models.Resource.tags.op('@>')(cast([tag.lower()], ARRAY(String))))

    return query.limit(20).all()


# post a resource
@router.post("/resources", response_model=schema.ResourceOut)
def create_resource(resource: schema.ResourceCreate, db: Session = Depends(get_db)):
    db_resource = models.Resource(**resource.model_dump())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource