"""
Project: JANKEN
Description: GUI functions to help display, buttons, text, and images.
Date: 3/19/2019
Author: Jaimito
"""

try:
    import pygame
    from pygame.locals import *
    from .constants import *
    from sys import exit
except ImportError as err:
    print('could not load module. %s' % err)
    exit(2)

# INITIALIZE
pygame.font.init()
pygame.mixer.init()


def display_image(surface, image, pos):
    """ Blits images to surface. """
    try:
        image = pygame.image.load(image)
    except pygame.error:
        print('Cannot load image:', image)
        raise SystemExit

    image = image.convert_alpha()
    rect = image.get_rect()

    surface.blit(image, [pos[0] - rect[2] / 2, pos[1] - rect[3] / 2])


def display_box(surface, x, y, w, h):
    """ Makes rectangle surface with border, bilts to surface. """
    rect = pygame.surface.Surface([w, h]).convert_alpha()
    rect.fill(DEEP_NAVY)

    pygame.draw.rect(surface, WHITE_SMOKE, (x - w / 2, y - h / 2, w, h), 4)

    surface.blit(rect, [x - w / 2, y - h / 2])


def display_text(surface, text, size=20, color=WHITE_SMOKE, pos=[], centered=True):
    """ Blits a single line of text to surface. """
    font = pygame.font.Font(STYLE, size)

    text_object = font.render(text, True, color).convert_alpha()
    width, height = text_object.get_size()

    if centered is True:
        pos[0] -= width / 2
        pos[1] -= height / 2

    surface.blit(text_object, pos)


def multiline_text(surface, size=20, spacing=20, color=WHITE_SMOKE, pos=[0, 0], centered=True, *text):
    """ Blits multiple lines of text to surface using display_text function.  """
    next_line = 0

    for i in text:
        if i == "<n>":
            next_line += spacing
        else:
            display_text(surface, i, size, color, [pos[0], pos[1] + next_line], centered)
            next_line += spacing


def wrap_text(surface, text, size=20, color=WHITE_SMOKE, rect=(), aa=True):
    """ Wraps text according to rect size and blits it, returns left over text. """
    font = pygame.font.Font(STYLE, size)
    frame = pygame.Rect(rect)
    y = frame.top
    line_spacing = -2
    font_height = font.size("Tg")[1]

    while text:
        i = 1
        # Determines if the row of text will be outside our area.
        if y + font_height > frame.bottom:
            break
        # Determine maximum width of line.
        while font.size(text[:i])[0] < frame.width and i < len(text):
            i += 1
        # If text is wrapped, then adjust the wrap to the last word.
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1
        # Blit.
        image = font.render(text[:i], aa, color).convert_alpha()
        surface.blit(image, (frame.left, y))
        y += font_height + line_spacing
        text = text[i:]
    return text


def button(surface, x, y, target=False, old_state="title", new_state=False, option=False, args=None):
    """ Makes buttons from pygame.surface for switching between states, choosing options, or returns a function. """
    click = pygame.mixer.Sound(SOUND)
    pos = pygame.mouse.get_pos()
    keys = pygame.mouse.get_pressed()

    w, h = 100, 35
    x, y = x, y

    rect = pygame.surface.Surface([w, h])
    rect.convert_alpha()

    selected = False

    if (x - w / 2 + w) > pos[0] > (x - w / 2) and (y - h / 2 + h) > pos[1] > (y - h / 2):
        # pos[0] > x - w//2 and pos[0] < x - w//2 + w and pos[1] > y - h//2 and pos[1] < y - h//2 +h:
        selected = True
        rect.fill(SELECTED)
        rect.set_alpha(60)
        surface.blit(rect, [x - w / 2, y - h / 2])

    else:
        selected = False
        rect.fill(DEEP_NAVY)
        surface.blit(rect, [x - w / 2, y - h / 2])

    if selected is True:
        if new_state is not False:
            if keys[0]:
                click.play()
                return new_state
            else:
                return old_state

        elif target is not False:
            if keys[0]:
                click.play()
                if args is not None:
                    return target(args)
                else:
                    return target()

        elif option is not False:
            if keys[0]:
                click.play()
                return True
            else:
                return False

    else:
        if new_state is not False:
            return old_state

        elif option is not False:
            return False


def power_off():
    """ Exits out of the game. """
    pygame.quit()
    exit()
