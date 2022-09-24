#-----------------Starve Ending-----------------
label starve_ending:
    play music "audio/ost/failure.mp3" fadein 10.0

    me "I just don't think I'm really cut out for this kind of thing, you know?"

    me "I'll just… wait here patiently for a solution. Something's gotta come up, I just know it. Since this is a dream, if I believe in it hard enough, surely something will happen, right...?" 

    s "{cps=3}...{/cps}"

    s "i see"

    s "{cps=3}...{/cps}"

    hide spring neutral with moveoutright

    me "She's... gone."

    "Now that I look around more, this place really doesn't seem that great."

    "Everything is a gray husk. Cold. Stale. Empty of life."
    
    "Death truly spares nothing, huh?"
    
    "..."

    "Is it too late to go find the porcupine again?"

    "..."

    "Ah.. I'm.. tired.."

    "I think I'll take a nap here.. under this tree."

    "..."

    "....."

    scene bg black with fade

    play music "audio/ost/tryagain.mp3" fadein 5.0 fadeout 2.0

    "{cps=10}if you look back into the empty soulless fields,{/cps}"
    
    "{cps=10}you can spot a skeleton lying below a dead tree,{/cps}"
    
    "{cps=10}and a small colourful porcupine doing their absolute best,{/cps}"
    
    "{cps=10}scuttling back and forth to bring their friends back,{/cps}"
    
    "{cps=10}day after day,{/cps}"
    
    "{cps=10}though to no avail...{/cps}"

    "{cps=6}BAD END{/cps}"
    return
#-----------------Prison Ending-----------------
label prisonending:

    stop music

    play sound "audio/sfx/record scratch.mp3" volume 0.3

    s "hm"

    s "nope i'm done"

    s "you've joked around so often i'm honestly not even sure if you're taking this seriously"

    s "im just gonna declare you guilty i'm not bothered enough for this"

    if willwriting == True:

        g "Damnit! I told you I should've written a will... I never should've trusted a rookie to help me out."
    
    me "Wait, Spring, you can't just do that! We're your friends-"

    play music "audio/ost/failure.mp3" fadein 10.0

    scene bg black with pixellate

    "It's too late..."

    "..."

    pause(2)

    scene bg prison with fade

    me "Ugh... that was a horrible teleporting experience. 1 star rating on Uber."

    me "Where... am I?"

    mys "Quieten down, inmate! You're in prison. Now just sit tight in your cell and wait out your sentence."

    "Oh no."

    me "And how long is that sentence?"

    mys "Lifetime sentence."

    me "That long?!"

    mys "Unlucky, mate. Maybe you should've thought about that before getting yourself into trouble."

    me "But that wasn't even my fault! I got dragged-{nw}"

    mys "Didn't I tell you to shut up?!"

    me "..."

    scene bg black with fade

    play music "audio/ost/tryagain.mp3" fadein 5.0 fadeout 2.0

    "And so, I begin my new life in prison."

    "{cps=18}The routine isn't too bad at first, just waking up, eating food, working, then sleeping, and repeat.{/cps}"

    "{cps=15}But soon...{/cps}"

    "{cps=12}I started to lose a sense of myself...{/cps}"

    "{cps=9}I don't remember how many years it's been.{/cps}"

    "{cps=9}I don't even think I remember my own name.{/cps}"

    "{cps=9}All I know is that I have to wake up to see tomorrow.{/cps}"

    "{cps=6}BAD END{/cps}"

    return