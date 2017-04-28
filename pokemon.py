'''
Okay this class allows you to call !wtp from chat
A random pokemon will appear as a silloutted bitmap and then users
will get some time to guess the pkmn before the time is up.

Upon a correct guess or when the time runs out, the correct pokemon 
will display with the corresponding win or loss message.

Features might include something that lets you guess from a 
specific gen of pokemon rather than all of them. For nows we will
only include gen one
'''
from os import listdir
from os.path import isfile, join, dirname, abspath, basename
import re
from random import randint

from PokeAPI import PokeAPI
from PIL import Image

MESSAGE = "You are now playing Who's That Pokemon" \
          "\n Guess the pokemon in the shadow to win."

class pkmn(object):
    '''This class contains the pokemon to be guessed.
        It also contains functions to output a sillouetted image
        of a given pokemon (filename)
    '''
    papi = PokeAPI()  # ayeee papiii

    LOCK = False

    DEX = "sugimori"
    KURO = "kuro_cache"

    TIME_TO_START = 5
    TIME_TO_GUESS = 30
    MAX_PKMN = 721

    def __init__(self):
        super(pkmn, self).__init__()

        self.pkmn_data = None
        self.pkmn_id = 0
        self.pkmn_name = ''

        self.initialize() #initialize random id and derived name

    def initialize(self):
        id = pkmn.generate_id()
        data = pkmn.papi.get_pokemon(id)
        name = data['name']

        self.pkmn_data = data
        self.pkmn_id = id
        self.pkmn_name = name

        LOCK = True #sets lock as long as game is still being played
        return

    def display_message(self):
        return MESSAGE

    def display_img(self, silhouette = False):
        #if sihouette edit the image to mask the pokemon in question
        if silhouette:
            return self.generate_silhouette(self.get_img_path(self.pkmn_id))

        #from folder return the appropriate image path to the pokemon
        return self.get_img_path(self.pkmn_id)

    def check_guess(self, guess):
        if guess == self.pkmn_name:
            return True
        else: return False

    @staticmethod
    def get_img_path(id, folder=DEX):
        path = join(dirname(abspath(__file__)), folder)
        files = []
        try:
            files = [f for f in listdir(path) if str(id) in f]
        except FileNotFoundError:
            print("Could not find in ", path)
        except TypeError:
            print("Wrong type dummy")
        finally:
            return join(path, files[0])

    @staticmethod
    def generate_id():
        return randint(1, pkmn.MAX_PKMN)

    @staticmethod
    def generate_silhouette(image_path, folder=KURO):
        filename = basename(image_path)
        new_path = join(dirname(abspath(__file__)), folder, filename)
        # don't do any work if there is already an image cached
        if isfile(new_path):
            return new_path

        #converts image to rgba pixel data
        image = Image.open(image_path).convert('RGBA')
        pixel_data = list(image.getdata())

        #changes each solid pixel to a black one
        for i,pixel in enumerate(pixel_data):
            if pixel[:3] >= (0,0,0) and pkmn.almostEquals(pixel[3], 255): #pixel[3] >= 10
                pixel_data[i] = (0,0,0,255)
        image.putdata(pixel_data)
        image.save(new_path)

        #returns the path at the end to be referenced
        return new_path

    @staticmethod
    def almostEquals(a, b, thres=50):
        return abs(a - b) < thres

'''
Design flow:
    1. user launches command
    2. bot generates a random number (pokemon)
    3. bot displays the silloetted image of the pokemon to client
    4. user attempts to guess pokemon name
    5. bot compares the name to the database
    6. if correct or out of time move on - else repeat 4 & 5
    7. display correct image and appropriate win/lose text
'''