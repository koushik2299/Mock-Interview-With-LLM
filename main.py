import whisper
import os

# Load the Whisper model
model = whisper.load_model("base")

# Define the path to the audio file using a raw string
file_path = "C:/Users/Koushik/OneDrive/Documents/GitHub/Mock-Interview-With-LLM/test.mp3"


# Transcribe the audio file
results = model.transcribe(file_path)

# Write the transcription to a text file
with open("C:/Users/Koushik/OneDrive/Documents/GitHub/Mock-Interview-With-LLM/requirments.txt", "w") as f:
    f.write(results["text"])
