from flask import Flask, render_template

app = Flask(__name__, static_folder="static")


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html", name = "User")

@app.route("/catalogue.html")
def go_to_catalogue():
    return render_template("catalogue.html")

@app.route("/contact.html")
def go_to_contact():
    return render_template("contact.html")

@app.route("/login.html")
def go_to_login():
    return render_template("login.html")

@app.route("/register.html")
def go_to_register():
    return render_template("register.html")

@app.route("/<name>")
def index_with_custom_greeting(name):
    return render_template("index.html", name = name)


if __name__ == "__main__":
    app.run(debug=False)
