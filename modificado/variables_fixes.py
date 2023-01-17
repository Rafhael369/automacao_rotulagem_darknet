class_names = []

with open("models/coco.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

#ID DAS CLASSES E CAMINHOS
id_pessoa, caminho_pessoa_imagem, caminho_pessoa_voc, caminho_pessoa_yolo, objeto_pessoa = 0, "imagens_rotulos/pessoa/imagem/pessoa", "imagens_rotulos/pessoa/voc/pessoa", "imagens_rotulos/pessoa/yolo/pessoa", "person"
id_placa, caminho_placa_imagem, caminho_placa_voc, caminho_placa_yolo, objeto_placa = 1, "imagens_rotulos/placa/imagem/placa", "imagens_rotulos/placa/voc/placa", "imagens_rotulos/placa/yolo/placa", "license plate"
id_moto, caminho_moto_imagem, caminho_moto_voc, caminho_moto_yolo, objeto_moto = 2, "imagens_rotulos/moto/imagem/moto", "imagens_rotulos/moto/voc/moto", "imagens_rotulos/moto/yolo/moto", "motorcycle"
id_carro, caminho_carro_imagem, caminho_carro_voc, caminho_carro_yolo, objeto_carro = 3, "imagens_rotulos/carro/imagem/carro", "imagens_rotulos/carro/voc/carro", "imagens_rotulos/carro/yolo/carro", "car"
id_caminhao, caminho_caminhao_imagem, caminho_caminhao_voc, caminho_caminhao_yolo, objeto_caminhao = 4, "imagens_rotulos/caminhao/imagem/caminhao", "imagens_rotulos/caminhao/voc/caminhao", "imagens_rotulos/caminhao/yolo/caminhao", "truck"
id_onibus, caminho_onibus_imagem, caminho_onibus_voc, caminho_onibus_yolo, objeto_onibus = 5, "imagens_rotulos/onibus/imagem/onibus", "imagens_rotulos/onibus/voc/onibus", "imagens_rotulos/onibus/yolo/onibus", "bus"