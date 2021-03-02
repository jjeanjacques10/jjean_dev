import re
message = "Entre em contato: jjean_dev@teste.com ou jjean@teste2.com"

emails = re.findall(r'[\w\.-]+@[\w\.-]+',message)
print(emails)