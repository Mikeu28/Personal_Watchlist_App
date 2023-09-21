from models import User, Show, UserShow
from config import app, api, db
from flask_restful import Resource
from flask import make_response, request, session


@app.route('/')
def index():
    return '<h1>Phase 5 project</h1>'

class Users( Resource ):

    def post( self ):
        data = request.json
        the_username = data['username']
        plaintext_password = data['password']
        try:
            new_user = User( username = the_username, password = plaintext_password )
            db.session.add( new_user )
            db.session.commit()
        except:
            raise ValueError( "Something went wrong" )

        return make_response( new_user.to_dict(), 201 )
    
    def get( self ):    
        return make_response( [ m.to_dict() for m in User.query.all() ], 200 )
    
api.add_resource( Users, "/users" )

@app.route ( '/login', method = [ 'POST' ] )
def login():
    data = request.json
    username = data[ 'name' ]
    password = data[ 'password' ]
    user = User.query.filter_by( name = username ).first()

    if not user:
        return make_response( { 'error': 'User was not found' }, 404 )
    
    if not user.authenticate( password ):
        return make_response( { 'error': 'Password incorrect' }, 401 )
    
    session[ 'user_id' ] = user.id
    return make_response( user.to_dict() )


class Shows( Resource ):

    def get( self ):
        return make_response( [ m.to_dict() for m in Show.query.all() ], 200 )
    
api.add_resource( Shows, "/shows" )

class UserShows( Resource ):
    
    def get( self ):
        return make_response( [ m.to_dict() for m in UserShow.query.all() ], 200)

api.add_resource( UserShows, "/usershows")

if __name__ == '__main__':
    app.run( port=5555, debug=True )

