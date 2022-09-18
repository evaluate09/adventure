#Script!!
#Effects
define flashbang = Fade(0.2, 0.0, 0.2, color="#fff")
define damage = Fade(0.2, 0.0, 0.2, color='#ad0011')

#Characters 
define s = Character(_("???"), color="#ffffff", what_slow_cps=20) 
define me = Character(_("ME"), color="#c5f4fb", what_slow_cps=20)
define aw = Character(_("ALISON"), color="#9e62e7", what_slow_cps=20)
define al = Character(_("ALLY"), color="#FF8674", what_slow_cps=20)
define j = Character(_("JASON"), color="#76ba68", what_slow_cps=20)
define ez = Character(_("EDWARD"), color="#e8814d", what_slow_cps=20)
define em = Character(_("EVE"), color="#ac7241", what_slow_cps=20)
define l = Character(_("LUCAS"), color="#295cd4", what_slow_cps=20)
define g = Character(_("GOGI"), color="#c11d1f", what_slow_cps=20)

#Background Images
image bg street evening = "bg/street evening.png"
image bw street evening = "bg/bw/street evening.png"
image bg black = "bg/black.png"

#Sprites
image springsuperzoom:
    "sprites/sping.png"
    xsize 10000 ysize 10000
    xalign 0.495 yalign 0.55

image springzoom:
    "sprites/sping.png"
    xsize 5000 ysize 5000
    xalign 0.495 yalign 0.55

image springreg:
    "sprites/sping.png"
    xsize 1750 ysize 1750
    xalign 0.495 yalign 0.6

# The game starts here.

label start:

    #-----------------The Bonkening-----------------
    scene bg black 
    
    with fade
    
    play music "audio/seeyoutomorrow.mp3" fadein 5.0
    
    scene bg street evening 
    
    with fade
    
    me "Man, I'm tired..."
    
    me "It's so late already..."
    
    me "When my teacher asked me to stay back and help with moving the boxes, I didn't think I'd be staying back until 6pm, and yet..."
    
    me "Here I am."

    me "{i}... Is this even legal??{/i}"

    pause(1)

    me "Strange. It's ... quiet ..."

    pause(1)

    me "wh-{nw}"

    stop music

    play audio "audio/hit.ogg" 
    
    with vpunch 
    
    with hpunch

    "{i}{size=+20}Thwack!{nw}{/size}{/i}"

    with damage

    scene bg black 
    
    with fade

    play audio "audio/vine_boom.mp3"
    
    "{i}Thud.{/i}"

    #-----------------Into the Dreamworld-----------------
    play music "audio/buzz.mp3" fadein 1.0 

    "{cps=6}...{/cps}"

    "{cps=6}......{/cps}"

    scene bw street evening

    show springzoom

    $ zoomed = True

    with pixellate

    pause(1)

    s "{cps=3}...{/cps}"

    s "ah, good you're finally awake"

    me "WHA-"

    s "you've been out for 1 hour, 4 minutes and 3 seconds"

    me "WHAT IS GOIN-"

    s "you should invest in an alarm clock or something, jimmy"

    me "OK, OK, HOLD UP."

    me "I have {i}SEVERAL{/i} questions and you're not giving me the chance to say anything."

    s "oh huh ok then"

    s "what do you wanna ask?"

    #-----------------Questioning-----------------
label questioning:
    menu questionspring:
        "Who are you?":
            me "Who are you?"

            s "I'm spring, I'm a porcupine for some reason"

            $s = Character(_("SPRING"), color="#fec29f")

            me "And I'm guessing you don't know what that reason is?"

            s "correct, wow you're so smart jimmy"

            jump questioning

        "Where am I?":
            me "Where am I?"

            s "oh you're in the <REDACTED>"

            me "The what?"

            s "<REDACTED>, idk figure it out lol you've seen this before, haven't you?"

            me "...<REDACTED>??"

            me "Holy shit, how did I do that??"

            s "lol"

            jump questioning

        "How are you talking like that?":
            me "How are you talking like that?"
            
            s "like what"

            me "Like that!!"

            s "i have no idea what you're talking about lol"

            me "Alright.. fine.."

            jump questioning

        "How do you know my name?":
            me "How do you know my name?"
            
            s "there was like this floating book that appeared in front of me and gave me ritual instructions on how to summon this guy called “jimmy” here"

            s "so i completed the ritual, went to earth, beat up a person that looked like you, and dragged them back here so now you're here"

            me "Uhh... ok.."

            jump questioning

        "Can you move back a bit?":
            me "Can you move back a bit?"

            s "oh lol ok"

            pause(0.5)

            hide springzoom

            show springreg

            pause(0.5)
            
            s "there"

            me "Thanks..."

            jump questioning

        "That's everything I wanted to know for now.":
            pass

    me "I'm guessing this is some kind of weirdly elaborate dream my mind has cooked up or a prank of some kind?"

    s "{i}shrug{/i}"

    me "Right, that's cool and all that you summoned me here, but… can I go home now?" 

    me "I'm kinda starting to get hungry, and uh, my parents are probably gonna be worried if I don't get home soon."

    s "n o"

    s "we need you to save the world"

    me "H-huh?"

    s "you see the landscape around us? it's dark"

    s "and colourless"

    s "and d e a d"

    if zoomed:
        me "I can't really see with you s-"
    else:
        me "Yeah..?"

    s "yeah it used to be super colourful and a bunch of friends would hang around here doing friend stuff"

    s "but then something happened. as time went on they were given more and more work to deal with, and one by one they all eventually left because they were all too busy with things"

    s "work, school, family, responsibilities, other friends, you name it"

    s "without the friends, the colour slowly started to fade away from the world and then only i remained here"

    s "i wonder why i'm still coloured..."

    s "hm"

    s "i can't bring back everyone, you know?"

    s "that's why i need your help, jimmy"

    s "help me save everyone from their responsibilities and restore life to the world around us"

    s "also i have no idea how to get you home anyway so you may as well help me lol"

    s "what do you say?"

    menu tostarveornot:
        "Yeah, sure. Why not?":
            me "Yeah, sure. Why not?"

            s "great :D"

            jump gogi_edward

        "I mean, I don't know...":
            me "I mean, I don't know..."

            hide springzoom

            show springsuperzoom

            s "a r e  y o u  s u r e ?"

            menu confirmstarve:
                "Yes.":
                    me "Yes."

                    hide springsuperzoom

                    show springreg

                    s "{cps=3}...{/cps}"

                    jump starve_ending

                "No, sorry. I'll help you.":
                    me "No, sorry. I'll help you."

                    s "great :D"

                    jump gogi_edward

        
label gogi_edward:
    return
#-----------------Starve Ending Choice-----------------
label starve_ending:
    play music "audio/failure.mp3" fadein 20.0

    me "I just don't think I'm really cut out for this kind of thing, you know?"

    me "I'll just… wait here patiently for a solution. Something's gotta come up, I just know it. Since this is a dream, if I believe in it hard enough, surely something will happen, right...?" 

    s "{cps=3}...{/cps}"

    s "i see"

    s "{cps=3}...{/cps}"

    hide springreg with moveoutright

    me "She's... gone."

    "{cps=20}Now that I look around more, this place really doesn't seem that great.{/cps}"

    "{cps=20}Everything is a gray husk. Cold. Stale. Empty of life.{/cps}"
    
    "{cps=20}Death truly spares nothing, huh?{/cps}"
    
    "{cps=20}...{/cps}"

    "{cps=20}Is it too late to go find the porcupine again?{/cps}"

    "{cps=20}...{/cps}"

    "{cps=20}Ah.. I'm.. tired..{/cps}"

    "{cps=20}I think I'll take a nap here.. under this tree.{/cps}"

    "{cps=20}...{/cps}"

    "{cps=20}.....{/cps}"

    scene bg black with fade

    play music "audio/tryagain.mp3" fadein 10.0 fadeout 10.0

    "{cps=10}if you look back into the empty soulless fields,{/cps}"
    
    "{cps=10}you can spot a skeleton lying below a dead tree,{/cps}"
    
    "{cps=10}and a small colourful porcupine doing their absolute best,{/cps}"
    
    "{cps=10}scuttling back and forth to bring their friends back,{/cps}"
    
    "{cps=10}day after day,{/cps}"
    
    "{cps=10}though to no avail...{/cps}"

    "{cps=6}BAD END{/cps}"
    return
