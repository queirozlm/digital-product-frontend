from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "
<html>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
"

if __name__ == '__main__':
    app.run()
