""" 
JANKEN
"""
from sys import exit
from time import sleep
from random import choice
from resources.constants import *
from resources.base import BaseModel
# from resources.checks import Control


class Game:
    def __init__(self):
        self.play = False
        self.player = BaseModel('Player')
        self.opponent = BaseModel('Opponent')

    def start(self):
        while True:
            print('JANKEN: Rock, Paper, Scissors \n')
            print('1 - Start game!')
            print('2 - How to play?')
            print('3 - Exit.\n')
            choice = input("Make your choice: ")

            if choice == '1':
                self.player.name = input("Choose your name: ").capitalize().strip()
                print('')  # Just a space.
                self.play = True
                sleep(1)
                self.main_loop()
            elif choice == '2':
                self.how_to()
            elif choice == '3':
                yes = ['y', 'yes']
                answer = input('Are you sure you would like to Exit? (y/n): ').lower().strip()
                if answer in yes:
                    print('Good bye!')
                    exit()
                else:
                    continue

    def how_to(self):
        print('\nHow to play:')
        print('First choose either Rock, Paper, or Scissors. You can Attack, use Magic, or Defend.')
        print('If using Magic, you will be prompted to choose Fire, Water, or Earth. Using Magic will cost Mana.\n')

    def main_loop(self):
        # check = Control(self.player, self.opponent)
        while self.play:
            # Score/Stats
            self.player.print_stats()
            self.opponent.print_stats()
            # Health check
            # check.check_health()
            # Player inputs
            rps_choice = self.player.throw_input()
            amd_choice = self.player.action_input()
            # Random comp input
            opp_rps_choice = choice(RPS)
            opp_amd_choice = self.opponent.random_action()
            # Magic system


if __name__ == '__main__':
    app = Game()
    app.start()
