from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from extensions import db
import sys




#initialize the app
app = Flask(__name__)
if __name__ == '__main__':
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite+pysqlite:///project.db"
else: 
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite+pysqlite:///../../instance/project.db"


#initialize the database
db.init_app(app)


from controller import DobotController

dobot = ''
port = ""


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
def get_trackss():
    message = dobot.get_tracks()
    return message
@app.get('/get_track')
def get_track():
    data = request.get_json()
    message = dobot.get_track(data)
    return message

@app.post("/add_position")
def add_position():
    data = request.get_json()
    message = dobot().add_position(data)
    return message
@app.get("/magnet_on")
def magnet_on():
    return dobot.magnet_on()
@app.get("/magnet_off")
def magnet_off():
    return dobot().magnet_off()
@app.post("/run_track")
def run_track():
    data = request.get_json()
    return dobot.run_track(data)
@app.get("/add_position_dobot")
def add_position_dobot():
    data = request.get_json()
    return dobot().add_position_dobot(data)
@app.get("/add_position_dobot2")
def add_position_dobot2():
    # data = request.get_json()
    return dobot.add_position_dobot2()
@app.delete("/delete_track")
def delete_tracks():
    data = request.get_json()
    return  dobot.delete_track(data)

@app.post("/add_track")
def add_track():
    data = request.get_json()
    message = dobot.add_track(data["data"])
    return message

@app.get("/home")
def home():
    return dobot.run_home()

@app.post("/change_default_track")
def change_default_track():
    data = request.get_json()
    return dobot.change_default_track(data)

if __name__ == '__main__':

    if sys.argv[1] == "COM1":
        print("porta não selecionada!")
        pass
    else:
        dobotPort = sys.argv[1]
        raspPort = sys.argv[2]
        dobot = DobotController(dobotPort, raspPort)

    app.run(debug=False)