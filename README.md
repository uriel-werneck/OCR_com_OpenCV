# 📝 OCR_with_OpenCV

## 📄 Descrição
Este projeto demonstra como o OpenCV pode ser utilizado para pré-processar imagens e melhorar os resultados do OCR (Optical Character Recognition) utilizando o Pytesseract.
A abordagem inclui técnicas de otimização de imagem, como conversão para tons de cinza, limiarização (thresholding) e remoção de ruídos, para aumentar a precisão na extração de textos.

## 🚀 Tecnologias Utilizadas
- **Visão Computacional:** OpenCV
- **Reconhecimento de Texto:** Pytesseract
- **Visualização:** Matplotlib
- **Ambiente de Execução:** Jupyter Notebook

## ⚙️ Configuração do Tesseract
Além das bibliotecas Python, é necessário instalar o Tesseract OCR no sistema:
### Windows
Baixe o instalador em: [Tesseact OCR](https://github.com/UB-Mannheim/tesseract/wiki).
### Linux
```bash
sudo apt update
sudo apt install tesseract-ocr
```
### Configuração no Código
```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Caminho para o Windows
```

## 📦 Instalação das Dependências
```bash
pip install -r requirements.txt
```

## 🖼️ Exemplo de Otimização de Imagem
### Imagem Original
![original](https://github.com/user-attachments/assets/73b046da-8e0f-4824-ada7-acb15381e0c9)
### Imagem Otimizada
![otimizada](https://github.com/user-attachments/assets/84c3c648-a0d5-4f75-80f0-2a32e56a7ba3)
