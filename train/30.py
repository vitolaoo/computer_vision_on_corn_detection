import os
import random
import shutil

# Caminho da pasta de origem
input_dir = "D:/CVCD_Data/ervas_da_boa"  # ajuste para sua pasta
extensoes_validas = ('.jpg', '.jpeg', '.png')

# Listar todos os arquivos válidos
arquivos = [f for f in os.listdir(input_dir) if f.lower().endswith(extensoes_validas)]

# Embaralhar e selecionar 30%
random.shuffle(arquivos)
quantidade = int(len(arquivos) * 0.3)
selecionados = arquivos[:quantidade]

# Renomear os arquivos selecionados
for i, nome_original in enumerate(selecionados, start=9001):
    extensao = os.path.splitext(nome_original)[1]
    novo_nome = f"val_{i}{extensao}"
    
    caminho_antigo = os.path.join(input_dir, nome_original)
    caminho_novo = os.path.join(input_dir, novo_nome)

    os.rename(caminho_antigo, caminho_novo)

print(f"{quantidade} arquivos foram renomeados com sucesso.")
