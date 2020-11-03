#Programas utilizados
# PyCharm, WampServer e QT Design.

# Importando PyQt5 - QT Design / mysql.connector - MySQL.
from PyQt5 import uic,QtWidgets
import mysql.connector

# Definindo a database do Banco de Dados, utilizando WampServer - MySQL.
bd = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_jogos"
)
# Definindo a função de cadastro de novos Jogos.
def funcao_principal():
    line1 = tela_cadastrar.lineEdit_3.text()
    line2 = tela_cadastrar.lineEdit_4.text()
    line3 = tela_cadastrar.lineEdit_5.text()

    plataforma = ""

    if tela_cadastrar.radioButton.isChecked() :
        plataforma ="Playstation"
    elif tela_cadastrar.radioButton_2.isChecked() :
        plataforma ="Xbox"
    elif tela_cadastrar.radioButton_3.isChecked() :
        plataforma ="PC"
    else :
        plataforma = "Nintendo"


# Comando para introduzir ao banco de dados os novos valores.
    cursor = bd.cursor()
    fun_SQL = "INSERT INTO jogos (codigo,jogo,preco,plataforma) VALUES (%s,%s,%s,%s)"
    dados = (str(line1),str(line2),str(line3),plataforma)
    cursor.execute(fun_SQL,dados)
    bd.commit()

# Limpando o campo de digitação
    tela_cadastrar.lineEdit_3.setText("")
    tela_cadastrar.lineEdit_4.setText("")
    tela_cadastrar.lineEdit_5.setText("")

# Definindo função de listar para o Banco de Dados - MySQL.
def funcao_listar():
    tela_listar.show()
    tela_cadastrar.close()

    cursor = bd.cursor()
    fun_SQL = "SELECT * FROM jogos"
    cursor.execute(fun_SQL)
    dados_lidos = cursor.fetchall()

    tela_listar.tableWidget.setRowCount(len(dados_lidos))
    tela_listar.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            tela_listar.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

# Fazer a troca de layout de forma limpa.
def tela_change():
    tela_update.show()
    tela_listar.close()

def tela_change2():
    tela_listar.close()
    tela_cadastrar.show()

def tela_change3():
    tela_update.close()
    tela_listar.show()

# Fazer UPDATE no Banco de Dados - MySQL.
def update_games():

    codigo = tela_update.lineEdit.text()
    jogo = tela_update.lineEdit_2.text()
    preco = tela_update.lineEdit_3.text()
    plataforma = ""

    if tela_update.radioButton.isChecked():
        plataforma = "Playstation"
    elif tela_update.radioButton_2.isChecked():
        plataforma = "Xbox"
    elif tela_update.radioButton_3.isChecked():
        plataforma = "PC"
    else:
        plataforma = "Nintendo"

    try:
        cursor = bd.cursor()
        fun_SQL = (f"UPDATE jogos SET jogo = '{jogo}', preco = '{preco}', plataforma = '{plataforma}' WHERE codigo = '{codigo}';")
        cursor.execute(fun_SQL)
        bd.commit()
    except:
        print('Este jogo não está em nossa biblioteca')

    tela_update.close()
    tela_listar.show()

# Definindo a função deletar no Banco de Dados - MySQL.
def delete_dados():

    linha = tela_listar.tableWidget.currentRow()
    tela_listar.tableWidget.removeRow(linha)

    cursor = bd.cursor()
    cursor.execute("SELECT id FROM jogos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM jogos WHERE id="+ str(valor_id))

    tela_listar.close()
    tela_cadastrar.show()

# Definindo as importações dos layouts, que foram criados com QT Design.
app=QtWidgets.QApplication([])
tela_cadastrar=uic.loadUi("cadastrar_jogos.ui")
tela_listar=uic.loadUi("listar_jogos.ui")
tela_update=uic.loadUi("update_jogos.ui")

#Definindo a conexão dos botões.
tela_cadastrar.pushButton.clicked.connect(funcao_principal)
tela_cadastrar.pushButton_2.clicked.connect(funcao_listar)
tela_listar.pushButton.clicked.connect(delete_dados)
tela_listar.pushButton_2.clicked.connect(tela_change)
tela_listar.pushButton_3.clicked.connect(tela_change2)
tela_update.pushButton.clicked.connect(update_games)
tela_update.pushButton_2.clicked.connect(update_games)

tela_cadastrar.show()
app.exec()
