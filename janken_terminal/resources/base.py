from random import choice
from .constants import *


class BaseModel:
    def __init__(self, name):
        self.name = name
        self.hp = 5
        self.mp = 4
        self.rps_input = ''
        self.amd_input = ''
        self.fwe_input = ''

    def throw_input(self):
        # Validation
        while self.rps_input not in RPS:
            self.rps_input = input('\nChoose Rock, Paper, or Scissors: ').strip().lower()
            if self.rps_input == RPS[0]:
                return RPS[0]
            elif self.rps_input == RPS[1]:
                return RPS[1]
            elif self.rps_input == RPS[2]:
                return RPS[2]
            else:
                print(AGAIN)
    
    def action_input(self):
        # Validation
        while self.amd_input not in AMD:
            print("\n{}".format(self.rps_input.capitalize()))
            self.amd_input = input('Choose Attack, Magic, Defend: ').strip().lower()
            # Attack
            if self.amd_input == AMD[0]:
                return AMD[0]
            # MAGIC & DEFEND
            if self.amd_input == AMD[1] and self.mp >= 2:
                return AMD[1]
            elif self.amd_input == AMD[1] and self.mp <= 1:
                print('No MP -- MP: {}'.format(self.mp))
            else:
                print(AGAIN)

    def magic_input(self):
        # Validation
        while self.fwe_input not in FWE:
            print("{}".format(self.rps_input.capitalize()), "--- {}".format(self.amd_input).capitalize())
            self.fwe_input = input('Chose Fire, Water, or Earth: ').lower().strip()
            if self.fwe_input == FWE[0]:
                return FWE[0]
            elif self.fwe_input == FWE[1]:
                return FWE[1]
            elif self.fwe_input == FWE[2]:
                return FWE[2]
            else:
                print(AGAIN)

    def random_action(self):
        while True:
            amd_choice = choice(AMD)
            # ATTACK
            if amd_choice == AMD[0]:
                return AMD[0]
            # DEFEND
            if amd_choice == self.amd[2]:
                return AMD[2]
            # MAGIC
            if amd_choice == AMD[1] and self.mp >= 2:
                return AMD[1]
            elif amd_choice == AMD[1] and self.mp <= 1:
                return AMD[0]

    def random_magic(self):
        while True:
            fwe_choice = choice(FWE)
            # MAGIC
            if fwe_choice == FWE[0]:
                return FWE[0]
            elif fwe_choice == FWE[1]:
                return FWE[1]
            elif fwe_choice == FWE[2]:
                return FWE[2]

    def print_stats(self):
        print(STATS.format(self.name, self.hp, self.mp))
