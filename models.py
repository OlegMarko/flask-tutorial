import datetime, re
from app import db


def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()


class Entry(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    slug = db.Column(db.String(100), unique=True)
    body = db.Column(db.Text)
    create_timestamp = db.Column(db.DateTime, default=datetime.datetime.now())
    modify_timestamp = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now())

    def __init__(self, *args, **kwargs):
        super(Entry, self).__init__(*args, **kwargs)
        self.generate_slug

    def generate_slug(self):
        self.slug = ''
        if self.title:
            self.slug = slugify(self.title)

    def __str__(self):
        return 'Entry: %s>' % self.title
