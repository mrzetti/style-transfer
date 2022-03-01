import argparse
from style_functions import *

parser = argparse.ArgumentParser(description='Style Transfer')
parser.add_argument('--style', default="van_gogh_starry_night", 
                    help="""Choose style:\n
'kanagawa_great_wave'
'kandinsky_composition_7'
'hubble_pillars_of_creation'
'van_gogh_starry_night'
'turner_nantes'
'munch_scream'
'picasso_demoiselles_avignon'
'picasso_violin'
'picasso_bottle_of_rum'
'fire'
'derkovits_woman_head'
'amadeo_style_life'
'derkovtis_talig'
'amadeo_cardoso'""")

args = parser.parse_args()
style = args["style"]

styles = [
    'kanagawa_great_wave',
    'kandinsky_composition_7',
    'hubble_pillars_of_creation',
    'van_gogh_starry_night',
    'turner_nantes',
    'munch_scream',
    'picasso_demoiselles_avignon',
    'picasso_violin',
    'picasso_bottle_of_rum',
    'fire',
    'derkovits_woman_head',
    'amadeo_style_life',
    'derkovtis_talig',
    'amadeo_cardoso'
    ]

if any(style in string for string in styles):
    pass
else:
    raise ValueError('Style not supported.')
    

