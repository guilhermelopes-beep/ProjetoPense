from flask import Flask, request, render_template
from markupsafe import escape
import jinja2


app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined

@app.get("/")
def Index():
    
    pessoa = {"nome": "Guilherme", "idade":18}
    lista = [1, 2, 3, 4, 5]
    return render_template("index.html", pessoa=pessoa, lista=lista)
#   termo = request.args.get('q')
#   return render_template("index.html", nome=termo)

@app.route('/teste', methods=['GET', 'POST']) 
def teste(): 
    if request.method == 'POST': 
        return "Você enviou um POST! (Dados processados)" 
    return "Você enviou um GET! (Página visualizada)" 

@app.route("/usuarios/<nome_usuario>")
def perfil(nome_usuario): 
    return f"Olá, {nome_usuario}! Este é o seu perfil." 


@app.route("/soma/<int:n1>/<int:n2>")
def somar(n1, n2):
    resultado = n1 + n2
    return f"A soma de {n1} + {n2} é igual a: {resultado}"

@app.route("/pagamento/<any(cartao, boleto, pix):metodo>")
def processar_pagamento(metodo):
    return f"Processando pagamento via {metodo}"

@app.route("/busca") 
def pesquisar(): 
    #http://127.0.0.1:5000/busca?q=Caminhao%20Monster%20Truck
    termo = request.args.get('q') 
    prioridade = request.args.get('ordem', default='recente') 
    return f"Você buscou por: {termo} (Ordenado por: {prioridade})" 

#Atente a ordem das rotas:
@app.route('/user/<username>')
def profile(username):
    return f"Perfil de {username}"

# Nunca será acessada, pois vai parar na anterior
#Inverta a ordem permitir o acesso
@app.route('/user/admin')
def admin():
    return "Área do Administrador"

@app.route("/rastrear")
def rastrear():
    info = {
        "ip_do_usuario": request.remote_addr,
        "metodo": request.method,
        "caminho": request.path,
        "navegador": request.user_agent.string
    }
    return info

@app.route('/livros/')
def listar_livros():
    return "<h1>Biblioteca</h1>"

@app.route('/sobre')
def sobre():
    return f"<h1>Sobre</h1><p>Este é um projeto sobre Flask.</p>"

@app.route('/livro/<int:livro_id>')
def detalhes_livro(livro_id):
    return f"<h1>Detalhes</h1><p>livro ID: {livro_id}</p>"


@app.route('/genero/<any(ficcao, terror, biografia):tipo>')
def filtrar_genero(tipo):
    return f"<h1>Gênero: {tipo.capitalize()}</h1>"

# @app.errorhandler(404)
# def erro_404():
#     return render_template('erros/404.html')

@app.route("/frutas")
def frutas():
    lista = ["Banana", "Maçã", "Abacate", "Laranja", "Caqui"]
    return render_template("frutas.html", lista=lista)

@app.route("/fruta-status")
def fruta_status():
    q = request.args.get('q')
    
    lista_status = [
        {"Nome":"Banana", "Preco": 19.2, "Quantidade": 10},
        {"Nome":"Maça", "Preco": 5.2, "Quantidade": 100},
        {"Nome":"Abacate", "Preco": 49.2, "Quantidade": 20},
        {"Nome":"Abacaxi", "Preco": 39.2, "Quantidade": 0},
        {"Nome":"Kiwi", "Preco": 29.2, "Quantidade": 110}
        ]

    fruta = lista_status[int(q)]

    return render_template("index.html", fruta=fruta)


if __name__ == '__main__':
    print("Servidor Flask rodando em http://localhost:5000")
    app.run(debug=True, port=5000)
