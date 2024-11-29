import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY")
    if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set. Please set it in your environment.")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")


class LocalConfig(Config):
    # Use SQLite for local development
    SQLALCHEMY_DATABASE_URI = "sqlite:///local.db"
    DEBUG = True


class DevelopmentConfig(Config):
    # Use PostgreSQL for development and UAT
    SQLALCHEMY_DATABASE_URI = "postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}".format(
        dbuser=os.getenv("DBUSER"),
        dbpass=os.getenv("DBPASS"),
        dbhost=os.getenv("DBHOST"),
        dbname=os.getenv("DBNAME"),
    )
    DEBUG = True


class ProductionConfig(Config):
    # Use PostgreSQL or another production database
    SQLALCHEMY_DATABASE_URI = "postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}".format(
        dbuser=os.getenv("DBUSER"),
        dbpass=os.getenv("DBPASS"),
        dbhost=os.getenv("DBHOST"),
        dbname=os.getenv("DBNAME"),
    )
    DEBUG = False


class GithubCIConfig(Config):
    # Use SQLite for testing in GitHub Actions
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"  # Ephemeral database for tests
    DEBUG = True
