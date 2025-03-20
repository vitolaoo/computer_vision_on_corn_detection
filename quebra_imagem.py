import rasterio
from PIL import Image

def split_image(input_path, output_folder, tile_size=600):
    # Abrir a imagem com rasterio
    with rasterio.open(input_path) as src:
        # Obter as dimensões da imagem
        width = src.width
        height = src.height
        
        # Ler a imagem inteira
        image = src.read([1, 2, 3])  # R, G e B 
        
        # Transpor para a ordem de canais, pois o rasterio retorna de forma diferente do Pillow
        image = image.transpose((1, 2, 0))  # Converte para formato (altura, largura, canais)

        # Criar uma imagem PIL
        pil_image = Image.fromarray(image)

        # Número de tiles no eixo X e Y
        num_tiles_x = (width // tile_size) + (1 if width % tile_size != 0 else 0)
        num_tiles_y = (height // tile_size) + (1 if height % tile_size != 0 else 0)

        # Quebrar em blocos de 600x600
        tile_id = 0
        for i in range(num_tiles_y):
            for j in range(num_tiles_x):
                # Definir as coordenadas do bloco
                left = j * tile_size
                upper = i * tile_size
                right = min((j + 1) * tile_size, width)
                lower = min((i + 1) * tile_size, height)

                # Cortar a imagem no bloco
                tile = pil_image.crop((left, upper, right, lower))

                # Salvar o bloco
                tile.save(f"{output_folder}/tile_{tile_id}.png")
                tile_id += 1

# Caminho para a imagem de entrada
input_path = 'Mangueirinha1.tif'

# Pasta de saída para os segmentos
output_folder = 'teste'

# Chamar a função
split_image(input_path, output_folder)
