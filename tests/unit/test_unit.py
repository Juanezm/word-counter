from wordcounter.domain.operations import add_list_to_words, get_unique_words, \
    get_repeated_words, get_top_five_frequent_words


def test_add_list_to_words_new_word_is_added():
    words = {}
    word = 'new_word'
    add_list_to_words(words, [word])
    assert word in words


def test_add_list_to_words_word_is_incremented():
    words = {'new_word': 1}
    word = 'new_word'
    add_list_to_words(words, [word])
    assert words.get(word) is 2


def test_add_list_to_words_empty_list():
    words = {'new_word': 1}
    add_list_to_words(words, [])
    assert words == words


def test_get_repeated_words():
    words = {'a': 2, 'b': 2, 'c': 1}
    repeated_words = get_repeated_words(words)
    assert repeated_words == ['a', 'b']


def test_get_repeated_words_with_no_repeated_words():
    words = {'a': 1, 'b': 1, 'c': 1}
    repeated_words = get_repeated_words(words)
    assert not repeated_words


def test_get_unique_words():
    words = {'a': 1, 'b': 2, 'c': 1}
    unique_words = get_unique_words(words)
    assert unique_words == ['a', 'c']


def test_get_unique_words_with_no_unique_words():
    words = {'a': 2, 'b': 2, 'c': 2}
    unique_words = get_unique_words(words)
    assert not unique_words


def test_get_top_five_frequent_words():
    words = {'a': 100, 'b': 75, 'c': 50, 'd': 25, 'e': 10, 'f': 5, 'g': 1}
    top_five_repeated_words = get_top_five_frequent_words(words)
    assert top_five_repeated_words == ['a', 'b', 'c', 'd', 'e']


def test_get_top_five_frequent_words_non_unique():
    words = {'a': 100, 'b': 75, 'c': 50, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
    top_five_repeated_words = get_top_five_frequent_words(words)
    assert top_five_repeated_words == ['a', 'b', 'c', None, None]
