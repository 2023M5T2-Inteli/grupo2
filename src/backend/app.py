#importa flask para criar nosso server
from flask import Flask, request
#importa o controller para fazer a comunicação com o Dobot
from controller import Controller

#cria o server
app = Flask(__name__)



#cria as rotas para cada função do Dobot
#rota para o mover para baixo
@app.post("/down")
def down_claw():
    print(request.get_json()["value"])
    message = Controller().down(request.get_json()["value"])
    return message

#rota para o mover para cima
@app.post("/up")
def up_claw():
    print(request.get_json())
    message = Controller().up()
    return message

#rota para o mover para em uma linha reta
@app.post("/line")
def line_claw():
    print(request.get_json())
    message = Controller().line(request.get_json()["value"])
    return message

#rota para rotacionar no sentido horário
@app.post("/rotate")
def clockwise_claw():
    print(request.get_json())
    message = Controller().rotate(request.get_json()["value"])
    return message
#liga o server
if __name__ == "__main__":
    app.run(host="10.128.30.205",port=5000,debug=True)
