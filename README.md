# Cadastro_Jogos

I make this project just to traine my MySQL and python skills, using some basic SQL commands, and I enjoyed so much making this.


# First scene 

In the First Scene, we can insert new data for MySQL Server.

![1](https://user-images.githubusercontent.com/73801769/98025092-0812cc80-1de8-11eb-8738-9c47499aa388.png)


```
# Definindo a função de cadastro de novos jogos.
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
```

# Second Scene
In the First Scene we can see the button "Listar Jogos" pressing this button open the Second Scene that basically check all data we insert previously.

![2](https://user-images.githubusercontent.com/73801769/98026761-617bfb00-1dea-11eb-9b2d-a881e009e0d7.png)

```
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

```

# Second Scene - Delete
In the Second Scene we can see the button "excluir", basically this delete the data in the current row that your selected.

![4](https://user-images.githubusercontent.com/73801769/98028082-56c26580-1dec-11eb-8bd3-5948d79e8537.png)

```
linha = tela_listar.tableWidget.currentRow()
    tela_listar.tableWidget.removeRow(linha)

    cursor = bd.cursor()
    cursor.execute("SELECT id FROM jogos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM jogos WHERE id="+ str(valor_id))
```

# Third Scene
Previously in the Second Scene we can see the "Alterar" button, when we press the program change for the Third Scene, and in this scene we can update all data we insert previosly.

![3](https://user-images.githubusercontent.com/73801769/98026773-65a81880-1dea-11eb-94cc-af43b9ad22ef.png)

```
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
```
