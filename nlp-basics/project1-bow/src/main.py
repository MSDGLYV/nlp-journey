from sklearn.feature_extraction.text import CountVectorizer

texts = [
    "I love this movie",
    "This film is amazing",
    "I hate this movie",
    "This film is terrible"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

print("Vocabulary:")
print(vectorizer.vocabulary_)

print("\nBoW Matrix:")
print(X.toarray())

new_text = ["I love this film"]

X_new = vectorizer.transform(new_text)

print("\nNew sentence vector:")
print(X_new.toarray())