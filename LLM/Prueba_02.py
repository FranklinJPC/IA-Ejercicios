# import speech_recognition as sr
# import pyttsx3
# reconocimiento = sr.Recognizer()

# # Especificar el archivo de audio de entrada 
# engine = pyttsx3.init()
# engine.say("Hola ALGO..........")
# engine.runAndWait()
# with sr.Microphone() as source:
#     print("Hola en que puedo ayudarte?")
#     audio = reconocimiento.listen(source)

# # Imprimir el texto del audio

# print("Acabas de decir: ")
# frase = reconocimiento.recognize_google(audio, language='es-EC')
# print(frase)

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


import speech_recognition as sr
import time
import pyttsx3

def Manejo_instrucciones():
    reconocimiento = sr.Recognizer()
    engine = pyttsx3.init()
    with sr.Microphone() as source:
        print("Hola, ¿en qué puedo ayudarte?\n")
        engine.say("Hola, ¿en qué puedo ayudarte?")
        engine.runAndWait()
        # voices = engine.getProperty('voices')
        # for voice in voices:
        #     engine.setProperty('voice', voice.id)
        #     engine.say('The quick brown fox jumped over the lazy dog.')
        # engine.runAndWait()
        # audio = reconocimiento.listen(source)

    try:
        frase = reconocimiento.recognize_google(audio, language="es-EC")
        print("Usuario: ", frase)

        Manejo_Reglas(frase.lower())
    except sr.UnknownValueError:
        print("Lo siento, no pude entender lo que dijiste.\n")
    except sr.RequestError as e:
        print("No se pudo obtener una respuesta de Google Speech Recognition; {0}\n".format(e))

def Manejo_Reglas(instruccion):
    if "hola" in instruccion:
        print("Hola, ¿en qué puedo ayudarte?\n")
        time.sleep(1.5)

    elif "encender la luz de la cocina" in instruccion:
        print("Estoy encendiendo la luz de la cocina para ti.\n")
        time.sleep(1.5)

    elif "enciende el microondas" in instruccion:
        print("estoy encendiendo el microondas.\n")
        time.sleep(1.5)

    elif "enciende el horno" in instruccion:
        print("Estoy encendiendo el horno\n")
        time.sleep(1.5)

    elif "abre la ventana" in instruccion:
        print("Estoy abriendo la ventana\n")
        time.sleep(1.5)

    elif "finalizar" in instruccion:
        print("Hasta luego. ¡Que tengas un buen día!\n")
        time.sleep(1.5)
        exit()
    else:
        print("Instrucción no reconocida. Por favor, intenta nuevamente.\n")
        time.sleep(1.5)

if __name__ == "__main__":
    while True:
        Manejo_instrucciones()