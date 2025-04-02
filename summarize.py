import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Load lyrics
with open("lyrics.txt", "r") as f:
    text = f.read()

# Tokenize into sentences
sentences = sent_tokenize(text)
words = word_tokenize(text.lower())

# Remove stopwords (common words like "the", "and")
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word not in stop_words]

# Calculate word frequency
freq = nltk.FreqDist(filtered_words)

# Score sentences based on frequent words
sentence_scores = {}
for sentence in sentences:
    for word, freq_score in freq.most_common(10):  # Top 10 frequent words
        if word in sentence.lower():
            if sentence in sentence_scores:
                sentence_scores[sentence] += freq_score
            else:
                sentence_scores[sentence] = freq_score

# Pick top 2 sentences as summary
summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]
summary = " ".join(summary_sentences)

print("Summary:", summary)
with open("summary.txt", "w") as f:
    f.write(summary)
