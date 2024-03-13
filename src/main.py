#Python 3.10.12
"""
            @Author: TechnoDark-ti
        Todos os direitos resevados
    GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007.
"""
from flet import *
import sqlite3

# Conectando ao banco de dados
conexao = sqlite3.connect("dados.db", check_same_thread=False)
cursor = conexao.cursor()

#Criando uma tabela no BD
def tabela_base():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)
    ''')

#Classe do aplicativo principal que será instanciado no main()
class App(UserControl):
    def __init__(self):
        super().__init__()

        self.todos_dados = Column(auto_scroll=True)
        self.adicionar_dados = TextField(label='Nome do dado')
        self.editar_dado = TextField(label='Editar')

    #Func de deletar dados
    def deletar(self, id_user, dialog):
        cursor.execute("DELETE FROM clientes where id = ?", [id_user])
        conexao.commit()
        dialog.open = False
        # chamar a função de renderizar dados
        self.todos_dados.controls.clear()
        self.renderizar_todos()
        self.page.update

    #Func para abrir as ações do programa
    def abrir_acoes(self, e):
        id_user = e.control.subtitle.value
        self.editar_dado.value = e.control.title.value
        self.update()

        alerta_dialogo = AlertDialog(
            title = Text(f"EDITAR ID {id_user}"),
            content = self.editar_dado,
            #Botões
            actions = [
                ElevatedButton('Deletar', color='white', bgcolor='red',
                               on_click=lambda e: self.deletar(id_user, alerta_dialogo)
                               ),
                ElevatedButton(
                    'Atualizar',
                    on_click=lambda e: self.atualizar(id_user, self.editar_dado, alerta_dialogo)
                )
            ], actions_alignment='spaceBetween'
        )
        self.page.dialog = alerta_dialogo
        alerta_dialogo.open = True

        self.page.update()

    #READ - Apresentar todos os dados do BD
    def renderizar_todos(self):
        cursor.execute("SELECT * FROM clientes")
        conexao.commit()

        meus_dados = cursor.fetchall()

        for dado in meus_dados:
            self.todos_dados.controls.append(
                ListTile(
                    subtitle=Text(dado[0]),
                    title=Text(dado[1]),
                    onclick=self.abrir_acoes
                )
            )

    #Criar um dado persistente para o BD através do SQL
    def adicionar_novo_dado(self, e):
        cursor.execute("INSERT INTO clientes (nome) values(?)", [self.adicionar_dados.value])
        conexao.commit()

        self.todos_dados.controls.clear()
        self.renderizar_todos()
        self.page.update()

    def build(self):
        return Column([
            #Primeiro Titulo
            Text("GERENCIAMENTO COMERCIAL", text_align="center", size=20, weight='bold'),
            self.adicionar_dados,

            #Botão para adicionar o novo dado
            ElevatedButton('Adicionar Dado',
                            on_click=self.adicionar_novo_dado,
                            ),
            self.todos_dados  # Correção aqui
        ])

def main(page: Page):
    my_application = App()

    page.add(
        my_application,
    )

if __name__ == "__main__":
    app(target=main)
