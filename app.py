import speech_recognition as sr

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()

    # Abra o arquivo de áudio
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)  # Leitura do áudio

    try:
        # Realize a transcrição utilizando o mecanismo de reconhecimento de fala gratuito
        text = recognizer.recognize_google(audio, language="pt-PT")
        return text
    except sr.UnknownValueError:
        return "Não foi possível reconhecer o áudio."
    except sr.RequestError as e:
        return f"Erro na requisição ao serviço de reconhecimento de fala: {e}"

# Exemplo de uso:
audio_file_path = "./teste.wav"
transcription = transcribe_audio(audio_file_path)
print("A transcrever aguarde...")
print(transcription)
