
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():
    mensagem = ""

    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")

        if email and password:
            mensagem = "Formulário enviado com sucesso!"
        else:
            mensagem = "Preencha todos os campos."

    return render_template("login.html", mensagem=mensagem)


if __name__ == "__main__":
    app.run(debug=True)
