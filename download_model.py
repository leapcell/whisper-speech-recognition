import whisper


# load the whisper model in build step
def load_whisper_model():
    return whisper.load_model("base", download_root="models")

if __name__ == "__main__":
    model = load_whisper_model()
