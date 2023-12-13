from decouple import config
import whisper


# api_key = config("OPENAI_API_KEY")

# client = OpenAI(api_key=api_key)

model = whisper.load_model("base")

def transcribe(audio):
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    return result.text


def main():
    # arquivo só para teste, excluir dps
    speech_text = transcribe("/content/harvard.wav")
    print(speech_text)

if __name__ == "__main__":
    main()