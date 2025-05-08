import time
import random
import sys

# Constants
MAX_SCORE = 10     # Win threshold
MIN_SCORE = -5     # Lose threshold
TYPE_SPEED = 0.03  # Typewriter effect speed


def type_writer(text, speed=TYPE_SPEED):
    """Prints text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def get_choice(valid_options):
    """Prompts the user until a valid input is received."""
    while True:
        choice = input("> ").strip().lower()
        if choice in valid_options:
            return choice
        type_writer("Please enter a valid option.")


def check_game_over(score):
    """Checks whether the game should end based on score."""
    if score >= MAX_SCORE:
        type_writer("\n🎉 You’ve reached a turning point. The story ends on a hopeful note.")
        return True
    elif score <= MIN_SCORE:
        type_writer("\n💀 Things took a dark turn. The story ends in shadows.")
        return True
    return False


def wake_up_scene():
    type_writer("You wake up suddenly. It's dark.")
    type_writer(f"Outside, {random.choice(['a siren wails faintly', 'the wind whispers', 'a knock echoes in the hallway'])}.")
    type_writer("There’s a knock at your apartment door.\n")
    type_writer("1 - Open the door immediately")
    type_writer("2 - Wait and listen")

    choice = get_choice(['1', '2'])
    if choice == '1':
        type_writer("You open the door. A boy stands there, barefoot and frightened.")
        return 2, encounter_boy
    else:
        type_writer("You wait. The knock comes again, more urgent.")
        return 1, encounter_boy


def encounter_boy():
    type_writer("He asks for your phone. He's shaking.\n")
    type_writer("y - Give it to him")
    type_writer("n - Refuse")

    choice = get_choice(['y', 'n'])
    if choice == 'y':
        if random.random() < 0.5:
            type_writer("He grabs it and runs into the night.")
            return -3, chase_scene
        else:
            type_writer("He dials. Whispers. Hands it back. 'Thank you,' he says.")
            return 4, reflection_scene
    else:
        type_writer("He looks down, then disappears down the hallway.")
        return 0, reflection_scene


def chase_scene():
    type_writer("You run after him, heart pounding.\n")
    type_writer("1 - Tackle him")
    type_writer("2 - Call out and ask him to stop")

    choice = get_choice(['1', '2'])
    if choice == '1':
        type_writer("You catch up, grab his arm. He drops the phone.")
        return 2, discovery_scene
    else:
        type_writer("He stops briefly, then keeps running, but drops your phone.")
        return 1, discovery_scene


def discovery_scene():
    type_writer("As you pick up your phone, something falls from his pocket.")
    type_writer("It’s a hospital ID badge. His name: Elias.\n")
    type_writer("1 - Go after him")
    type_writer("2 - Keep the badge and return home")

    choice = get_choice(['1', '2'])
    if choice == '1':
        type_writer("You decide to follow him. Something’s not right.")
        return 2, alley_scene
    else:
        type_writer("You pocket the badge, unsure what to think.")
        return 1, alley_scene


def alley_scene():
    type_writer("In a dark alley, a stranger steps from the shadows.")
    type_writer('"They’re looking for the boy," he says. "Be careful who you trust."\n')
    type_writer("1 - Ask him who 'they' are")
    type_writer("2 - Walk away silently")

    choice = get_choice(['1', '2'])
    if choice == '1':
        type_writer("He hands you a card. No name, just a symbol.")
        return 2, final_decision
    else:
        type_writer("You ignore him. But the symbol burns into your memory.")
        return 0, final_decision


def reflection_scene():
    type_writer("You sit in the quiet. Something about the encounter lingers.")
    return 0, final_decision


def final_decision():
    type_writer("You see Elias again, near the train station.\n")
    type_writer("1 - Alert the authorities")
    type_writer("2 - Offer to help him")
    type_writer("3 - Turn away and let him go")

    choice = get_choice(['1', '2', '3'])
    if choice == '1':
        type_writer("Police take him. He goes quietly. Too quietly.")
        return 3, end_game
    elif choice == '2':
        type_writer("He smiles, tears in his eyes. 'Thank you,' he whispers.")
        return 4, end_game
    else:
        type_writer("He vanishes into the crowd. You never see him again.")
        return -1, end_game


def end_game():
    type_writer("Your choices led here. A story with echoes.")
    return 0, None  # End of story


def main():
    try:
        while True:
            score = 0
            scene = wake_up_scene

            while scene:
                points, next_scene = scene()
                score += points

                if points > 0:
                    type_writer(f"✅ You gained {points} points.")
                elif points < 0:
                    type_writer(f"⚠️ You lost {abs(points)} points.")
                else:
                    type_writer("➖ No points gained or lost.")

                type_writer(f"📊 Your score: {score}\n")

                if check_game_over(score):
                    break

                scene = next_scene

            type_writer(f"🏁 Final Score: {score}")
            type_writer("Would you like to play again? (y/n)")
            if get_choice(['y', 'n']) == 'n':
                type_writer("Thanks for playing. Until next time.")
                break
    except KeyboardInterrupt:
        type_writer("\n👋 Exiting the game. Goodbye!")


if __name__ == "__main__":
    main()