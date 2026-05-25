from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "cooporigen_2026_nueva_clave"

# Usuarios autorizados
users = {
    "Juan.londono": "Cooporigen.2026*",
    "Sara.gonzales": "Cooporigen.2026*",
    "Juan.garcia": "Cooporigen.2026*",
    "Vanessa.espinal": "Eslop.2026*",
    "Yeison.saldarriaga": "Cooporigen.2026*",
    "Juliana.salgado": "Cooporigen.2026*"
}

@app.route("/", methods=["GET", "POST"])
def login():

    error = False

    # Cerrar sesión anterior automáticamente
    session.clear()

    if request.method == "POST":

        user = request.form["username"].strip()
        password = request.form["password"].strip()

        # Validar usuario y contraseña
        if user in users and users[user] == password:

            session["logged_in"] = True
            session["user"] = user

            return redirect("/dashboard")

        else:
            error = True

    return render_template("login.html", error=error)

@app.route("/dashboard")
def dashboard():

    # Si no ha iniciado sesión
    if not session.get("logged_in"):
        return redirect("/")

    return render_template("dashboard.html")

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)