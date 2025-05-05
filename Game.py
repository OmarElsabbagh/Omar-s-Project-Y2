import sys
import time
import random

# Constants
END_SCENE = "end"
DEFAULT_SPEED = 0.03

def type_writer(text, speed=DEFAULT_SPEED):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def get_choice(valid_choices):
    while True:
        choice = input('> ').strip().lower()
        if choice in valid_choices:
            return choice
        type_writer('That did not work. Try again.')

def random_noise():
    return random.choice([
        'a cat makes a loud noise',
        'a soft sound comes from the hall',
        'the wind slams a door',
        'your phone screen flashes, then turns off',
        'you feel like someone is watching you'
    ])

def wake_up():
    type_writer('You open your eyes. It is very dark. The power is out.')
    type_writer(f'Then... {random_noise()}.')
    type_writer('Someone knocks on your door. First soft, then louder.')
    type_writer('What do you do?\n1 - Open the door\n2 - Look for a flashlight first')
    choice = get_choice(['1', '2'])
    if choice == '1':
        type_writer('You open the door. A boy is standing there. He looks scared.')
        return 3, boy_encounter
    else:
        type_writer('You try to find a flashlight, but you fail.')
        type_writer('You open the door. A boy is standing there, crying.')
        return 1, boy_encounter

def boy_encounter():
    type_writer('He asks if he can use your phone.')
    type_writer('Do you give him the phone? (y/n)')
    choice = get_choice(['y', 'n'])
    if choice == 'y':
        if random.random() < 0.5:
            type_writer('He grabs it and runs. "Thanks!" he yells.')
            return -5, phone_chase
        else:
            type_writer('He makes a call, says thanks, and gives the phone back.')
            return 5, reflection
    else:
        type_writer('You say no. He leaves quietly.')
        return 0, reflection

def phone_chase():
    type_writer('You run after him.')
    type_writer('Do you:\n1 - Try to stop him\n2 - Try to talk to him')
    choice = get_choice(['1', '2'])
    if choice == '1':
        type_writer('You catch him and take the phone back.')
        return 3, badge_discovery
    else:
        type_writer('You ask him why he did it.')
        type_writer('He looks scared and drops the phone.')
        return 4, badge_discovery

def badge_discovery():
    type_writer('You see something on the ground.')
    type_writer('It is a small badge from an old orphanage.')
    type_writer('Do you:\n1 - Learn more\n2 - Ignore it')
    choice = get_choice(['1', '2'])
    if choice == '1':
        type_writer('You read that bad things happened at that place.')
        return 4, alley_encounter
    else:
        type_writer('You keep the badge but do nothing else.')
        return 1, alley_encounter

def alley_encounter():
    type_writer('You walk outside. A man steps out of the dark.')
    type_writer('"That boy is running from something bad."')
    type_writer('Do you:\n1 - Ask more\n2 - Keep walking')
    choice = get_choice(['1', '2'])
    if choice == '1':
        type_writer('"He got away from a bad place. Be careful."')
        return 2, decision_point
    else:
        type_writer('You walk away. He keeps talking behind you.')
        return -1, decision_point

def decision_point():
    type_writer('You see the boy again.')
    type_writer('What do you do?\n1 - Call the police\n2 - Let him go\n3 - Invite him inside')
    choice = get_choice(['1', '2', '3'])
    if choice == '1':
        type_writer('The police say he was missing. They thank you.')
        return 5, end_scene
    elif choice == '2':
        type_writer('He walks away. You wonder about his story.')
        return -2, end_scene
    else:
        type_writer('He waits, then nods. He comes inside.')
        return 4, end_scene

def reflection():
    type_writer('That night, you sit and think about the boy.')
    return 0, end_scene

def end_scene():
    type_writer('The night is quiet. Your part in this is over.')
    return 0, END_SCENE

def play_again_prompt():
    type_writer('Do you want to try again? (y/n)')
    choice = get_choice(['y', 'n'])
    return choice == 'y'

def main():
    while True:
        score = 0
        current_scene = wake_up
        while current_scene != END_SCENE:
            points, current_scene = current_scene()
            score += points
        type_writer(f'Your score: {score}')
        if not play_again_prompt():
            type_writer('Thanks for playing.')
            break

if __name__ == '__main__':
    main()
