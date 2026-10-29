from flask import Flask, render_template, request, flash, redirect, url_for, session
from cifraCesar import cifraCesar, withoutCifraCesar

app = Flask(
    __name__,
    template_folder="src/templates",
    static_folder="src",
    static_url_path="/static"
)
app.secret_key = "chave-temporaria-securelogin"

usuarios = {}
chaveCifra = 3

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "")

        if not email or not senha:
            flash("Preencha todos os campos.")
        elif email not in usuarios:
            flash("E-mail ou senha incorretos.")
        else:
            senhaCifrada = cifraCesar(senha, chaveCifra)
            senhaGuardada = usuarios[email]["senha"]
            nomeUser = usuarios[email]["nome"]
            senhaDescriptografada = withoutCifraCesar(
                senhaGuardada,
                chaveCifra
            )

            print("LOGIN:")
            print("Entrando na sessão de", nomeUser)
            # print("Senha digitada:", senha)
            print("Senha cifrada:", senhaCifrada)
            # print("Senha armazenada:", senhaGuardada)
            # print("Senha descriptografada:", senhaDescriptografada)
            # ativar somente para mostrar o uso da crpitografia.

            if senhaCifrada == senhaGuardada:
                session["email"] = email
                return redirect(url_for("dashboard"))

            else:
                flash("E-mail ou senha incorretos.")

    return render_template("pages/login.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "")
        confirmar = request.form.get("confirmar", "")

        if not nome or not email or not senha or not confirmar:
            flash("Preencha todos os campos.")
        elif email.count("@") != 1 or "." not in email.split("@")[-1]: 
            flash("Digite um endereço de e-mail válido.")
        elif not senha.isalnum() or not senha.isascii():
            flash("Não pode conter caracteres especiais.") 
        elif senha != confirmar:
            flash("As senhas não são iguais.")
        elif len(senha) < 8:
            flash("A senha deve ter pelo menos 8 caracteres.")
        else:
            if email in usuarios:
                flash("Este e-mail já está cadastrado.")
            else:
                senhaCifrada = cifraCesar(senha, chaveCifra)

                usuarios[email] = {
                    "nome": nome,
                    "senha": senhaCifrada
                }

                print("CADASTRO:")
                print(usuarios)
                # print("Senha digitada:", senha)
                # ativar somente para mostrar o uso da crpitografia.

                flash("Cadastro realizado! Entre na sua conta para realizar seu Login.", "sucesso")
                
    return render_template("pages/register.html")

@app.route("/dashboard")
def dashboard():
    email = session.get("email")
    if not email or email not in usuarios:
        session.clear()
        return redirect(url_for("login"))

    nome = usuarios[email]["nome"]
    return render_template("dashboard.html", nome=nome)

@app.route("/sair")
def sair():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)