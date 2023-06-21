from flask import Flask, render_template, request, redirect, session, flash, url_for


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria=categoria
        self.console = console
class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

app = Flask(__name__)
app.secret_key = 'ferrari'

jogo1 = Jogo('F1 2013', 'Corrida', 'xbox 360')
jogo2 = Jogo('Halo4', 'Tiro', 'Xbox one')
jogo3 = Jogo('Flight Simulator 2020', 'Simulação', 'Xbox Series s/x')
lista = [jogo1, jogo2, jogo3]

usuario1 = Usuario("Lucas", "LB", "scuderia")
usuario2 = Usuario("Andressa", "andy", "louis")

usuarios= {usuario1.nickname : usuario1, usuario2.nickname : usuario2}
@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not  in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo = 'Novo Jogo')

@app.route('/adicionar', methods=['POST', ])
def adicionar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash('Usuário ' + session['usuario_logado'] + ' com sucesso')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuarío não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('usuario deslogado com sucesso')
    return redirect(url_for('index'))

app.run(debug=True)
