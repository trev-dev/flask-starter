import os
from flask import Flask
from flaskr.routes.get import get

# from routes.post import post
# 

def create_app():
    # Check and change the default env if need
    # Instantiate Flask
    app = Flask(
        __name__,
        instance_relative_config=True
    )

    app.config.from_object('flaskr.config')
    print(app.instance_path)

    # Apply GET method routes
    app.register_blueprint(get)
    # app.register_blueprint(post)

    return app

application = create_app()

if __name__ == '__main__':
    application.run()