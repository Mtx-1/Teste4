import cv2
from cvzone.HandTrackingModule import HandDetector

webcan = cv2.VideoCapture(0)
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    sucesso, imagem = webcan.read()
    coordenadas, imagem_maos = rastreador.findHands(imagem)

    cv2.imshow('projeto 4 - IA', imagem)

    print(coordenadas)

    if cv2.waitKey(1) != -1:
        break

webcan.release()
cv2.destroyAllWindows()    
