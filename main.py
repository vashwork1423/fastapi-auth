import uvicorn
from fastapi import FastAPI
from app.api.v1.endpoints import user, auth
from app.db.session import engine
from app.db.base import Base
from app.core.config import settings 

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.on_event("startup")
async def on_startup():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    print(f"Starting server on port {settings.PORT}")
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=True)
