from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from extensions import db

#initialize the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite+pysqlite:///project.db"


#initialize the database
db.init_app(app)


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

@app.get("/get_tracks")
def get_tracks():
    message = dobot.get_tracks()
    return message
@app.get('/get_track')
def get_track():
    data = request.get_json()
    message = dobot.get_track(data)
    return message

@app.post("/add_track")
def add_track():
    data = request.get_json()
    message = dobot().add_position(data)
    return message
@app.get("/magnet_on")
def magnet_on():
    return dobot.magnet_on()
@app.get("/magnet_off")
def magnet_off():
    return dobot.magnet_off()
@app.get("/run_track")
def run_track():
    data = request.get_json()
    return dobot.run_track(data)
@app.get("/add_position_dobot")
def add_position_dobot():
    data = request.get_json()
    return dobot().add_position_dobot(data)
@app.delete("/delete_track")
def delete_tracks():
    data = request.get_json()
    return  dobot.delete_track(data)

if __name__ == '__main__':
    app.run(debug=True)