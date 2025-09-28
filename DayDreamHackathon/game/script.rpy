# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rabbi", color="#e5f011")
define j = Character("Jack")
define d = Character("Dillon", color="#854d2a")
define dd = Character("DDawg Officer", color="#485096")
define s = Character("Stranger", color="#ffffff")
define n = Character("Nick", color="#308f1d")
define u = Character("???", color="#8f2727")

#BACKGROUNDS
image home = "dining"
image outside = "alley"
image nd1 = "transition 1"
image doffice = "office"
image building = "front"
image warehouse = "warehouse_floor"
image around_warehouse1 = "warehouse_break"
image around_warehouse2 = "warehouse_control"
image bk = "black"

#ENDINGS
image gossip_g = "good_gossip"
image gossip_b = "bad_gossip"

#SPRITES
image j_n = "j_norm"
image j_s = "j_srs"
image j_h = "j_happy"
image s_gf = "s_grateful"
image s_n = "s_norm"
image dd_n = "dd_norm"
image dd_m = "dd_mad"

image person = "character.jpg"

# The game starts here.

label start:
    default t_points = 0
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
    scene home with fade
    r "I’m so {i}tired{/i} today…"
    show j_s
    j "When are you not tired? You should lay back a bit before you work yourself to death."
    r "Listen, I’m doing this to keep my sanity. Trust me, {w=.5}I’m fine."
    show j_s
    j "Whatever."
    hide j_s
    show j_norm
    j "On another note, I saw something on the news today.{w=.5} Some bullshit about the “Mighty Dillon” and his crew."
    r "What about them? Every time they’re mentioned on the news they’re up to no good."
    hide j_norm
    show j_s
    j "Well, obviously. It makes me astonished knowing people blindly follow {i}AND{/i} trust their statements"
    r "Yeah, a bit braindead in my opinion. What’d the news mention about them?"
    j "RIGHT. It makes me furious how they don’t question anything."
    r "{cps=15}Okay, we get it. {/cps}{w=.75}So what’d they do to warrant being broadcasted by the news? "
    hide j_s
    show j_norm
    j "There were a group of individuals who attempted to escape the walls. Dillon ordered his crew to take them out before they could even reach the forest."

    menu:
        "Good. I don’t know why they even thought of trying to escape.":
            jump p1a
        "That’s terrible. There’s got to be something out there they don’t want us to see.":
            jump p1b

label p1a:
    j "Didn't take you to be a wuss, haha."
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
    scene outside with fade
    #add beating up sfx

    "{size=40}{b}{color=#589c51}OUTSIDE{/b}{/color}" #walking
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
    s "{i}{size=40}PLEASE, STOP!{/i}" with vpunch
    r "HEY SHRIMPY, your crustacean ass deaf or something? He said stop."
    dd "Huh? Who do you think you're talking to kid? Do you know what I am? Do you know who I work for?"
    r "{size=40}WOW{size=33}, you're annoying. You think we don't see that big dog on your vest?"
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
    s "I don't have anything on me that I could give you, but if you need anything, please don't hesitate to call me."
    "{size=40}{i}Obtained BUSINESS CARD{/i}"
    s "Have a nice day!"
    jump ddd


label p2b:
    r "That is genuinely not my problem. I don't want to involve myself in anything that would put me on Dillon's bad side."
    j "I guess. I do feel bad, though... That guy probably didn't even do anything..."
    r "Jack, there's no point in feeling bad. We don't even know the guy, he might've done something to tick the officer off."
    j "..."
    jump start3


label ddd:
    scene doffice with fade
    "{size=40}{b}{color=#589c51}DDAWG HEADQUARTERS{/b}{/color}"
    dd "Boss... T-they.."
    d "What's wrong, number 1078? Use your words."
    dd "THEY MADE A FOOL OUT OF ME!!" with vpunch
    dd "Called me shrimpy... told me my trapezoids looked tense!"
    dd "I'm gonna kill them... I swear... The next time to see them..."
    d "Now now, we must not be rash. Tell me, who were these people? How did they look?"
    dd "Ugly ones... Both the same height."
    dd "I think one had purple eyes, a poo-coloured mullet, and like... purple... Just purple."
    dd "The one that needs to die is green. I think he has brown hair too, but it was tied up."
    dd "Big boss, you can just unfocus your eyes and look for something that resembles barney!"
    d "Okay. I will take note of this, do not worry. They will be dealt with."
    dd "Thank you big boss!! I owe you my life and honor."
    dd "Tomorrow, I will bring you a tasty pie."
    d "Okay, 1078."
    jump start3

label start3:
    scene nd1 with fade
    ""
    scene home with fade
    r "Thanks for helping me out with my errands yesterday, Jack"
    j "Yeah, of course."
    ##serious sprite
    j "..."
    j "Something's been on my mind since yesterday."
    r "What is it? Is it related to DDawgs?"
    j "Well, sort of..."
    j "I was thinking about that stranger who was getting beat up by the DDawg officer."
    if stranger_help == True:
        $ t_points += 1
        r "Yeah, same. I'm glad we were there to help them."
        j "I agree."
        j "Hey, what you did yesterday was admirable! I know a lot of people who would've just walked away and ignored him."
        j "I'm glad we're friends, Rabbi!"
        r "Ditto. I'm pretty sure that officer only backed down because there were two of us, haha."
    else: 
        r "Jack, we can't keep dwelling on the past."
        r "I understand it was hard to walk away from that situation. But in the end, what matters is our own safety."
        r "You can't keep looking out for others."
        j "..."
        j "Rabbi... I don't agree with that."
        j "We could've stopped that! Even if that man did something, I'm sure he wasn't deserving of a beating!"
        j "This isn't right, I can't believe how cold you've become."
    "{b}{i}{size=50}Crash{/b}{/i}"
    "{cps=5}...{/cps}{w=1}{size=50}{i}{b}AHHHHHHHHHHHHHHHHHHHHHHHH!{/i}{/b}"
    j "What in the-"
    r "What happened outside?"
    j "Let's go check."
    
    scene building with fade
    "{size=40}{b}{color=#589c51}OUTSIDE{/b}{/color}"
    j "I saw someone run towards that building."
    r "Are you sure we should check it out?"
    r "I'm pretty sure screaming means something BAD happened."
    j "Come on, a little curiosity never hurt."
    r "You know damn well it killed the cat."
    j "Pish posh, I'm going."
    r "Okay..."

    scene warehouse with fade
    "{size=40}{b}{color=#589c51}WAREHOUSE{/b}{/color}"
    
    if stranger_help == True:
        u "You two!"
        j "Wha-"
        s "What a coincidence!"
        r "Oh, it's you!!"
    else:
        u "..."
    r "Are you okay? We heard a loud crash and something screaming."
    s "Oh, yeah. I think someone put a hit out on me or something."
    j "{size=50}???"
    j "How are you so calm about that?"
    s "Come on, I literally dealt with that DDawg Officer yesterday."
    if stranger_help == True:
        j "Oh yeah, he was a pain. Glad we got him to stop though."
        s "Yeah, huge thanks to you guys!"
        s "I've been watching those Ip Man movies. Makes me super motivated to beat some punks up!"
        r "That's nice, glad you're not traumatized, haha."
    else:
        j "Sorry we didn't help you yesterday... That DDawg Officer was really intimidating."
        j "If you need any help now, though, we'd be glad to help!"
        r "I guess, yeah."
    s "Haha, I'm good."
    s "Some wall got smashed in, pretty sure they thought I was behind it."
    j "Holy smokes, dude! That's insane, they tried to kill you!"
    s "Well, I guess the fact I survived after yesterday hurt their egos."
    r "Dillon and his crew are terrifying..."

    menu:
        "Inquire more":
            jump p3a
        "Walk around the building":
            jump p3b
        "Leave building":
            jump p3c

label p3a:
    $ t_points +=1
    r "So what happened after we left?"
    if stranger_help == True:
        r "Did he come back or anything?"
        s "Nah, I left right after that. I think I got followed home, though."
        j "{size=50}{i}WHAT???{/i}" with vpunch
        r "What was your name again?"
        s "Oh, I forgot to introduce myself, haha!"
        n "My name is Nick, I work here at the warehouse. Basically move a bunch of boxes around."
        j "Nice to meet you, Nick!"
        j "My name is Jack."
        r "And my name is Rabbi, nice to meet you."
        s "Great! Now I know the names of my saviors!"
        r "I don't even know if we're saviors or not since they're trying to assassinate you now."
        s "Oh, don't worry about that! It's definitely not your fault."
    else:
        s "Well, he did keep beating me up and stuff."
        j "Again, sorry about that..."
        s "No, don't worry about that!"
        j "We forgot to introduce ourselves, by the way."
        j "My name is Jack."
        r "My name is Rabbi..."
        s "Anyway, he ran out of breath or something. I think I heard something crack. {w=.5}So he kind of just stopped and walked away."
        j "... {w=1} Well I'm glad he stopped. That could have ended badly."
        s "Yeah, probably."


label p3b:
    $ t_points += 1
    r "Okay, well it was nice seeing you again."
    r "I'd like to take a look around the building."
    j "Yeah, that might be beneficial. We'll see you another day, Nick. Stay safe!"
    n "You guys as well. Have a good one!"
    scene around_warehouse1 with fade
    "{size=40}{b}{color=#589c51}BREAKROOM{/b}{/color}"
    r "See anything around here?"
    j "Nah, just some snacks. {w=.5}Want some?"
    r "No, thank you."
    j "I feel like a little detective running around the building."
    r "I guess that's what we're kind of doing, haha."
    scene around_warehouse2 with fade
    "{size=40}{b}{color=#589c51}CONTROL ROOM{/b}{/color}"
    u "..."
    j "Oops, didn't think there were people still in here."
    if stranger_help ==  True:
        u "Purple and green... Like barney..?"
        r "What is this person talking abou-{w=.3}{nw}"
        j "OH MY-{nw}{w=.3}"
        r "DILL-{nw}{w=.3}"
        d "So you two were the ones who were causing trouble yesterday."
        j "Are you kidding me? That krill actually complained about us."
    else:
        "{size=40}{b}...{/b}"
        r "Well, I guess they're gone now."


label p3c:
    r "Okay, well, it was nice seeing you again. However we have things to attend to, so we have to go now."
    s "Awe, what a shame! I wanted to tell you guys about yesterday."
    j "Hey, we have s-{w=.3}{nw}"
    r "No, sorry we have to go now."
    scene front
    "{size=40}{b}{color=#589c51}OUTSIDE{/b}{/color}"    
    if stranger_help == True:
        j "So what do we have to do today?"
        r "Well, we're not super busy today but I was thinking of going to get some groceries."
        j "Oh, we could have talked to that guy for a bit longer then if we weren't in a rush..."
        r "It's okay, I didn't want to get home too late either."
        scene outside with fade
        "{size=40}{b}After purchasing groceries.{/b}"
        dd "{size=40}{b}Freakin' pests ALL {w=.5}AROUND {w=.5}ME!{/b}"
        dd "{size=40}{b}YOU ALL NEED TO DIE!!{/b}"
        j "Why did we go back this way..."
        r "I forgot about him..."
        dd "{size=50}{b}{cps=25}YOU BARNEYS!!{/b}" with vpunch
        r "I think we should run."
        j "Yeah, definitely."
        dd "{size=50}{b}{cps=25}I'LL KILL YOU BOTH, I SWEAR!!{/b}" with vpunch
    else:
        j "I know you did that because you're scared of being associated with him. But it wouldn't have been a huge deal if we just had a conversation with him."
        r "I don't care, Jack. Talking to him would have been a waste of our time."
        menu:
            "You notice the same DDawg Officer from yesterday talking on the phone."
            "Listen in.":
                dd "...{w=.3}Yeah, what a guy!"
                dd "I know, and then guess what! That kid took out a knife and tried swinging at me."
                dd "Yeah, but I put him in a chokehold and left him on the street."
                dd "I mean, yeah, I could have done worse... but come, on he's just a kid."
                dd "Yeah, yeah, haha... Anyway I better head off soon, got to continue working."
                r "...{w=.3} Interesting..."
                if stranger_help == True and t_points >=1:
                    menu:
                        "Call number on BUSINESS CARD.":
                            jump gossip
                        "Leave it be, you don't gossip.":
                            j "Let's not involve ourselves in that..."
                else:
                    menu:
                        "Call number on BUSINESS CARD.":
                            "{size=40}{b}{color=#589c51}ring ring ring...{/b}{/color}"
                            n "{i}bzt...{/i} Hey, this is Nick speaking."  
                            r "Hey, Nick. People who saved you here!"
                            j "You wanna know the chisme, Nick??"
                            n "Oh yeah, I'm all for that."
                            r "The officer from yester-{w=.3}{nw}" with fade
                            j "The one that wears green... Their name is Rabbi. They hired the DDawg officer to beat "
                        "Leave it be, you don't gossip.":
                            j "Let's not involve ourselves in that..."

            "Walk away.":
                j "You tryna head home now?"
                r "Yeah, I'm getting a bit tired."
                if t_points >=1:
                    "{size=50}{b}WHACK{/b}" with vpunch
                    scene black
                    "{size=50}{b}TEXT......{/b}"
                else:
                    "{size=50}{b}WHACK{/b}" with vpunch
                    j "Sorry, Rabbi... I just don't think this will work out."
                    "{size=40}{i}Your decisions throughout this game led to Jack {b}not trusting you{/b}.{/i}"
                    "{size=40}{i}He believes taking you out is a sacrifice worth taking to keep his freedom and sanity.{/i}"
                    "{size=40}{i}Maybe next time you can make better decisions to turn the tables.{/i}"

                

label gossip:
    "{size=40}{b}{color=#589c51}ring ring ring...{/b}{/color}"
    n "{i}bzt...{/i} Hey, this is Nick speaking."  
    r "Hey, Nick. People who saved you here!"
    j "You wanna know the chisme, Nick??"
    n "Oh yeah, I'm all for that."
    j "Mister DDawg is over here. Talking mad diss about you."
    r "Yeah I think you should do something about that."
    n "Yeahhhhh ehhhh no chance fam this goober done mod tingz eh"
    j "*starts frat flicking*"
    scene gossip_b with fade
label no_gossip:
    j "So we're just avoiding everything at this point."
    r ""