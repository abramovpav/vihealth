from sqlalchemy import desc

__all__ = ['vihealth_app', 'db']
import os

from flask import Flask
from flask import render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy



vihealth_app = Flask(__name__)
vihealth_app.config.from_object('config')
db = SQLAlchemy(vihealth_app)
migrate = Migrate(vihealth_app, db)


from application.state.models import ViState
from application.school_mark.models import SchoolMark
@vihealth_app.route('/')
def hello_world():
    print os.path.abspath(os.path.dirname(__file__))
    states = ViState.query.order_by(desc(ViState.happened_at)).all()
    return render_template('index.html', states=states)
