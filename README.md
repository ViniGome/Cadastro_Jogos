# Cadastro_Jogos

I make this project just to traine my MySQL and python skills, using some basic SQL commands, and I enjoyed so much making this.


# First scene 

In the first scene, we can insert new dados for MySQL Server.

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

#Second Scene
In the First Scene we can see the button "Listar Jogos" that basically check all dados we insert previously.


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
