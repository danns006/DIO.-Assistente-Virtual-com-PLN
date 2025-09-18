---

## 🧠 assistente_virtual.py

```python
# ================================
# Assistente Virtual com PLN
# ================================

# Módulo 1: Texto para Fala
# -------------------------
# Transforma texto em áudio usando pyttsx3

import pyttsx3

def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# Módulo 2: Fala para Texto
# -------------------------
# Captura áudio do microfone e converte em texto usando speech_recognition

import speech_recognition as sr

def ouvir():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Pode falar...")
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language='pt-BR')
        print(f"🗣️ Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        print("❌ Não entendi o que você disse.")
        return ""
    except sr.RequestError:
        print("⚠️ Erro ao conectar com o serviço de reconhecimento.")
        return ""

# Módulo 3: Comandos Automatizados
# --------------------------------
# Interpreta o texto reconhecido e executa ações como abrir sites

import webbrowser

def executar_comando(comando):
    comando = comando.lower()

    if "wikipedia" in comando:
        termo = comando.replace("pesquisar", "").replace("no wikipedia", "").strip()
        url = f"https://pt.wikipedia.org/wiki/{termo}"
        webbrowser.open(url)
        falar(f"Abrindo Wikipedia para {termo}")

    elif "youtube" in comando:
        webbrowser.open("https://www.youtube.com")
        falar("Abrindo YouTube")

    elif "farmácia" in comando:
        webbrowser.open("https://www.google.com/maps/search/farmácia+próxima")
        falar("Mostrando farmácias próximas")

    else:
        falar("Desculpe, não reconheci esse comando.")

# Loop Principal
# --------------
# Escuta continuamente e executa comandos reconhecidos

def iniciar_assistente():
    falar("Olá! Sou seu assistente virtual. Pode falar um comando.")
    while True:
        comando = ouvir()
        if comando:
            executar_comando(comando)

# Para rodar o assistente, descomente a linha abaixo:
# iniciar_assistente()
