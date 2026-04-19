from fastapi import FastAPI

from app.routes import bookmarks, health, tags

app = FastAPI(title="Bookmarks API", version="0.1.0")

app.include_router(health.router)
app.include_router(bookmarks.router, prefix="/bookmarks", tags=["bookmarks"])
app.include_router(tags.router, prefix="/tags", tags=["tags"])
