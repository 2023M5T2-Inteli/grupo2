from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy



#initialize the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)

from controller import DobotController as dobot

#engine:[//[user[:password]@][host]/[dbname]]
# engine -> postgresql
# user -> postgres (see `owner` field in previous screenshot)
# password -> password (my db password is the string, `password`)
# host -> localhost (because we are running locally on out machine)
# dbname -> flasksql (this is the name I gave to the db in the previous step)


@app.route('/')
def api():
    return 'Hello World'

@app.post('/add')
def add():
    data = request.get_json()
    message = dobot.add(data)
    return message
       
@app.get('/get')
def get():
    message = dobot.get()
    return message
@app.get('/get_track')
def get_track():
    data = request.get_json()
    message = dobot.get_track(data)
    return message

@app.get('/get_highest_order')
def get_highest_order():
    data = request.get_json()
    message = dobot.get_highest_order(data)
    return message

@app.get("/get_highest_order_track")
def get_highest_order_track():
    
    message = dobot.get_highest_order_track()
    return message
@app.post("/add_track")
def add_track():
    data = request.get_json()
    message = dobot.add_track(data)
    return message
if __name__ == '__main__':
    app.run(debug=True)