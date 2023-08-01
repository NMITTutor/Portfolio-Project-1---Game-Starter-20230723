"""_summary_
Manages the commands - may not be the best name at this time

"""
import cmd_parser.token as token

game_state = 'Forest'
game_places = {'Forest': {'Story': 'You are in the forest.\nTo the north is a cave.\nTo the south is a castle',
                          'North': 'Cave', 'South': 'Castle', 'Image': 'forest.png'},
               'Cave': {'Story': 'You are at the cave.\nTo the south is forest.',
                        'North': '', 'South': 'Forest', 'Image': 'forest_circle.png'},
               'Castle': {'Story': 'You are at the castle.\nTo the north is forest.',
                          'North': 'Forest', 'South': '', 'Image': 'frog.png'},
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
        string: the story at the current place
    """
    global game_state

    valid_tokens = token.valid_list(command_input)

    for atoken in valid_tokens:
        game_place = game_places[game_state]
        if atoken.capitalize() in game_place:
            proposed_state = game_place[atoken.capitalize()]
            if proposed_state == '':
                return 'You can not go that way.\n'+game_places[game_state]['Story']
            else:
                game_state = proposed_state
                return game_places[game_state]['Story']
    return f'Cannot do that here.\n'+game_places[game_state]['Story']
