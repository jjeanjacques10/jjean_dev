# Author: Jean J Barros
# Github: https://github.com/jjeanjacques10/

# --- Fazendo requests com Python ---
import requests

r = requests.get('https://github.com/timeline.json')

print(r.text) #Resposta do GET