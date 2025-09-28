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
image rabbi = "rabbii"
image dillon = "dillonn"

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
    play music "audio/background_music.mp3"
    scene home with fade
    show rabbi
    r "I’m so {i}tired{/i} today…"
    hide rabbi
    show j_s
    j "When are you not tired? You should lay back a bit before you work yourself to death."
    hide j_s
    show rabbi
    r "Listen, I’m doing this to keep my sanity. Trust me, {w=.5}I’m fine."
    hide rabbi
    show j_s
    j "Whatever."
    hide j_s
    show j_norm
    j "On another note, I saw something on the news today.{w=.5} Some bullshit about the “Mighty Dillon” and his crew."
    hide j_norm
    show rabbi
    r "What about them? Every time they’re mentioned on the news they’re up to no good."
    hide rabbi
    show j_s
    j "Well, obviously. It makes me astonished knowing people blindly follow {i}AND{/i} trust their statements"
    hide j_s
    show rabbi
    r "Yeah, a bit braindead in my opinion. What’d the news mention about them?"
    hide rabbi
    show j_s
    j "RIGHT. It makes me furious how they don’t question anything."
    hide j_s
    show rabbi
    r "{cps=15}Okay, we get it. {/cps}{w=.75}So what’d they do to warrant being broadcasted by the news? "
    hide j_s
    show j_norm
    j "There were a group of individuals who attempted to escape the walls. Dillon ordered his crew to take them out before they could even reach the forest."
    hide j_norm
    menu:
        "Good. I don’t know why they even thought of trying to escape.":
            jump p1a
        "That’s terrible. There’s got to be something out there they don’t want us to see.":
            jump p1b

label p1a:
    show j_h
    j "Didn't take you to be a wuss, haha."
    hide j_h
    show rabbi
    r "Shut up, Jack. They knew what'd happen to them if they tried."
    hide rabbi
    show j_s
    j "Yikes, okay."
    hide j_s
    show rabbi
    r "..."
    r "I need to go run errands. Would you like to come with me?"
    hide rabbi
    show j_norm
    j "I guess I have nothing else to do."
    hide j_norm
    jump start2


label p1b:
    $ t_points +=1
    show j_s
    j "That's what I've been thinking. If they're going to the extent of knocking their heads off for trying to escape, I don't feel safe living here."
    hide j_s
    show rabbi
    r "I understand what you mean, but you're not thinking of escaping yourself are you?"
    hide rabbi
    show j_norm
    j "I mean..."
    hide j_norm
    show rabbi
    r "Jack. I'm not against that at all. Actually, I think that's very courageous of you. I'm just worried you'd suffer the same consequences as that group."
    hide rabbi
    show j_h
    j "Don't worry, Rabbi. If anything, this is just a small thought; I probably wouldn't go through with it."
    hide j_h
    show rabbi
    r "Okay, good. Though if you're thinking of actually escaping, I'd be glad to help you out."
    hide rabbi
    show j_h
    j "Thanks, I appreciate that a lot."
    hide j_h
    show rabbi
    r "Anyway... Enough with the whole government convo, I actually need to go out and run some errands. Want to come with me?"
    hide rabbi
    show j_h
    j "Of course, I got nothing else to do."
    hide j_h
    jump start2

label start2:
    #Change to outside background
    scene outside with fade
    #add beating up sfx

    "{size=40}{b}{color=#589c51}OUTSIDE{/b}{/color}" #walking
    show dd_m
    dd "Shut up and stop resisting."
    hide dd_m
    show s_n
    s "YOU CAN'T DO THIS! I DIDN'T DO ANYTHING WRONG!"
    hide s_n
    show dd_n
    dd "You're hurting my ears. I better shut you up."
    hide dd_n
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
    show s_n
    s "{i}{size=40}PLEASE, STOP!{/i}" with vpunch
    hide s_n
    show rabbi
    r "HEY SHRIMPY, your crustacean ass deaf or something? He said stop."
    hide rabbi
    show dd_n
    dd "Huh? Who do you think you're talking to kid? Do you know what I am? Do you know who I work for?"
    hide dd_n
    show rabbi
    r "{size=40}WOW{size=33}, you're annoying. You think we don't see that big dog on your vest?"
    hide rabbi
    show j_s
    j "Just because you're a DDawg officer doesn't mean you can go around beating everyone up."
    hide j_s
    show dd_n
    dd "Yes it does. It literally said in my contract that I could beat anyone up without consequences."
    hide dd_n
    show rabbi
    r "You for real?"
    hide rabbi
    show dd_n
    dd "Ya."
    hide dd_n
    show j_n
    j "Okay, well. Beating people up is no good. I'd say you spend your time finding a chiropractor or something. It looks like you've got a lot of tension in your... trapezius?"
    hide h_n
    show dd_m
    dd "You people and your big words. You know what, you guys really piss me off. You'll hear about this from the big boss."
    hide dd_m
    ""
    show j_n
    j "The big boss? You don't think he'll tell Dillon, right?"
    hide j_n
    show rabbi
    r "That guy has got to be like the pleb of all plebs. No way is his complaint reaching Dillon; we have nothing to worry about."
    hide rabbi 
    show j_n
    j "Yeah, you're right."
    hide j_n
    show s_n
    s "Sorry, I don't mean to interupt..."
    hide s_n
    show s_gf
    s "I just wanted to thank you guys for saving me. I have no doubt he would've killed me if you guys hadn't stepped in."
    s "I don't have anything on me that I could give you, but if you need anything, please don't hesitate to call me."
    "{size=40}{i}Obtained BUSINESS CARD{/i}"
    s "Have a nice day!"
    hide s_gf
    jump ddd


label p2b:
    show rabbi
    r "That is genuinely not my problem. I don't want to involve myself in anything that would put me on Dillon's bad side."
    hide rabbi
    show j_s
    j "I guess. I do feel bad, though... That guy probably didn't even do anything..."
    hide j_s
    show rabbi
    r "Jack, there's no point in feeling bad. We don't even know the guy, he might've done something to tick the officer off."
    hide rabbi
    show j_s
    j "..."
    hide j_s
    jump start3


label ddd:
    scene doffice with fade
    "{size=40}{b}{color=#589c51}DDAWG HEADQUARTERS{/b}{/color}"
    show dd_n
    dd "Boss... T-they.."
    hide dd_n
    show dillon
    d "What's wrong, number 1078? Use your words."
    hide dillon
    show dd_m
    dd "THEY MADE A FOOL OUT OF ME!!" with vpunch
    dd "Called me shrimpy... told me my trapezoids looked tense!"
    dd "I'm gonna kill them... I swear... The next time to see them..."
    hide dd_m
    show dillon
    d "Now now, we must not be rash. Tell me, who were these people? How did they look?"
    hide dillon
    show dd_n
    dd "Ugly ones... Both the same height."
    dd "I think one had purple eyes, a poo-coloured mullet, and like... purple... Just purple."
    dd "The one that needs to die is green. I think he has brown hair too, but it was tied up."
    dd "Big boss, you can just unfocus your eyes and look for something that resembles barney!"
    hide dd_n
    show dillon
    d "Okay. I will take note of this, do not worry. They will be dealt with."
    hide dillon
    show dd_n
    dd "Thank you big boss!! I owe you my life and honor."
    dd "Tomorrow, I will bring you a tasty pie."
    hide dd_n
    show dillon
    d "Okay, 1078."
    hide dillon
    jump start3

label start3:
    scene nd1 with fade
    ""
    scene home with fade
    show rabbi
    r "Thanks for helping me out with my errands yesterday, Jack"
    hide rabbi
    show j_h
    j "Yeah, of course."
    hide j_h
    show j_s
    j "..."
    j "Something's been on my mind since yesterday."
    hide j_s
    show rabbi
    r "What is it? Is it related to DDawgs?"
    hide rabbi
    show j_s
    j "Well, sort of..."
    j "I was thinking about that stranger who was getting beat up by the DDawg officer."
    hide j_s
    if stranger_help == True:
        $ t_points += 1
        show rabbi
        r "Yeah, same. I'm glad we were there to help them."
        hide rabbi
        show j_n
        j "I agree."
        hide j_n
        show j_h
        j "Hey, what you did yesterday was admirable! I know a lot of people who would've just walked away and ignored him."
        j "I'm glad we're friends, Rabbi!"
        hide j_h
        show rabbi
        r "Ditto. I'm pretty sure that officer only backed down because there were two of us, haha."
        hide rabbi
    else: 
        show rabbi
        r "Jack, we can't keep dwelling on the past."
        r "I understand it was hard to walk away from that situation. But in the end, what matters is our own safety."
        r "You can't keep looking out for others."
        hide rabbi
        show j_s
        j "..."
        j "Rabbi... I don't agree with that."
        j "We could've stopped that! Even if that man did something, I'm sure he wasn't deserving of a beating!"
        j "This isn't right, I can't believe how cold you've become."
        hide j_s
    "{b}{i}{size=50}Crash{/b}{/i}"
    "{cps=5}...{/cps}{w=1}{size=50}{i}{b}AHHHHHHHHHHHHHHHHHHHHHHHH!{/i}{/b}"
    show j_s
    j "What in the-"
    hide j_s
    show rabbi
    r "What happened outside?"
    hide rabbi
    show j_s
    j "Let's go check."
    hide j_s
    scene building with fade
    "{size=40}{b}{color=#589c51}OUTSIDE{/b}{/color}"
    show j_s
    j "I saw someone run towards that building."
    hide j_s
    show rabbi
    r "Are you sure we should check it out?"
    r "I'm pretty sure screaming means something BAD happened."
    hide rabbi
    show j_h
    j "Come on, a little curiosity never hurt."
    hide j_h
    show rabbi
    r "You know damn well it killed the cat."
    hide rabbi
    show j_h
    j "Pish posh, I'm going."
    hide j_h
    show rabbi
    r "Okay..."
    hide rabbi
    scene warehouse with fade
    "{size=40}{b}{color=#589c51}WAREHOUSE{/b}{/color}"
    
    if stranger_help == True:
        u "You two!"
        show j_n
        j "Wha-"
        hide j_s
        show s_gf
        s "What a coincidence!"
        show s_gf
        show rabbi
        r "Oh, it's you!!"
        hide rabbi
    else:
        u "..."
    show rabbi
    r "Are you okay? We heard a loud crash and something screaming."
    hide rabbi
    show s_n
    s "Oh, yeah. I think someone put a hit out on me or something."
    hide s_n
    show j_s
    j "{size=50}???"
    j "How are you so calm about that?"
    hide j_s
    show s_n
    s "Come on, I literally dealt with that DDawg Officer yesterday."
    hide s_n
    if stranger_help == True:
        show j_h
        j "Oh yeah, he was a pain. Glad we got him to stop though."
        hide j_h
        show s_gf
        s "Yeah, huge thanks to you guys!"
        s "I've been watching those Ip Man movies. Makes me super motivated to beat some punks up!"
        hide s_gf
        show rabbi
        r "That's nice, glad you're not traumatized, haha."
        hide rabbi
    else:
        show j_s
        j "Sorry we didn't help you yesterday... That DDawg Officer was really intimidating."
        hide j_s
        show j_n
        j "If you need any help now, though, we'd be glad to help!"
        hide j_s
        show rabbi
        r "I guess, yeah."
        hide rabbi
    show s_n
    s "Haha, I'm good."
    hide s_n
    show s_gf
    s "Some wall got smashed in, pretty sure they thought I was behind it."
    hide s_gf
    show j_s
    j "Holy smokes, dude! That's insane, they tried to kill you!"
    hide j_s
    show s_n
    s "Well, I guess the fact I survived after yesterday hurt their egos."
    hide s_n
    show rabbi
    r "Dillon and his crew are terrifying..."
    hide rabbi

    menu:
        "Inquire more":
            jump p3a
        "Walk around the building":
            jump p3b
        "Leave building":
            jump p3c

label p3a:
    $ t_points +=1
    show rabbi
    r "So what happened after we left?"
    hide rabbi
    if stranger_help == True:
        show rabbi
        r "Did he come back or anything?"
        hide rabbi
        show s_n
        s "Nah, I left right after that. I think I got followed home, though."
        hide s_n
        show j_s
        j "{size=50}{i}WHAT???{/i}" with vpunch
        hide j_s
        show rabbi
        r "What was your name again?"
        hide rabbi
        show s_n
        s "Oh, I forgot to introduce myself, haha!"
        hide s_n
        show s_gf
        n "My name is Nick, I work here at the warehouse. Basically move a bunch of boxes around."
        hide s_gf
        show j_h
        j "Nice to meet you, Nick!"
        j "My name is Jack."
        hide j_h
        show rabbi
        r "And my name is Rabbi, nice to meet you."
        hide rabbi
        show s_gf
        s "Great! Now I know the names of my saviors!"
        hide s_gf
        show rabbi
        r "I don't even know if we're saviors or not since they're trying to assassinate you now."
        hide rabbi
        show s_n
        s "Oh, don't worry about that! It's definitely not your fault."
        hide s_n
    else:
        show s_n
        s "Well, he did keep beating me up and stuff."
        hide s_n
        show j_s
        j "Again, sorry about that..."
        hide j_s
        show s_n
        s "No, don't worry about that!"
        hide s_n
        show j_n
        j "We forgot to introduce ourselves, by the way."
        j "My name is Jack."
        hide j_n
        show rabbi
        r "My name is Rabbi..."
        hide rabbi
        show s_n
        s "Anyway, he ran out of breath or something. I think I heard something crack. {w=.5}So he kind of just stopped and walked away."
        hide s_n
        show j_s
        j "... {w=1} Well I'm glad he stopped. That could have ended badly."
        hide j_s
        show s_n
        s "Yeah, probably."
        hide s_n

label p3b:
    $ t_points += 1
    show rabbi
    r "Okay, well it was nice seeing you again."
    r "I'd like to take a look around the building."

    hide rabbi
    j "Yeah, that might be beneficial. We'll see you another day, Nick. Stay safe!"
    n "You guys as well. Have a good one!"
    scene around_warehouse1 with fade
    "{size=40}{b}{color=#589c51}BREAKROOM{/b}{/color}"
    
    show rabbi
    r "See anything around here?"
    hide rabbi

    j "Nah, just some snacks. {w=.5}Want some?"
    
    show rabbi
    r "No, thank you."
    hide rabbi

    j "I feel like a little detective running around the building."
    
    show rabbi
    r "I guess that's what we're kind of doing, haha."
    hide rabbi

    scene around_warehouse2 with fade
    "{size=40}{b}{color=#589c51}CONTROL ROOM{/b}{/color}"
    u "..."
    j "Oops, didn't think there were people still in here."
    if stranger_help ==  True:
        u "Purple and green... Like barney..?"
        
        show rabbi
        r "What is this person talking abou-{w=.3}{nw}"
        hide rabbi

        j "OH MY-{nw}{w=.3}"
        
        show rabbi
        r "DILL-{nw}{w=.3}"
        hide rabbi

        d "So you two were the ones who were causing trouble yesterday."
        j "Are you kidding me? That krill actually complained about us."
        
    else:
        "{size=40}{b}...{/b}"
        show rabbi
        r "Well, I guess they're gone now."
        hide rabbi


label p3c:
    show rabbi
    r "Okay, well, it was nice seeing you again. However we have things to attend to, so we have to go now."
    hide rabbi

    s "Awe, what a shame! I wanted to tell you guys about yesterday."
    j "Hey, we have s-{w=.3}{nw}"
    
    show rabbi
    r "No, sorry we have to go now."
    scene front
    "{size=40}{b}{color=#589c51}OUTSIDE{/b}{/color}"    
    if stranger_help == True:
        j "So what do we have to do today?"
        
        show rabbi
        r "Well, we're not super busy today but I was thinking of going to get some groceries."
        hide rabbi

        j "Oh, we could have talked to that guy for a bit longer then if we weren't in a rush..."
        
        show rabbi
        r "It's okay, I didn't want to get home too late either."
        hide rabbi

        scene outside with fade
        "{size=40}{b}After purchasing groceries.{/b}"
        dd "{size=40}{b}Freakin' pests ALL {w=.5}AROUND {w=.5}ME!{/b}"
        dd "{size=40}{b}YOU ALL NEED TO DIE!!{/b}"
        j "Why did we go back this way..."
        
        show rabbi
        r "I forgot about him..."
        hide rabbi

        dd "{size=50}{b}{cps=25}YOU BARNEYS!!{/b}" with vpunch
        
        show rabbi
        r "I think we should run."
        hide rabbi

        j "Yeah, definitely."
        dd "{size=50}{b}{cps=25}I'LL KILL YOU BOTH, I SWEAR!!{/b}" with vpunch
    else:
        j "I know you did that because you're scared of being associated with him. But it wouldn't have been a huge deal if we just had a conversation with him."
        
        show rabbi
        r "I don't care, Jack. Talking to him would have been a waste of our time."
        hide rabbi

        menu:
            "You notice the same DDawg Officer from yesterday talking on the phone."
            "Listen in.":
                dd "...{w=.3}Yeah, what a guy!"
                dd "I know, and then guess what! That kid took out a knife and tried swinging at me."
                dd "Yeah, but I put him in a chokehold and left him on the street."
                dd "I mean, yeah, I could have done worse... but come, on he's just a kid."
                dd "Yeah, yeah, haha... Anyway I better head off soon, got to continue working."
                
                show rabbi
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
                            
                            show rabbi
                            r "Hey, Nick. People who saved you here!"
                            hide rabbi

                            j "You wanna know the chisme, Nick??"
                            n "Oh yeah, I'm all for that."
                            
                            show rabbi
                            r "The officer from yester-{w=.3}{nw}" with fade
                            hide rabbi

                            j "The one that wears green... Their name is Rabbi. They hired the DDawg officer to beat you up."
                            
                            show rabbi
                            r "Jack, what are you sayi-{w=.3}"
                            hide rabbi

                            j "They're outside right now. I packed them up for you."
                            jump jack
                        "Leave it be, you don't gossip.":
                            j "Let's not involve ourselves in that..."

            "Walk away.":
                j "You tryna head home now?"
                
                show rabbi
                r "Yeah, I'm getting a bit tired."
                hide rabbi
                if t_points >=1:
                    "{size=50}{b}WHACK{/b}" with vpunch
                    scene black
                    jump jack
                else:
                    jump rabbi

                

label gossip:
    "{size=40}{b}{color=#589c51}ring ring ring...{/b}{/color}"
    n "{i}bzt...{/i} Hey, this is Nick speaking."  
    
    show rabbi
    r "Hey, Nick. People who saved you here!"
    hide rabbi

    j "You wanna know the chisme, Nick??"
    n "Oh yeah, I'm all for that."
    j "Mister DDawg is over here. Talking mad diss about you."
    
    show rabbi
    r "Yeah I think you should do something about that."
    hide rabbi

    n "Yeahhhhh ehhhh no chance fam this goober done mod tingz eh"
    j "*starts frat flicking*"
    scene gossip_g with fade

label jack:
    show rabbi
    r "Glad we got this idiot out of the way."
    hide rabbi
    "{size=40}{i}Your decisions throughout this game led to Jack {b}trusting you{/b}.{/i}"
    "{size=40}{i}After having a private call with the Dillon, you were ultimately bribed to out him out and eliminate him.{/i}"
    "{size=40}{i}With his trust, you were able to attack him while his guard was down.{/i}"
    "{size=40}{i}Maybe next time you can make better decisions to turn the tables.{/i}"
    return

label rabbi:
    "{size=50}{b}WHACK{/b}" with vpunch
    show j_s
    j "Sorry, Rabbi... I just don't think this will work out."
    hide j_s
    "{size=40}{i}Your decisions throughout this game led to Jack {b}not trusting you{/b}.{/i}"
    "{size=40}{i}He believes taking you out is a sacrifice worth taking to keep his freedom and sanity.{/i}"
    "{size=40}{i}Maybe next time you can make better decisions to turn the tables.{/i}"
    scene gossip_b with fade
    return