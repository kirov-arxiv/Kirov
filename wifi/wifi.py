

class modulo_wifi(object):
    def __init__(self):
        pass

    # Scan da rede wifi
    def scan(self, ssid):

        pass

def main():

    # Chamando a classe wifi
    mod_wifi = modulo_wifi()

    def help_main():
        print("""
Comandos principais
-------------------

Comando 		Descrição
---------		-------
scan <nome do wifi> 	Escanear o wifi a procura de falha
""")

    entrada = input("Kirov@Wifi > ")

    if(entrada.split(" ")[0] == "ajuda"):
        help_main()
        main()

    # Funçaõ scan
    elif(entrada.split(" ")[0] == "scan"):

        # Nome não especificado
        if(len(entrada) < 5):
            print("\nNome do wifi não foi especificado\n")
            main()

        # Nome especificado
        elif(len(entrada) > 5):
            ssid = entrada.split(" ")[1]
            mod_wifi.scan(ssid=ssid)

        else:
            print("\nNome do wifi não foi especificado\n")
            main()
