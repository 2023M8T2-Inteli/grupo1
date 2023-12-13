# from decouple import config
# import whisper

from openai import OpenAI


api_key = config("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


class STT:
    def __init__(self, filename=None):
        self.model = whisper.load_model("base")
        self.filename = filename


    def transcribe(self):
        if self.filename is not None:
            # load audio and pad/trim it to fit 30 seconds
            audio = whisper.load_audio(self.filename)
            audio = whisper.pad_or_trim(audio)

            # make log-Mel spectrogram and move to the same device as the model
            mel = whisper.log_mel_spectrogram(audio).to(self.model.device)

            # detect the spoken language
            _, probs = self.model.detect_language(mel)
            print(f"Detected language: {max(probs, key=probs.get)}")

            # decode the audio
            options = whisper.DecodingOptions()
            result = whisper.decode(self.model, mel, options)
            return result.text


def main():
    # stt = STT(filename='./media/harvard.wav')
    # speech_text = stt.transcribe()
    # # arquivo só para teste, excluir dps
    # # speech_text = transcribe("./media/harvard.wav")
    # print(speech_text)
    client = OpenAI()

    audio_file = open("./media/harvard.wav", "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
    )
    print(transcript)

if __name__ == "__main__":
    main()