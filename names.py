import pandas as pd
import numpy as np

from my_rand import choose_from_list, randint
from util import repeat
from lists import *

table = pd.read_csv('data/language_frequencies.csv', delimiter=' ')
letters = table['letter']

def capitalize(word):
  word = list(word)
  word[0] = word[0].upper()
  return ''.join(word)

def syllable():
  a = choose_from_list(consonants)[0]
  b = choose_from_list(vowels)[0]

  if flip(.3):
    c = choose_from_list(consonants)[0]
  else:
    c = ''

  return a+b+c

def name():
  syllables = randint(1, 5)
  x = ''
  for _ in range(syllables):
    x += syllable()
  return x

def generate_first_name():
  length = randint(3, 10)
  language = choose_from_list(table.columns[1:])
  probabilities = (table[language]).as_matrix()
  probabilities /= probabilities.sum()

  name = np.random.choice(letters, size=length, p=probabilities)
  return capitalize(''.join(name))

def generate_surname():
  adjective = capitalize(choose_from_list(surname_first_parts))
  noun = choose_from_list(surname_last_parts)

  return adjective + noun


def generate_name():
  return generate_first_name() + ' ' + generate_surname()

# find all combinations
def list_to_markov_chain(l, order=1):

  def combinations(order):
    output = set()
    for word in l:
      for i in range(len(word)-order):
        pair = word[i:i+order]
        output.add(str(pair))

    return output

  node_values = list(combinations(order))
  characters = list(combinations(1))

  markov_chain = {}
  node_map = {node: i for i, node in enumerate(characters)}

  for word in l:
    for i in range(len(word) - order):
      current_char = word[i:i+order]
      next_char = word[i+order]

      if current_char in markov_chain:
        markov_chain[current_char][node_map[next_char]] += 1
      else:
        markov_chain[current_char] = [0]*len(characters)
        markov_chain[current_char][node_map[next_char]] += 1

  def sample_n(n):
    chars = []
    current_char = choose_from_list(node_values)
    first_char = current_char

    while len([first_char] + chars) < n:
      try:
        probabilities = np.array(markov_chain[current_char]).astype(float)
        probabilities /= np.sum(probabilities)
        next_char = np.random.choice(characters, p=probabilities)
        chars.append(next_char)
        if order == 1:
          current_char = next_char
        else:
          current_char = ''.join(list(current_char)[-order + 1:]) + next_char
      except KeyError:
        chars = []
        current_char = choose_from_list(node_values)
        first_char = current_char


    return ''.join([first_char] + chars)

  return sample_n

ORDER = 2

chains = {
  'dwarf': list_to_markov_chain(dwarf_names, ORDER),
  'elf': list_to_markov_chain(elf_names, ORDER),
  'halfling': list_to_markov_chain(halfling_names, ORDER),
  'human': list_to_markov_chain(human_names, ORDER),
  'goblin': list_to_markov_chain(goblin_names, ORDER),
  'gnome': list_to_markov_chain(gnome_names, ORDER),
  'tiefling': list_to_markov_chain(tiefling_names, ORDER)
}


def markov_name(type):
  length = randint(3, 10)
  return chains[type](length)


if __name__ == '__main__':
  for i in range(100):
    print('markov_name("human")', markov_name("goblin"))
