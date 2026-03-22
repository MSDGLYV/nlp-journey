# Project 4 — Word2Vec

## Objective
Learn how dense word embeddings work and how models can capture word similarity from context.

---

## Method
Used `Word2Vec` from `gensim`.

Two modes were tested:

- **Skip-gram (`sg=1`)**: predicts surrounding words from a target word  
- **CBOW (`sg=0`)**: predicts the target word from surrounding words  

---

## Main Idea

Word2Vec learns vectors for words based on context.

Words used in similar contexts tend to get similar vectors.

Example idea:

- `coffee` and `tea`
- `nlp` and related words

---

## Code Example

```python
model = Word2Vec(
    sentences=sentences,
    vector_size=20,
    window=2,
    min_count=1,
    sg=1
)

Key Parameters
vector_size → embedding size
window → context window
min_count → minimum frequency of a word
sg → training mode (1 = Skip-gram, 0 = CBOW)


Output
vocabulary of learned words
vector for a selected word
most similar words to a selected word


Notes
Output vectors are dense, not sparse
Results on very small datasets may look weak or noisy
The important point is understanding the learning idea, not perfect similarity scores