from models import User, Show, UserShow
from config import app, db, api

@app.route('/')
def index():
    return '<h1>Phase 5 project</h1>'