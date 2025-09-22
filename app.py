from flask import Flask, render_template #importando biblioteca 
app = Flask(__name__) 

@app.route('/') #@ significa anotação / route=rota / "/" signfica a rota raíz
def index(): #criando método
    return 'Olá Alba' #exibindo mensagem na tela

@app.route('/contato')
def contato():
  return render_template('contato.html', nome = 'Maria', email = 'maria@email.com')

@app.route('/exemplo')
def exemplo():
  return render_template('exemplo.html')

@app.route('/exemplo2')
def exemplo2():
   return render_template('exemplo2.html')


@app.route('/perfil/')
@app.route('/perfil/<nome>')
def perfil(nome='fulano'):
    return render_template('perfil.html', nome=nome)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

