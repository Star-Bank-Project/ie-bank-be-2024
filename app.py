import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

if os.getenv('ENV') == 'local':
    app.config.from_object('config.LocalConfig')
elif os.getenv('ENV') == 'dev':
    app.config.from_object('config.DevelopmentConfig')
else:
    raise RuntimeError("Invalid or missing ENV variable")

db = SQLAlchemy(app)

# Import your routes and models
from iebank_api import routes, models

if __name__ == '__main__':
    app.run(debug=True)