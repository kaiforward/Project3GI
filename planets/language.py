import random

def create_planet_affix():
    affix_list = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota",
                  "Kappa", "Lambda", "Xi", "Omicron", "Pi", "San", "Rho", "Sigma", "Tau", 'Upsilon']
    affix_choice = random.choice(affix_list)
    return affix_choice

def get_language():
    # IMPORTS MY LANGUAGE TEXT FILE WHICH CONTAINS A LIST OF FICTIONAL "VERBS"
    lines = []
    with open('alienlanguage.txt') as language:
        for line in language:
            lines.append(line.strip())
    return lines

def word_creator(number_of_words):
    syllable_list = get_language()
    # use to create a set of different word elements.
    prefix_list = syllable_list[2:26]
    connecting_letters = syllable_list[28:32]
    affix_list_vowels = syllable_list[34:46]
    affix_list_consonant = syllable_list[48:95]
    final_word = ""

    for word in xrange(0, number_of_words):
        short_word = random.choice(prefix_list)
        shorter_word = random.choice(prefix_list) + random.choice(connecting_letters)
        long_word = random.choice(prefix_list) + random.choice(affix_list_vowels)
        # longest_word = random.choice(prefix_list) + random.choice(connecting_letters) + random.choice(affix_list_consonant)
        words = [short_word, short_word, shorter_word, long_word]
        chosen_word = random.choice(words)
        final_word += chosen_word+" "
        final_word = final_word[:-1]
    final_word = final_word.title()  # capitalise name
    return final_word