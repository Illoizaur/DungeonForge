from fastapi import FastAPI

from app.routes.userRoute import router as user_router
from app.routes.adventurerRoute import router as adventurer_router
from app.db.database import init_db
#from app.seed.seed_admin import seed_admin_user

app = FastAPI()

app.include_router(user_router)
app.include_router(adventurer_router)

@app.on_event("startup")
def on_startup():
    init_db()
