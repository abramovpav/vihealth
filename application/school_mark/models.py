from datetime import datetime

from application import db


class SchoolMark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mark = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(100))
    happened_at = db.Column(db.Date, nullable=False)
    notes = db.Column(db.String(512))
    state_id = db.Column(db.Integer, db.ForeignKey('vi_state.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<SchoolMark {0} {1}>'.format(self.mark, self.happened_at)
