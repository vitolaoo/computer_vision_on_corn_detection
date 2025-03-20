from PIL import Image
import os
import rasterio

im = Image.open("teste.jpg")

r, g, b = im.split()

"""
r.save("r.jpg")
g.save("g.jpg")
b.save("b.jpg")"

r.show()
g.show()
b.show()"
"""

largura_fatia, altura_fatia = 600, 600

largura, altura = im.size

output_dir = "fragmentos"
os.makedirs(output_dir, exist_ok=True)

contador = 1
for i in range(0, altura, altura_fatia):
    for j in range(0, largura, largura_fatia):
    
        caixa = (j, i, j + largura_fatia, i + altura_fatia)
        fragmento = im.crop(caixa)

        # Verificando se o fragmento tem tamanho correto
        if fragmento.size == (largura_fatia, altura_fatia):
            # Separar canais RGB
            r, g, b = fragmento.split()

            # Criar subpastas para R, G e B
            os.makedirs(f"{output_dir}/R", exist_ok=True)
            os.makedirs(f"{output_dir}/G", exist_ok=True)
            os.makedirs(f"{output_dir}/B", exist_ok=True)

            # Salvar os fragmentos de cada canal
            r.save(f"{output_dir}/R/fragmento_{contador}_R.jpg")
            g.save(f"{output_dir}/G/fragmento_{contador}_G.jpg")
            b.save(f"{output_dir}/B/fragmento_{contador}_B.jpg")

            print(f"Fragmento {contador} salvo!")
            contador += 1
