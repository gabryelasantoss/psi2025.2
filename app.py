from flask import Flask, render_template #importando biblioteca 
app = Flask(__name__) 

@app.route('/') #@ significa anotação / route=rota / "/" signfica a rota raíz
def index(): #criando método
    return 'Olá Alba' #exibindo mensagem na tela

@app.route('/contato')
def contato():
  return 'alba.lopes@ifrn.edu.br'

@app.route('/exemplo')
def exemplo():
  return render_template('exemplo.html')

@app.route('/exemplo2')
def exemplo2():
   return render_template('exemplo2.html')

if __name__ == '__main__':
    app.run()

