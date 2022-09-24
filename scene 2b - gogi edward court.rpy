label court:

    play music "audio/ost/courtroom.mp3" fadein 1.0

    scene bg courtroomlobby 

    show edward neutral:
        xalign -1.1 yalign 0.1
        flip
    
    show gogi neutral:
        xalign 1.1 yalign 0.8
    
    with Fade(0.5, 1.0, 0.5)

    me "Umm... are you guys sure we're in the right game?"

    g "This is the courtroom, where the All-Mighty Judge resides and makes decisions. It's a little rough, and hasn't been used in a while, but if we want to survive we're gonna have to do our best."

    if willwriting == True:

        show gogi concerned

        g "You guys have your wills ready, right? Any family to say goodbye to?"

        me "Can you stop talking like we're gonna fail?!"
    
    me "We got this! Don't worry about it."

    me "Let's go in."

    show edward neutral:
        flipreverse
        pause(0.3)
      
    hide edward with moveoutleft
    
    hide gogi with moveoutleft
    
    scene bg courtroom with fade

    show edward neutral:
        xalign -1.1 yalign 0.1
    with moveinright
    show edward neutral:
        flip
    
    show gogi neutral:
        xalign 1.1 yalign 0.8
    with moveinright

    me "So how do the proceedings work?"

    ez "well, i go right up to that podium up there and i gotta give witness accounts, so does any witnesses i guess, and then you guys go like bing and boom and bababooey and im all good!"

    "I'm not entirely sure that's how it works..."

    show gogi confused

    g "Ugh, whatever, don't listen to him, that bozo only knows how to mansplain about economics, his future career and cheeseburgers."
    
    g "listen man, just whatever you do, do NOT say skill diff, or i will personally skin you alive before the judge can sentence you to eternal prison"
    
    ez "yeah yeah i get it sure"

    show edward smirk

    ez "but like. totally a skill diff"

    show gogi angry

    ez "cuz like, you also ate the same food and survived, so guess that guy's just built worse?"

    g "..."

    show gogi confused

    g "alright alright save it for the judge, we gotta get started. C'mon Jimmy, let's go up to the side bench."

    show gogi confused:
        flip
        pause(0.3)
    hide gogi with moveoutright

    show edward smirk:
        flipreverse
        pause(0.3)
    hide edward with moveoutleft
    
    scene sidebench with fade

    show gogi confused:
        flip
        pause(0.3)
        
    with moveinleft

    "Alright."

    "Gogi and I will be organising our notes and presenting our case. Edward will be giving a witness statement. [s] will..."

    "Wait. Where the heck is [s]?"

    stop music

    play sound "audio/sfx/spotlight.mp3"

    scene bg dimjudgechair
    
    pause(1) 

    g "Dude, stand up, it's the judge!"

    mys "all rise for the All-Mighty Honourable Venerable Master Judge of All Time Space and Creation!"

    play sound "audio/sfx/applause.mp3"

    me "Wait isn't that-?"

    stop sound fadeout 5.0

    scene bg judgechair

    show spring judge

    play sound "audio/sfx/spotlight.mp3"

    pause(1)

    "Surely that can't be right."

    scene bg sidebench 

    show gogi confused:
        flip
    
    with fade

    show spring neutral:
        xcenter 0.8
        #xoffset 300

    with pixellate

    s "hey dude sup"

    me "Wait, weren't you-"

    s "yeah i had some stuff to deal with but i'm here now lmao just call for me if you ever need help ok?"

    me "I-sure?"

    me "I'm so confused right now."

    scene bg judgechair

    show spring judge

    with fade

    pause(1)

    scene bg sidebench 

    show gogi confused:
        flip

    show spring neutral:
        xcenter 0.8
        #xoffset 300
    
    with fade

    pause(1)
    
    scene bg judgechair

    show spring judge

    with fade

    me "... IS NO ONE GOING TO QUESTION THIS??"

    s "silence order in the court pls etc etc"

    play music "audio/ost/court.mp3" fadein 2.0

    s "alright today we are here to witness the trial between edward “chezburger4lyfe” zhang and irrelevant npc #3, defendants may we hear a case statement"

    "Oh boy, this is gonna be a long day..."

    g "Your honour, today we're defending Zhang in his claim that he did not poison the food, and that he was in fact framed by none other than the plaintiff themselves!"

    window hide

    show ast holdit

    play sound "audio/sfx/wlHOLDIT.mp3"

    pause(1)

    window show
    
    scene bg sidebench:
        flip

    show william neutral

    wl "Kekekeke..."

    wl "Your honour, I would like to object to the defendant's statement. You see, it's quite simple really."
    
    wl "Why on Earth would my client, Irrelevant NPC #3, ever consider hurting themselves to get money?"
    
    wl "The disadvantages outweigh the benefits. You have no proof that NPC ever committed the act, or indeed is guilty here."

    g "Shoot, he's good..."

    me "Who the heck is he!?"

    scene bg judgechair
    
    show spring judge

    s "mr lewis that's cool and all but like you haven't introduced yourself as the plaintiff yet so your previous statement will not be part of your case"

    scene bg sidebench:
        flip

    show william neutral
    
    $ wl = Character(_("Mr. Lewis"), color="#ffffff")

    show william angry
    
    wl "Kh!"

    s "now, will the plaintiff please describe their case and the accusation they will make"

    wl "Well, can't you just take what I said before?!"

    s "no"

    show william neutral

    wl "Fine. Your honour, today I am representing my client, Irrelevant NPC #3 in his claims of food poisoning and attempted murder."
    
    wl "He will be prosecuting the suspect Zhang and suing him for 3 million Stellis in addition to a lifetime sentence in jail."

    g "That isn't even the currency we use here! What's up with this guy..."

    s "very well, let's hear from the suspect themselves as a first witness. defendants, please begin your cross examination"

    s "and as a disclaimer this does not reflect how court proceedings work in real life, you are literally playing a visual novel game made for your birthday jimmy"

    me "What do I have to do with this?"

    s "nothing"

    scene bg witness

    show edward smirk:
        yalign 0.1
        xalign 0.53

    with fade

    ez "I guess I'm up then"

    stop music fadeout 2.0

    play music "audio/ost/questioning moderato.mp3" fadein 2.0

    show ast wtaccount with dissolve

    pause(0.4)
    
    hide ast wtaccount with dissolve

    ez "well your all-mighty honourable honour sir, it started out something like this."

    ez "I was cooking in my kitchen as I always do, since I wanted to get some bread as you do"

    ez "when suddenly, gogi came in with a bunch of people"

    ez "and i was like damn"

    ez "its time to make some moneyy"

    ez "so I made the food as normal and gave it to the people"

    ez "they ate it, i got the dough, and they all left"

    ez "except gogi who stayed behind because she wanted to learn how to cook food or whatever so she wouldn't have to pay me all the time"

    ez "we got started cooking and then suddenly we got a call from this guy telling me that i poisoned his food and he would be taking me to court"

    ez "so gogi started accusing me of being bad at cooking"

    ez "and then i accused her of being bad at cooking (cuz she is)"

    ez "and here we are"

    show ast wtendaccount with dissolve

    pause(0.4)

    hide ast wtendaccount with dissolve

    scene bg sidebenchlook
    
    show gogi happy

    with fade

    g "There's gotta be something in that statement we can use to prove his evidence. Let's go Jimmy, you've got this!"

    me "Aren't you the lawyer here?!?!"

    s "defendant you may now begin your cross examination"

    scene bg witness

    show edward smirk:
        yalign 0.1
        xalign 0.53

    with fade

    show ast crossexam with dissolve

    pause(0.4)

    hide ast crossexam with dissolve

    stop music

    play music "audio/ost/questioning allegro.mp3" fadein 1.0

    $firsttransition = True

$ life = 3
$ livesorlife = 'lives'

label crossexam:

    if firsttransition == False:

        scene bg witness

        show edward smirk:
            yalign 0.1
            xalign 0.53

        with fade

    "Which part of Edward's statement should I press in order to get more clues?"

    window hide

    menu press:
        '"when suddenly, gogi came in with a bunch of people"': 

            window hide

            show ast holdit

            play sound "audio/sfx/jimHOLDIT.mp3"

            pause(1)

            hide ast holdit

            window show

            me "So you're saying that Gogi came in with a bunch of people?"

            ez "yeah basically"

            me "That means that there were other people there! Who else specifically was at the restaurant?"

            ez "well there was me, gogi, Irrelevant NPC #3..."

            ez "oh and there was also NPC's friend there too, though they didn't say much, just paid for their food and left"

            me "Your honour! I think there are more witnesses we must find and bring to court at once to provide more clues about this case!"

            me "Plus, there's something suspicious I realised about Edward's statement previously, while we were waiting in the lobby..."

            stop music fadeout 5.0

            play music "audio/ost/pressing pursuit.mp3" fadein 5.0

            me "For one, he mentioned that Gogi, NPC, and NPC's friend ate the food, so one would assume that they would all get poisoned, but..."

            me "Why is it that only NPC is sick and not the others?!"

            with hpunch

            with vpunch

            scene bg sidebenchlook

            show gogi shock

            with fade

            g "oh my god jimmy you're so smart"

            scene bg judgechair

            show spring judge

            with fade

            s "hmm... i see your point..."

            s "well then, lets review our current evidence"

            window hide

            show ast objection

            play sound "audio/sfx/wlOBJECTION.mp3"

            pause(1)

            hide ast objection

            scene bg sidebench:
                flip

            show william neutral

            with fade

            window show

            wl "Your honour, this is unnecessary, who's to say that these people haven't bribed NPC's Friend into lying for them?!"

            s "hmm"

            show william angry

            s "objection overruled"

            scene bg judgechair

            show spring judge

            with fade

            s "so? Jimmy, do you think we have all the facts needed to end this once and for all?"

            window hide

            menu choices:
                "Yes.":
                    me "Yes."
                    me "I think that's all we need. Let's ask the prosecutor to present their evidence and get the verdict as soon as possible!"
                    jump springbored

                "No.":
                    me "No."
                    me "There's still so much evidence we need. Plus, we also need to refute anything the prosecution throws at us... Let's keep working at it. "
                    jump springbored

        '"they ate it, i got the dough, and they all left"': #incorrect 
            
            window hide

            show ast holdit

            play sound "audio/sfx/jimHOLDIT.mp3"

            pause(1)

            hide ast holdit

            window show

            me "Edward, when you say you 'got the dough', could you be more specific?"

            scene bg sidebenchlook

            show gogi concerned

            with fade

            g "Bruh there's no way you don't know what dough means..."

            me "Aren't you meant to be specific in a court of the law?!"

            g "Well..."

            show gogi confused

            g "Wait, it's not even relevant! try pressing him on something else!"

            with hpunch

            with vpunch

            $ life -= 1

            scene bg judgechair

            show spring judge

            with fade

            s "uh bro i dont think that's right that makes like no sense"

            s "gonna have to penalise you for that buddy"

            if life == 0:
                jump prisonending
            
            if life == 1:
                $ livesorlife = 'life'
            else:
                $ livesorlife = 'lives'

            "Crap! I better press the right statement before I lose my credibility in this court! ([life] [livesorlife] remaining)."

            $firsttransition = False
            
            jump crossexam

        '"suddenly we got a call from this guy telling me that i poisoned his food"': #incorrect

            window hide

            show ast holdit

            play sound "audio/sfx/jimHOLDIT.mp3"

            pause(1)

            hide ast holdit

            window show

            me "A call from a guy? Who was he? What did he say exactly?"

            scene bg sidebench:
                flip

            show william neutral

            with fade
            
            wl "Oh come on, even idiots can figure out that he's talking about my client..."

            scene bg sidebenchlook

            show gogi confused

            with fade

            g "Get it together, Jimmy! Try focusing on something else!"

            with hpunch 
            
            with vpunch

            $ life -= 1

            scene bg judgechair

            show spring judge

            with fade

            s "uh bro i dont think that's right that makes like no sense"

            s "gonna have to penalise you for that buddy"

            if life == 0:
                jump prisonending
            
            if life == 1:
                $ livesorlife = 'life'
            else:
                $ livesorlife = 'lives'

            "Crap! I better press the right statement before I lose my credibility in this court! ([life] [livesorlife] remaining)."

            $firsttransition = False
            
            jump crossexam

        '"and then i accused her of being bad at cooking (cuz she is)"': #incorrect

            window hide

            show ast holdit

            play sound "audio/sfx/jimHOLDIT.mp3"

            pause(1)

            hide ast holdit

            window show

            me "Is that so? How was she bad at cooking?"

            ez "uh well, she set the water on fire like uhh... you gotta be pretty bad to do that lmao"

            ez "or maybe even impressive"

            scene bg sidebenchlook

            show gogi angry

            with fade

            g "THIS ISN'T EVEN ABOUT ME??"

            g "I don't know what you have against me Jimmy, but I don't think this'll lead anywhere..."

            show gogi confused

            g "Maybe you should try pressing him on something else."

            show gogi concerned

            g "And not... roasting me in the process..."

            with hpunch
            
            with vpunch

            $ life -= 1

            scene bg judgechair

            show spring judge

            with fade

            s "uh bro i dont think that's right that makes like no sense"

            s "gonna have to penalise you for that buddy"

            if life == 0:

                jump prisonending

            if life == 1:
                $ livesorlife = 'life'
            else:
                $ livesorlife = 'lives'

            "Crap! I better press the right statement before I lose my credibility in this court! ([life] [livesorlife] remaining)."

            $firsttransition = False
            
            jump crossexam

label springbored:

    s "well then, prosecutor state your case blah blah blah"

    scene bg sidebench:
        flip

    show william neutral

    with fade

    wl "Well, you see your honour-{nw}"

    stop music

    play sound "audio/sfx/record scratch.mp3" volume 0.3

    scene bg judgechair

    show spring judge

    with fade
    
    s "nvm you guys are taking so long"

    s "bro literally i am so hungry i haven't had anything to eat"

    s "and like u guys keep talking about food"

    s "im calling a lunch break and uhhhh"

    play music "audio/ost/court victory.mp3" fadein 2

    s "edward is free ig idk"

    s "all crimes are excused or something can i get lunch at your place now"

    scene bg sidebenchlook

    show gogi neutral

    with fade

    g "..."

    show gogi shock

    g "Wait."

    show gogi plead

    g "Just... Like that...?"

    g "Wow."

    show gogi happy

    g "SLAY this is the easiest case of my LIFE I am putting this in my resume."

    scene bg courtroomlobby

    show edward smirk:
        xalign -1.1 yalign 0.1
        flip
    
    show gogi happy:
        xalign 1.1 yalign 0.8

    with Fade(0.5, 1.0, 0.5)

    g "Won... a case... in 10 minutes..."

    show gogi wtf

    g "EZ CLAP."

    ez "bruh it was literally all Jimmy you did like nothing"

    show gogi angry

    g "SHUT UP LOSER I did plenty"

    show gogi happy

    g "ANYWAY"

    g "I'm not gonna lie this has been super fun!!"

    show gogi confused

    g "even with this bozo"

    show gogi happy

    g "Thanks for your help Jimbo but I gotta get back to work now so if you didn't need anything..."

    me "Well, actually-"

    show edward neutral

    ez "ok no dude you need to like take a break"

    ez "you haven't had a holiday or a break in like 6 years or something"

    ez "like bro just go chill somewhere"

    g "SAYS YOU BRUH"

    g "you've been like stuck at that restaurant and your whole freezer is going to shit because of how badly maintained it is"

    g "there's like several lifeforms growing there apparently"

    g "also you stink of fast food"

    g "also L + ratio"

    g "also-{nw}"

    me "Okay, {i}okay{/i}, again, what if you two {i}both{/i} take a break?"

    show gogi shock

    show edward mc

    both "..."

    "{i}{b}RING! RING! RING!{/b}{/i}"

    g "Ah crap that's my phone, hang on..."

    show gogi plead

    g "Hello? Yeah this is Gogi..."

    g "... A robbery...?"

    g "And you want me to... {i}defend you{/i}...?"

    g "..."

    g "nah i'm done here im gonna pass the phone to someone just as capable here you go"

    g "{i}I'm{/i} going to take a break."

    show gogi happy

    g "Have the phone, Jimmy."

    me "Woah, wait wait wai-"

    ld "HELLO? WHO'S THERE I NEED YOUR HELP RIGHT NOW I'M KIND OF IN A PINCH"

    me "HI, WAIT, WHO IS THIS?"

    ld "HI IT'S LINH IF YOU KNOW GOGI YOU PROBABLY KNOW ME"

    $ ld = Character(_("LINH"), color = "#cecece")

    me "UH NO I DON'T???"

    ld "Well, that sucks"

    ld "BUT STILL HELP ME OUT OKAY I NEED IT OK THANKS BYE BITCH"

    me "..."

    me "She hung up..."

    me "Gogi, why are your friends all like this?"

    show gogi concerned

    g "... Honestly I'm starting to ask myself the same question too."

    me "Oh, right! Before you guys go and have your break, I think Spring wanted you guys for something...?"

    show spring neutral with pixellate

    show gogi concerned:
        linear 0.2 xcenter 0.85

    show edward mc:
        linear 0.2 xcenter 0.15

    s "i was summoned?"

    show gogi happy

    g "Oh hey Spring! What did you want me and this bozo here for?"

    s "right well"

    s "i wanted to bring the gang back together one more time back in the main dreamworld because"

    s "it's kinda sad rn"

    s "so what do say"

    s "hangout at 8pm?"

    ez "well... we are on a break"

    g "Lets do it!! We'll be there, we just have to sort out some stuff first."

    me "Woohoo! That's two! Out of... how many?"

    s "hm"

    s "i'm actually not sure"

    s "we'll get to them all though don't worry"

    s "next stop: wherever the heck linh is"

    me "Oh no, you're not gonna do the teleporting thing again are you?"

    s "no"

    me "Oh, okay, phew-{nw}"

    jump heiststart