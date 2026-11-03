from flask import Flask, render_template, request, redirect, flash
from dao.db_cofig import get_connection
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO

app = Flask(__name__)

app = Flask(__name__)
app.secret_key = "uma_chave_muito_secreta_e_unica"


@app.route('/')
def home():
    return render_template('dashboard/index.html')


@app.route('/sobre')
def sobre_o_Sistema():
    return render_template('dashboard/sobre.html')

@app.route('/aluno')
def lista_aluno():

        dao = AlunoDAO()
        
        lista = dao.listar()
        return render_template('aluno/lista.html', lista=lista)


@app.route('/aluno/form') 
def form_aluno():
    
    return render_template('aluno/form.html',aluno=None)


@app.route('/aluno/salvar/', methods=['POST'])
def salvar_aluno(id=None):
        nome = request.form['nome'],
        idade = request.form['idade'],
        cidade = request.form['cidade']
        dao=AlunoDAO()
        result=dao.salvar(id, nome, idade, cidade)
        if result["status"] == "ok":
                flash("Aluno salvo com sucesso!", "success")
        else:
                flash(result["mensagem"], "danger")
        return redirect('/aluno')


@app.route('/aluno/editar/<int:id>')
def editar_aluno(id):
    dao = AlunoDAO()
    aluno = dao.buscar_por_id(id)
    return render_template('aluno/form.html', aluno=aluno)


@app.route("/aluno/remover/<int:id>")
def remover_aluno(id):
    dao = AlunoDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/aluno')

 

@app.route('/professor')
def lista_professor():
    
        dao = ProfessorDAO()
                
        lista = dao.listar()
        return render_template('professor/lista.html', lista=lista)


@app.route('/professor/form') 
def form_professor():
    return render_template('professor/form.html', professor=None)


@app.route('/professor/salvar/', methods=['POST'])
def salvar_professor(id=None):

    nome = request.form['nome']
    disciplina = request.form['disciplina']
    
    dao = ProfessorDAO()
    result = dao.salvar(id, nome, disciplina)
    

    if result["status"] == "ok":
        flash("Professor salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")
        

    return redirect('/professor')
    
@app.route('/turma')
def lista_turma():
    
        dao = TurmaDAO()
                        
        lista = dao.listar()
        return render_template('turma/lista.html', lista=lista)

@app.route('/turma/form')
def form_turma():
    cursos = CursoDAO().listar()
    professores = ProfessorDAO().listar()
    return render_template('turma/form.html', cursos=cursos, professores=professores, turma=None)


@app.route('/turma/salvar/', methods=['POST'])
def salvar_turma(id=None):
    semestre = request.form['semestre']
    curso_id = request.form['curso_id']
    professor_id = request.form['professor_id']

    dao = TurmaDAO()
    result = dao.salvar(id, semestre, curso_id, professor_id)

    if result["status"] == "ok":
        flash("Turma salva com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/turma')
    
@app.route('/curso')
def lista_curso():
    
        dao = CursoDAO()
                        
        lista = dao.listar()
        return render_template('curso/lista.html', lista=lista)


@app.route('/curso/form')
def form_curso():
    return render_template('curso/form.html', curso=None)


@app.route('/curso/salvar/', methods=['POST'])
def salvar_curso(id=None):
    nome_curso = request.form['nome_curso']
    duracao = request.form['duracao']

    dao = CursoDAO()
    result = dao.salvar(id, nome_curso, duracao)

    if result["status"] == "ok":
        flash("Curso salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/curso')
    


@app.route('/ajuda')
def ajuda():
    return 'Ajuda Sobre o Sistema!'


@app.route('/saudacao1/<nome>')
def saudacao1(nome):
      return render_template('saudacao/saudacao.html',valor_recebido=nome)

@app.route('/saudacao2/')
def saudacao2():
      nome= request.args.get('nome')
      return render_template('saudacao/saudacao.html',valor_recebido=nome)  


@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
                usuario = request.form['usuario']
                senha = request.form['senha']

                return f'''
                        <h1>Login realizado!</h1>
                        <p>Usuário: {usuario}</p>
                        <p>Senha: {senha}</p>
                '''


        return render_template('login.html')


@app.route('/desafio1/<nome>')
def desafio1(nome):
      return render_template('desafio1/desafio.html',valor_recebido=nome)

@app.route('/desafio', methods=['GET', 'POST'])
def loginDesafio():
        nome= request.form['nome']
        dataNasc= request.form['dataNasc']
        cpf= request.form['cpf']
        nomeMae= request.form['nomeMae']

        return render_template('/desafio1/dada.html', nome=nome, dataNasc=dataNasc, cpf=cpf, nomeMae=nomeMae )

@app.route('/formdesafio')
def formdesafio():
      return render_template('desafio1/desafio.html')
        

      

if __name__ == '__main__':
    app.run(debug=True)
