from sqlalchemy.orm import Session
from backend.db.models import User
from backend.schemas.user import SignUpModel
import datetime, uuid
from backend.db.hashing import Hasher


def list_users(db : Session):
    users = db.query(User).all()
    return users


def create_user(user: SignUpModel, db: Session):
    user_date = str(datetime.datetime.now())
    user_id   = str(uuid.uuid1())
    user_object = User(
        id = user_id,
        username   = user.username,
        password   = Hasher.get_password_hash(user.password),
        email      = user.email,
        first_name = user.first_name,
        gender     = user.gender,
        create_at  = user_date,
        is_staff   = user.is_staff,
    )
    db.add(user_object)
    db.commit()
    db.refresh(user_object)
    return user_object