from fastapi import FastAPI
from app.database import engine, Base
from app.models import user as user_model
from app.routers import auth, roles # Import your new roles router file

# Create SQLite tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Loonlet Auth Assignment")

# Connect all your endpoints to the application
app.include_router(auth.router)
app.include_router(roles.router) # <-- Add this line here!

@app.get("/")
def home():
    return {"message": "Backend server is running smoothly and tables are created!"}