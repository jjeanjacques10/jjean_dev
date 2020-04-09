# Author: Jean J Barros
# Github: https://github.com/jjeanjacques10/

# --- Acessando o texto de um arquivo PDF ---
from PyPDF2 import PdfFileReader

path = 'pdf/123.pdf'

with open(path, 'rb') as f:
    pdf = PdfFileReader(f)
    page = pdf.getPage(0)
    text = page.extractText()

print(text)