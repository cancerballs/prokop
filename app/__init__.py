import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.login import LoginManager
from flask_wtf.csrf import CsrfProtect
from config import basedir
import redis

from flask.ext.restful import Api

from flask import render_template

from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)

CSRF_ENABLED = True

# csrf = CsrfProtect()
# csrf.init_app(app)
#red = redis.Redis("localhost")
bcrypt = Bcrypt(app)
api = Api(app)

app.debug = True

# sqlalchemy, migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

app.config.from_object('config')
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'main.login'
lm.logout_view = 'main.logout'
lm.login_message = u"Please log in to access this page."

# File Uploads
UPLOAD_FOLDER = os.path.join(basedir, 'app/static/uploads/')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

toolbar = DebugToolbarExtension(app)


PROJECT_STATUS = [('1', 'Looking for People'),
                  ('2', 'In Progress'),
                  ('3', 'Finished')]

app.config['PROJECT_STATUS'] = PROJECT_STATUS

from app.main import models, views, api
from app.main.views import main

app.register_blueprint(main, url_prefix='')
