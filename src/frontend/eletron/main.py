from flask import Flask, render_template, request

app = Flask(__name__)

print("flaskei")

@app.route("/robot" , methods=["GET", "POST"])
def robot():
    if request.method == "POST":
        print(request.form)
    return "Hello World"



if __name__ == "__main__":
    app.run(host='localhost', port=5000)

