# DIO.-Assistente-Virtual-com-PLN

# 🧠 Assistente Virtual com Processamento de Linguagem Natural

Este projeto implementa um sistema de assistência virtual utilizando técnicas de PLN (Processamento de Linguagem Natural) com Python. Ele possui três módulos principais:

1. **Text to Speech**: transforma texto em fala.
2. **Speech to Text**: reconhece fala e converte em texto.
3. **Comandos por voz**: executa ações como abrir Wikipedia, YouTube ou localizar farmácias próximas.

## ⚠️ Limitação do Colab

O módulo de reconhecimento de voz (`speech_recognition`) depende da biblioteca `PyAudio`, que **não funciona no Google Colab** por limitações de acesso ao microfone. Para testar o sistema completo, recomenda-se rodar o projeto localmente em um ambiente como VS Code ou Anaconda.

## ✅ Requisitos

Instale as bibliotecas com:

```bash
pip install pyttsx3 SpeechRecognition pyaudio
