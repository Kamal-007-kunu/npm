from flask import Flask
import logging

def create_app():
    app = Flask(__name__)
    
    # Load config
    app.config.from_object('app.config.Config')
    
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Register routes
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app

