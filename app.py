from flask import Flask , render_template , request

app = Flask(__name__)

# rota para pagina inicial com o formulário

@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'POST':

        # pega os dados do formulario
        
        nome = request.form['nome']
        idade = request.form ['idade']
        return render_template('resultado.html',nome=nome , idade=idade)
    return render_template('index.html')

# rota que mostra os resultados

@app.route('/resultado')
def resultado():
    return render_template('resultado.html')

# rota pra pagina do autor

@app.route('/autor')
def autor():
    return render_template('autor.html')

#rodar a aplicaçao

if __name__== '__main__':
    app.run(debug=False)