import pandas as pd

def text_to_list(filename):
  return open('data/{}'.format(filename)).read().split('\n')

def write_list(l, name):
  string = '\n'.join(l)
  open('data/{}.txt'.format(name), 'w').write(string)

consonants = sorted(list('qwrtpsdfghjklzxcvbnm'))
vowels = sorted(list('eyuioa'))
letters = sorted(consonants + vowels)

################ person stuff ################

person_attributes = text_to_list('person_attributes.txt')

surname_first_parts = text_to_list('surname_first_parts.txt')

surname_last_parts = text_to_list('surname_last_parts.txt')
last_names_to_check = text_to_list('last_names_to_check.txt')

dwarf_names = text_to_list('dwarf_names.txt')
elf_names = text_to_list('elf_names.txt')
halfling_names = text_to_list('halfling_names.txt')
human_names = text_to_list('human_names.txt')
goblin_names = text_to_list('goblin_names.txt')
gnome_names = text_to_list('gnome_names.txt')
tiefling_names = text_to_list('tiefling_names.txt')

races = text_to_list('races.txt')
professions = text_to_list('professions.txt')
backgrounds = text_to_list('backgrounds.txt')

quirks = text_to_list('quirks.txt')
simple_weapons = text_to_list('simple_weapons.txt')
magic_items = text_to_list('magic_items.txt')


################ city stuff ################

city_types = text_to_list('city_types.txt')
water_sources = text_to_list('water_sources.txt')
biomes = text_to_list('biomes.txt')
city_govs = text_to_list('city_govs.txt')
special_buildings = text_to_list('special_buildings.txt')

################ combat stuff ################

body_parts =  {'high': ['base of skull', 'cheek', 'chin', 'ear', 'eye', 'forehead', 'head', 'jaw', 'mouth', 'neck', 'nose', 'temple', 'throat'], 
                'mid': ['arm', 'arms', 'chest', 'elbow', 'forearm', 'hand', 'kidney', 'lower back', 'ribs', 'shoulder', 'shoulder blade', 'small of back', 'solar plexus', 'sternum', 'stomach', 'tailbone', 'torso', 'upper arm', 'upper back'], 
                'low': ['ankle', 'calf', 'foot', 'groin', 'knee (front)', 'knee (side)', 'leg', 'legs', 'shin', 'thigh', 'toe'] }
all_body_parts = body_parts['high'] + body_parts['mid'] + body_parts['low']

martial_moves = text_to_list('martial_moves.txt')
forms = text_to_list('forms.txt')

################ procedural environment stuff ################

cave_parts = text_to_list('cave_parts.txt')
forest_parts = text_to_list('forest_parts.txt')


building_parts = text_to_list('building_parts.txt')
residential_parts = text_to_list('residential_parts.txt')
commercial_parts = text_to_list('commercial_parts.txt')
tavern_parts = text_to_list('tavern_parts.txt')

busyness = text_to_list('busyness.txt')
quality = text_to_list('quality.txt')

plot_hooks = text_to_list('plot_hooks.txt')

lore_stuff = text_to_list('lore_stuff.txt')

all_names = {
  'dwarf': dwarf_names,
  'elf': elf_names,
  'half-elf': elf_names + human_names,
  'halfling': halfling_names,
  'human': human_names,
  'goblin': goblin_names,
  'gnome': gnome_names,
  'tiefling': tiefling_names,
}

tasks = text_to_list('tasks.txt')
monsters = text_to_list('monsters.txt')
