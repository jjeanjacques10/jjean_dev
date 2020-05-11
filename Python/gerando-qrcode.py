# Author: Jean J Barros
# Github: https://github.com/jjeanjacques10/

# --- Gerando Qrcode ---
import pyqrcode

site = "https://www.instagram.com/jjean_dev/"
url = pyqrcode.create(site)
url.svg("instagramQrCode.svg", scale=10)