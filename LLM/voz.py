# Instalar las librerias necesarias

import speech_recognition as sr
import webbrowser as wb

reconocimiento = sr.Recognizer()

# Especificar el archivo de audio de entrada 

with sr.Microphone() as source:
    print("Hola en que puedo ayudarte?")
    audio = reconocimiento.listen(source)

# Imprimir el texto del audio

print("Acabas de decir: ")
frase = reconocimiento.recognize_google(audio, language='es-EC')
print(frase)
url="https://www.google.com/search?q="
wb.open(url+frase)

# import speech_recognition as sr
# import pyttsx3

# def reconocer_instrucciones():
#     reconocimiento = sr.Recognizer()
#     engine = pyttsx3.init()

#     with sr.Microphone() as source:
#         print("Hola, ¿en qué puedo ayudarte?")
#         engine.say("Hola, ¿en qué puedo ayudarte?")
#         engine.runAndWait()
#         audio = reconocimiento.listen(source)

#     try:
#         frase = reconocimiento.recognize_google(audio, language="es-EC")
#         print("Usuario: ", frase)

#         # Procesar la instrucción y obtener la respuesta
#         respuesta = procesar_instruccion(frase.lower()) # Convertir a minúsculas para facilitar el manejo de instrucciones

#         # Reproducir la respuesta en voz
#         engine.say(respuesta)
#         engine.runAndWait()
#     except sr.UnknownValueError:
#         print("Lo siento, no pude entender lo que dijiste.")
#     except sr.RequestError as e:
#         print("No se pudo obtener una respuesta de Google Speech Recognition; {0}".format(e))

# def procesar_instruccion(instruccion):
#     if "reproducir" in instruccion:
#         return "Estoy reproduciendo música o videos para ti."
#     elif "información" in instruccion:
#         return "Estoy proporcionando información sobre un tema específico."
#     elif "salir" in instruccion:
#         return "Hasta luego. ¡Que tengas un buen día!"
#     else:
#         return "Instrucción no reconocida. Por favor, intenta nuevamente."

# if __name__ == "__main__":
#     while True:
#         reconocer_instrucciones()