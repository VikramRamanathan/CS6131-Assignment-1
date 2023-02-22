from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return "This is the default page"

@app.route("/bye")
def bye():
    return render_template("bye.html")

if __name__ == "__main__":
    app.run(debug=True)
