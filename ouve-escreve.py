import speech_recognition as sr

def transcribe_continuous():
    recognizer = sr.Recognizer()

    # Use o microfone como fonte de áudio
    with sr.Microphone() as source:
        print("Diga alguma coisa...")
        recognizer.adjust_for_ambient_noise(source)  # Ajuste do nível de ruído de fundo
        while True:
            try:
                audio = recognizer.listen(source, timeout=5)  # Escute por até 5 segundos
                text = recognizer.recognize_google(audio, language="pt-BR")
                print("Você disse:", text)
            except sr.UnknownValueError:
                print("Não foi possível reconhecer o áudio.")
            except sr.RequestError as e:
                print(f"Erro na requisição ao serviço de reconhecimento de fala: {e}")
            except sr.WaitTimeoutError:
                print("Tempo limite excedido. Pare de falar para finalizar a transcrição.")

if __name__ == "__main__":
    transcribe_continuous()
