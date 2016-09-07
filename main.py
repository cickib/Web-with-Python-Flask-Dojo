from flask import *
from peewee import *


db = PostgresqlDatabase('flask_dojo', user='cickib')
db.connect()

DEBUG = True


class BaseModel(Model):
    class Meta:
        database = db


class RequestCount(BaseModel):
    count = IntegerField(default=1)


def db_init():
    db.drop_tables([RequestCount], safe=True)
    db.create_tables([RequestCount], safe=True)
    default_count = RequestCount.create()

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello():
    return count_requests()

@app.route('/request-counter')
def count_requests():
    recent = RequestCount.select().get()
    recent.count += 1
    recent.save()
    return "{} view(s)".format(recent.count)


if __name__ == "__main__":
    app.run()
