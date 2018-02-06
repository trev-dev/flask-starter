from flask import Flask
from flask_assets import Environment, Bundle
from routes.get import get

# Instantiate Flask
app = Flask(
    __name__,
    static_folder='static',
    static_path='/static',
    template_folder='views'
)

# Apply configurations
app.config.from_pyfile('site.cfg')
assets = Environment(app)

#JS/CSS bundlers for minification
js = Bundle('js/site.js', filters='jsmin', output='js/bundle.min.js')
css = Bundle('css/styles.css', filters='cssmin', output='css/bundle.min.css')

assets.register('js_modules', js)
assets.register('css_modules', css)

# Apply GET method routes
app.register_blueprint(get)

# Run application
if __name__ == '__main__':
  app.run()
