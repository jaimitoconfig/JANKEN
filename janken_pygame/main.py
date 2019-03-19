"""
Project: JANKEN
Description: Control class helps with switching between states and constantly looping and updating.
Date: 3/19/2019
Author: Jaimito
"""

try:
    import pygame
    from pygame.locals import *
    from sys import exit
    from resources.states import Title, Help, Game
except ImportError as err:
    print('could not load module. %s' % err)
    exit(2)


class Control:
    """ Control class helps with switching between states and constantly looping and updating. """
    def __init__(self, **settings):
        self.__dict__.update(settings)
        self.done = False
        self.screen = pygame.display.set_mode(self.size, HWSURFACE | DOUBLEBUF)
        self.clock = pygame.time.Clock()

    def setup_states(self, state_dict, start_state):
        """ Sets up the current state. """
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        """ Changes to the next state. """
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous

    def update(self):
        """ Constantly updates in the main_game_loop while loop. """
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen)

    def event_loop(self):
        """ Event update function for key presses. """
        for event in pygame.event.get():
            if event.type is QUIT:
                self.done = True
            elif event.type is KEYUP and event.key is K_ESCAPE:
                self.done = True
            self.state.get_event(event)

    def main_game_loop(self):
        """ Main loop where all the magic happens! """
        while not self.done:
            self.event_loop()
            self.update()
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    settings = {
       'size': (600, 400),
       'fps': 60
    }

    app = Control(**settings)
    state_dict = {
        'title': Title(),
        'help': Help(),
        'game': Game()
    }
    app.setup_states(state_dict, 'title')
    app.main_game_loop()
    pygame.quit()
    exit()
