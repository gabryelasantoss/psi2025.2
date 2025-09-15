from flask import Flask #importando biblioteca 
app = Flask(__name__) 

@app.route('/') #@ significa anotação / route=rota / "/" signfica a rota raíz
def index(): #criando método
    return 'Olá Alba' #exibindo mensagem na tela

if __name__ == '__main__':
    app.run()

