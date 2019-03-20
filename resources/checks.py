"""
Project: JANKEN
Description: Check result functions for game logic. Return results.
Date: 3/19/2019
Author: Jaimito
"""

try:
    from .constants import *
    from sys import exit
except ImportError as err:
    print('could not load module. %s' % err)
    exit(2)


def check_health(player, opponent):
    """ Once player or opponent HP is 0 return game winning result else continue. """
    if player.hp <= 0:
        return LOST
    elif opponent.hp <= 0:
        return WIN
    else:
        pass


def check_throw(player_throw, opponent_throw, throw_type):
    """ This checks throws (rock, paper, scissors, fire, water, earth) and returns the result. """
    if player_throw is opponent_throw:  # RPS = RPS or FWE = FWE
        return EQUAL
    elif (player_throw is throw_type[0] and opponent_throw is throw_type[2]) or \
            (player_throw is throw_type[1] and opponent_throw is throw_type[0]) or \
            (player_throw is throw_type[2] and opponent_throw is throw_type[1]):  # RPS > RPS or FWE > FWE
        return GREATER
    elif (player_throw is throw_type[0] and opponent_throw is throw_type[1]) or \
            (player_throw is throw_type[1] and opponent_throw is throw_type[2]) or \
            (player_throw is throw_type[2] and opponent_throw is throw_type[0]):  # RPS < RPS or FWE < FWE
        return LESS


def check_actions(throw_result, player_actions, opponent_actions, player, opponent):
    """ This checks the action (attack, magic, defend), removes HP and MP as needed and returns result. """
    if throw_result is EQUAL:  # RPS = RPS
        if player_actions[1] is AMD[0] and opponent_actions[1] is AMD[0] or\
                player_actions[1] is AMD[0] and opponent_actions[1] is AMD[2] or\
                player_actions[1] is AMD[2] and opponent_actions[1] is AMD[2] or\
                player_actions[1] is AMD[2] and opponent_actions[1] is AMD[0]:  # A = A or A = D or D = D or D = A.
            player.stat_changes = [0, 0]
            opponent.stat_changes = [0, 0]
            return DRAW
        elif player_actions[1] is AMD[1] and opponent_actions[1] is AMD[2]:  # M = D - player MP -2.
            player.stat_changes = [0, 2]
            opponent.stat_changes = [0, 0]
            player.mp -= player.stat_changes[1]
            return DRAW
        elif player_actions[1] is AMD[2] and opponent_actions[1] is AMD[1]:  # D = M - opponent MP -2.
            player.stat_changes = [0, 0]
            opponent.stat_changes = [0, 2]
            opponent.mp -= opponent.stat_changes[1]
            return DRAW
        elif player_actions[1] is AMD[0] and opponent_actions[1] is AMD[1]:  # A <  M - player HP -1, opponent MP -2.
            player.stat_changes = [1, 0]
            opponent.stat_changes = [0, 2]
            player.hp -= player.stat_changes[0]
            opponent.mp -= opponent.stat_changes[1]
            player.opponent_hit = True
            return HIT
        elif player_actions[1] is AMD[1] and opponent_actions[1] is AMD[0]:  # M > A - opponent HP -1, player MP -2.
            player.stat_changes = [0, 2]
            opponent.stat_changes = [1, 0]
            opponent.hp -= opponent.stat_changes[0]
            player.mp -= player.stat_changes[1]
            return HIT
        # Magic check.
        if player_actions[1] is AMD[1] and opponent_actions[1] is AMD[1]:
                if check_throw(player_actions[2], opponent_actions[2], FWE) is EQUAL:  # M = M - player MP -2, opponent MP -2.
                    player.stat_changes = [0, 2]
                    opponent.stat_changes = [0, 2]
                    player.mp -= player.stat_changes[1]
                    opponent.mp -= opponent.stat_changes[1]
                    return DRAW
                elif check_throw(player_actions[2], opponent_actions[2], FWE) is GREATER:  # M > M - opponent HP -1, opponent MP -2, player MP -2.
                    player.stat_changes = [0, 2]
                    opponent.stat_changes = [1, 2]
                    opponent.hp -= opponent.stat_changes[0]
                    player.mp -= player.stat_changes[1]
                    opponent.mp -= opponent.stat_changes[1]
                    return HIT
                elif check_throw(player_actions[2], opponent_actions[2], FWE) is LESS:  # M < M - player HP -1, player MP -2, opponent MP -2.
                    player.stat_changes = [1, 2]
                    opponent.stat_changes = [0, 2]
                    player.hp -= player.stat_changes[0]
                    player.mp -= player.stat_changes[1]
                    opponent.mp -= opponent.stat_changes[1]
                    player.opponent_hit = True
                    return HIT

    elif throw_result is GREATER:
        if player_actions[1] is AMD[0] and opponent_actions[1] is AMD[2] or\
                player_actions[1] is AMD[2] and opponent_actions[1] is AMD[0] or\
                player_actions[1] is AMD[2] and opponent_actions[1] is AMD[2]:  # A = D or D = A or D = D
            player.stat_changes = [0, 0]
            opponent.stat_changes = [0, 0]
            return DRAW
        elif player_actions[1] is AMD[2] and opponent_actions[1] is AMD[1]:  # D = M - opponent MP -2.
            player.stat_changes = [0, 0]
            opponent.stat_changes = [0, 2]
            opponent.mp -= opponent.stat_changes[1]
            return DRAW
        elif player_actions[1] is AMD[0] and opponent_actions[1] is AMD[0]:  # A > A - opponent HP -1.
            player.stat_changes = [0, 0]
            opponent.stat_changes = [1, 0]
            opponent.hp -= opponent.stat_changes[0]
            return HIT
        elif player_actions[1] is AMD[0] and opponent_actions[1] is AMD[1]:  # A = M - player HP -1, opponent HP -1, opponent MP -2.
            player.stat_changes = [1, 0]
            opponent.stat_changes = [1, 2]
            player.hp -= player.stat_changes[0]
            opponent.hp -= opponent.stat_changes[0]
            opponent.mp -= opponent.stat_changes[1]
            return HIT
        elif player_actions[1] is AMD[1] and opponent_actions[1] is AMD[0]:  # M > A - opponent HP -2, player MP -2.
            player.stat_changes = [0, 2]
            opponent.stat_changes = [2, 0]
            opponent.hp -= opponent.stat_changes[0]
            player.mp -= player.stat_changes[1]
            return HIT
        elif player_actions[1] is AMD[1] and opponent_actions[1] is AMD[2]:  # M > D - opponent HP -1, player MP -2.
            player.stat_changes = [0, 2]
            opponent.stat_changes = [1, 0]
            opponent.hp -= opponent.stat_changes[0]
            player.mp -= player.stat_changes[1]
            return HIT

        # Magic check.
        if player_actions[1] is AMD[1] and opponent_actions[1] is AMD[1]:
                if check_throw(player_actions[2], opponent_actions[2], FWE) is EQUAL:  # M = M - player MP -2, opponent HP -2, opponent MP -2.
                    player.stat_changes = [0, 2]
                    opponent.stat_changes = [2, 2]
                    opponent.hp -= opponent.stat_changes[0]
                    player.mp -= player.stat_changes[1]
                    opponent.mp -= opponent.stat_changes[1]
                    return HIT
                elif check_throw(player_actions[2], opponent_actions[2], FWE) is GREATER:   # M > M - player MP -2, opponent HP -2, opponent MP -2.
                    player.stat_changes = [0, 2]
                    opponent.stat_changes = [2, 2]
                    opponent.hp -= opponent.stat_changes[0]
                    player.mp -= player.stat_changes[1]
                    opponent.mp -= opponent.stat_changes[1]
                    return HIT
                elif check_throw(player_actions[2], opponent_actions[2], FWE) is LESS:  # M < M - player HP -1, player MP -2, opponent MP -2.
                    player.stat_changes = [1, 2]
                    opponent.stat_changes = [1, 2]
                    player.hp -= player.stat_changes[0]
                    opponent.hp -= opponent.stat_changes[0]
                    player.mp -= player.stat_changes[1]
                    opponent.mp -= opponent.stat_changes[1]
                    player.opponent_hit = True
                    return HIT

    elif throw_result is LESS:
        if player_actions[1] is AMD[0] and opponent_actions[1] is AMD[2] or\
                player_actions[1] is AMD[2] and opponent_actions[1] is AMD[0] or\
                player_actions[1] is AMD[2] and opponent_actions[1] is AMD[2]:  # A = D or D = A or D = D
            player.stat_changes = [0, 0]
            opponent.stat_changes = [0, 0]
            return DRAW
        elif player_actions[1] is AMD[1] and opponent_actions[1] is AMD[2]:  # M = D - player MP -2.
            player.stat_changes = [0, 2]
            opponent.stat_changes = [0, 0]
            player.mp -= player.stat_changes[1]
            return DRAW
        elif player_actions[1] is AMD[0] and opponent_actions[1] is AMD[0]:  # A < A - player HP -1.
            player.stat_changes = [1, 0]
            opponent.stat_changes = [0, 0]
            player.hp -= player.stat_changes[0]
            player.opponent_hit = True
            return HIT
        elif player_actions[1] is AMD[0] and opponent_actions[1] is AMD[1]:  # A < M - player HP -2, opponent MP -2.
            player.stat_changes = [2, 0]
            opponent.stat_changes = [0, 2]
            player.hp -= player.stat_changes[0]
            opponent.mp -= opponent.stat_changes[1]
            player.opponent_hit = True
            return HIT
        elif player_actions[1] is AMD[1] and opponent_actions[1] is AMD[0]:  # M = A - player HP -1, player MP -2, opponent HP -2.
            player.stat_changes = [1, 2]
            opponent.stat_changes = [1, 0]
            player.hp -= player.stat_changes[0]
            opponent.hp -= opponent.stat_changes[0]
            player.mp -= player.stat_changes[1]
            return HIT
        elif player_actions[1] is AMD[2] and opponent_actions[1] is AMD[1]:  # D < M - player HP -1, opponent MP -2.
            player.stat_changes = [1, 0]
            opponent.stat_changes = [0, 2]
            player.hp -= player.stat_changes[0]
            opponent.mp -= opponent.stat_changes[1]
            player.opponent_hit = True
            return HIT

        # Magic check.
        if player_actions[1] is AMD[1] and opponent_actions[1] is AMD[1]:
                if check_throw(player_actions[2], opponent_actions[2], FWE) is EQUAL:  # M = M - player HP -1, player MP -2, opponent MP -2.
                    player.stat_changes = [2, 2]
                    opponent.stat_changes = [0, 2]
                    player.hp -= player.stat_changes[0]
                    player.mp -= player.stat_changes[1]
                    opponent.mp -= opponent.stat_changes[1]
                    return HIT
                elif check_throw(player_actions[2], opponent_actions[2], FWE) is GREATER:  # M > M - player HP -1, player MP -2, opponent HP -1, opponent MP -2.
                    player.stat_changes = [1, 2]
                    opponent.stat_changes = [1, 2]
                    opponent.hp -= opponent.stat_changes[0]
                    player.hp -= player.stat_changes[0]
                    player.mp -= player.stat_changes[1]
                    opponent.mp -= opponent.stat_changes[1]
                    return HIT
                elif check_throw(player_actions[2], opponent_actions[2], FWE) is LESS:  # M < M - player HP -2, player MP -2, opponent MP -2.
                    player.stat_changes = [2, 2]
                    opponent.stat_changes = [0, 2]
                    player.hp -= player.stat_changes[0]
                    player.mp -= player.stat_changes[1]
                    opponent.mp -= opponent.stat_changes[1]
                    player.opponent_hit = True
                    return HIT