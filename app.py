from flask import Flask, render_template

# Importando os códigos dos alunos (Student Code)
from student_code.aula01_variaveis import configurar_personagem
from student_code.aula02_condicionais import verificar_acesso
from student_code.aula03_repeticao import gerar_inventario
from student_code.aula04_media import calcular_resultado
from student_code.aula05_idade import validar_maioridade

app = Flask(__name__)

# ==================================================
# ROTA 1: VARIÁVEIS (Home)
# URL: http://localhost:5000/
# ==================================================
@app.route('/')
def rota_variaveis():
    # Chama a função do aluno
    dados = configurar_personagem()
    # Renderiza o HTML com os dados do aluno
    return render_template('aula01.html', **dados)

# ==================================================
# ROTA 2: CONDICIONAIS (Input via URL)
# URL: http://localhost:5000/porta/<senha>
# Exemplo: http://localhost:5000/porta/1234
# ==================================================
@app.route('/porta/')
@app.route('/porta/<string:senha_digitada>')
def rota_condicionais(senha_digitada=""):
    
    # Envia o que foi digitado na URL para o código do aluno
    resultado = verificar_acesso(senha_digitada)
    
    return render_template('aula02.html', **resultado, senha_input=senha_digitada)

# ==================================================
# ROTA 3: REPETIÇÃO (Input via URL)
# URL: http://localhost:5000/loja/<quantidade>
# Exemplo: http://localhost:5000/loja/50
# ==================================================
@app.route('/loja/')
@app.route('/loja/<int:quantidade_itens>')
def rota_repeticao(quantidade_itens=5):
    
    # Envia o número para o loop do aluno
    dados_loja = gerar_inventario(quantidade_itens)
    
    return render_template('aula03.html', **dados_loja, qtd_input=quantidade_itens)


# ==================================================
# ROTA 4: MÉDIA (2 floats na URL)
# URL: http://localhost:5000/media/8.0/6.5
# ==================================================
@app.route('/media/')
@app.route('/media/<float:n1>/<float:n2>')
def rota_media(n1=0.0, n2=0.0):
    dados = calcular_resultado(n1, n2)
    return render_template('aula04.html', **dados, nota1=n1, nota2=n2)

# ==================================================
# ROTA 5: IDADE (1 int na URL)
# URL: http://localhost:5000/balada/17
# ==================================================
@app.route('/balada/')
@app.route('/balada/<int:idade>')
def rota_idade(idade=0):
    dados = validar_maioridade(idade)
    return render_template('aula05.html', **dados, idade_input=idade)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)