#importa flask para criar nosso server
from flask import Flask, request
#importa o controller para fazer a comunicação com o Dobot
from controller import Controller

#cria o server
app = Flask(__name__)



#cria as rotas para cada função do Dobot

#rota para o quadrado
@app.post("/square")
def square_app():
    print(request.get_json()["side"])
    message = Controller.square(request.get_json()["side"])
    return message

#rota para o fechar a garra
@app.post('/close')
def close_claw():
    print("foiiii")
    message = Controller.close()
    return message

#rota para o abrir a garra
@app.post('/open')
def open_claw():
    message = open()
    return message

#rota para o mover para baixo
@app.post("/down")
def down_claw():
    print(request.get_json()["value"])
    message = Controller.down(request.get_json()["value"])
    return message

#rota para o mover para cima
@app.post("/up")
def up_claw():
    print(request.get_json())
    message = Controller.up()
    return message

#rota para o mover para em uma linha reta
@app.post("/line")
def line_claw():
    print(request.get_json())
    message = Controller.line(request.get_json()["value"])
    return message

#rota para rotacionar no sentido horário
@app.post("/rotate")
def rotate_claw():
    message = Controller.rotate(request.get_json()["value"])
    return message

#liga o server
if __name__ == "__main__":
    app.run(host="10.128.30.205",port=5000,debug=True)
