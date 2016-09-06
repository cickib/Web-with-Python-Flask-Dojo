from flask import *
from peewee import *


db = PostgresqlDatabase('flask_dojo')
db.connect()


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()