# Cadastro_Jogos

I make this project just to traine my MySQL and python skills, using some basic SQL commands, and I enjoyed so much making this.


# First scene 

In the first scene, we can insert new dados for MySQL Server.

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
