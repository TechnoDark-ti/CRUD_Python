from flet import *
import crud

# Função principal para iniciar a interface
def main(page: Page):
    page.title = "Gerenciamento Comercial"
    page.vertical_alignment = "center"

    # Inicializar o banco de dados
    crud.initDB()

    # Definir as funções de callback
    def adicionar_cliente(e):
        crud.insert(nome_input.value, sobrenome_input.value, email_input.value, cpf_input.value)
        nome_input.value = ""
        sobrenome_input.value = ""
        email_input.value = ""
        cpf_input.value = ""
        atualizar_lista()

    def atualizar_lista():
        clientes = crud.view()
        lista_dados.controls.clear()
        for cliente in clientes:
            lista_dados.controls.append(
                ListTile(
                    title=Text(cliente[1]),
                    subtitle=Text(f"ID: {cliente[0]} | Sobrenome: {cliente[2]} | Email: {cliente[3]} | CPF: {cliente[4]}"),
                    trailing=Row([
                        IconButton(icons.EDIT, on_click=lambda e, id=cliente[0]: editar_cliente(id)),
                        IconButton(icons.DELETE, on_click=lambda e, id=cliente[0]: deletar_cliente(id))
                    ])
                )
            )
        page.update()

    def editar_cliente(cliente_id):
        cliente = crud.search(id=cliente_id)[0]
        nome_input.value = cliente[1]
        sobrenome_input.value = cliente[2]
        email_input.value = cliente[3]
        cpf_input.value = cliente[4]
        atualizar_button.data = cliente_id
        atualizar_button.visible = True
        adicionar_button.visible = False
        page.update()

    def atualizar_cliente(e):
        cliente_id = e.control.data
        crud.update(cliente_id, nome_input.value, sobrenome_input.value, email_input.value, cpf_input.value)
        nome_input.value = ""
        sobrenome_input.value = ""
        email_input.value = ""
        cpf_input.value = ""
        atualizar_button.visible = False
        adicionar_button.visible = True
        atualizar_lista()

    def deletar_cliente(cliente_id):
        crud.delete(cliente_id)
        atualizar_lista()

    # Criar os componentes da interface
    nome_input = TextField(label="Nome")
    sobrenome_input = TextField(label="Sobrenome")
    email_input = TextField(label="Email")
    cpf_input = TextField(label="CPF")

    adicionar_button = ElevatedButton(text="Adicionar Cliente", on_click=adicionar_cliente)
    atualizar_button = ElevatedButton(text="Atualizar Cliente", on_click=atualizar_cliente, visible=False)

    lista_dados = Column()

    atualizar_lista()

    # Layout da página
    page.add(
        Column(
            [
                Text("Gerenciamento Comercial", size=30, weight="bold"),
                nome_input,
                sobrenome_input,
                email_input,
                cpf_input,
                Row([adicionar_button, atualizar_button]),
                lista_dados
            ],
            alignment="center"
        )
    )

if __name__ == "__main__":
    app(target=main)
