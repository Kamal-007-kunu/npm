import os

class Config:
    DEBUG = True
    ENV = os.getenv('FLASK_ENV', 'development')
    SECRET_KEY = os.getenv('SECRET_KEY', 'devkey')

