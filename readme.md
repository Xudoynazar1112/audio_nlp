
# AudioNLP: Audio Processing Pipeline

**AudioNLP** is a Python-based tool that processes audio files to separate vocals, transcribe lyrics, summarize them, and categorize the song by genre, mood, and theme. Built for my portfolio, it showcases data engineering and machine learning skills through an end-to-end audio pipeline with a user-friendly CLI.

- **Project Size**: ~1.9 GB (includes dependencies and pre-trained models).
- **Average Processing Time**: ~10 minutes per song (depending on file size and system specs).
- **License**: MIT (see [LICENSE](#license)).

## Features
- **Vocal Separation**: Isolates vocals from music using Spleeter.
- **Transcription**: Converts vocals to lyrics with AssemblyAI (requires your own API key).
- **Summarization**: Generates a concise summary of lyrics using NLTK.
- **Categorization**: Assigns genre, mood, and theme with TextBlob.
- **CLI**: Interactive command-line interface powered by Typer.

## Demo
- **Input**: `kings_and_queens.mp3` (a sample audio file).
- **Outputs**:
  - `output_directory/kings_and_queens/vocals.wav`: Separated vocal track.
  - `lyrics.txt`: Transcribed lyrics.
  - `summary.txt`: Summary of the lyrics.
  - `category.txt`: Genre, mood, and theme classification.

Example terminal output:
```
$ ./audio_nlp.py all kings_and_queens.mp3
Vocals separated to output_directory/kings_and_queens/vocals.wav
Lyrics saved to lyrics.txt: "We rise like kings and queens..."
Summary saved to summary.txt: "The song depicts rising to power..."
Category saved to category.txt: Genre: Rock/Epic Pop, Mood: Uplifting, Theme: Power/Leadership
```

## Prerequisites
- **Python**: 3.9+ (tested on 3.9).
- **System**: Linux/macOS/Windows with ~2 GB free disk space.
- **AssemblyAI API Key**: You must obtain your own key from [AssemblyAI](https://www.assemblyai.com/). See [Installation](#installation) for details.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/AudioNLP.git
   cd AudioNLP
   ```
2. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   - Note: The 1.9 GB size comes from large dependencies like TensorFlow and Spleeter models.
4. **Get Your AssemblyAI API Key**:
   - Sign up for a free account at [AssemblyAI](https://www.assemblyai.com/).
   - Log in, go to your dashboard, and copy your API key.
   - Open `audio_nlp.py` in a text editor.
   - Find the line: `aai.settings.api_key = "your_assemblyai_api_key_here"`.
   - Replace `"your_assemblyai_api_key_here"` with your actual API key (e.g., `aai.settings.api_key = "abc123xyz"`).
   - Save the file.

## Usage
The CLI uses a portable shebang (`#!/usr/bin/env python3`) for compatibility across systems. Run commands from the project directory after setting up your AssemblyAI API key.

### Commands
- **Separate Vocals**:
  ```bash
  ./audio_nlp.py separate kings_and_queens.mp3
  ```
- **Transcribe Vocals**:
  ```bash
  ./audio_nlp.py transcribe output_directory/kings_and_queens/vocals.wav
  ```
- **Summarize Lyrics**:
  ```bash
  ./audio_nlp.py summarize
  ```
- **Categorize Song**:
  ```bash
  ./audio_nlp.py categorize
  ```
- **Run All Steps**:
  ```bash
  ./audio_nlp.py all kings_and_queens.mp3
  ```
  - Expect ~10 minutes for completion.

### Notes
- Make the script executable (Linux/macOS):
  ```bash
  chmod +x audio_nlp.py
  ```
- If not using the shebang, run with:
  ```bash
  python3 audio_nlp.py <command>
  ```
- **API Key Requirement**: The `transcribe` and `all` commands will fail without a valid AssemblyAI API key configured in `audio_nlp.py`.

## Project Structure
```
AudioNLP/
├── audio_nlp.py         # Main CLI script
├── requirements.txt     # Dependencies
├── kings_and_queens.mp3 # Sample audio file
├── output_directory/    # Separated audio outputs
├── lyrics.txt          # Transcribed lyrics
├── summary.txt         # Lyrics summary
└── category.txt        # Song categorization
```

## Technical Details
- **Vocal Separation**: Uses Spleeter (TensorFlow-based) with the `2stems` model.
- **Transcription**: Leverages AssemblyAI’s speech-to-text API (user-provided key required).
- **Summarization**: NLTK frequency-based sentence scoring.
- **Categorization**: TextBlob sentiment analysis + keyword matching.
- **CLI**: Typer for a clean, portable interface.

### Challenges Overcome
- Fixed NumPy 2.x compatibility by downgrading to 1.23.5 for TensorFlow 2.9.3.
- Made the shebang dynamic with `/usr/bin/env python3` for portability.

## Requirements
See `requirements.txt`. Key packages:
- `spleeter==2.4.0`
- `tensorflow==2.9.3`
- `numpy==1.23.5`
- `assemblyai`
- `nltk`
- `textblob`
- `typer`

## Limitations
- Processing time (~10 min) due to Spleeter’s model and transcription API latency.
- Transcription accuracy may vary with complex vocals or background noise; requires a valid AssemblyAI API key.
- Categorization is basic (keyword-based); could be enhanced with ML models.

## Future Improvements
- Optimize processing time with GPU support for Spleeter.
- Improve categorization with a trained classifier.
- Add real-time progress feedback in the CLI.

## License
MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgments
- [Spleeter](https://github.com/deezer/spleeter) for audio separation.
- [AssemblyAI](https://www.assemblyai.com/) for transcription (thanks for the free tier!).
- [NLTK](https://www.nltk.org/) and [TextBlob](https://textblob.readthedocs.io/) for NLP.

---
Questions? Open an issue or tweak the code to make it your own!

---

### Key Changes
1. **AssemblyAI API Key**:
   - Added a dedicated step in "Installation" to guide users to get their own key from AssemblyAI.
   - Clarified where to add it in `audio_nlp.py`.
   - Noted in "Usage" that transcription fails without it.
2. **Clarity**: Kept instructions beginner-friendly, assuming users might not know how to handle API keys.
3. **Everything Else**: Retained the 1.9 GB size, 10-minute processing time, and all previous features.

### Next Steps
- Save this as `README.md` in your project folder.
- Update `audio_nlp.py` to ensure the API key placeholder (`"your_assemblyai_api_key_here"`) is still there for users to replace.
- If you don’t have a `requirements.txt`, generate it:
  ```bash
  pip freeze > requirements.txt
  ```
- Push to GitHub and test the instructions yourself (or ask a friend) to ensure they work!

Let me know if you want to refine this further—maybe add a screenshot or tweak the tone? How’s the portfolio coming along?