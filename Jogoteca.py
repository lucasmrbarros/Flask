from flask import Flask, render_template, request, redirect, session, flash


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria=categoria
        self.console = console

app = Flask(__name__)
app.secret_key = 'ferrari'

jogo1 = Jogo('F1 2013', 'Corrida', 'xbox 360')
jogo2 = Jogo('Halo4', 'Tiro', 'Xbox one')
jogo3 = Jogo('Flight Simulator 2020', 'Simulação', 'Xbox Series s/x')
lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not  in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('novo.html', titulo = 'Novo Jogo')

@app.route('/adicionar', methods=['POST', ])
def adicionar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST', ])
def autentincar():
    if('teste' == request.form['senha']):
        session['usuario_logado'] = request.form['usuario']
        flash('Usuário ' + session['usuario_logado'] + ' com sucesso')
        return redirect('/')
    else:
        flash('Usuarío não logado.')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('usuario deslogado com sucesso')
    return redirect('/')

app.run(debug=True)
