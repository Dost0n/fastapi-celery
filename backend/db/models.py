from sqlalchemy import Column, String,  Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    username = Column(String(25), unique=True)
    password = Column(String(255))
    email = Column(String(80), unique=True)
    first_name = Column(Text, nullable = True)
    is_staff = Column(Boolean, default = False)
    gender = Column(String(1))
    create_at = Column(String(50))

    def __repr__(self):
        return f"<User {self.username}>"