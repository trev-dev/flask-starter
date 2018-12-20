import os


class BaseConfig:
    DEBUG = os.getenv('FLASK_DEBUG', False)
    STATIC_PATH = '/static'
    STATIC_FOLDER = 'static'
    TEMPLATE_FOLDER = 'views'


class DevConfig(BaseConfig):
    DEBUG = os.getenv('FLASK_DEBUG', True)


class ProdConfig(BaseConfig):
    DEBUG = os.getenv('FLASK_DEBUG', False)
