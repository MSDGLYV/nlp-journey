# Project 5 - Contextual Embeddings (BERT)

## Overview

This project demonstrates how **contextual embeddings** work using BERT.

Unlike traditional methods (BoW, TF-IDF, Word2Vec), where each word has a fixed representation, BERT generates embeddings based on context.

---

## Example

We use the word **"bank"** in two different sentences:

* "I deposited money in the bank."
* "The boat is near the bank of the river."

---

## Approach

* Load a pre-trained BERT model
* Tokenize sentences
* Extract embeddings for the word "bank"
* Compute cosine similarity between them

---

## Result

The similarity is not 1.0, showing that the same word has **different embeddings depending on context**.

---

## Key Insight

* Word2Vec → one vector per word
* BERT → context-dependent vectors

This highlights why transformer-based models are more powerful in modern NLP.
