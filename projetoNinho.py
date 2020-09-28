from flask import Flask
from flask import render_template
from flask import request,redirect,abort,url_for 
from declaracaoForm import SolicitacaoForm
from loginForm import LoginForm
import json
import os.path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'projetoNinho'

@app.route('/projetoNinho/home')
def ninhoHome ():
    return render_template('index.html')
@app.route('/projetoNinho/painelOng')
def painelOng ():
    
    with open('./data/solicitacao.json') as json_file:
        data = json.load(json_file)
    return render_template('dashOng.html',solicitacoes=data)
    
@app.route('/projetoNinho/registro-necessidade', methods=['GET','POST'])
def registroNecessidade():
    form = SolicitacaoForm()
    if form.is_submitted():
        result = request.form
        solicitacoes = [""]
        with open('./data/solicitacao.json') as json_file:
            solicitacoes = json.load(json_file)
            solicitacoes.append(result)
        with open('./data/solicitacao.json','w') as json_file:
            json.dump(solicitacoes,json_file)    
        return redirect('/projetoNinho/home')
    return render_template('declaracaoNecessidade.html',form=form)
@app.route('/projetoNinho/cadastro')
def cadastroOng():
    return render_template('cadastroONG.html')
@app.route('/projetoNinho/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.is_submitted():
        return redirect('/projetoNinho/painelOng')
    
    return render_template('loginOng.html',form=form)

@app.route('/projetoNinho/valida-solicitacao', methods=['POST','GET'])
def validaSolicitacao():
    if request.method == 'POST':
        return redirect('/projetoNinho/home')
    else: 
        return redirect(url_for('/projetoNinho/registro-necessidade'))

@app.route('/projetoNinho/sobre')
def sobre():
        return render_template('About.html')