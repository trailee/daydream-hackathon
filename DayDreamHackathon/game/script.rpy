# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rabbi")
define j = Character("Jack")
define d = Character("Dillon")
define dd = Character("DDawg Officer")
define s = Character("Stranger")


# The game starts here.

label start:
    default t_points = 0
    default officer = False
    default stranger_help = False
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
    j "On another note, I saw something on the news today. Some bullshit about the “Mighty Dillon” and his crew."
    r "What about them? Every time they’re mentioned on the news they’re up to no good."
    j "Well, obviously. It makes me astonished knowing people blindly follow AND trust their statements"
    r "Yeah, a bit braindead in my opinion. What’d the news mention about them?"
    j "RIGHT. It makes me furious how they don’t question anything."
    r "Okay, we get it. So what’d they do to warrant being broadcasted by the news? "
    j "There was a group of individuals who attempted to escape the walls. Dhillon ordered his crew to take them out before they could even reach the forest."

    menu:
        "Good. I don’t know why they even thought of trying to escape.":
            jump p1a
        "That’s terrible. There’s got to be something out there they don’t want us to see.":
            jump p1b

label p1a:
    j "Didn't take you to be a wuss haha."
    r "Shut up, Jack. They knew what'd happen to them if they tried."
    j "Yikes, okay."
    r "..."
    r "I need to go run errands. Would you like to come with me?"
    j "I guess I have nothing else to do."
    jump start2


label p1b:
    $ t_points +=1
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
    #add beating up sfx

    "" #walking
    dd "Shut up and stop resisting."
    s "YOU CAN'T DO THIS! I DIDN'T DO ANYTHING WRONG!"
    dd "You're hurting my ears. I better shut you up."

    menu: 
        "Help the stranger":
            #stop sfx
            jump p2a
        "Ignore and keep walking":
            #stop sfx
            jump p2b

label p2a:
    $ t_points +=1
    $ officer = True
    $ stranger_help = True
    s "PLEASE, STOP!"
    r "HEY SHRIMPY, your crustacean ass deaf or something? He said stop."
    dd "Huh? Who do you think you're talking to kid? Do you know what I am? Do you know who I work for?"
    r "WOW, you're annoying. You think we don't see that big dog on your vest?"
    j "Just because you're a DDawg officer doesn't mean you can go around beating everyone up."
    dd "Yes it does. It literally said in my contract that I could beat anyone up without consequences."
    r "You for real?"
    dd "Ya."
    j "Okay, well. Beating people up is no good. I'd say you spend your time finding a chiropractor or something. It looks like you've got a lot of tension in your... trapezius?"
    dd "You people and your big words. You know what, you guys really piss me off. You'll hear about this from the big boss."
    ""
    j "The big boss? You don't think he'll tell Dillon, right?"
    r "That guy has got to be like the pleb of all plebs. No way is his complaint reaching Dillon; we have nothing to worry about."
    j "Yeah, you're right."
    s "Sorry, I don't mean to interupt..."
    s "I just wanted to thank you guys for saving me. I have no doubt he would've killed me if you guys hadn't stepped in."
    s "I don't have anything on me that I could give, but if you need anything, please don't hesitate to call me."
    "Obtained BUSINESS CARD"
    s "Have a nice day!"
    jump ddd


label p2b:
    r "That is genuinely not my problem. I don't want to involve myself in anything that would put me on Dillon's bad side."
    j "I guess. I do feel bad, though... That guy probably didn't even do anything..."
    r "Jack, there's no point in feeling bad. We don't even know the guy, he might've done something to tick the officer off."
    j "..."
    jump start3


label ddd:
    ""
    "DDAWG HEADQUARTERS"
    dd "Boss... T-they.."
    d "What's wrong, number 1078? Use your words."
    dd "They made a fool out of me!!"
    dd "Called me shrimpy... told me my trapezoids looked tense!"
    dd "I'm gonna kill them... I swear... The next time to see them..."
    d "Now now, we must not be rash. Tell me, who were these people? How did they look?"
    dd "Ugly ones... Both the same height. I think one had _________"
    d "Okay. I will take note of this, do not worry. They will be dealt with."
    dd "Thank you big boss!! I owe you my life and honor."
    dd "Tomorrow, I will bring you a tasty pie."
    d "Okay, 1078."
    jump start3

label start3:
    j 