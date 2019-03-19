"""
Project: JANKEN
Description: Base model for player, helps with decision making and displaying results.
Date: 3/19/2019
Author: Jaimito
"""

try:
    import pygame
    from .constants import *
    from .ui import *
    from sys import exit
except ImportError as err:
    print('could not load module. %s' % err)
    exit(2)


class BaseModel:
    """ Base model for player, helps with decision making and displaying results. """
    def __init__(self, name):
        self.name = name
        self.hp = 5  # 5
        self.mp = 4  # 4
        self.score = 0
        self.stat_changes = []
        self.decisions = []
        self.options = []
        self.rps_choice = None
        self.amd_choice = None
        self.fwe_choice = None
        self.opponent_hit = False

    def reset_stats(self):
        """ Resets ALL stats to default values. """
        self.hp = 5  # 5
        self.mp = 4  # 4
        self.score = 0
        self.stat_changes = []
        self.decisions = []
        self.options = []
        self.rps_choice = None
        self.amd_choice = None
        self.fwe_choice = None
        self.opponent_hit = False

    def reset_choices(self):
        """ Resets the choices ONLY to the default values. """
        self.stat_changes = []
        self.decisions = []
        self.options = []
        self.rps_choice = None
        self.amd_choice = None
        self.fwe_choice = None
        self.opponent_hit = False

    def soft_reset(self):
        """ This is for the play again option. Score is not included in this. """
        self.hp = 5
        self.mp = 4
        self.reset_choices()

    def display_results(self, surface, result, opponent):
        """ Displays the outcome of each game while HP is not 0. """
        x, y = surface.get_rect().centerx, surface.get_rect().centerx
        display_box(surface, x + 70, y - 185, 420, 210)

        if result is HIT:
            if self.opponent_hit is True:
                display_text(surface, result, 80, RED, pos=[x + 70, y - 220])  # Opponent hit.
            else:
                display_text(surface, result, 80, GREEN, pos=[x + 70, y - 220])  # Player hit.

            display_text(surface, '{} - HP: {} MP {}'.format(self.name, self.stat_changes[0], self.stat_changes[1]),
                         15, pos=[260, 190])
            display_text(surface,
                         '{} - HP: {} MP {}'.format(opponent.name, opponent.stat_changes[0], opponent.stat_changes[1]),
                         15, pos=[460, 190])

            if self.decisions[1] in ATTACK_DEFEND or opponent.decisions[1] in ATTACK_DEFEND:
                multiline_text(surface, 15, 20, WHITE_SMOKE, [x + 70, y - 165], True,
                               DISPLAY_RESULT.format(self.name, self.decisions[0], self.decisions[1]),
                               DISPLAY_RESULT.format(opponent.name, opponent.decisions[0], opponent.decisions[1]))

            elif (self.decisions[1] is MAGIC and self.decisions[2] in FWE) and\
                    (opponent.decisions[1] is MAGIC and opponent.decisions[2] in FWE):
                multiline_text(surface, 15, 20, WHITE_SMOKE, [x + 70, y - 165], True,
                               DISPLAY_RESULT.format(self.name, self.decisions[0], self.decisions[2]),
                               DISPLAY_RESULT.format(opponent.name, opponent.decisions[0], opponent.decisions[2]))

        elif result is DRAW:
            display_text(surface, result, 80, YELLOW, pos=[x + 70, y - 240])

            display_text(surface, '{} - HP: {} MP {}'.format(self.name, self.stat_changes[0], self.stat_changes[1]),
                         15, pos=[260, 190])
            display_text(surface,
                         '{} - HP: {} MP {}'.format(opponent.name, opponent.stat_changes[0], opponent.stat_changes[1]),
                         15, pos=[460, 190])

            if self.decisions[1] in ATTACK_DEFEND or opponent.decisions[1] in ATTACK_DEFEND:
                multiline_text(surface, 15, 20, WHITE_SMOKE, [x + 70, y - 165], True,
                               DISPLAY_RESULT.format(self.name, self.decisions[0], self.decisions[1]),
                               DISPLAY_RESULT.format(opponent.name, opponent.decisions[0], opponent.decisions[1]))

            elif (self.decisions[1] is MAGIC and self.decisions[2] in FWE) and\
                    (opponent.decisions[1] is MAGIC and opponent.decisions[2] in FWE):
                multiline_text(surface, 15, 20, WHITE_SMOKE, [x + 70, y - 165], True,
                               DISPLAY_RESULT.format(self.name, self.decisions[0], self.decisions[2]),
                               DISPLAY_RESULT.format(opponent.name, opponent.decisions[0], opponent.decisions[2]))

    def display_stats(self, surface, pos=[]):
        """ Displays HP, MP and SCORE stats. """
        display_box(surface, pos[0], pos[1] + 40, 120, 100)
        multiline_text(surface, 20, 20, WHITE_SMOKE, [(pos[0] / 2) - 10, pos[1]], False,
                       self.name + ':',
                       'HP: {}'.format(self.hp),
                       'MP: {}'.format(self.mp),
                       'SCORE: {}'.format(self.score))

    def display_options(self, surface, option_one, option_two, option_three):
        """ Displays player options. """
        x, y = 80, 260
        display_box(surface,  x, y + 50, 120, 150)
        self.options = [button(surface,  x, y, option=True),
                        button(surface,  x, y + 50, option=True),
                        button(surface,  x, y + 100, option=True)]
        multiline_text(surface, 20, 50, WHITE_SMOKE, [x, y], True,
                       option_one, option_two, option_three)

    def _choose_magic(self, surface):
        """ Appends fire, water, or earth choice to player decision list after choice is made. """
        self.display_options(surface, FIRE, WATER, EARTH)

        if True in self.options:
            if self.options[0] is True:
                self.fwe_choice = FIRE
            elif self.options[1] is True:
                self.fwe_choice = WATER
            elif self.options[2] is True:
                self.fwe_choice = EARTH

            pygame.time.delay(DELAY)  # Build a lil drama.
            del self.options
            self.decisions.append(self.fwe_choice)

    def _choose_action(self, surface):
        """
        Appends action (attack, magic, defend) to decisions list.
        if MP is low it will append 'Low MP' to decisions and loop back.
        """
        self.display_options(surface, ATTACK, MAGIC, DEFEND)

        if self.amd_choice is LOW_MP:  # Low MP warning, took me a while, but I did it!
            display_text(surface, LOW_MP, color=YELLOW, size=40, pos=[230 + 145, 310])

        if True in self.options:
            if self.options[0] is True:
                self.amd_choice = ATTACK
            elif self.options[1] is True and self.mp >= 2:
                self.amd_choice = MAGIC
            elif self.options[2] is True:
                self.amd_choice = DEFEND
            else:
                self.amd_choice = LOW_MP

            pygame.time.delay(DELAY)
            del self.options
            self.decisions.append(self.amd_choice)

    def _choose_throw(self, surface):
        """ Appends throw (rock, paper, scissors) to decisions list after choice is made. """
        self.display_options(surface, ROCK, PAPER, SCISSORS)

        if True in self.options:
            if self.options[0] is True:
                self.rps_choice = ROCK
            elif self.options[1] is True:
                self.rps_choice = PAPER
            elif self.options[2] is True:
                self.rps_choice = SCISSORS

            pygame.time.delay(DELAY)
            del self.options
            self.decisions.append(self.rps_choice)

    def choose_option(self, surface):
        """ Returns the decision made. """
        if len(self.decisions) is 0:
            self._choose_throw(surface)
        elif len(self.decisions) is 1:
            self._choose_action(surface)
        elif len(self.decisions) is 2 and self.decisions[1] is LOW_MP:  # If low MP logic!
            self.decisions.pop(1)
            self._choose_action(surface)
        elif len(self.decisions) is 2 and self.decisions[1] is not MAGIC:
            return self.decisions
        elif len(self.decisions) is 2 and self.decisions[1] is MAGIC:
            self._choose_magic(surface)
        elif len(self.decisions) is 3 and self.decisions[2] in FWE:
            return self.decisions
