from flask import Flask 

def create_app(): 
    app = Flask(__name__) 

    # Import and register the web blueprint
    from .routes.web_routes import web_bp
    app.register_blueprint(web_bp) 
    
    # Import and register the API blueprint with a URL prefix
    from .routes.api_routes import api_bp
    app.register_blueprint(api_bp, url_prefix="/api") 

    return app 
