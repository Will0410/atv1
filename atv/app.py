from flask import Flask, render_template
#from mongoengine import connect, Document, StringField, DateTimeField, ListField

app = Flask(__name__)
#Criando uma rota com o decorator para a pagina inicial#
#connect(host='mongodb+srv://arthurverdadeiro:atividade007@cluster0.o3x1fun.mongodb.net/test')

#class Projeto(Document):
#    nome_do_projeto = StringField(required=True)
#    data_de_entrega = DateTimeField(required=True)
#    lider = StringField(required=True)
#    integrantes = ListField(StringField())

#projeto = Projeto(
#    nome_do_projeto='Projeto A',
#    data_de_entrega='2023-12-31',
#    lider='João',
#    integrantes=['Maria', 'Pedro']
#)

#projetos = Projeto.objects()
#for projeto in projetos:
    #print(projeto.nome_do_projeto)

#projeto = Projeto.objects(nome_do_projeto='Projeto A').first()
#projeto.lider = 'José'
#projeto.save()

#projeto = Projeto.objects(nome_do_projeto='Projeto A').first()
#projeto.delete()#



@app.route("/")
def index():
    return render_template("template.html", Tarefa="Ai", Tarefa2="Zé", Tarefa3="Da", Tarefa4="Manga 🥭")

@app.route("/login")
def log():
    return render_template("tela_log.html")

@app.route("/project")
def project():
    return render_template("telacad_project.html")

@app.route("/tarefa")
def tarefa():
    return render_template("telacad_tarefa.html")

@app.route("/user")
def user():
    return render_template("telacad_user.html")
