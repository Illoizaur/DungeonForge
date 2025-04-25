#тут щось накосячено... вернусь до цього пізніше
from app.services.authService import get_password_hash
from sqlmodel import Session, select
from app.db.database import engine
from app.models.userModel import User
import os
from dotenv import load_dotenv

load_dotenv("./.env")

def seed_admin_user():
    with Session(engine) as session:
        if session.exec(select(User).where(User.is_admin == True)).first():
            print("Адмін вже існує.")
            return

        user = User(
            username=os.getenv("ADMIN_USERNAME", "admin"),
            email=os.getenv("ADMIN_EMAIL", "admin@example.com"),
            password=get_password_hash(os.getenv("ADMIN_PASSWORD", "admin123")),
            is_admin=True
        )
        session.add(user)
        session.commit()
        print("Адміна створено успішно!")

if __name__ == "__main__":
    seed_admin_user()
