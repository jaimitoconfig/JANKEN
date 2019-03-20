"""
Project: JANKEN
Description: Game settings and constants.
Date: 03/19/2019
Author: Jaimito
"""

from os import path


# Strings.
TITLE = 'JANKEN'
DESCRIPTION = 'A game of Rock, Paper, Scissors.'
CHOICE = 'Make your choice!'
LOW_MP = 'Low MP'
WON = 'Won'
DISPLAY_RESULT = '{} choose to use {} and {}.'
HELP_MENU = (
    {
      'instructions': 'Click the Left Mouse Button to choose either Rock, Paper, or Scissors. You can Attack, use Magic, or Defend. If using Magic, you will be prompted to choose Fire, Water, or Earth. Using Magic will cost MP. Game is won once HP is at 0.',
      'learn': 'Learn how to play!',
      'options': 'Click the Left Mouse Button on one of the options to the left and learn more.',
      'back': 'Click on Back to return to the title menu or press [ BACKSPACE ].',
      'tips': 'TIPS:',
      'enter': 'Press [ ENTER ] at title menu to start game.',
      'tab': 'Press [ TAB ] at title menu to enter help menu.',
    },
    {
      'rps': 'Rock, Paper, Scissors:',
      'r>s': 'Rock beats Scissors',
      'p>r': 'Paper beats Rock',
      's>p': 'Scissors beats Paper',
      'r=r': 'Rock is equal to Rock',
      'p=p': 'Scissors is equal to Scissors',
      's=s': 'Paper is equal to Paper'
    },
    {
      'amd': 'Attack, Magic, Defend:',
      'rps>': 'RPS >:',
      'a>a': 'Attack > Attack',
      'a=d': 'Attack = Defend',
      'a=m': 'Attack = Magic',
      'm>d': 'Magic > Defend',
      'm>a': 'Magic > Attack',
      'd=d': 'Defend = Defend',
      'd=m': 'Defend = Magic',
      'd=a': 'Defend = Attack',
      'rps=': 'RPS =:',
      'a=a': 'Attack = Attack',
      'a<m': 'Attack < Magic',
      'm=d': 'Magic = Defend',
      'm>a': 'Magic > Attack',
      'd=d': 'Defend = Defend',
      'd=m': 'Defend = Magic',
      'd=a': 'Defend = Attack'
      },
    {
      'fwe': 'Fire, Water, Earth:',
      'f>e': 'Fire beats Earth',
      'w>f': 'Water beats Fire',
      'e>w': 'Earth beats Water',
      'f=f': 'Fire is equal to Fire',
      'e=e': 'Earth is equal to Earth',
      'w=w': 'Water is equal to Water'
    }
    )

# Options.
PLAY = 'Play'
HELP = 'Help'
EXIT = 'Quit'
RESTART = 'Restart'
BACK = 'Back'
ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'
ATTACK = 'Attack'
MAGIC = 'Magic'
DEFEND = 'Defend'
FIRE = 'Fire'
WATER = 'Water'
EARTH = 'Earth'
EQUAL = '='
GREATER = '>'
LESS = '<'
DRAW = 'Draw'
HIT = 'Hit'
WIN = 'Win'
LOST = 'Lost'
CONTINUE = 'Continue'
CHECK_RESULTS = [HIT, DRAW]
RPS = [ROCK, PAPER, SCISSORS]
AMD = [ATTACK, MAGIC, DEFEND]
FWE = [FIRE, WATER, EARTH]
ATTACK_DEFEND = [ATTACK, DEFEND]

# Settings.
STATES = ('title', 'help', 'game')
DELAY = 120*2
STYLE = path.join('assets', 'fonts', 'Perfect DOS VGA 437.ttf')
SOUND = path.join('assets', 'sounds', 'Blip1.ogg')
ROCK_IMAGE = path.join('assets', 'images', 'battle_axe_5_2x.png')
PAPER_IMAGE = path.join('assets', 'images', 'shortbow_3_2x.png')
SCISSORS_IMAGE = path.join('assets', 'images', 'claymore_blessed_2x.png')
ATTACK_IMAGE = path.join('assets', 'images', 'glove_5_2x.png')
MAGIC_IMAGE = path.join('assets', 'images', 'scroll_old_2x.png')
DEFEND_IMAGE = path.join('assets', 'images', 'large_shield_3_2x.png')
WATER_IMAGE = path.join('assets', 'images', 'scroll-blue_2x.png')
EARTH_IMAGE = path.join('assets', 'images', 'scroll-brown_2x.png')
FIRE_IMAGE = path.join('assets', 'images', 'scroll-Red_2x.png')

# Colors.
WHITE_SMOKE = (245, 245, 245)
GREEN = (0, 255, 0)
DEEP_NAVY = (4, 0, 157)
SPACE = (25, 25, 25)
SELECTED = (242, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)