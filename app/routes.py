from flask import Blueprint 

main_bp = Blueprint('main', __name__) 

@main_bp.route('/') 
def index(): 
    return "<h1>Welcome to the main page!</h1>" 

@main_bp.route('/hello') 
def hello(): 
    return "Hello, World!" 
