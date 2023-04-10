from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from controller import DobotController
from extensions import db
import sys

app = Flask(__name__)
dobot = ""

# O arquivo app.py é importado no models.py, que roda antes do servidor iniciar
# O código abaixo só funciona caso receba a porta do dobot via argumento de linha de comando, desse jeito: "python app.py COM3"
# Logo, se arquivo é importado e roda sem receber esse argumento, o programa crasha
# Portanto o código que depende desse argumento está na condição abaixo, para que rodem só se o processo for realmente iniciado com a linha de comando, e não importado 
if __name__ == '__main__':
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite+pysqlite:///project.db"
    
    # a porta COM1 é a default, ou seja, nenhuma porta foi identificada
    if sys.argv[1] == "COM1":
        print("porta não selecionada!")
        pass

    # instancia a classe dobotController com as portas do dobot e raspberry recebidas pela linha de comando
    else:
        dobotPort = sys.argv[1]
        raspPort = sys.argv[2]
        dobot = DobotController(dobotPort, raspPort)

else: 
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite+pysqlite:///../../instance/project.db"

#incializa o banco de dados
db.init_app(app)

#----------------------------------------------------------------------------
# Cada rota abaixo executa uma função homônima na classe dobotController.
# As funções estão devidamente comentadas no arquivo 'controller.py'
#----------------------------------------------------------------------------

@app.get("/get_tracks")
def get_trackss():
    message = dobot.get_tracks()
    return message

@app.get('/get_track')
def get_track():
    # recebe o ID de uma rota (de trabalho) do robo
    data = request.get_json()
    message = dobot.get_track(data)
    return message

@app.get("/magnet_on")
def magnet_on():
    return dobot.magnet_on()

@app.get("/magnet_off")
def magnet_off():
    return dobot.magnet_off()

@app.post("/run_track")
def run_track():
    data = request.get_json()
    return dobot.run_track(data)

@app.get("/add_position_dobot")
def add_position_dobot2():
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
    app.run(debug=False)