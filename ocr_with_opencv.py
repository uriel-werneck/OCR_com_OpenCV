import pytesseract
import cv2

# definindo o path do tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\uriel\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

# lendo e apresentando a imagem original
imagem_original = cv2.imread('./images/imagem_borrada.jpg')
cv2.imshow('IMAGEM ORIGINAL', imagem_original)

# fazendo ocr na imagem original
texto_imagem_original = pytesseract.image_to_string(imagem_original)
print(texto_imagem_original)

# usando OpenCV para otimizar a imagem original
imagem_cinza = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)
imagem_otimizada = cv2.adaptiveThreshold(imagem_cinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255, 5)

# apresentando a imagem otimizada
cv2.imwrite('./images/imagem_otimizada.jpg', imagem_otimizada)
cv2.imshow('IMAGEM OTIMIZADA', imagem_otimizada)

# realizando OCR na imagem otimizada
texto_imagem_otimizada = pytesseract.image_to_string(imagem_otimizada)
print(texto_imagem_otimizada)

# "0" fecha as janelas abertas
cv2.waitKey(0)