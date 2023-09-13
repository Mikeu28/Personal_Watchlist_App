from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, metadata
#from sqlalchemy.orm import validates
#from sqlalchemy.ext.hybrid import hybrid_property

metadata = metadata
db = db

class User ( db.Model, SerializerMixin ):
    __tablename__ = 'user'

    id = db.Column( db.Integer, primary_key = True )
    username = db.Column( db.String, nullable = False )
    password = db.Column( db.String, nullable = False )

    #Relationships

    user_shows = db.relationship( "UserShow", back_populates = "user", cascade = "all, delete-orphan" )
    shows = association_proxy( "user_shows", "show" )


class UserShow ( db.Model, SerializerMixin ):
    __tablename__ = 'usershow'

    id = db.Column( db.Integer, primary_key = True )
    rating = db.Column( db.Integer, nullable = False)

    #Relationships

    user = db.relationship( "User", back_populates = "user_show" )
    show = db.relationship( "Show", back_populates = "user_show" )

class Show ( db.Model, SerializerMixin ):
    __tablename__ = 'show'

    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String, nullable = False )
    image = db.Column( db.String )
    platform = db.Column( db.String, nullable = False )

    #Relationships

    user_shows = db.relationship( "UserShow", back_populates = "show" )
    users = association_proxy( "user_shows", "user" )
