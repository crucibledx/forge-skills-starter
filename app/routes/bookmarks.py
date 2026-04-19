from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Bookmark, Tag
from app.schemas import BookmarkCreate, BookmarkResponse, BookmarkUpdate

router = APIRouter()


def get_or_create_tags(db: Session, tag_names: list[str]) -> list[Tag]:
    tags = []
    for name in tag_names:
        tag = db.query(Tag).filter(Tag.name == name).first()
        if not tag:
            tag = Tag(name=name)
            db.add(tag)
        tags.append(tag)
    return tags


@router.get("/", response_model=list[BookmarkResponse])
def list_bookmarks(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return db.query(Bookmark).offset(skip).limit(limit).all()


@router.post("/", response_model=BookmarkResponse, status_code=201)
def create_bookmark(payload: BookmarkCreate, db: Session = Depends(get_db)):
    bookmark = Bookmark(
        url=str(payload.url),
        title=payload.title,
        description=payload.description,
    )
    if payload.tags:
        bookmark.tags = get_or_create_tags(db, payload.tags)
    db.add(bookmark)
    db.commit()
    db.refresh(bookmark)
    return bookmark


@router.get("/search", response_model=list[BookmarkResponse])
def search_bookmarks(q: str, db: Session = Depends(get_db)):
    return (
        db.query(Bookmark)
        .filter(
            Bookmark.title.ilike(f"%{q}%") | Bookmark.description.ilike(f"%{q}%")
        )
        .all()
    )


@router.get("/{bookmark_id}", response_model=BookmarkResponse)
def get_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    bookmark = db.query(Bookmark).filter(Bookmark.id == bookmark_id).first()
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return bookmark


@router.put("/{bookmark_id}", response_model=BookmarkResponse)
def update_bookmark(
    bookmark_id: int, payload: BookmarkUpdate, db: Session = Depends(get_db)
):
    bookmark = db.query(Bookmark).filter(Bookmark.id == bookmark_id).first()
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")

    if payload.url is not None:
        bookmark.url = str(payload.url)
    if payload.title is not None:
        bookmark.title = payload.title
    if payload.description is not None:
        bookmark.description = payload.description
    if payload.tags is not None:
        bookmark.tags = get_or_create_tags(db, payload.tags)

    db.commit()
    db.refresh(bookmark)
    return bookmark


@router.delete("/{bookmark_id}", status_code=204)
def delete_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    bookmark = db.query(Bookmark).filter(Bookmark.id == bookmark_id).first()
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    db.delete(bookmark)
    db.commit()
