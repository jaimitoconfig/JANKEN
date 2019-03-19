from .constants import *

class Control:
    def __init__(self, player, opponent):
        self.rps_throw = None
        self.player = player
        self.opponent = opponent

    def check_actions(self, rps_throw, first_action, second_action, first_magic_choice = None, second_magic_choice = None):
        # RPS = RPS
        if rps_throw == EQUAL:
            # A = A
            if first_action == AMD[0] and second_action == AMD[0]:
                print(DRAW)
            # A = D
            elif first_action == AMD[0] and second_action == AMD[2]:
                # Make better prints where it states what what used.
                # Check if I can shorten these by adding to if statement above as 'or' since it's the same outcome.
                print(DRAW)
            # A <  M
            elif first_action == AMD[0] and second_action == AMD[1]:
                print(HIT)
                self.player.health -= 1
                self.opponent.mana -= 2
            # M = D
            elif first_action == AMD[1] and second_action == AMD[2]:
                print(DRAW)
                self.player.mana -= 2
            # M > A
            elif first_action == AMD[1] and second_action == AMD[0]:
                print(HIT)
                self.opponent.health -= 1
                self.player.mana -= 2
            # D = D
            elif first_action == AMD[2] and second_action == AMD[2]:
                print(DRAW)
            # D = M
            elif first_action == AMD[2] and second_action == AMD[1]:
                print(DRAW)
                self.opponent.mana -= 2
            # D = A
            elif first_action == AMD[2] and second_action == AMD[0]:
                # Also consider adding this to the top if statement to save space.
                print(DRAW)

            # MAGIC
            # Need to work on how to properly implement the magic system choice.
            # M = M
            if (player_amd_choice == Player.amd[1] and enemy_amd_choice == Enemy.amd[1]) and \
                        player_fwe_choice == enemy_fwe_choice:
                    print(print_dialogue("magic") \
                          .format(player_fwe_choice, Player.name, player_amd_choice, player_rps_choice, Enemy.name,
                                  enemy_amd_choice, enemy_rps_choice))
                    Player.health -= 1
                    Enemy.health -= 1
                    Player.mana -= 2
                    Enemy.mana -= 2
                # M>M
                elif (player_amd_choice == Player.amd[1] and enemy_amd_choice == Enemy.amd[1]) and \
                        player_fwe_choice > enemy_fwe_choice:
                    print(print_dialogue("magic:hit") \
                          .format(player_amd_choice, Player.name, player_fwe_choice, Enemy.name, Player.name,
                                  player_amd_choice, player_rps_choice, Enemy.name, enemy_amd_choice, enemy_rps_choice))
                    Enemy.health -= 1
                    Player.mana -= 2
                    Enemy.mana -= 2
                # M<M
                elif (player_amd_choice == Player.amd[1] and enemy_amd_choice == Enemy.amd[1]) and \
                        player_fwe_choice < enemy_fwe_choice:
                    print(print_dialogue("magic:hit") \
                          .format(enemy_amd_choice, Enemy.name, enemy_fwe_choice, Player.name, Player.name,
                                  player_amd_choice, player_rps_choice, Enemy.name, enemy_amd_choice, enemy_rps_choice))
                    Player.health -= 1
                    Player.mana -= 2
                    Enemy.mana -= 2

        # At the end run a health check

        elif rps_throw == GREATER:

        elif rps_throw == LESS:

    def check_health(self):
        pass


    def main_check(self, first_choice, second_choice, first_action, second_action):
        # Possibly check magic choice here and enter as attribute to action.
        if first_action == AMD[1]: first_magic_choice = self.player.magic_input()
        if second_action == AMD[1]: second_magic_choice = self.opponent.magic_input()
        # Or add the attribute above and just pass it to the check_actions. This one might work better.
        # RPS = RPS
        if first_choice == second_choice:
            self.rps_throw = EQUAL
            self.check_actions(self.rps_throw, first_action, second_action)
        # RPS > RPS
        elif (first_choice == RPS[0] and second_choice == RPS[2]) or\
            (first_choice == RPS[1] and second_choice == RPS[0]) or\
            (first_choice == RPS[2] and second_choice == RPS[1]):
            self.rps_throw = GREATER
            self.check_actions(self.rps_throw, first_action, second_action)
        # RPS < RPS
        elif (first_choice == RPS[0] and second_choice == RPS[1]) or\
            (first_choice == RPS[1] and second_choice == RPS[2]) or\
            (first_choice == RPS[2] and second_choice == RPS[0]):
            self.rps_throw = LESS
            self.check_actions(self.rps_throw, first_action, second_action)


