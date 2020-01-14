import time
import random


def message_player(messaging_player):  # This code simplifies slow sentences.
    print(messaging_player)
    time.sleep(3)


def suspensful_message(suspense_message):  # Dramatic effect for sentences.
    print(suspense_message)
    time.sleep(4)


def sudden_message(quick_message):  # Quick sentences show up
    print(quick_message)            # for dramatic effect.
    time.sleep(1)


def intro(inventory, realities):  # introduction to the game.
    message_player("\nYou have just woken up and appear to be "
                   "slightly dizzy.. There is no one around, "
                   "it's dead silent.")


def walk_inside(inventory, realities):  # This section is a subsection-code
    message_player("You walk inside the room..")  # for organisation
    message_player("it appears to be bigger than it looked before.")
    message_player("It's a Hall!")
    message_player("There's a chest at the end of the hall.. \n"
                   "Upon inspecting the chest..")
    message_player("It looks... Alien.")
    message_player("The Z-drive is glowing!\n")
    while not '1' or '2':  # Options to open the chest.
        try_key = input("Enter '1' to attempt to open the chest "
                        "with the Z-drive.\n"
                        "Enter '2' to ask the Cryobot to "
                        "shoot the chest.\n")
        if try_key == '1':
            message_player("You place the Z-drive in the middle-socket "
                           "of the chest.")
            message_player("It seems that the Z-drive opens the chest!\n")
            sudden_message("It opened!")
            message_player("A bright light shines through the entire hall "
                           "from the chest!")
            sudden_message("\nYou're being teleported!\n")
            if "Kepler-186f" in realities:  # Kepler Random choice.
                message_player("You have been teleported to planet "
                               "'Kepler-186f'.")
                message_player("You can still breath! Phew, you have been "
                               "teleported to an inhabited planet\nIt looks "
                               "like you were teleported to the "
                               "'City of Tessevel'.\n")
                message_player("There is a woman standing in front of you, "
                               "she stares at you...")
                message_player("The woman suddenly says:\n")
                message_player("You Won! Congratulations!")
                message_player("VR engines are getting tough ah?\nGood Job! "
                               "You Win!\n")
                play_again(inventory, realities)
            elif "Gliese 581g" in realities:  # Gliese Random choice.
                while not '1' or '2':
                    message_player("You appeared to have been teleported to "
                                   "planet 'Gliese 581g'.")
                    message_player("You are in a field.\n"
                                   "There's a small box resting on your foot.")
                    message_player("You open the box.")
                    message_player("It appears to have two pills inside.")
                    pills = input("There are two pills, please choose a pill "
                                  "to swallow: (Enter '1' or '2')\n"
                                  "1. Blue Pill\n"
                                  "2. Red Pill\n")
                    if pills == '1':
                        message_player("You are shaking..\n"
                                       "You faint\n"
                                       "You are slowly..\n"
                                       "Losing your memories.")
                        crossroads(inventory, realities)
                    elif pills == '2':
                        message_player("You have taken the Red Pill.. \n"
                                       "You faint\n"
                                       "You wake up on planet 'Kepler-186f'..")
                        message_player("You appear to be in the 'City of "
                                       "Tessevel'..")
                        message_player("There is a woman standing "
                                       "in front of you,\n"
                                       "she stares at you.. ")
                        message_player("The woman suddenly smiles and says:")
                        message_player("You Won! Congratulations!")
                        message_player("VR engines are getting crazy tough "
                                       "ah?")
                        message_player("Good Job!")
                        suspensful_message("GAME OVER - YOU WIN\n")
                        play_again(inventory, realities)
                    else:
                        message_player("You throw away the pills on the "
                                       "ground..")
                        message_player("You start choking")
                        sudden_message("\nSmack!\n")
                        message_player("You wake up after a while..")
        elif try_key == '2':
            message_player("You ask Cryobot to shoot the chest.")
            sudden_message("Zap!")
            suspensful_message("It doesn't seem to work..")
            sudden_message("\nBLINK!\n")
            message_player("There's a bright flash!")
            sudden_message("You must have triggered the Defense System!")
            crossroads(inventory, realities)
        else:
            message_player("That doesn't seem to work..")


def door(inventory, realities):  # Door option.
    suspensful_message("You knock on the door\nThere's a strange noise...\n")
    sudden_message("A Celestial Being appears, the figure reaches their hand"
                   " over..\n"
                   "To erase your memories!")
    if "Cryobot" in inventory:
        message_player("All of a sudden, the Cryobot turns on and flys above"
                       " you.")
        sudden_message("\nZAP!\n")
        message_player("The Cryobot shoots laser at the Celestial Being "
                       "mercilessly!")
        message_player("It appears that it was a hologram..")
        sudden_message("\nBAM!\n")
        message_player("A Nanobot drops down to the ground.")
        message_player("You notice the Cryobot flys inside through the door.\n"
                       "The Cryobot Sings!\n'La! La! La!'\n"
                       "'I'm here'")
        sudden_message("\nPlack!\n")
        message_player("You look down.. it's a Z-drive!")
        message_player("That might come in handy..")
        inventory.append("Z-drive")
        if "Cryobot" and "Z-drive" in inventory:
            walk_inside(inventory, realities)  # Section call- Continue Game.
    else:
        while not '1' or '2':
            runaway = input("\nEnter 1 to Run away\n"
                            "Enter 2 to Fight the Celestial Being\n")
            if runaway == '1':
                message_player("You sprint like mad! Away from that.. THING!")
                crossroads(inventory, realities)
            elif runaway == '2':
                message_player("Your hand goes through the Celestial Being!")
                message_player("The Celestial Being gently touches your "
                               "forehead...")
                message_player("You feel lightheaded..")
                sudden_message("\nSmack!\n")
                message_player("You fall down to the ground and forget "
                               "everything..")
                message_player("You have been defeated!")
                message_player("\nGAME OVER")
                play_again(inventory, realities)
            else:
                message_player("That's not an option!")


def dark_path(inventory, realities):  # Dark Path Option.
    message_player("You walk along the dark path..")
    message_player("The path.. It's curving towards the right..")
    message_player("You continue along the path, until you look up, all of"
                   " a sudden..")
    message_player("There are thousands of what it seems to be..")
    sudden_message("\nFireflies!\n")
    message_player("The fireflies are lighting up the entire cave!")
    message_player("It appears that you have arrived to an underground lake..")
    message_player("There's a Cryobot near the coastline of the lake.")
    message_player("It's small.. It appears to be turned off.. or broken.")
    while not '1' or '2':
        boting = input("\nEnter '1' to take the Cryobot\n"
                       "Enter '2' to leave it and go back to the crossing.\n")
        if boting == '1':
            message_player("You take the Cryobot and put it in your pocket.")
            inventory.append("Cryobot")
            crossroads(inventory, realities)
        elif boting == '2':
            message_player("You can't see there's anything else here...")
            message_player("You decide to go back to the crossing.")
            crossroads(inventory, realities)
        else:
            message_player("You look up, to the sides.. Nothing..")
            message_player("That might not be an option..")


def play_again(inventory, realities):  # Play the game again.
    try_again = input("Would you like to play again? (yes / no)\n").lower
    if try_again == "yes":
        play_game()
    elif try_again == "no":
        suspensful_message("Thank you for playing, Goodbye!")
        sys.exit()
    else:
        message_player("I didn't get that..")
        play_again(inventory, realities)


def crossroads(inventory, realities):  # Intro Path options.
    message_player("You find yourself in a cave")
    message_player("In front of you are two passages.")
    message_player("You can see a dim light through the left path "
                   "that leads to a door.\n"
                   "The right, leads to a dark path.")
    decision = input("\nEnter '1' to run towards the dim light and "
                     "knock on the door.\n"
                     "Enter '2' to run towards the dark path.\n")
    if decision == '1':
        door(inventory, realities)
    elif decision == '2':
        dark_path(inventory, realities)
    else:
        message_player("Hmm.. It seems there aren't any other options..")
        crossroads(inventory, realities)


def play_game():  # Game Function.
    inventory = []
    realities = random.choice(["Kepler-186f", "Gliese 581g"])
    intro(inventory, realities)
    crossroads(inventory, realities)


play_game()  # Function call to play the game.
