from flask import Flask 

app = Flask(__name__)

@app.route("/")
def head():
    return "<h1>You are gonna be a goooood DevOps!</h1>"

@app.route("/second")
def second():
    return "<h2>This is my second page</h2>"

@app.route("/third/subthird")
def third():
    return "<h2>This is the subpath of third page.. Serdar</h2>"

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'


if __name__ == "__main__":
    app.run(debug=True)