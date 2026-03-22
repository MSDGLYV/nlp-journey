from collections import Counter

words = ["welcome", "welcomest", "welcomar", "welcomeblya"]

split_words = [list(word) for word in words]


def get_pair_counts(words_list):
    pair_counts = Counter()

    for word in words_list:
        for i in range(len(word) - 1):
            pair = (word[i], word[i + 1])
            pair_counts[pair] += 1

    return pair_counts


def merge_pair(word, pair):
    merged = []
    i = 0

    while i < len(word):
        if i < len(word) - 1 and (word[i], word[i + 1]) == pair:
            merged.append(word[i] + word[i + 1])
            i += 2
        else:
            merged.append(word[i])
            i += 1

    return merged


print("Initial words:")
for w in split_words:
    print(w)

num_merges = 5

for step in range(num_merges):
    pair_counts = get_pair_counts(split_words)

    if not pair_counts:
        break

    best_pair = pair_counts.most_common(1)[0][0]

    print(f"\nStep {step + 1} - best pair: {best_pair}")

    split_words = [merge_pair(word, best_pair) for word in split_words]

    for w in split_words:
        print(w)