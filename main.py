from spleeter.separator import Separator
import speech_recognition as sr
from transformers import pipeline
import librosa  # For audio file handling

# Step 1: Load audio and separate vocals
audio_file = "./kings_and_queens.mp3"
separator = Separator("spleeter:2stems")  # 2stems = vocals + accompaniment
separator.separate_to_file(audio_file, "output/")  # Outputs vocal track to "output/song/vocals.wav"

# Step 2: Transcribe vocals to text
recognizer = sr.Recognizer()
vocal_file = "output/song/vocals.wav"
with sr.AudioFile(vocal_file) as source:
    audio_data = recognizer.record(source)
    transcribed_lyrics = recognizer.recognize_google(audio_data)  # Requires internet and API key

# Step 3: Summarize the transcribed lyrics
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summary = summarizer(transcribed_lyrics, max_length=50, min_length=25, do_sample=False)[0]["summary_text"]

# Step 4: Categorize the summary
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
categories = ["love", "politics", "nature"]
result = classifier(summary, candidate_labels=categories)
category = result["labels"][0]

# Step 5: Output results
print(f"Summary: {summary}")
print(f"Category: {category}")
