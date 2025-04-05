from main import app

@app.route("/")
def homepage():
    return "Meu Site no Flask"

@app.route("/contato")
def contato():
    return "SEGUE TODOS OS CONTATOS"

@app.route("/teste")
def teste():
    return "AAAAAAAAAAAAAAAAAAAAAAAAAAA"
