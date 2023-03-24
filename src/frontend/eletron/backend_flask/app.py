from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from extensions import db

#initialize the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"


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
@app.get("/magnet_on")
def magnet_on():
    import serial
    import time
    try:
        tempo_espera = 2
        taxa_transmissao = 115200
        comunicacao_serial = serial.Serial("COM8", taxa_transmissao, timeout = tempo_espera)
        comunicacao_serial.write(b"on\n") # Escreve "on" na serial
        time.sleep(1)
        return "on"
    except Exception as e:
        return str(e)
@app.get("/magnet_off")
def magnet_off():
    import serial
    import time
    try:
        tempo_espera = 2
        taxa_transmissao = 115200
        comunicacao_serial = serial.Serial("COM8", taxa_transmissao, timeout = tempo_espera)
        comunicacao_serial.write(b"off\n") # Escreve "on" na serial
        time.sleep(1)
        return "off"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)