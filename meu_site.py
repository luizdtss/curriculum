

from flask import Flask, render_template

app = Flask(__name__)

# Criar a 1pagina do site
# route -> data4.com.br/
# função -> o que precisa exibir na página

@app.route("/")
def homepage():
    return render_template('homepage.html')

# colocar o site no ar

if __name__ == "__main__":
    app.run(debug=True)