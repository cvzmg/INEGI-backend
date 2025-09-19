from flask import Flask 

def create_app(): 
    app = Flask(__name__) 

    # Import and register blueprints 
    from . import routes 
    app.register_blueprint(routes.main_bp) 

    return app 
