from flask import Flask, request, render_template
import os
import tempfile
import time
from download_model import load_whisper_model

# Import the Whisper library for speech recognition
import whisper

app = Flask(__name__)

# Configure example audio file information with descriptions
EXAMPLE_AUDIOS = [
    {
        "filename": "audio1.mp3",
        "description": "This is a sample audio about nature sounds.",
    },
    {
        "filename": "audio2.mp3",
        "description": "This audio contains a short speech about technology.",
    },
    {
        "filename": "audio3.mp3",
        "description": "An audio recording of a beautiful song.",
    },
]


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    audio_duration = 0
    file_size = 0
    recognition_time = 0

    if request.method == "POST":
        # Check if an example audio is selected
        example_audio = request.form.get("example_audio")
        if example_audio:
            # Construct the file path for the selected example audio
            file_path = os.path.join("static", "audio_files", example_audio)
        else:
            # Get the uploaded audio file
            audio_file = request.files.get("audio_file")
            if audio_file:
                # Create a temporary file to save the uploaded audio
                with tempfile.NamedTemporaryFile(
                    delete=False, suffix=".wav"
                ) as temp_audio:
                    audio_file.save(temp_audio.name)
                    file_path = temp_audio.name
            else:
                # Render the template without a result if no audio is provided
                return render_template(
                    "index.html",
                    result=None,
                    example_audios=EXAMPLE_AUDIOS,
                    audio_duration=audio_duration,
                    file_size=file_size,
                    recognition_time=recognition_time,
                )

        # Record the start time for measuring recognition duration
        start_time = time.time()

        try:
            # Load the Whisper model (using the 'base' model here, can choose others)
            model = load_whisper_model()
            # Perform speech recognition on the audio file
            result_data = model.transcribe(file_path)
            # Extract the transcribed text from the result
            result = result_data["text"]
        except Exception as e:
            # Handle errors during speech recognition
            result = f"Speech recognition error: {e}"
        finally:
            # Delete the temporary audio file if it exists
            if "temp_audio" in locals():
                os.remove(temp_audio.name)

        # Record the end time and calculate the recognition duration
        end_time = time.time()
        recognition_time = round(end_time - start_time, 2)
        # Get the size of the audio file
        file_size = os.path.getsize(file_path)

    # Render the template with the result and other information
    return render_template(
        "index.html",
        result=result,
        example_audios=EXAMPLE_AUDIOS,
        audio_duration=audio_duration,
        file_size=file_size,
        recognition_time=recognition_time,
    )


if __name__ == "__main__":
    app.run(debug=True)
