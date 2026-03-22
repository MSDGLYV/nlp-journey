from gensim.models import Word2Vec

sentences = [
    ["i", "love", "nlp"],
    ["i", "love", "machine", "learning"],
    ["nlp", "is", "fun"],
    ["machine", "learning", "is", "powerful"],
    ["i", "enjoy", "nlp"],
    ["deep", "learning", "is", "interesting"],
]

# create a model
model = Word2Vec(
    sentences=sentences,
    vector_size=20,
    window=2,
    min_count=1,
    sg=1
)

# vocabulary
print("Vocabulary:")
print(model.wv.key_to_index)

# single word's vector
print("\nVector for 'nlp':")
print(model.wv["nlp"])

# similar words
print("\nWords similar to 'nlp':")
print(model.wv.most_similar("nlp"))