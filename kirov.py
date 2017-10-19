
# Modulos do programa
import wifi.wifi

# Cores em python
Branco =    '\033[0m'
Vermelho =  '\033[31m'

def main():
    def funcao_ajuda():
        print("""
Comandos principais
-------------------

Comando   	Descrição
-------   	---------
ajuda 		Menu de ajuda
loadmod 	Carregar modulo especifico
info		Informações do modulo especifico
mods 		Lista de todos os modulos
	""")

    def lista_modulos():
        print("""
Modulos Disponiveis
-------------------

Modulo 		Descrição
------		---------
Wifi		Modulo para ataque a redes wireless
	""")

    def info_wifi():
        print("""
Comandos Disponiveis
----------------------

Comando 		Descrição
---------		-------
scan <nome do wifi> 	Escanear o wifi a procura de falha
""")

    entrada = input("Kirov > ")

    # Menu de ajuda
    if (entrada.split(" ")[0] == "ajuda"):
        funcao_ajuda()
        main()

    # Carregar modulo
    elif (entrada.split(" ")[0] == "loadmod"):

        if (entrada.split(" ")[1] == "wifi"):
            print("\nModulo Wifi carregado\n")
            wifi.wifi.main()

        else:
            print("\nModulo não reconhecido\n")

        main()

    # Informações dos modulos
    elif (entrada.split(" ")[0] == "info"):

        # Modulo não especificado
        if (len(entrada) < 5):
            print("\nModulo não especificado\n")
            main()

        # Modulo já especificado
        elif (len(entrada) > 5):

            if (entrada.split(" ")[1] == "wifi"):
                info_wifi()
                main()

            elif(entrada.split(" ")[1] == " "):
                print("\nModulo não reconhecido\n")
                main()

            else:
                print("\nModulo não reconhecido\n")
                main()

    # Lista de todos os modulos
    elif (entrada.split(" ")[0] == "mods"):
        lista_modulos()
        main()

    else:
        print("\nComando não reconhecido\nDigite ajuda para ver os comandos disponiveis")
        main()

# Executar a função principal
if __name__ == "__main__":
    print("""\n[ Kirov v0.0.1 Copyright 2017 ]\n""")
    main()
