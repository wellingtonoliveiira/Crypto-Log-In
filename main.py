
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "chave-temporaria-securelogin"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "")

        if email and senha:
            flash("Formulário enviado com sucesso!")
        else:
            flash("Preencha todos os campos.")

    return render_template("login.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "")

        if not nome or not email or not senha:
            flash("Preencha todos os campos.")
        elif len(senha) < 8:
            flash("A senha deve ter pelo menos 8 caracteres.")
        else:
            flash("Formulário de cadastro enviado com sucesso!")

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
