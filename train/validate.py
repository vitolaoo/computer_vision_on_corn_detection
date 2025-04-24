import os
import re
from ultralytics import YOLO
import cv2

def detect_and_save(image_path, model_path, output_base_dir="results"):
    # Extraindo o nome da pasta do modelo (exemplo: "train2")
    model_folder = re.search(r'train\d+', model_path)
    if not model_folder:
        print("Erro: O caminho do modelo não segue o padrão esperado com 'trainX'.")
        return
    model_name = model_folder.group(0)

    # Criando o diretório de saída específico para o modelo
    model_output_dir = os.path.join(output_base_dir, model_name)
    os.makedirs(model_output_dir, exist_ok=True)

    # Carregando o modelo YOLO
    model = YOLO(model_path)

    # Carregando a imagem
    image = cv2.imread(image_path)
    if image is None:
        print(f"Erro: Não foi possível carregar a imagem '{image_path}'.")
        return

    # Realizando a detecção
    results = model.predict(image, conf=0.4)
    result = results[0]

    # Contagem de detecções por label
    detections = {}
    for box in result.boxes:
        label = int(box.cls[0])  # Classe detectada (0: corn, 1: weed)
        conf = box.conf[0]       # Confiança da detecção

        if label not in detections:
            detections[label] = {"count": 0, "total_conf": 0.0}
        detections[label]["count"] += 1
        detections[label]["total_conf"] += float(conf)

    # Imprimindo informações de detecções
    for label, stats in detections.items():
        avg_conf = stats["total_conf"] / stats["count"] if stats["count"] > 0 else 0
        print(f"Label {label}: {stats['count']} detecções, Precisão Média: {avg_conf:.2f}")

    # Nomeando o próximo arquivo na pasta do modelo
    existing_files = os.listdir(model_output_dir)
    file_count = len([f for f in existing_files if f.endswith(".jpg")])
    output_filename = f"{file_count + 1:02d}.jpg"
    output_path = os.path.join(model_output_dir, output_filename)

    # Desenhando as bounding boxes na imagem e salvando
    annotated_image = result.plot()
    cv2.imwrite(output_path, annotated_image)
    print(f"Resultados salvos em: {output_path}")

image_path = "D:/CVCD_Data/ervas_da_boa/erva2_rot90_ajustada.jpg"
model_path = "D:/computer_vision_on_corn_detection/train/runs/detect/train4/weights/best.pt"  

# Executar a detecção
detect_and_save(image_path, model_path)
