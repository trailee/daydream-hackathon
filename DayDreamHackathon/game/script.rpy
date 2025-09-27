# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rabbi")
define j = Character("Jack")
define d = Character("Dillon")


# The game starts here.

label start:
    default t_points = 0
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
    show character
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
            jump e1p1
        "That’s terrible. There’s got to be something out there they don’t want us to see.":
            jump e2p1

label e1p1:
    j "Didn't take you to be a wuss haha."
    r "Shut up, Jack. They knew what'd happen to them if they tried."
    j "Yikes, okay."
    r "I need some fresh air, let's go outside."
    jump start2


label e2p1:
    j "That's what I've been thinking. If they're going to the extent of knocking their heads off for trying to escape, I don't feel safe living here."
    r "I understand what you mean, but you're not thinking of escaping yourself are you?"
    j "I mean..."
    r "Jack. I'm not against that at all. Actually, I think that's very courageous of you. I'm just worried you'd suffer the same consequences as that group."
    j "Don't worry, Rabbi. If anything, this is just a small thought; I probably wouldn't go through with it."
    r "Okay, good. Though if you're thinking of actually escaping, I'd be glad to help you out."
    j "Thanks, I appreciate that a lot."
    r "Anyway... Enough with the whole government convo, I actually need to go out and run some errands. Want to come with me?"
    j "Of course, I got nothing else to do."
    jump start2

label start2:
    #Change to outside background
    j"testing"