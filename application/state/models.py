from datetime import datetime

from application import *


class ViState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    general_health = db.Column(db.String(256), nullable=False)
    mood = db.Column(db.String(256))
    happened_at = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<ViState {0} {1} C>'.format(self.happened_at, self.temperature)
