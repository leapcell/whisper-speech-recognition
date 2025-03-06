import whisper


# load the whisper model in build step
# for faster inference, we choose the "tiny" model, you can choose other models
def load_whisper_model():
    return whisper.load_model("tiny", download_root="models")


if __name__ == "__main__":
    model = load_whisper_model()
