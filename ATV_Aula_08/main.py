from categoria import Categoria
from desktop import Desktop
from notebook import Notebook

if __name__ == "__main__":
    categoria = Categoria(id=1, nome="Eletrônicos")

    desktop1 = Desktop(modelo="Lenovo Thinkcenter", cor="Azul", preco=3500, categoria=categoria, potenciaDaFonte=450)
    desktop2 = Desktop(modelo="Positivo do Governo", cor="Preto", preco=7500, categoria=categoria, potenciaDaFonte=200)
    desktop3 = Desktop(modelo="HP All In One", cor="Cinza", preco=5000, categoria=categoria, potenciaDaFonte=500)

    print("-----------------------------------------------------------------------------------------------------------------")
    print("DESKTOPS:")
    print(desktop1.getInformacoes())
    print(desktop2.getInformacoes())
    print(desktop3.getInformacoes())


    notebook1 = Notebook(modelo="Lenovo IdeaPad", cor="Branco", preco=1800, categoria=categoria, tempoBateria=4)
    notebook2 = Notebook(modelo="Dell G15", cor="Cinza", preco=4500, categoria=categoria, tempoBateria=10)
    notebook3 = Notebook(modelo="Asus Vivobook 15", cor="Preto", preco=3000, categoria=categoria, tempoBateria=8)
    print("-----------------------------------------------------------------------------------------------------------------")

    print("\n-----------------------------------------------------------------------------------------------------------------")
    print("NOTEBOOKS:")
    print(notebook1.getInformacoes())
    print(notebook2.getInformacoes())
    print(notebook3.getInformacoes())
    print("-----------------------------------------------------------------------------------------------------------------")


