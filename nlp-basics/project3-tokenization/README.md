# Project 3 — Tokenization & BPE

## Objective
Understand how text is split into tokens and how different tokenization methods affect NLP models.

---

## Methods Covered

### 1. Word Tokenization
Splits text by spaces:
"I love NLP" → ["i", "love", "nlp"]

- Simple but has OOV (unknown word) problem

---

### 2. Better Tokenization (Regex)
Removes punctuation:
"amazing!" → ["amazing"]

- Cleaner than basic split

---

### 3. Character Tokenization
Splits into characters:
"love" → ['l','o','v','e']

- No OOV problem  
- But loses meaning

---

## OOV Problem

If a word is not seen in training:

"I love film"  
"I love *fucking* film"

→ "fucking" is ignored

---

## Subword Idea

Break words into meaningful parts:

"fucking" → ["fuck", "ing"]

- Handles unseen words  
- Preserves partial meaning

---

## BPE (Byte Pair Encoding)

- Starts with characters  
- Repeatedly merges most frequent pairs  
- Learns common subword units  

Example:
"lower" → ["low", "er"]

---

## Summary

- Word → simple but fragile  
- Character → robust but weak meaning  
- Subword/BPE → balanced solution  

Tokenization determines what the model sees.