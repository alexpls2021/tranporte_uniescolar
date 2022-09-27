from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pessoas.sqlite3"
db = SQLAlchemy(app)


class Pessoas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    end = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    tipo_cliente = db.Column(db.String(11), nullable=False)

    def __init__(self, nome, cpf, end, email, telefone, tipo_cliente):
        self.nome = nome
        self.cpf = cpf
        self.end = end
        self.email = email
        self.telefone = telefone
        self.tipo_cliente = tipo_cliente


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        pessoa = Pessoas(
            request.form["nome"],
            request.form["cpf"],
            request.form["end"],
            request.form["email"],
            request.form["telefone"],
            request.form["tipo_cliente"]
        )
        db.session.add(pessoa)
        db.session.commit()
        return redirect("/#header")
    return render_template("cadastro.html", active='cadastro')


@app.route("/consultar")
def consultar():
    pessoas = Pessoas.query.all()
    return render_template("consultar.html", pessoas=pessoas, active='consultar')


@app.route("/delete/<id>")
def delete(id):
    pessoa = Pessoas.query.get(id)
    db.session.delete(pessoa)
    db.session.commit()
    return redirect("/consultar")


@app.route("/formulario")
def formulario():
    return render_template("formulario.html", active='formulario')


@app.route("/escola")
def escola():
    return render_template("escola.html", active='escola')
    

@app.route("/localizacao")
def localizacao():
    return render_template("localizacao.html", active='localizacao')


if __name__ == "__main__":
    db.create_all()
    
