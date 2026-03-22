from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# model yükle
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

sent1 = "I deposited money in the bank."
sent2 = "The boat is near the bank of the river."

def get_word_embedding(sentence, target_word):
    inputs = tokenizer(sentence, return_tensors="pt")
    outputs = model(**inputs)

    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
    embeddings = outputs.last_hidden_state[0]

    for i, token in enumerate(tokens):
        if target_word in token:
            return embeddings[i].detach().numpy()

# bank embedding in 2 sentences
emb1 = get_word_embedding(sent1, "bank")
emb2 = get_word_embedding(sent2, "bank")

# similarity calculation
sim = cosine_similarity([emb1], [emb2])[0][0]

print("Sentence 1:", sent1)
print("Sentence 2:", sent2)
print("Similarity (bank vs bank):", sim)