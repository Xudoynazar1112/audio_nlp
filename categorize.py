from textblob import TextBlob

# Load lyrics
with open("lyrics.txt", "r") as f:
    text = f.read()

# Sentiment analysis (mood)
blob = TextBlob(text)
polarity = blob.sentiment.polarity  # -1 (negative) to 1 (positive)
if polarity > 0.2:
    mood = "Positive/Uplifting"
elif polarity < -0.2:
    mood = "Negative/Sad"
else:
    mood = "Neutral"

# Simple genre/theme guess based on keywords
text_lower = text.lower()
if "love" in text_lower or "heart" in text_lower:
    genre = "Pop/Romance"
    theme = "Love"
elif "king" in text_lower or "queen" in text_lower or "power" in text_lower:
    genre = "Rock/Epic Pop"
    theme = "Power/Leadership"
elif "dance" in text_lower or "beat" in text_lower:
    genre = "Dance/Pop"
    theme = "Energy"
else:
    genre = "Unknown"
    theme = "General"

# Output
category = f"Genre: {genre}, Mood: {mood}, Theme: {theme}"
print(category)
with open("category.txt", "w") as f:
    f.write(category)
