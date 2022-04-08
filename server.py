from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index1():
    return render_template("index.html", rows = 8, columns = 8)

@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
def index2(x, y = 8):
    x = int(x/2)
    return render_template("index.html", rows = x, columns = y)

if __name__=="__main__":
    app.run(debug=True)
