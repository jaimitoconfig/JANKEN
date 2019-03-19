"""
Project: JANKEN
Description: Title, Help, and Game States.
Date: 3/19/2019
Author: Jaimito
"""

try:
    import pygame
    from pygame.locals import *
    from .ui import *
    from .constants import *
    from .checks import *
    from .base import BaseModel
    from .bot import Bot
    from sys import exit
except ImportError as err:
    print('could not load module. %s' % err)
    exit(2)


class States:
    """ States class initializes variables that help with moving between states. """
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None


class Title(States):
    """
    Title state. Will display options to play the Game, go into Help, or quit.
    [RETURN] will go into Game state. [TAB] will go into Help state.
    """
    def __init__(self):
        States.__init__(self)
        self.state_selection = []

    def cleanup(self):
        """ Cleans up variables and others, as it switches to a new state. """
        self.next = None
        del self.state_selection

    def startup(self):
        """ Starts up variables and others, as the state is being switched in this one. """
        self.state_selection = []

    def get_event(self, event):
        """ Event update function for key presses. """
        if event.type is KEYDOWN and event.key is K_RETURN:
            self.next = STATES[2]
            self.done = True
        elif event.type is KEYDOWN and event.key is K_TAB:
            self.next = STATES[1]
            self.done = True

    def display_menu(self, screen):
        """ Displays Title menu options. """
        center_x, center_y = screen.get_rect().centerx, screen.get_rect().centery  # 300, 200

        display_box(screen, center_x + 60, center_y, 360, 160)
        display_text(screen, TITLE, size=60, pos=[center_x + 60, center_y])
        display_text(screen, DESCRIPTION, size=15, pos=[center_x + 60, center_y + 40])

        display_box(screen, 110, center_y, 100, 160)
        self.state_selection = [button(screen, 110, center_y - 45, new_state=STATES[2]),
                                button(screen, 110, center_y, new_state=STATES[1])]
        button(screen, 110, center_y + 45, target=power_off)
        multiline_text(screen, 20, 45, WHITE_SMOKE, [110, center_y - 45], True, PLAY, HELP, EXIT)

        display_box(screen, center_x, 340, 360, 50)
        multiline_text(screen, 15, 20, WHITE_SMOKE, [center_x, 330], True,
                       'Click [Left Mouse Button] to select option.',
                       'Press [ESC] to exit at any time.')

    def update(self, screen):
        """ Constantly updating. """
        self.draw(screen)

    def draw(self, screen):
        """ Draws onto the screen and changes states depending on the option chosen. """
        pygame.display.set_caption(TITLE + ' | Title Menu')
        screen.fill(SPACE)

        self.display_menu(screen)
        if STATES[2] in self.state_selection:
            pygame.time.delay(DELAY)
            self.next = STATES[2]
            self.done = True
        elif STATES[1] in self.state_selection:
            pygame.time.delay(DELAY)
            self.next = STATES[1]
            self.done = True


class Help(States):
    """
    Help menu state. Will display instructions and an option to go back. [BACKSPACE] returns to Title.
    """
    def __init__(self):
        States.__init__(self)
        self.state_selection = []
        self.selected = None

    def cleanup(self):
        """ Cleans up variables and others, as it switches to a new state. """
        self.next = None
        del self.state_selection

    def startup(self):  # Consider removing.
        """ Starts up variables and others, as the state is being switched in this one. """
        self.state_selection = []
        self.selected = None

    def get_event(self, event):
        """ Event update function for key presses. """
        if event.type == KEYDOWN and event.key is K_BACKSPACE:
            self.next = STATES[0]
            self.done = True

    def display_help_menu(self, screen):
        """ Displays help menu text and options. """
        center_x, center_y = screen.get_rect().centerx, screen.get_rect().centery  # 300, 200

        display_box(screen, center_x + 60, 65, 430, 100)
        wrap_text(screen, HELP_MENU[0]['instructions'], size=15, rect=(160, 30, 430, 120))

        display_box(screen, center_x + 60, center_y + 45, 430, 220)
        if self.selected is None:
            display_text(screen, HELP_MENU[0]['learn'], size=20, pos=[center_x + 60, center_y - 45])
            wrap_text(screen, HELP_MENU[0]['options'], size=15, rect=(center_x - 65, center_y - 25, 260, 100))
            wrap_text(screen, HELP_MENU[0]['back'], size=15, rect=(center_x - 70, center_y + 25, 280, 100))
            multiline_text(screen, 15, 20, WHITE_SMOKE, [center_x + 60, center_y + 80], True,
                           HELP_MENU[0]['tips'],
                           HELP_MENU[0]['enter'],
                           HELP_MENU[0]['tab'])

        elif self.selected is 'rps':
            display_text(screen, HELP_MENU[1]['rps'], size=20, color=RED, pos=[center_x + 60, center_y - 45])
            multiline_text(screen, 15, 20, WHITE_SMOKE, [center_x + 60, center_y], True,
                           HELP_MENU[1]['r>s'],
                           HELP_MENU[1]['p>r'],
                           HELP_MENU[1]['s>p'])
            multiline_text(screen, 15, 20, WHITE_SMOKE, [center_x + 60, center_y + 70], True,
                           HELP_MENU[1]['r=r'],
                           HELP_MENU[1]['p=p'],
                           HELP_MENU[1]['s=s'])

        elif self.selected is 'amd':
            display_text(screen, HELP_MENU[2]['amd'], size=20, color=GREEN, pos=[center_x + 60, center_y - 45])
            multiline_text(screen, 15, 20, WHITE_SMOKE, [center_x - 60, center_y - 20], True,
                           HELP_MENU[2]['rps>'],
                           HELP_MENU[2]['a>a'],
                           HELP_MENU[2]['a=d'],
                           HELP_MENU[2]['a=m'],
                           HELP_MENU[2]['m>d'],
                           HELP_MENU[2]['m>a'],
                           HELP_MENU[2]['d=d'],
                           HELP_MENU[2]['d=m'],
                           HELP_MENU[2]['d=a'])
            multiline_text(screen, 15, 20, WHITE_SMOKE, [center_x + 160, center_y - 20], True,
                           HELP_MENU[2]['rps='],
                           HELP_MENU[2]['a=a'],
                           HELP_MENU[2]['a<m'],
                           HELP_MENU[2]['m=d'],
                           HELP_MENU[2]['m>a'],
                           HELP_MENU[2]['d=d'],
                           HELP_MENU[2]['d=m'],
                           HELP_MENU[2]['d=a'])

        elif self.selected is 'fwe':
            display_text(screen, HELP_MENU[3]['fwe'], size=20, color=YELLOW, pos=[center_x + 60, center_y - 45])
            multiline_text(screen, 15, 20, WHITE_SMOKE, [center_x + 60, center_y], True,
                           HELP_MENU[3]['f>e'],
                           HELP_MENU[3]['w>f'],
                           HELP_MENU[3]['e>w'])
            multiline_text(screen, 15, 20, WHITE_SMOKE, [center_x + 60, center_y + 70], True,
                           HELP_MENU[3]['f=f'],
                           HELP_MENU[3]['e=e'],
                           HELP_MENU[3]['w=w'])

        display_box(screen, 80, center_y, 100, 160)
        help_details = [button(screen, 80, center_y - 55, option=True),
                        button(screen, 80, center_y - 20, option=True),
                        button(screen, 80, center_y + 15, option=True)]
        self.state_selection = button(screen, 80, center_y + 55, old_state=STATES[1], new_state=STATES[0])
        multiline_text(screen, 20, 38, WHITE_SMOKE, [80, center_y - 55], True, 'RPS', 'AMD', 'FWE', BACK)

        if True in help_details:
            pygame.time.delay(DELAY)
            if help_details[0] is True:
                self.selected = 'rps'
            elif help_details[1] is True:
                self.selected = 'amd'
            elif help_details[2] is True:
                self.selected = 'fwe'

    def update(self, screen):
        """ Constantly updating. """
        self.draw(screen)

    def draw(self, screen):
        """ Draws onto the screen and changes states depending on the option chosen. """
        pygame.display.set_caption(TITLE + ' | Help Menu')
        screen.fill(SPACE)
        self.display_help_menu(screen)

        if STATES[0] in self.state_selection:
            pygame.time.delay(DELAY)
            self.next = STATES[0]
            self.done = True


class Game(States):
    """
    Game state. This is the main game loop. [r] will go back to Title.
    """
    def __init__(self):
        States.__init__(self)
        self.player = BaseModel('Player')
        self.opponent = Bot()
        self.result = None
        self.game_result = None
        self.game_done = CONTINUE

    def cleanup(self):
        """ Cleans up variables and others, as it switches to a new state. """
        self.player.reset_stats()
        self.opponent.reset_stats()
        self.reset_results()

    def startup(self):
        """ Starts up variables and others, as the state is being switched in this one. """
        self.game_done = CONTINUE

    def get_event(self, event):
        """ Event update function for key presses. """
        if event.type is KEYDOWN and event.key is K_r:  # Quick restart.
            self.game_done = RESTART

    def reset_results(self):
        """ Resets the result variables for when switching states or continuing. """
        self.result = None
        self.game_result = None

    def game_loop(self, screen):
        """
        This is the main game loop function.
        First allows to select Rock, Paper, Scissors.
        Then Attack, Magic or Defend. If Magic is chosen it will display Fire, Water, Earth options.
        It then checks the options and provide a result which determines the games outcome.
        """
        global player_actions, opponent_actions

        if self.result is None and self.game_result is None:
            player_actions = self.player.choose_option(screen)
            opponent_actions = self.opponent.choose_option()
            if player_actions is not None and opponent_actions is not None:
                throw_result = check_throw(player_actions[0], opponent_actions[0], RPS)
                self.result = check_actions(throw_result, player_actions, opponent_actions, self.player, self.opponent)

        elif self.result in CHECK_RESULTS and self.game_result is None:
            self.player.display_options(screen, CONTINUE, RESTART, EXIT)
            self.player.display_results(screen, self.result, self.opponent)

            if True in self.player.options:
                pygame.time.delay(DELAY)
                if self.player.options[0] is True:
                    self.player.reset_choices()
                    self.opponent.reset_choices()
                    self.reset_results()
                    self.game_done = CONTINUE
                elif self.player.options[1] is True:
                    self.game_done = RESTART
                elif self.player.options[2] is True:
                    self.game_done = EXIT

    def end_result(self, screen, result, color):
        """ This displays the WIN or LOSE outcome after HP is 0. """
        x, y = screen.get_rect().centerx, screen.get_rect().centerx
        display_box(screen, x + 70, y - 185, 420, 210)
        display_text(screen, 'You {}!'.format(result), size=60, color=color,
                     pos=[x + 70, y - 185])
        self.player.display_options(screen, PLAY, RESTART, EXIT)

        if True in self.player.options:
            pygame.time.delay(DELAY)
            if self.player.options[0] is True:
                self.player.soft_reset()
                self.opponent.soft_reset()
                self.reset_results()
                if result is WON:
                    self.player.score += 1  # Player score up.
                elif result is LOST:
                    self.opponent.score += 1  # Opponent score up.
                self.game_done = CONTINUE
            elif self.player.options[1] is True:
                self.player.reset_stats()
                self.opponent.reset_stats()
                self.game_result = None
                self.game_done = RESTART
            elif self.player.options[2] is True:
                self.player.reset_stats()
                self.opponent.reset_stats()
                self.game_result = None
                self.game_done = EXIT

    def display_decisions(self, screen):
        """ Displays the decisions being made by the player. """
        w, h = 420, 150
        x = screen.get_rect().centerx
        y = 310
        display_box(screen, x + 70, y, w, h)

        if len(self.player.decisions) is 0:
            display_text(screen, CHOICE, size=40, pos=[230 + 145, 310])
            display_text(screen, 'Press [ r ] at any time to restart.', size=15, pos=[230 + 145, 340])
        elif len(self.player.decisions) is 1:
                if self.player.decisions[0] is ROCK:
                    display_image(screen, ROCK_IMAGE, [230, 310])
                elif self.player.decisions[0] is PAPER:
                    display_image(screen, PAPER_IMAGE, [230, 310])
                elif self.player.decisions[0] is SCISSORS:
                    display_image(screen, SCISSORS_IMAGE, [230, 310])  # SCISSORS image.
                display_text(screen, self.player.decisions[0], pos=[230, 310 + 63])

        elif len(self.player.decisions) is 2:
                if self.player.decisions[0] is ROCK:
                    display_image(screen, ROCK_IMAGE, [230, 310])
                elif self.player.decisions[0] is PAPER:
                    display_image(screen, PAPER_IMAGE, [230, 310])
                elif self.player.decisions[0] is SCISSORS:
                    display_image(screen, SCISSORS_IMAGE, [230, 310])
                display_text(screen, self.player.decisions[0], pos=[230, 310 + 63])

                if self.player.decisions[1] is ATTACK:
                    display_image(screen, ATTACK_IMAGE, [230 + 145, 310])
                elif self.player.decisions[1] is MAGIC:
                    display_image(screen, MAGIC_IMAGE, [230 + 145, 310])
                elif self.player.decisions[1] is DEFEND:
                    display_image(screen, DEFEND_IMAGE, [230 + 145, 310])
                display_text(screen, self.player.decisions[1], pos=[230 + 145, 310 + 63])

        elif len(self.player.decisions) is 3:
                if self.player.decisions[0] is ROCK:
                    display_image(screen, ROCK_IMAGE, [230, 310])
                elif self.player.decisions[0] is PAPER:
                    display_image(screen, PAPER_IMAGE, [230, 310])
                elif self.player.decisions[0] is SCISSORS:
                    display_image(screen, SCISSORS_IMAGE, [230, 310])
                display_text(screen, self.player.decisions[0], pos=[230, 310 + 63])

                if self.player.decisions[1] is ATTACK:
                    display_image(screen, ATTACK_IMAGE, [230 + 145, 310])
                elif self.player.decisions[1] is MAGIC:
                    display_image(screen, MAGIC_IMAGE, [230 + 145, 310])
                elif self.player.decisions[1] is DEFEND:
                    display_image(screen, DEFEND_IMAGE, [230 + 145, 310])
                display_text(screen, self.player.decisions[1], pos=[230 + 145, 310 + 63])

                if self.player.decisions[2] is FIRE:
                    display_image(screen, FIRE_IMAGE, [230 + 280, 310])
                elif self.player.decisions[2] is WATER:
                    display_image(screen, WATER_IMAGE, [230 + 280, 310])
                elif self.player.decisions[2] is EARTH:
                    display_image(screen, EARTH_IMAGE, [230 + 280, 310])
                display_text(screen, self.player.decisions[2], pos=[230 + 280, 310 + 63])

    def update(self, screen):
        """ Constantly updating. """
        self.draw(screen)

    def draw(self, screen):
        """
        Draws onto the screen and changes states depending on the option chosen.
        The health check helps with the WIN or LOSE results of the game by constantly checking HP.
        """
        pygame.display.set_caption(TITLE + ' | Player:{} vs Opponent:{}'.format(self.player.score, self.opponent.score))
        screen.fill(SPACE)

        self.player.display_stats(screen, [80, 20])
        self.opponent.display_stats(screen, [80, 130])

        self.game_result = check_health(self.player, self.opponent)

        self.display_decisions(screen)

        if self.game_result is None:
            if self.game_done is CONTINUE:
                self.game_loop(screen)
            elif self.game_done is EXIT:
                power_off()
            elif self.game_done is RESTART:
                self.next = STATES[0]
                self.done = True

        elif self.game_result is LOST:
            self.end_result(screen, LOST, RED)

        elif self.game_result is WIN:
            self.end_result(screen, WON, GREEN)

        # print(self.player.decisions)
        # print(self.opponent.decisions)
