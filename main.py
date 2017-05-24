import numpy as np


from lists import *
from my_rand import choose_from_list, randint, percentile, dc
from names import generate_first_name, generate_surname
from util import repeat_format
import names

########################################

def random_alignment():
  a = ['lawful', 'neutral', 'chaotic']
  b = ['good', 'neutral', 'evil']
  return choose_from_list(a) + ' ' + choose_from_list(b)

def npc(race=None):
  attributes = choose_from_list(person_attributes, 3)
  race = race if race is not None else choose_from_list(races)

  if race in names.chains:
    first_name_options = ', '.join([names.markov_name(race) for _ in range(5)])
  else:
    first_name_options = repeat_format(generate_first_name, 5)

  print('\nDetails\n==============')
  print('  first name: ', first_name_options)
  print('  surname:    ', repeat_format(generate_surname, 5))
  print('  alignment:  ', random_alignment())
  print('  profession: ', choose_from_list(professions))
  print('  attributes: ', ', '.join(attributes))

  print('\nDescription\n==========')
  print('  race:       ', race)
  print('  age:        ', randint(10, 100))
  print('  height:     ', percentile())
  print('  mood:       ', percentile())
  print('  voice pitch:', percentile())
  print('  voice speed:', percentile())
  print('  vocabulary: ', percentile())
  print('  quirk:      ', choose_from_list(['eyebrows', 'cheeks', 'um', 'ear', 'hair', 'jewelry', 'eye', 'nose', 'walk', 'overweight', 'underweight', 'fixation on topic', 'awkward', 'prefers a PC', 'too kind', 'impatient', 'angry']))
  print()

def city():
  print('City details ============')
  print('  race:       ', choose_from_list(races))
  print('  type:       ', choose_from_list(city_types))
  print('  biome:      ', choose_from_list(biomes, 3))
  print('  government: ', choose_from_list(city_govs))
  print('  city age:   ', percentile())
  print('  population: ', percentile())
  print('  density:    ', percentile())
  print('  special:    ', choose_from_list(special_buildings, 3))
  
  print('\nDemographics ==============')  
  print('  diversity:  ', percentile())
  print('  technology: ', percentile())
  print('  crime:      ', percentile())
  print('  wealth:     ', percentile(3))
  print('  industries: ', choose_from_list(professions, 3))
  print('  education:  ', percentile())
  print('  family:     ', percentile())
  print('  religion:   ', percentile())
  print('  politics:   ', percentile())

  # special buildings - prisons, hospitals, asylum, sights to see, tourism/entertainment, souvenirs
  # shopping
  # transportation

def d(count, die=None):
  if die is None:
    die = count
    count = 1

  rolls = np.random.randint(1, die + 1, count)
  print('\nroll: ', rolls)
  print('total: ', np.sum(rolls))

if __name__ == '__main__':
  pass
