import wikipedia

wikipedia.set_lang("pt")
info = wikipedia.summary('Kotlin')

print(info)