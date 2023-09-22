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

class Shows( Resource ):

    def get( self ):
        return make_response( [ m.to_dict() for m in Show.query.all() ], 200 )
    
api.add_resource( Shows, "/shows" )

class UserShows( Resource ):
    
    def get( self ):
        return make_response( [ m.to_dict() for m in UserShow.query.all() ], 200)

api.add_resource( UserShows, "/usershows")

@app.route ( '/login', methods = [ 'POST' ] )
def login():
    data = request.json
    username = data[ 'name' ]
    password = data[ 'password' ]
    try:
        user = User.query.filter_by( name = username ).first()
        if user.authenticate( password ):
            session[ 'user_id' ] = user
            response = make_response( user.to_dict(), 200 )
            return response
    except:
        return make_response( { 'error': 'Name or password incorrect' }, 401 )

@app.route( '/authorized', methods = [ 'GET' ] )
def authorized():
    try:
        user = User.query.filter_by( id = session.get( 'user_id' ) ).first()
        response  = make_response( user.to_dict(), 200 )
        return response
    except:
        return make_response( { 'error': "User not found" }, 404 )
    
@app.route( '/logout', methods = [ 'DELETE' ] )
def logout():
    session[ 'user_id' ] = None
    return make_response( '', 204 )



if __name__ == '__main__':
    app.run( port=5555, debug = True )