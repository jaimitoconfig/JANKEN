"""
Project: JANKEN
Description: Base model for opponent, it's a child class from the Player Base Model.
Date: 3/19/2019
Author: Jaimito
"""

try:
    from .constants import *
    from .base import BaseModel
    from random import shuffle, choice
    from sys import exit
except ImportError as err:
    print('could not load module. %s' % err)
    exit(2)


class Bot(BaseModel):
    """ This is the Bot class which helps with random choices for the opponent. """
    def __init__(self):
        BaseModel.__init__(self, 'Opponent')

    def _random_throw(self):
        """ Appends random rock, paper, or scissor choice to decision list. """
        self.options = []

        for i in range(4):
            self.options.append(ROCK)
            self.options.append(PAPER)
            self.options.append(SCISSORS)

        for i in range(10):
            shuffle(self.options)

        self.rps_choice = choice(self.options)
        del self.options
        self.decisions.append(self.rps_choice)

    def _random_action(self):
        """ Appends random action attack, magic, or defend choice to decision list. """
        self.options = []
        self.options.extend(AMD)

        shuffle(self.options)

        if self.amd_choice is LOW_MP:
            self.options.remove(MAGIC)

        self.amd_choice = choice(self.options)

        if self.amd_choice is MAGIC and self.mp < 2:
            self.amd_choice = LOW_MP

        del self.options
        self.decisions.append(self.amd_choice)

    def _random_magic(self):
        """ Appends random fire, water, or earth choice to decision list. """
        self.options = []

        for i in range(4):
            self.options.append(FIRE)
            self.options.append(WATER)
            self.options.append(EARTH)

        for i in range(10):
            shuffle(self.options)

        self.fwe_choice = choice(self.options)
        del self.options
        self.decisions.append(self.fwe_choice)

    def choose_option(self):
        """ Returns the decision made. """
        if len(self.decisions) is 0:
            self._random_throw()
        elif len(self.decisions) is 1:
            self._random_action()
        elif len(self.decisions) is 2 and self.decisions[1] is LOW_MP:
            self.decisions.pop(1)
            self._random_action()
        elif len(self.decisions) is 2 and self.decisions[1] is not MAGIC:
            return self.decisions
        elif len(self.decisions) is 2 and self.decisions[1] is MAGIC:
            self._random_magic()
        elif len(self.decisions) is 3 and self.decisions[2] in FWE:
            return self.decisions
