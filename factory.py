from config import DevConfig, ProdConfig
from flask import Flask
from flask_assets import Environment, Bundle
from routes.get import get
# from routes.post import post

CONFIGS = {'dev': DevConfig, 'prod': ProdConfig}


def create_app(env):
    config = CONFIGS[env]

    # Instantiate Flask
    app = Flask(
                __name__,
                template_folder=config.TEMPLATE_FOLDER,
                static_path=config.STATIC_PATH,
                static_folder=config.STATIC_FOLDER
                )

    app.config.from_object(config)
    assets = Environment(app)
    # JS/CSS bundlers for minification
    js = Bundle('js/site.js', filters='jsmin', output='js/bundle.min.js')
    css = Bundle(
                'css/styles.css',
                filters='cssmin',
                output='css/bundle.min.css'
                )

    assets.register('js_modules', js)
    assets.register('css_modules', css)

    # Apply GET method routes
    app.register_blueprint(get)
    # app.register_blueprint(post)

    return app
