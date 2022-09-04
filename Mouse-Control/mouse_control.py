'''
============================================
Estudante: Guilherme Ceratti
============================================
'''

# Fazendo as importações necessárias
import cv2 as cv
import numpy as np
import pyautogui

# Configura funções do pyautogui
pyautogui.FAILSAFE = False
# Define uma variável para trabalhar com a câmera
camera = cv.VideoCapture(0)
# Captura o tamanho da tela onde o mouse se moverá
b, c = pyautogui.size()
# Cria uma variável boolean para executar e fechar o programa
execute = True

# Criando um while para não encerrar a execução da câmera no processo
while execute == True:
    # Faz as leituras dos frames da câmera, basicamente serve 
    # para identificar os objetos distintos na câmera
    _, frame = camera.read()
    # Inverte a imagem da câmera
    frame = cv.flip(frame, 1)
    # Transforma para o padrão HSV para leitura e identificação dos objetos
    frameHsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # Valores do azul em HSV
    lowerBlue = np.array([94, 80, 2])
    upperBlue = np.array([130, 255, 255])
    # Criando a máscara que apresenta apenas o azul
    maskBlue = cv.inRange(frameHsv, lowerBlue, upperBlue)
    # Aplica a máscara e apresenta o result
    resultBlue = cv.bitwise_and(frame, frame, mask=maskBlue)
    frameBlue = cv.cvtColor(resultBlue, cv.COLOR_BGR2GRAY)
    
    # Valores do verde em HSV
    lowerGreen = np.array([70,100,98])
    upperGreen = np.array([100, 255,255])
    maskGreen = cv.inRange(frameHsv, lowerGreen, upperGreen)
    resultGreen = cv.bitwise_and(frame, frame, mask=maskGreen)
    frameGreen = cv.cvtColor(resultGreen, cv.COLOR_BGR2GRAY)
    
    # Valores do amarelo em HSV
    lowerYellow = np.array([20, 100, 100])
    upperYellow = np.array([30, 255, 255])
    maskYellow = cv.inRange(frameHsv, lowerYellow, upperYellow)
    resultYellow = cv.bitwise_and(frame, frame, mask=maskYellow)
    frameYellow = cv.cvtColor(resultYellow, cv.COLOR_BGR2GRAY)

    # Valores do vermelho em HSV
    lowerRed = np.array([160, 70, 100])
    upperRed = np.array([255, 255, 255])
    maskRed = cv.inRange(frameHsv, lowerRed, upperRed)
    resultRed = cv.bitwise_and(frame, frame, mask=maskRed)
    frameRed = cv.cvtColor(resultRed, cv.COLOR_BGR2GRAY)

    # Utiliza a máscara para captar o azul no frame da cam
    _, thresh = cv.threshold(frameBlue, 2, 255, cv.THRESH_BINARY)
    # Gera contornos para os objetos na cor azul
    contornos, _ = cv.findContours(
        thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    # Aplica os contornos gerados em todas os objetos daquela cor
    # enquanto aparecem na cam
    for contorno in contornos:
        # Capta as posições x, y, w, h do objeto para desenhar o contorno
        (x, y, w, h) = cv.boundingRect(contorno)
        # Sabendo as posições ele retorna o tamanho
        area = cv.contourArea(contorno)
        # Cria uma condição para identificar apenas o objeto em questão,
        # essa condição leva em conta apenas o tamanho do objeto
        if area > 1000:
            # Insere texto indicando que apenas o Mouse foi localizado
            cv.putText(frame, "Mouse Detectado", (10, 50),
                        cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0))
            # Gera um retangulo ao redor do texto
            cv.rectangle(frame, (0, 20), (300, 60), (0, 0, 0), 2)
            # Desenha os contornos ao redor da cor detectada
            cv.drawContours(frame, contorno, -1, (0, 0, 0), 5)
            # Gera um retangulo ao redor do objeto detectado
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
            # Pega o tamanho da tela e define a posição do objeto
            # em x e y
            p = int((b*x)/580)
            q = int((c*y)/440)
            # Faz a movimentação do mouse para as posições onde o objeto está
            pyautogui.moveTo(p, q)
    
    _, thresh = cv.threshold(frameGreen, 2, 255, cv.THRESH_BINARY)
    contornos, _ = cv.findContours(
        thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    for contorno in contornos:
        (x, y, w, h) = cv.boundingRect(contorno)
        area = cv.contourArea(contorno)
        if area > 1000:
            cv.putText(frame, "Botao direito Detectado", (10, 100),
                        cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))
            cv.rectangle(frame, (0, 70), (410, 110), (0, 0, 0), 2)
            cv.drawContours(frame, contorno, -1, (0, 0, 0), 5)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
            # Faz o clique com o botão direito do mouse
            pyautogui.click(button='right')
    
    _, thresh = cv.threshold(frameYellow, 2, 255, cv.THRESH_BINARY)
    contornos, _ = cv.findContours(
        thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    for contorno in contornos:
        (x, y, w, h) = cv.boundingRect(contorno)
        area = cv.contourArea(contorno)
        if area > 1000:
            cv.putText(frame, "Botao esquerdo Detectado", (10, 150),
                        cv.FONT_HERSHEY_SIMPLEX, 1, (0,165,255))
            cv.rectangle(frame, (0, 120), (450, 160), (0, 0, 0), 2)
            cv.drawContours(frame, contorno, -1, (0, 0, 0), 5)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1) 
            # Faz o clique com o botão esquerdo do mouse
            pyautogui.click(button='left')   
    
    _, thresh = cv.threshold(frameRed, 2, 255, cv.THRESH_BINARY)
    contornos, _ = cv.findContours(
        thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    for contorno in contornos:
        (x, y, w, h) = cv.boundingRect(contorno)
        area = cv.contourArea(contorno)
        if area > 1000:
            # Altera o valor do boolean que faz o projeto rodar
            # causando o fechamento do mesmo
            execute = False

    # Mostra a imagem exibida na câmera
    cv.imshow("Camera", frame)
    # Cria uma "chave" para fechar o programa
    key = cv.waitKey(60)
    # Define a chave como esc
    if key == 27:
        # Encerra o while, fechando o programa
        break
# Fecha as janelas abertas no programa
cv.destroyAllWindows()
# "Libera" a câmera, garantindo que ela não ficará
# aberta após fechar o programa
camera.release()