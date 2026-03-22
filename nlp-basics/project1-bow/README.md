# Project 1 — Bag of Words (BoW)

## Objective
The goal of this project is to learn how to convert text data into numerical vectors that machine learning models can understand.

---

## Method Used
For this transformation, `CountVectorizer` from scikit-learn is used. This tool automatically converts text into a numerical representation.

---

## How It Works

### 1. Tokenization
Sentences are split into words:

"I love this movie" → ["love", "this", "movie"]

(Note: by default, single-character words like "I" are ignored)

---

### 2. Vocabulary Creation
All unique words from the dataset are collected and assigned an index:

```python
vectorizer.vocabulary_

Example::

amazing → 0  
film → 1  
hate → 2  
is → 3  
love → 4  
movie → 5  
terrible → 6  
this → 7  

3. Vector Creation (BoW)

Each sentence is converted into a numerical vector based on this vocabulary:

"I love this movie" → [0 0 0 0 1 1 0 1]

Meaning:

love → 1
movie → 1
this → 1
others → 0

Code Logic

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

fit → learns the vocabulary
transform → converts text into numbers
fit_transform → does both

Key Points
vectorizer → the learning object (stores vocabulary)
X → resulting BoW matrix
X.toarray() → makes the result readable


Train vs Test Concept
fit is applied only on training data
new data is processed using transform with the same vocabulary

Limitations
word order is ignored
no semantic understanding

Example:

"I love this movie"
"I hate this movie"

→ produce very similar vectors