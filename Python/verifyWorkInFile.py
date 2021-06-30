with open('file.txt', 'r') as f:
    data = f.read()
    word = 'Agumon'
    if(word in data):
        print(f'{word} está no arquivo!')
    else:
        print(f'{word} não foi encontrado...')
