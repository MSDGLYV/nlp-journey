from sklearn.feature_extraction.text import TfidfVectorizer

texts = [
    "I love this movie",
    "This film is amazing",
    "I hate this movie",
    "This film is terrible"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

print("Vocabulary:")
print(vectorizer.vocabulary_)

print("\nTF-IDF Matrix:")
print(X.toarray())