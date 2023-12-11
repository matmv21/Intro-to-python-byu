print('ALL_CAPS words are the options for each scenario:\nEach scenario contains at least 2 options to decide. Pick and type in your answer.')

chosen = input("\n\nYou awake, you're sitting on a chair in the front porch of a house, it's cold, the sun is rising on the horizon. You get up, face the sun and look around expecting to see somebody, suddenly, you hear a noise inside the house. Do you CHECK the noise, or STAY aoutside the house?\n\nR: ")

# If statements
# CHECK
if chosen.lower() == 'check':

    chosen = input("\n\nYou open the door, enter the living room and everything in the room is spread out on the floor. The noise continues in the kitchen. You see on the table a baseball bat. Do you TAKE the baseball bat, WALK towards the kitchen or LEAVE the house?\n\nR: ")

    #TAKE
    if chosen.lower() == 'take':
        chosen = input("\n\nYou take the bat and walk towards the kitchen, as you get closer the noise gets louder. You start smelling gas coming from the kitchen. Do you RUN from the house or CHECK the kitchen?\n\nR: ")

        if chosen.lower() == 'run':
            print("\n\nYou run out of the house and BOOOOMMMM, the kichen exploded. Sadly the explosion affected houses from the neighborhood. THE END.\n\n")
        elif chosen.lower() == 'check':
            print("\n\nYou enter the kicthen, sees a kid about to light a match, you rushes yourself and stops the kid. Congrats, you stopped a tragedy. THE END.\n\n")
        else:
            print("\n\n* This option isn't available! Start again. *\n\n")

    # WALK
    elif chosen.lower() == 'walk':
        chosen = input("\n\nYou walk fearless towards the kitchen and start smelling gas. Do you RUN from the house or CHECK the kitchen?\n\nR: ")

        if chosen.lower() == 'run':
            print("\n\nYou run out of the house and BOOOOMMMM, the kichen exploded. Sadly the explosion affected houses from the neighborhood. THE END.\n\n")
        elif chosen.lower() == 'check':
            print("\n\nYou enter the kicthen, sees a kid about to light a match, you rush yourself and stops the kid. Congrats, you stopped a tragedy. THE END.\n\n")
        else:
            print("\n\n* This option isn't available! Start again. *\n\n")
    
    # LEAVE
    elif chosen.lower() == 'leave':
        chosen = input('\n\nYou leave the house and moments later BOOOM, the kitchen explodes.\n\n')
    else:
        print("\n\n* This option isn't available! Start again. *\n\n")

# STAYS
elif chosen.lower() == 'stay':

    chosen = input("\n\nAfter a few minutes you hear the noise again. Do you CHECK or STAY?\n\nR: ")

    if chosen.lower() == 'check':
        chosen = input("\n\nYou enter the kitchen, sees a kid about to light a match, you rushes yourself and stops the kid. Congrats, you stopped a tragedy. THE END.\n\n")
    elif chosen.lower() == 'stays':
        chosen = input("\n\nBOOOOMMMM, the kichen exploded. Sadly the explosion affected houses from the neighborhood. THE END.\n\n")
    else:
        print("This option isn't available! Start again.")
else:
    print("This option isn't available! Start again.")