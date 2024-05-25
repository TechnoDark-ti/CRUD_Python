# Gerenciamento Comercial ERP de Hotel

Este projeto é um sistema de Gerenciamento Comercial ERP simples, utilizando Python, SQLite e Flet para a interface gráfica. Ele permite realizar operações CRUD (Create, Read, Update, Delete) em um banco de dados de clientes.

## Estrutura do Projeto

```
.
├── database.py
├── crud.py
├── screen.py
└── main.py
```

- **database.py**: Gerencia a conexão e as operações com o banco de dados SQLite.
- **crud.py**: Funções CRUD para manipular os dados dos clientes.
- **screen.py**: Interface gráfica utilizando a biblioteca Flet.
- **main.py**: Inicia a aplicação Flet e chama a interface gráfica.

## Instalação

### Requisitos

- Python 3.10 ou superior
- Biblioteca Flet

### Passos

1. Clone o repositório:

    ```bash
    git clone https://github.com/
    cd 
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    virtualenv ven
    source venv/bin/activate  # Para Windows: venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip install flet sqlite3
    ```
    ```bash
    pip3 install flet sqlite3
    ```

## Uso

1. Inicialize a aplicação:

    ```bash
    python main.py
    ```

2. A interface gráfica será aberta em uma nova janela, permitindo adicionar, visualizar, atualizar e deletar clientes.


# Futuras Implementações
 - Criação de novos inventários de hotel
 - Tela de Login
 - Migração de SGBD 
 - Novas funções de Gerenciamento
 - Executáveis (Appimage e .exe )

## Licença

Este projeto está licenciado sob a GNU General Public License v3.0.

## Autor

**TechnoDark-ti**

---