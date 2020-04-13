# Author: Jean J Barros
# Github: https://github.com/jjeanjacques10/

# --- Criando um arquivo ZIP ---
import zipfile

zf = zipfile.ZipFile("jjean_compress.zip", "w")
zf.write("meu_arquivo.txt", compress_type=zipfile.ZIP_DEFLATED)

zf.close()