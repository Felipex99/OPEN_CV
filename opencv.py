import cv2 as cv
from scale import rescale_frame
import os
os.chdir("assets")
#print(os.getcwd())
# --------------------------------- ABRINDO IMAGENS OPEN CV ---------------------------------------------------------------------------------------------------------------------------
#dog = cv.imread("C:/Users/DELL/Documents/Projetos de IA/OPEN_CV/assets/imagem_5_cachorros.jpg")
#cv.imshow("Cachorro",dog)
#cv.waitKey(0) #Utilizado para que quando a imagem abra, ela só feche se apertar 0, senão ela abre e fecha rapido
#nos vídeos o cv.waitKey também é usado para determinar o tempo de cada frame do vídeo, quanto maior mais lento o vídeo, quanto menor, mais rápido


# --------------------------------- MANIPULANDO VÍDEOS ---------------------------------------------------------------------------------------------------------------------------
# capture = cv.VideoCapture('C:/Users/DELL/Documents/Projetos de IA/OPEN_CV/assets/video_gato.mp4')
# video = [] 
# while True:
#     isTrue, frame = capture.read()
#     video.append(frame)
#     cv.imshow("VIIIIIDEO",frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

# --------------------------------- MANIPULANDO ESCALAS DAS IMAGENS E VÍDEOS ---------------------------------------------------------------------------------------------------------------------------

# img = cv.imread("imagem_5_cachorros.jpg")
# cv.imshow("Cacho",img)

#CRIANDO UMA FUNÇÃO PARA REDIMENSIONAR OS FRAMES
# def rescaleFrame(frame, scale=0.75):
#     width = int(frame.shape[1]*scale)
#     height = int(frame.shape[0]*scale)
    
#     dimensions = (width,height)
#     return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
video = cv.VideoCapture("video_gato.mp4")
while True:
    isTrue, frame = video.read()
    menor = rescale_frame(frame,0.50)
    cv.imshow("VIDEO DO GATIM",frame)
    cv.imshow("menor",menor)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
cv.release()
cv.destroyAllWindows()
cv.waitKey(0)







































