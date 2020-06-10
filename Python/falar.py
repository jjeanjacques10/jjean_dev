# Author: Jean J Barros
# Github: https://github.com/jjeanjacques10/

# --- Fala para texto ---
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Fale: ")
    audio = r.listen(source)

print(r.recognize_google(audio))