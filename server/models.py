from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, metadata, flask_bcrypt
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

metadata = metadata
db = db

class User ( db.Model, SerializerMixin ):
    __tablename__ = 'user'

class UserShow ( db.Model, SerializerMixin ):
    __tablename__ = 'usershow'

class Show ( db.Model, SerializerMixin ):
    __tablename__ = 'show'