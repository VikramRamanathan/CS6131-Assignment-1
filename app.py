from flask import Flask, render_template

app = Flask(__name__, static_folder="static")


@app.route("/")
@app.route("/index.html")
def go_to_index():
    return render_template("index.html", name = "User")

@app.route("/<string:name>")
@app.route("/index.html?u=<string:name>")
def index_name(name):
    return render_template("index.html", name = name)

@app.route("/catalogue.html")
def go_to_catalogue():
    return render_template("catalogue.html")

@app.route("/catalogue.html?u=<string:name>")
def go_to_catalogue_name(name):
    return render_template("catalogue.html", name = name)

@app.route("/contact.html")
def go_to_contact():
    return render_template("contact.html")

@app.route("/contact.html?u=<string:name>")
def go_to_contact_name(name):
    return render_template("contact.html", name = name)

@app.route("/login.html")
def go_to_login():
    return render_template("login.html")

@app.route("/login.html?u=<string:name>")
def go_to_login_name(name):
    return render_template("login.html", name = name)

@app.route("/register.html")
def go_to_register():
    return render_template("register.html")

@app.route("/register.html?u=<string:name>")
def go_to_register_name(name):
    return render_template("register.html", name = name)




if __name__ == "__main__":
    app.run(debug=False)
