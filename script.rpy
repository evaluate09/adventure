# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define damage = Fade(0.2, 0.0, 0.2, color='#ad0011')

define me = Character(_("Me"), color="#fff")

define mystery = Character(_("???"), color="#ffffff") #This could be the death screen character

image bg street evening = "bg/street evening.png"
image bg black = "bg/black.png"


# The game starts here.

label start:

    scene bg black
    with fade

    play music "audio/begin.mp3" fadein 5.0

    scene bg street evening
    with fade

    me "It's so late already..."

    me "The teacher asked me to stay back a while to help with festival preparations, but then I ended up staying back at school until 6pm..."
    
    me "{size=-5}{i}... Is this even legal??{/i}{/size}"

    me "I couldn't come up with a valid reason to leave either. I think I'd feel too bad otherwise."
    
    me "But what's done is done, I guess."

    me "The only thing {i}I{/i} have to worry about now is not getting kidnapped in the dark while walking home."

    me "Even then, it's such an unlikely event that I can afford to let my guard down, right? Plus, I'm already really tired from having to go through all those applications and papers..."

    me "I really don't have to-"

    stop music

    play audio "audio/hit.ogg"
    with vpunch
    with hpunch
    with damage

    scene bg black
    with fade

    "{size=+20}{i}Thwack!{/size} Thud.{/i}"

    me "... was the last thing I heard before everything faded to black."

    play music "audio/buzz.mp3"

    "..."

    "Ally" "lol that's the end i don't have anything else interesting rn but here's a sample preview of what i can currently do in ren'py minus sprites because dear god those are hard"

    return
