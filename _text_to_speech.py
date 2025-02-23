from gtts import gTTS
import os

def text_to_speech(text, language='pt-br'):
    """
    Converts text to speech and plays the audio.

    Args:
        text: The text to convert to speech.
        language: The language of the text (default: 'pt-br').
    """
    try:
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save("speech.mp3")
        os.system("start speech.mp3")  # No Windows
        # os.system("mpg321 speech.mp3")  # No Linux/Mac
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    user_input = input("Digite o texto que deseja converter para fala (ou 'sair' para encerrar): ")
    if user_input.lower() == "sair":
        print("Encerrando o programa.")
        break
    text_to_speech(user_input)
