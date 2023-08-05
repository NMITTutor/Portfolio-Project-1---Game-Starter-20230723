""" 
A comment describing the game module
"""
import PySimpleGUI as sg


import cmd_parser.command_manager as cm


def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """

    sg.theme('Dark Blue 3')  # please make your windows
    prompt_input = [sg.Text('Enter your command', font='Any 14'), sg.Input(
        key='-IN-', size=(20, 1), font='Any 14')]
    buttons = [sg.Button('Enter',  bind_return_key=True), sg.Button('Exit')]
    command_col = sg.Column([prompt_input, buttons], element_justification='r')
    layout = [[sg.Image(r'images/forest.png', size=(100, 100), key="-IMG-"), sg.Text(cm.show_current_place(), size=(300, 8), font='Any 12', key='-OUTPUT-')],
              [command_col]]

    return sg.Window('Adventure Game', layout, size=(640, 400))


if __name__ == "__main__":
    # testing for now - these should be part of a test suite
    # print(show_current_place())
    # current_story = game_play('North')
    # print(show_current_place())

    # A persisent window - stays until "Exit" is pressed
    window = make_a_window()

    while True:
        event, values = window.read()
        print(event)
        if event == 'Enter':
            current_story = cm.game_play(values['-IN-'].lower())

            window['-OUTPUT-'].update(current_story)

            window['-IMG-'].update(r'images/'+cm.game_places[cm.game_state]
                                   ['Image'], size=(100, 100))

            pass
        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
            break
        else:
            pass

    window.close()
