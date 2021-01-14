import wikipedia

wikipedia.set_lang("pt")
info = wikipedia.summary('Guido van Rossum')

print(info)