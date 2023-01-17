import cv2
import pybboxes as pbx
from modificado.variables_fixes import *

def organizar(i, x, frame, classes, boxes, objeto_en, caminho_imagem, caminho_voc, caminho_yolo, id_classe):
    entrou = 0
    for (classid, box) in zip(classes, boxes):
        # print(x)
        if x == 51:
            x = 0
        if class_names[classid] == objeto_en[0] and x == 50:
            # print(class_names[classid], objeto_en)
            # cv2.rectangle(frame, box, (0, 255, 0), 2)
            cv2.imwrite(f"{caminho_imagem}{i}.jpg", frame)
            if entrou == 0:
                #Escrever arquivo VOC
                f = open(f"{caminho_voc}{i}.txt", "w")
                f.write(f"{len(boxes)}")
                for box in boxes:
                    voc_txt = f"{int(box[0])} {int(box[1])} {int(box[2])} {int(box[3])} {id_classe}"
                    f.write(f"\n{voc_txt}")
                f.close()
                
                #Escrever arquivo YOLO
                f = open(f"{caminho_yolo}{i}.txt", "w")
                j = 0
                for box in boxes:
                    voc = (int(box[0]), int(box[1]), int(box[2]), int(box[3]))
                    rotulo = pbx.convert_bbox(voc, from_type="voc", to_type="yolo", image_size=(frame.shape[1], frame.shape[0]))
                    r1, r2, r3, r4 = rotulo  # type: ignore
                    if j == 0:
                        f.write(f"{id_classe} {r1} {r2} {r3} {r4}")
                    else:
                        f.write(f"\n{id_classe} {r1} {r2} {r3} {r4}")
                    j += 1
                f.close()
                entrou += 1