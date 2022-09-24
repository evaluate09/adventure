#-----------------Spring Direct to Gogi Edward-----------------
label gogi_edward:
    s "great :D"
    
    me "So… how can I help? Is there like some quest I have to go on?"

    me "Perhaps a magical sword at the end that brings everyone together, ushering peace to the land?"

    s "oh no lmao u just gotta do some mediation between people"

    s "i'm sure you'll be fine though didn't u say u wanted to be a therapist"

    me "No, I did not ever say that to you, how do you know that?"

    s ""

    s "magic"

    me "Oh. Okay."

    s "anyway you said you were hungry right"

    me "Yeah…? I am a bit peckish. I've been sorting through papers for the last-{nw}"

    s "alright cool i've got a friend who used to hang out around here and they do some really pog cooking"

    s "we can head over and have them cook up something for us and convince them to come hang out to bring back the life"

    me "Cool..."
    
    me "You know, I'd really appreciate it if you didn't interrupt me every time I was going to say something."

    s "oh lol sorry about that bad habit"

    s "also it's funny"

    me "Well, better than nothing, I guess. Now, which way-{nw}"

    s "welp lets goooo"

    stop music fadeout 1.0

#-----------------Kitchen Choice-----------------
    scene bg kitchen with Pixellate(1.0, 10)

    play music "audio/ost/spongebob clown.mp3" fadein 10.0
    
    show spring neutral

    me "-do we go... Wait what happened? Why are we in a different place?"

    s "magic"

    me "You have teleportation powers?!"

    s "yeah B)"

    "This place seems to have originally belonged to a fast food restaurant."

    "Grease is dripping down the sides of the machines... It smells like oil and it's so humid..."

    "Urgh...My eyes are watering from the filth of this room."

    "More lifelike than the [worldname] place that I was just in at least..."

    s "anyway this is {color=#e8814d}edward's{/color} place it's a little drab right now but that's because his life force has been sucked dry by all these"

    s "{i}responsibilities{/i}"

    me "I see... Well, let's help him figure out how to get rid of these responsibilities first, and then everyone can come back to the [worldname]!"

    s "now we need to find him"

    me "Wait, you don't know where he is?"

    s "i did say this was his house he might not actually be in his house"

    "Well then, I guess I should probably look around."

    "..."

    "..."

    "There seems to be two doors."

    hide spring neutral

    scene bg kitchenleft with fade

    "On the left..."

    "I can feel a cold chill coming from this door... it's giving me goosebumps."

    scene bg kitchenright with fade

    "On the right..."

    "Ahh, it's much warmer on this side."

    "Huh, it also seems like there's several voices shouting from inside."

    scene bg kitchen 

    show spring neutral

    with fade

    me "Alright then, let's go..."

    menu choice:
        "...left":
            me "...left"
            jump edwardleft

        "...right":
            me "...right"
            jump edwardright
#-----------------Freezer (Left)-----------------
    label edwardleft:
        scene bg kitchenleft 

        show spring neutral

        with fade

        me "Doesn't this kind of give you a sense like... We're going to die or something?"

        s "Nah it's pretty... {i}chill{/i}"

        play sound "audio/sfx/joke.mp3"

        pause(2)

        me "Haha, very funny..."

        s "but seriously though i don't think it'll be that bad"
        
        s "like i dunno maybe edward actually is just hidden in a creepy freezer y'know"

        me "Ok...sure...let's investigate this place then."

        s "wooo"

        me "Wait. Hang on. I've seen this before. I know how this ends."

        me "Can you hold open the door while I look inside so I don't get locked in forever and freeze to death?"

        s "ye ok"
        
        s "try not to freeze though"

        me "..."

        "I haven't even opened the door and the smell is already so..."

        "My eyes are watering even more from whatever's inside..."

        scene bg black with fade

        play sound "audio/sfx/freezer door.mp3"

        "Well, here I go..."

        stop music

        play audio "audio/sfx/vine_boom.mp3"

        scene bg burgervault 
        
        with vpunch 
        
        with hpunch

        play music "audio/ost/edwardvault.mp3" fadein 5.0

        me "What."

        s ""

        me ""

        s "oh no that smell is horrendous"

        me "..."

        me "..."

        s "yeah see i'll be an extremly kind porcupine and hold this very heavy door open while you get to searching : )"

        me "..."

        s "you know that mountain of burgers looks like its moving a bit"
        
        s "huh i think its oozing grease"

        me "..."

        s "there also seems to be something festering over there in that corner"

        me "..."

        s "i also wonder what's creating that squelching sound"

        me "..."

        s "you gonna start searching?"

        me "..."

        me "You know, I don't think your friend is in this room. Let's just go to the other door..."

        s "aw"

        me "ALSO, don't you have magic powers?? Wouldn't you have super strength? Shouldn't it be super easy to hold that door open?"

        s "y e s  : )"

        me "Uh..."

        s "L bozo lol"

        me "Huh?!"

        s "let's go to the other room"
        
        play music "audio/ost/spongebob clown.mp3" fadein 5.0

        jump edwardright
#-----------------Office (Right)-----------------
    label edwardright:

        scene bg kitchenright 

        show spring neutral

        with fade
        
        "This door certainly seems better than the other one..."
        
        "But wow... that's an extremely aggressive conversation taking place in there."

        s "well that's definitely edward's voice but i wanna listen into their argument so..."

        hide spring neutral with moveoutright

        show spring popcorn with moveinright

        s "want some popcorn?"

        me "Sure."

        hide spring neutral

        scene bg kitchenright:
            zoom 2.0
            xalign 0.8 yalign 0.6
        with dissolve

        ez "WHAT THE MOTHERFRICKING FRICK HAVE YOU DONE THIS TIME"

        ez "WHY IS IT ALL ON FIRE"

        ez "HOW DID YOU SET THE WATER ON FIRE WTFFFF"

        g "SHUT YO MOUF MF YOU'RE SUPPOSED TO BE COOKING THAT DISH"

        g "IM TRYING TO GET THE SOUP BOILING OK, YOU PUT FOIL IN THE MICROWAVE!!!"

        ez "YEAH WELL"

        ez "YEAH"

        ez "Yeah." 

        g "yeah that's right one ball man"

        ez "ALRIGHT BUDDY YOU'VE GONE TOO FAR THIS TIME"

        g "BOUT TO TAKE YO OTHER BALL HAHAH"

        "Listening to this argument is torture."

        "..."

        "Argh, screw it, I'm going in there."

        scene bg officestart

        stop music

        play music "audio/ost/argument.mp3" fadein 5.0

        show edward neutral:
            xalign -1.1 yalign 0.1
            flip

        show gogi angry:
            xalign 1.1 yalign 0.8
        
        play sound "audio/sfx/office door open.mp3"

        with fade

        me "..."

        me "OKAY. STOP. WHAT IS GOING ON."

        g "IM THE ONE DEFENDING YOU IN COURT FOR FREE LITERALLY STFU"

        ez "if Irrelevant NPC #3 was just swaggie enough they wouldn't have just like died yk, just get stronger bozo kinda sounds like a skill differential"

        g "SKILL DIFFERENTIAL?? HOW AM I MEANT TO DEFEND YOU IN COURT IF YOU ADMIT YOU'RE GUILTY?"

        g "WHY THE HELL DOES MY CLIENT WANT TO GO TO JAIL IM GONNA CRY"

        ez "hey i'm not saying i wanna go to jail or smth like literally im just saying it wasnt my fault! if he died then it was either skill diff or someone swapped out the food because i would NEVER make food that bad"

        show gogi shock:
            xalign 1.1 yalign 0.8

        g "wait"

        g "what you said is kinda genius"

        g "holy crap i've been an idiot"

        ez "yeah lmao like im sayin clearly it was a skill di-{nw}"

        show gogi confused:
            xalign 1.1 yalign 0.8

        g "NO LOSER i mean- what if someone poisoned your food? and framed you? holy crap, I can make a case out of this."

        show edward smirk:
            xalign -1.1 yalign 0.1
            flip
        
        ez "sick thanks bro"

        g "c'mon we gotta go to court we gotta get this accusation off your profile otherwise you'll never get work opportunities in the future"

        ez "{cps=70}yeah the economic consequences of this is a far greater liability to my future employment opportunities as having a criminal record severely decreases your chances{/cps}{nw}"

        ez "{cps=70}of getting employment and also means you can't get a job with the government{/cps}"

        ez "by the way"

        ez "who's this guy? your sidekick or something?"

        me "Oh, no, I'm not..."

        show gogi plead:
            xalign 1.1 yalign 0.7
            ease 0.6 zoom 2 yalign 0.4 xalign 0.8
            
        g "Ooh perfect actually, you should be my assistant since I'll need a lot of help for this."

        me "Wait wha-{nw}"

        g "Come with me."

        scene bg officemessy 
        
        show gogi confused:
            yalign 0.4 xalign 0.8
            zoom 2
            pause(0.2)
            ease 0.6 zoom 1 xalign 1.1 yalign 0.5

        with fade

        play sound "audio/sfx/office door close.mp3"

        g "..."

        g "Now where was it..."

        show gogi confused:
            xalign 1.1 yalign 0.5
            ease 0.6 xalign -0.2

        g "Murder... {w=0.5}"

        show gogi confused:
            xalign -0.2 yalign 0.5
            flip
            linear 0.6 xalign 1.0

        g "Framed murder... {w=0.5}"

        show gogi confused:
            xalign 1.0 yalign 0.5
            flipreverse
            linear 0.3 xalign 0.6

        g "Attempted murder..."

        g "Ugh, where is that damn case? I need a case study that matches this one... it's the only way I can prove his innocence... "

        g "Ah."

        show gogi neutral:
            xalign 0.6 yalign 0.5
            ease 0.5 zoom 1.7 xalign 0.2 yalign 0.4

        g "You there! Help me look for the case file. It should be titled Green v Brooks 2030."

        "Wait, did she just cite a case from the future?"

        me "Er... I don't even know your name, but sure!"

        "Not like I have a choice anyways..."

        show gogi neutral:
            xalign 0.2 yalign 0.4
            ease 0.5 zoom 1 xalign 0.5 yalign 0.5
        

#-----------------File Search-----------------
label filesearch:
    show gogi neutral
    "Where should I search?"
    menu search:
        "The bookshelf":
            jump cupboard
        "The desk":
            jump desk
        "The fishbowl made of paper with no water and containing a single paper origami fish":
            jump fishbowl
        
label cupboard:
    
    hide gogi

    scene bg bookshelf 

    with fade

    "Wow... there's so many books here..."

    "Hm... Maybe the file is in these books?"
    
    "..."

    "I can't see anything relevant on the bottom shelves, maybe it's higher up on those top shelves."


    "Just need to reach those books."
    
    "..."

    "Nearly... there."

    "Just need to... reach a bit further..."

    "There! Got it-{nw}"

    me "Woah!!"

    g "Ah, wait, be careful-"

    play sound "audio/sfx/book falling.mp3"

    with hpunch

    with damage 

    scene bg black with fade

    scene bg bookshelf with dissolve

    show gogi shock with moveinright

    me "Ouch!"

    "{i}Took 5 bludgeoning damage and 7 slashing damage.{/i}"

    show gogi plead

    g "Oh my god. I am SO sorry I haven't organised my books and files in like years there's so many everywhere-"

    g "Are you okay??"

    me "Yeah... I'm fine... I think."

    show gogi happy

    g "Okay cool slay :star_struck:"

    "Ah. Looks like there's really nothing here then."

    scene bg officemessy

    show gogi happy

    with fade

    jump filesearch

label desk:

    "What a messy desk."

    me "Here, let me help you find that file."

    show gogi happy

    g "Oh slay, thanks so much!"

    pause(2)

    me "So... What is your name, anyway? I never did actually catch it."

    show gogi shock

    g "Oh!!! that's right!!! I haven't introduced myself."

    show gogi happy

    g "I'm Georgina! But you can just call me Gogi, I work as a lawyer here in Dreamworld. I'm not sure if you've met the idiot properly yet either, but his name is Edward."

    $g = Character(_("GOGI"), color="#c11d1f") #GOGI

    $ez = Character(_("EDWARD"), color="#e8814d") #EDWARD

    g "I'm sure you guys would get along like a house on fire"
    
    g "Well. He better hope that you like him because you and I will be defending him in court in front of the all-mighty judge."

    me "The- the all-mighty judge?"

    g "Yep. Oh, well her full name is the All-Mighty Honourable Venerable Master Judge of All Time Space and Creation but we just call them the all-mighty judge for short."

    g "Oh, by the way, what is your name?"
    
    g "I've never seen you around here, and believe me,"

    show gogi concerned with dissolve

    g "I've been here for a {i}long{/i} time."

    show gogi happy

    me "I'm Jimmy. I have no idea how I got here, but one day I was going home from school late, but then I got knocked out by Spring, and now I'm here... saving this world."

    g "How admirable!"

    show gogi neutral

    g "Wow."

    g "Anyway you're my assistant for today and it's your responsibility to not get Edward thrown in jail."

    g "If he goes to jail, we also get thrown in jail, so you'd better learn the case details."

    g "For example, do you remember the name of the file we're looking for?"

    me "Err... It's..."

    menu casename:
        "Green v Brooks 2030":
            jump green 
        "Genner v Barks 2040":
            jump genner 

label fishbowl: 

    hide gogi

    show bg bowlnofish

    show ast fish

    with fade

    "..."
    
    "What a wonderful fishbowl..."

    "So...decorative..."

    "Seems like there's a singular origami fish in there. I wonder if it has anything on it."

    "Surely it's an important document if it is kept in this unique manner."

    hide ast fish with moveoutbottom

    "Well, let's see then..."

    play sound "audio/sfx/vine_boom.mp3"

    show ast jimmysus with moveinbottom

    me "What."

    scene bg officemessy

    show gogi confused

    me "...how did you get this photo?"

    show gogi happy:
        xalign 0.6 yalign 0.5
        ease 0.5 zoom 1.7 xalign 0.2 yalign 0.4

    g "Oooh..."
    
    g "Not telling!"

    g "But a certain porcupine came to me..."

    show gogi happy:
        xalign 0.2 yalign 0.4
        ease 0.5 zoom 1 xalign 0.5 yalign 0.5

    "Looks like there's nothing else here."

    jump filesearch

label green:

    show gogi happy

    $ willwriting = False

    g "Oh, nice, that's correct!"

    g "I guess Edward is in capable hands then. Don't screw up on me, assistant!"

    jump filefound

label genner:

    $ willwriting = True

    show gogi vconcerned

    g "No! what? Oh god we're all gonna get thrown in jail aren't we?"
    
    g "I may as well start writing my will. Oh god."

    g "It's called Green v Brooks 2030."

    g "... Where did I even put it? It was in one of the files around here somewhere"

    jump filefound

label filefound:

    "I don't even have any lawyer experience..."

    "{i}How am I supposed to defend a guy in front of the All-Mighty Honourable Venerable Master Judge of All Time Space and Creation?!{/i}"

    "Ah well, for now I should just concentrate on the task at hand."

    "{i}A few minutes later...{/i}"

    me "AHA! Is this it, Gogi?"

    show gogi shock

    g "What? You found it??"

    show gogi happy

    g "You did it! You madlad, you found a file among millions in less than an hour, nice job!"

    me "Well, it was no easy feat... but yeah! Let's celebrate!"

    show gogi neutral

    g "Ah, not so fast, we still need to actually win the case. Let's use this case law to prove Edward's innocence so I can finally get back to my responsibilities."

    me "Of course, of course."

    g "Let's go back to where Edward is."

    hide gogi with moveoutleft

    scene bg officenofire

    show edward neutral:
        xalign -1.1 yalign 0.1
        flip
    
    with fade
    
    show gogi neutral:
        xalign 1.1 yalign 0.8
    
    with moveinright

    g "oh, good, you're still here, i was worried you would've run off and done some stupid shit like try to hide the evidence or something"

    ez "run off??" 
    
    ez "bro i got my future career on the line here i can't afford to leave."

    "Ah."
    
    "I see what Spring meant by 'responsibilities' now."

    "They're so caught up in their work, careers and whatever else the world has thrown at them, they've barely had any time to relax."

    "I'll do my very best to help Spring then."

    me "Alright! I didn't think I'd ever say this in my life, much less with such enthusiasm but... shall we go to court?"

    jump court