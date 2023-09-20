from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, metadata, flask_bcrypt
from sqlalchemy.orm import validates



metadata = metadata
db = db

class User ( db.Model, SerializerMixin ):
    __tablename__ = 'users'

    id = db.Column( db.Integer, primary_key = True )
    username = db.Column( db.String, nullable = False )
    _password_hash = db.Column( db.String, nullable = False )

    #Relationships

    user_shows = db.relationship( "UserShow", back_populates = "user", cascade = "all, delete-orphan" )
    shows = association_proxy( "user_shows", "show" )

    #Validations

    @property
    def password( self ):
        return self._password_hash

    @password.setter
    def password ( self, new_password_string ):
        byteobject = new_password_string.encode( 'utf-8' )
        encrypted_byteobject = flask_bcrypt.generate_password_hash( byteobject )
        hash_obj = encrypted_byteobject.decode( 'utf-8' )
        self._password_hash = hash_obj

    def authenticate ( self, some_string ):
        return flask_bcrypt.check_password_hash( self._password_hash, some_string.encode( 'utf-8' ) )


    @validates( "username" )
    def validates_username( self, key, new_first_name ):
        if not new_first_name:
            raise ValueError( "A Username must be provided" )
        elif len( new_first_name ) > 20:
            raise ValueError( "A Username must be shorter than 20 characters" )
        else:
            return new_first_name

class UserShow ( db.Model, SerializerMixin ):
    __tablename__ = 'user_shows'

    id = db.Column( db.Integer, primary_key = True )
    rating = db.Column( db.Integer, nullable = False)
    user_id = db.Column( db.Integer, db.ForeignKey( 'users.id' ) )
    show_id = db.Column( db.Integer, db.ForeignKey( 'shows.id' ) )

    #Relationships

    user = db.relationship( "User", back_populates = "user_shows" )
    show = db.relationship( "Show", back_populates = "user_shows" )

    #Validations

    @validates( "rating" )
    def validates_rating( self, key, new_rating ):
        if 1 <= new_rating <= 10:
            return new_rating
        else:
            raise ValueError( "Rating must be between 1 and 10!" )

class Show ( db.Model, SerializerMixin ):
    __tablename__ = 'shows'

    serialize_rules = ( '-user_shows', )

    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String, nullable = False )
    image = db.Column( db.String )
    platform = db.Column( db.String, nullable = False )

    #Relationships

    user_shows = db.relationship( "UserShow", back_populates = "show" )
    users = association_proxy( "user_shows", "user" )

    #Validations

    @validates( "name" )
    def validates_name( self, key, new_name ):
        if not new_name:
            raise ValueError( "A name must be provided" )
        elif len( new_name ) > 60:
            raise ValueError("A name must be shorter than 60 characters")
        else: 
            return new_name