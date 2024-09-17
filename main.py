from traductor_texto import TraductorTexto

class Main:
    def __init__(self):
        self.traductor = TraductorTexto()
    
    def run(self):
        print("Bienvenido al Traductor de Textos")
        self.traductor.ejecutar()

if __name__ == "__main__":
    main_app = Main()
    main_app.run()
