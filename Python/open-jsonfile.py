# Author: Jean J Barros
# Github: https://github.com/jjeanjacques10/

# --- Pegando o conteúdo de um arquivo Json ---
import json

with open(f'./config.json', 'r') as f:
    content = json.loads(f.read())
f.close()

user = content['user']
password = content['password']
website = content['website']

print(f"Usuário: {user} \n Senha: {password}")
