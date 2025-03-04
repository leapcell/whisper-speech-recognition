# Whisper Speech Recognition Service

This project demonstrates how to deploy a local speech recognition service using OpenAI's Whisper model in a Python environment with Flask. The goal is to help users learn how to deploy AI models with Leapcell (leapcell.io).

## Prerequisites

Before running the application, you need to prepare the environment by setting up dependencies and downloading the necessary Whisper model. Execute the following script:

```bash
sh prepare_env.sh
```

This will:

1. Install the required Python packages including Flask, Gunicorn, and necessary dependencies.
2. Install PyTorch and related libraries (specifically for CPU usage).
3. Install or update the OpenAI Whisper library.
4. Download the necessary Whisper model using a Python script.

## Project Structure

```plaintext
.
├── LICENSE                           # License file for the project
├── download_model.py                 # Python script to download the necessary Whisper model
├── prepare_env.sh                    # Script for setting up the environment and downloading model
├── static
│   └── audio_files
│       └── demo.wav                  # Sample audio file for testing the service
└── templates
    └── index.html                   # HTML template for the main page of the service
```

## Running the Application

Once you've prepared the environment, you can start the web service with the following command:

```bash
gunicorn -w 4 app:app
```

This will launch the Flask application using Gunicorn for production deployment. The service will be available at `http://localhost:5000`, and you can upload an audio file for transcription. It will return the transcribed text.

---

### Explanation of `prepare_env.sh`

This script is responsible for setting up the environment and downloading the Whisper model. Here's a breakdown of what each line does:

```bash
#!/bin/sh

# Exit immediately if a command exits with a non - zero status
set -e

# Install Flask, python - multipart and Gunicorn
pip install flask python-multipart gunicorn

# Install PyTorch and related libraries (torchvision, torchaudio)
# from the CPU - only wheel index of PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install or update the OpenAI Whisper library
pip install -U openai-whisper

# Run a Python script to download the necessary Whisper model
# This script will download the model in build step
python download_model.py
```

- `set -e`: Ensures that the script stops if any command fails.
- `pip install flask python-multipart gunicorn`: Installs Flask (for the web service), `python-multipart` (for handling file uploads), and Gunicorn (a production-grade WSGI HTTP server).
- `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu`: Installs PyTorch and related libraries (optimized for CPU) for running the Whisper model.
- `pip install -U openai-whisper`: Installs or updates the OpenAI Whisper library.
- `python download_model.py`: Runs the Python script to download the necessary Whisper model for transcription.

---

## Contact Support

If you have any issues or questions, feel free to reach out to support@leapcell.io.
