#!/bin/sh

# Exit immediately if a command exits with a non - zero status
set -e

echo "Preparing the environment..."
# Install Flask, python - multipart and Gunicorn
pip install flask python-multipart gunicorn

# Install PyTorch and related libraries (torchvision, torchaudio)
# from the CPU - only wheel index of PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install or update the OpenAI Whisper library
pip install -U openai-whisper

# Run a Python script to download the necessary Whisper model
# This script will download the model in build step
echo "Downloading the Whisper model..."
python download_model.py