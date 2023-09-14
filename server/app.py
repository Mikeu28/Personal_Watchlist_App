from models import User, Show, UserShow
from config import app, api#, db
from flask_restful import Resource
from flask import make_response#, request

@app.route('/')
def index():
    return '<h1>Phase 5 project</h1>'

class Users( Resource ):
    def get( self ):    
        return make_response( [ m.to_dict() for m in User.query.all() ], 200 )
    
api.add_resource( Users, "/users" )

class Shows( Resource ):

    def get( self ):
        return make_response( [ m.to_dict() for m in Show.query.all() ], 200 )
    
api.add_resource( Shows, "/shows" )