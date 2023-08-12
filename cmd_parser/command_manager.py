"""_summary_
Manages the commands - may not be the best name at this time

"""
# import typing
import cmd_parser.token as token
import inventory.contents as inventory
import status.health as health

# Game commands


def move(game_place):
    """_summary_

    Args:
        game_place (_type_): _description_

    Returns:
        _type_: _description_
    """
    global game_state

    location = game_place[1]
    game_state = location

    story_result = show_current_place()

    return story_result


def talk_to_hermit(game_place):
    """_summary_
        Hermit gives a key
        ( inventory update add)
    Args:
        game_place (_type_): _description_
    Returns:
        _type_: _description_
    """
    inventory.collect_item("key")
    return move(game_place)


def enter_castle(game_place):
    result = ""
    if inventory.has_item('key'):
        result = move(game_place)
    else:
        result = "Visit the hermit to recieve a key to enter the castle.\n"+show_current_place()
    return result


def fight(game_place):
    """

    Args:
        game_place (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Implement "fight"
    # Check inventory for a sword - if no sword go to blacksmith
    # If there is a sword then flip a random to decide if they win or lose
    # If they lose they lose health
    #    They die when health is zero. When they die,  empty inventory, game_state = Forest
    # If they win they can move into the Castle ...
    result = "You can not fight because you don\'t have a sword.\nGet a sword from the blacksmith\'s.\nFighting has not been implemented\n Can you implement it?"+show_current_place()

    return result


game_state = 'Forest'
game_places = {'Forest': {'Story': 'You are in the forest.\nTo the north is a cave.\nTo the south is a castle',
                          'North': (move, 'Cave'), 'South': (move, 'Castle'), 'Image': 'forest.png'},
               'Cave': {'Story': 'You are at the hermit\'s cave.\n Talk to the hermit? To the south is forest.',
                        'South': (move, 'Forest'), 'Talk': (talk_to_hermit, 'Hermit'), 'Image': 'forest_circle.png'},
               'Castle': {'Story': 'You are at the castle.\n Enter the castle?\nTo the north is forest.',
                          'North': (move, 'Forest'), 'Enter': (enter_castle, 'InCastle'), 'Image': 'frog.png'},
               'Hermit': {'Story': 'The hermit does not talk, but gives you a key.\n To the south is forest.',
                          'South': (move, 'Forest'), 'Image': 'frog.png'},
               'InCastle': {'Story': 'You are inside the Castle.\n A knight is standing in front of you with sword drawn.\n You can leave, or fight.', "Leave": (move, "Castle"), "Fight": (fight, "Castle"), 'Image': 'frog.png'}
               }


def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state
    health.reduce(10)  # Lose health as you move
    return f"[Health={health.get()}]\n"+game_places[game_state]['Story']


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
    if not valid_tokens:
        story_result = 'Can not understand that sorry\n'+show_current_place()
    else:
        for atoken in valid_tokens:
            game_place = game_places[game_state]
            the_place = atoken.capitalize()
            if the_place in game_place:
                place = game_place[the_place]
                story_result = place[0](place)  # Run the action
            else:
                story_result = f"Can't {the_place} here\n"+show_current_place()
    return story_result
