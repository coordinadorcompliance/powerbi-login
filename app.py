from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "clave_super_secreta"

# Lista de usuarios
users = {

    "Juan.londono": "Cooporigen.2026*",
    "Sara.gonzales": "Cooporigen.2026*",
    "Juan.garcia": "Cooporigen.2026*",
    "Vanessa.espinal": "Eslop.2026*",
    "Yeison.saldarriaga": "Cooporigen.2026*",

    # Nuevo usuario
    "Juliana.salgado": "Cooporigen.2026*"
}

@app.route("/", methods=["GET", "POST"])
def login():

    error = False

    if request.method == "POST":

        user = request.form["username"]
        password = request.form["password"]

        if user in users and users[user] == password:

            session["logged_in"] = True
            return redirect("/dashboard")

        else:
            error = True

    return render_template("login.html", error=error)

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