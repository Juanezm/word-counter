def add_list_to_words(words: dict, new_words: list):
    for word in new_words:
        words[word] = words.get(word, 0) + 1


def get_repeated_words(words: dict) -> list:
    return [k for k, v in words.items() if v > 1]


def get_unique_words(words: dict) -> list:
    return [k for k, v in words.items() if v == 1]


def get_top_five_frequent_words(words: dict) -> list:
    sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    top_five_words = [k for k, v in sorted_words if v > 1][:5]
    if len(top_five_words) < 5:
        top_five_words = top_five_words + [None] * (5 - len(top_five_words))

    return top_five_words
