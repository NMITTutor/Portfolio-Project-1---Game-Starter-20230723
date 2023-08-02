"""_summary_
Manages the commands - may not be the best name at this time

"""
import cmd_parser.token as token


def move(game_place):
    global game_state
    location = game_place[1]
    game_state = location

    story_result = show_current_place()

    return story_result


game_state = 'Forest'
game_places = {'Forest': {'Story': 'You are in the forest.\nTo the north is a cave.\nTo the south is a castle',
                          'North': (move, 'Cave'), 'South': (move, 'Castle'), 'Image': 'forest.png'},
               'Cave': {'Story': 'You are at the cave.\nTo the south is forest.',
                        'South': (move, 'Forest'), 'Image': 'forest_circle.png'},
               'Castle': {'Story': 'You are at the castle.\nTo the north is forest.',
                          'North': (move, 'Forest'), 'Image': 'frog.png'},
               }


def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state

    return game_places[game_state]['Story']


def game_play(command_input):
    """
    Runs the game_play

    Args:
        command input string:
    Returns:
        string: the story at the current place, after an action
    """
    global game_state
    story_result = ''
    valid_tokens = token.valid_list(command_input)

    for atoken in valid_tokens:
        game_place = game_places[game_state]
        the_place = atoken.capitalize()
        if the_place in game_place:
            place = game_place[the_place]
            story_result = place[0](place)
        else:
            story_result = f"Can't {the_place} here\n"+show_current_place()
    return story_result
