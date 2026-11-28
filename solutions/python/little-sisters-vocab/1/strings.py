"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return 'un'+word


def make_word_groups(vocab_words):
    n=len(vocab_words)
    s=vocab_words[0]
    for i in range(1,n):
        s +=' :: '
        s=s +  vocab_words[0] + vocab_words[i]
    return s
    # pass


def remove_suffix_ness(word):
    word_without_ness = word[:-4]

    if word_without_ness.endswith("i"):
        return word_without_ness[:-1] + "y"
    else:
        return word_without_ness

import string
def adjective_to_verb(sentence, index):
    l =sentence.split(" ")
    word = l[index].strip(string.punctuation)
    return word + 'en'
