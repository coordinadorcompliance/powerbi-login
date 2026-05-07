from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "clave_super_secreta"

# Usuario y contraseña
USER = "admin"
PASSWORD = "1234"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]

        if user == USER and password == PASSWORD:
            session["logged_in"] = True
            return redirect("/dashboard")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect("/")

    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)