from flask import Flask, render_template, request
# import and create sqlite database

app = Flask(__name__)

print("flaskei")

@app.route("/robot" , methods=["GET", "POST"])
def robot():
    if request.method == "POST":
        print(request.form)
    return "Hello World"

@app.route("/robot/getroutes", methods=["GET"])
def getroutes():
    print("Pegando rotas...")
    # function to get routes from database, if i had imported the database module
    return "rotasfodinasss"


if __name__ == "__main__":
    app.run(host='localhost', port=5000)

