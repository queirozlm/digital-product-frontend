from flask import Flask

app = Flask(name)

@app.route("/")
def pagina_inicial():
    return "Hello World"

if name == 'main':
    app.run()
