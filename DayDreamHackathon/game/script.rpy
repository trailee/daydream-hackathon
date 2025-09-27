# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rabbi")
define j = Character("Jack")
define d = Character("Dillon")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    ##scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    ##show eileen happy

    # These display lines of dialogue.

    # BEGINNING SCENE
    r "I’m so tired today…"
    j "When are you not tired? You should lay back a bit before you work yourself to death."
    r "Listen, I’m doing this to keep my sanity. Trust me, I’m fine."
    j "Whatever."
    j "On another note, I saw something on the news today. Some bs about the “Mighty Dillon” and his crew."
    r "What about them? Every time they’re mentioned on the news they’re up to no good."
    j "Well, obviously. It makes me astonished knowing people blindly follow AND trust their statements"
    r "Yeah, a bit braindead in my opinion. What’d the news mention about them?"
    j "RIGHT. It makes me furious how they don’t question anything."
    r "Okay, we get it. So what’d they do to warrant being broadcasted by the news? "
    j "There was a group of individuals who attempted to escape the walls. Dhillon ordered his crew to take them out before they could even reach the forest."

    menu:
        "Good. I don’t know why they even thought of trying to escape.":
            j"okay"
        "That’s terrible. There’s got to be something out there they don’t want us to see.":
            j"what"

        
    return
