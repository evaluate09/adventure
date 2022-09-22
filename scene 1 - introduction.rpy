label start:

#-----------------The Bonkening-----------------
    scene bg black 
    
    with fade
    
    play music "audio/ost/seeyoutomorrow.mp3" fadein 5.0
    
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

    play sound "audio/sfx/hit.ogg" 
    
    with vpunch 
    
    with hpunch

    "{i}{size=+20}Thwack!{nw}{/size}{/i}"

    with damage

    scene bg black 
    
    with fade

    play sound "audio/sfx/vine_boom.mp3"
    
    "{i}Thud.{/i}"

#-----------------Into the Dreamworld-----------------
    play music "audio/ost/buzz.mp3"

    "{cps=6}...{/cps}"

    "{cps=6}......{/cps}"

    scene bw street evening

    show spring neutral:
        zoom 3.0
        xalign 0.495 yalign 0.55

    $ zoomed = True

    with Pixellate(1.0, 10)

    pause(1)

    s "{cps=3}...{/cps}"

    s "oh, good you're finally awake"

    me "WHA-{nw}"

    s "you've been out for 1 hour, 4 minutes and 3 seconds"

    me "WHAT IS GOIN-{nw}"

    s "you should invest in an alarm clock or something, jimmy"

    me "OK, OK, HOLD UP."

    me "I have {i}SEVERAL{/i} questions and you're not giving me the chance to say anything."

    s "oh huh ok then"

    s "what do you wanna ask?"

    $ worldname = '<REDACTED>'

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

            s "oh you're in the [worldname]"

            me "[worldname]?"

            me "Wait how did I do that..."

            $ worldname = 'Dreamworld'

            s "Oh sorry, I meant the [worldname]"

            me "[worldname]..?"

            me "Huh..."

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

            show spring neutral:
                zoom 3 
                ease 0.5 zoom 1.0 xalign 0.495 yalign 0.6

            pause(0.5)
            
            s "there"

            me "Thanks."

            $ zoomed = False

            jump questioning

        "That's everything I wanted to know for now.":

            me "That's everything I wanted to know for now."

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
        me "I can't really see with you so close..."
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

            jump gogi_edward

        "I mean, I don't know...":
            me "I mean, I don't know..."

            show spring neutral:
                ease 1 zoom 4 xalign 0.495 yalign 0.55
                
            s "a r e  y o u  s u r e ?"

            menu confirmstarve:
                "Yes.":
                    me "Yes."

                    show spring neutral:
                        zoom 4
                        ease 0.5 zoom 1.0 xalign 0.495 yalign 0.6

                    s "{cps=3}...{/cps}"

                    jump starve_ending

                "No, sorry. I'll help you.":
                    me "No, sorry. I'll help you."

                    jump gogi_edward