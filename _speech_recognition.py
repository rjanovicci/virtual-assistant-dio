import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import urllib.parse
from youtube_search import YoutubeSearch

def main():
    r = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        with mic as source:
            print("Ajustando para ruído ambiente... Aguarde.")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Fale algo!")
            try:
                audio = r.listen(source, timeout=5)
            except sr.WaitTimeoutError:
                print("Tempo limite de áudio excedido. Tente novamente.")
                continue

        try:
            text = r.recognize_google(audio, language="pt-BR")
            print("Você disse: " + text)
            if text.lower() == "encerrar":
                print("Encerrando a aplicação...")
                break

            if text.lower().startswith("buscar significado de"):
                termo = text[len("buscar significado de"):].strip()
                if termo:
                    termo_encoded = urllib.parse.quote(termo)
                    url = f"https://pt.wikipedia.org/wiki/{termo_encoded}"
                    print(f"Abrindo o navegador para buscar o significado de '{termo}'...")
                    webbrowser.open(url)
                else:
                    print("Nenhum termo de busca informado para Wikipedia.")
            elif text.lower().startswith("buscar no youtube"):
                query = text[len("buscar no youtube"):].strip()
                if query:
                    print(f"Buscando no YouTube: {query}")
                    results = YoutubeSearch(query, max_results=1).to_dict()
                    if results:
                        video_url = "https://www.youtube.com" + results[0]['url_suffix']
                        print(f"Abrindo o primeiro vídeo: {video_url}")
                        webbrowser.open(video_url)
                    else:
                        print("Nenhum vídeo encontrado para a busca.")
                else:
                    print("Nenhum termo de busca informado para o YouTube.")
            else:
                print("Texto reconhecido: " + text)
        except sr.UnknownValueError:
            print("Não consegui entender o áudio.")
        except sr.RequestError as e:
            print("Erro na requisição ao serviço do Google Speech Recognition; {0}".format(e))

if __name__ == "__main__":
    main()
