# Project 2 — TF-IDF

## Objective
Convert text into numerical vectors while giving more importance to informative (rare) words.

---

## Method
Used `TfidfVectorizer` from scikit-learn.

---

## Idea

TF-IDF = TF × IDF

- **TF (Term Frequency)** → how often a word appears in a sentence  
- **IDF (Inverse Document Frequency)** → how rare the word is across all sentences  

---

## How It Works

- Common words (e.g. "this") → low weight  
- Rare words (e.g. "amazing", "terrible") → high weight  

Example:

"I love this movie"  
→ `[0 0 0 0 0.72 0.57 0 0.37]`

---

## Code

```python
vectorizer = TfidfVectorizer()

fit → learns vocabulary
transform → converts to weighted vectors

Key Points
Same pipeline as BoW, but with weights
Output values are between 0 and 1
Rare words get higher importance


Limitation
Still no word order
Still no real semantic understanding