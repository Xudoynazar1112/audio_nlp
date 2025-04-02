import assemblyai as aai
import os
from dotenv import load_dotenv


# load .env file to environment
load_dotenv()

aai.settings.api_key = os.getenv('ASSEMLYAI_API_KEY')
transcriber = aai.Transcriber()
transcript = transcriber.transcribe("/mnt/myhdd/Xudoynazar_hdd/audio_nlp/output_directory/Arrow-We-Are-Soldiers-Workout-Motivation/vocals.wav")

if transcript.status == aai.TranscriptStatus.completed:
    with open("lyrics.txt", "w") as f:
        f.write(transcript.text)
    print("Lyrics saved to lyrics.txt:", transcript.text)
else:
    print("Transcription failed:", transcript.error)
