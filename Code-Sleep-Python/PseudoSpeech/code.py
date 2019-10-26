import string
import random

upper = string.ascii_uppercase
lower = string.ascii_lowercase

n_sentences = 10
n_max_length_word = 7
n_min_length_word = 2


def get_word(n):
    return "".join(random.choices(lower, k=n))

def get_length():
    return random.randint(n_min_length_word, n_max_length_word)

def get_text():
    out = ""
    for i in range(10):
        out += random.choice(upper) + get_word(get_length())
        word_count = random.randint(1, 10)
        out += " ".join([get_word(get_length()) for i in range(word_count)])+ ". "
    return out

print(get_text())


#the output looks like it was crypted with Caesar or other one-to-one substitution cipher
#so this program could be used for confusing one's minds
