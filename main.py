import numpy as np


from lists import person_attributes, races, professions, simple_weapons
from my_rand import choose_from_list, randint, percentile, dc
from names import generate_first_name, generate_surname
from util import repeat_format
import names

########################################

def npc(race=None):
  attributes = choose_from_list(person_attributes, 3)
  age = randint(16, 100)
  race = race if race is not None else choose_from_list(races)

  if race in names.chains:
    first_name_options = ', '.join([names.markov_name(race) for _ in range(5)])
  else:
    first_name_options = repeat_format(generate_first_name, 5)

  print('\nDetails\n==============')
  print('  first name: {}'.format(first_name_options))
  print('  surname: ', repeat_format(generate_surname, 5))
  print('  profession: ', choose_from_list(professions))
  print('  attributes: ', ', '.join(attributes))
  print('\nDescription\n==========')
  print('  race: ', race)
  print('  age: ', age)
  print('  height: ', percentile())
  print('  voice pitch: ', percentile())
  print('  voice speed: ', percentile())
  print('  vocabulary: ', percentile())
  print('  quirk: ', choose_from_list(['eyebrows', 'cheeks', 'um', 'ear', 'hair', 'jewelry', 'eye', 'nose', 'walk', 'overweight', 'underweight', 'fixation on topic', 'awkward', 'prefers a PC', 'too kind']))
  print()


def d(count, die=None):
  if die is None:
    die = count
    count = 1

  rolls = np.random.randint(1, die + 1, count)
  print('\nroll: ', rolls)
  print('total: ', np.sum(rolls))

if __name__ == '__main__':
  pass
