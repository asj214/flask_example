from app import db
from database import BaseModel


class User(db.Model, BaseModel):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(75), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    last_login_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, email={self.email})'


class Banner(db.Model, BaseModel):
    __tablename__ = "banners"

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, nullable=False, default=1)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    desciption = db.Column(db.String(128), nullable=False)
