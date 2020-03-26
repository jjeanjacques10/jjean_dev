# Author: Jean J Barros
# Github: https://github.com/jjeanjacques10/

# --- Criando um chatbot simples com chatterbot ---
from chatterbot import ChatBot

bot = ChatBot('Terminal')

trainer = ListTrainer(chatbot)

trainer.train([
    "Olá, como posso lhe ajudar?",
    "Gosto muito de programar",
    "O naruto pode ser duro as vezes..."
])

while True:
    try:
        user_input = input()
        bot_response = bot.get_response(user_input)
        print(bot_response)
    # Pressione ctrl-c ou ctrl-d para sair
    except (KeyboardInterrupt, EOFError, SystemExit):
        break