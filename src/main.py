#Python 3.10.12
"""
            @Author: TechnoDark-ti
        Todos os direitos resevados
    GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007.
    
    --------------- ARQUIVO MAIN ---------------
    1 - Arquivo responsável em chamar as funções e script de outros códigos
    2 - Neste arquiv    o existirá apenas instância dos arquivos filhos
"""

## Começo do Código 
import flet 
from screen import main as screen_main

def main(page: flet.Page):
    screen_main(page)

if __name__ == "__main__":
    flet.app(target=main)
