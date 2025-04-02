#!/usr/bin/env python3
import typer
import os
import assemblyai as aai
from spleeter.separator import Separator
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from textblob import TextBlob
from dotenv import load_dotenv


# load .env file to environment
load_dotenv()

app = typer.Typer()

# Download NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Set your AssemblyAI API key here
aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY')

@app.command()
def separate(input_file: str, output_dir: str = "output_directory"):
    """Separate vocals from an audio file using Spleeter."""
    if not os.path.exists(input_file):
        typer.echo(f"Error: File {input_file} not found.")
        raise typer.Exit(code=1)
    separator = Separator("spleeter:2stems")
    separator.separate_to_file(input_file, output_dir)
    typer.echo(f"Vocals separated to {output_dir}/{os.path.splitext(os.path.basename(input_file))[0]}/vocals.wav")

@app.command()
def transcribe(vocal_file: str, output_file: str = "lyrics.txt"):
    """Transcribe vocals to text using AssemblyAI."""
    if not os.path.exists(vocal_file):
        typer.echo(f"Error: File {vocal_file} not found.")
        raise typer.Exit(code=1)
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(vocal_file)
    if transcript.status == aai.TranscriptStatus.completed:
        with open(output_file, "w") as f:
            f.write(transcript.text)
        typer.echo(f"Lyrics saved to {output_file}: {transcript.text}")
    else:
        typer.echo(f"Transcription failed: {transcript.error}")
        raise typer.Exit(code=1)

@app.command()
def summarize(input_file: str = "lyrics.txt", output_file: str = "summary.txt"):
    """Summarize lyrics from a text file."""
    if not os.path.exists(input_file):
        typer.echo(f"Error: File {input_file} not found.")
        raise typer.Exit(code=1)
    with open(input_file, "r") as f:
        text = f.read()
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word not in stop_words]
    freq = nltk.FreqDist(filtered_words)
    sentence_scores = {}
    for sentence in sentences:
        for word, freq_score in freq.most_common(10):
            if word in sentence.lower():
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq_score
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]
    summary = " ".join(summary_sentences)
    with open(output_file, "w") as f:
        f.write(summary)
    typer.echo(f"Summary saved to {output_file}: {summary}")

@app.command()
def categorize(input_file: str = "lyrics.txt", output_file: str = "category.txt"):
    """Categorize song based on lyrics."""
    if not os.path.exists(input_file):
        typer.echo(f"Error: File {input_file} not found.")
        raise typer.Exit(code=1)
    with open(input_file, "r") as f:
        text = f.read()
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    mood = "Positive/Uplifting" if polarity > 0.2 else "Negative/Sad" if polarity < -0.2 else "Neutral"
    text_lower = text.lower()
    if "love" in text_lower or "heart" in text_lower:
        genre, theme = "Pop/Romance", "Love"
    elif "king" in text_lower or "queen" in text_lower or "power" in text_lower:
        genre, theme = "Rock/Epic Pop", "Power/Leadership"
    elif "dance" in text_lower or "beat" in text_lower:
        genre, theme = "Dance/Pop", "Energy"
    else:
        genre, theme = "Unknown", "General"
    category = f"Genre: {genre}, Mood: {mood}, Theme: {theme}"
    with open(output_file, "w") as f:
        f.write(category)
    typer.echo(f"Category saved to {output_file}: {category}")

@app.command()
def all(input_file: str):
    """Run all steps: separate, transcribe, summarize, categorize."""
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    vocal_file = f"output_directory/{base_name}/vocals.wav"
    separate(input_file)
    transcribe(vocal_file)
    summarize()
    categorize()

if __name__ == "__main__":
    app()
