### Autor: Vitor de Jesus ###
   ### Projeto: ROVI-BR ###
       ### TCC DS ###

import json
import time
import cv2

#try:
while (1):
    with open("Teste.json", encoding='utf-8') as teste:
        dados = json.load(teste)
    for i in dados:
        valor = (i['valor'])
    print(valor)

    if (valor==0):
        logo = cv2.imread('C:/Users/vitor.jesus/Desktop/Dev/TCC_ROVI_FIRMWARE/Logo.png', cv2.IMREAD_COLOR)
        logo = cv2.resize(logo,(int(1280),int(780)))
        cv2.imshow('ROVI-BR', logo)
        cv2.waitKey()

    else:
        carga = cv2.imread('C:/Users/vitor.jesus/Desktop/Dev/TCC_ROVI_FIRMWARE/Carga.png', cv2.IMREAD_COLOR)
        carga = cv2.resize(carga,(int(1280),int(780)))
        cv2.imshow('ROVI-BR', carga)
        cv2.waitKey()

#except:
 #   print("Deu Ruim")
# largura, altura, canais = imagem.shape   #Caso queira utilizar o tamanho da imagem