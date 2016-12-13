activate_this = '/home/apps/catalog/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
import warnings
import sys
warnings.filterwarnings("ignore")

sys.path.insert(0, '/home/apps/catalog')

basedir = os.path.abspath(os.path.dirname(__file__))

try:
    from project import config_mysql
    os.environ['DATABASE_URL'] = 'mysql://%s:%s@localhost/%s' % (
        config_mysql.username, config_mysql.password, config_mysql.db)

except ImportError:
    os.environ['DATABASE_URL'] = 'sqlite:///' \
        + os.path.join(basedir, 'project/app.db')

from flup.server.fcgi import WSGIServer

from project import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app('production')
manager = Manager(app)
migrate = Migrate(app, db)

application = app

if __name__ == '__main__':

    application = app
