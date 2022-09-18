# Effects
define damage = Fade(0.2, 0.0, 0.2, color="#ad0011")
define flashbang = Fade(0.2, 0.0, 0.2, color="#fff")

# Characters
define me = Character(_("ME"), color="#c5f4fb")
define aw = Character(_("ALISON"), color="#9e62e7")
define al = Character(_("ALLY"), color="#FF8674")
define j = Character(_("JASON"), color="#76ba68")
define s = Character(_("SPRING"), color="#fec29f")
define ez = Character(_("EDWARD"), color="#e8814d")
define em = Character(_("EVE"), color="#ac7241")
define l = Character(_("LUCAS"), color="#295cd4")
define g = Character(_("GOGI"), color="#c11d1f")

# Images
image bg street evening = "bg/street evening.png"
image bg black = "bg/black.png"

# The game starts here.

label start:

    scene bg black
    with fade

    play music "audio/seeyoutomorrow.mp3" fadein 5.0

    scene bg street evening
    with fade

    me "Man, I'm tired..."

    pause 0.3

    me "It's so late already..."

    "When my teacher asked me to stay back and help with moving the boxes, I didn't think I'd be staying back until 6pm, and yet..."
    
    "Here I am."
    
    me "{i}... Is this even legal??{/i}"

    pause 1

    me "Strange. It's... quiet..."

    pause 1

    me "Wh-{nw}"

    stop music

    play audio "audio/hit.ogg"
    with vpunch
    with hpunch
    with damage

    scene bg black
    with fade

    play audio "audio/vine boom.mp3"
    "{i}Thud.{/i}"

    play music "audio/buzz.mp3" fadein 1.0 

    "..."

# TODO label dreamworld_intro:
# label questions
# label questions_finish
# label gogi_edward

label starve_ending:

    play music "audio/seeyoutomorrow.mp3"

    me "I mean, I don\’t know…"

    me "I just don\’t think I\’m really cut out for this kind of thing, you know?"

    me "I\’ll just… wait here patiently for a solution. Something\’s gotta come up, I just know it. Since this is a dream, if I believe in it hard enough, surely something will happen, right…?" 

    "Spring stared at me with a blank face, and I could almost make out what seemed like a flash of disappointment, before…"

    s "fine i get it"

    s "ok guess its up to me then"

    s "... bye"

    "With a twirl, Spring popped out of existence before my very eyes, leaving nothing but the smell of pies and nostalgia."

    me "... She disappeared."

    "And so because I elected to wait it out, I sat there in the empty white world."
    
    "I hadn\’t had a chance to look at it yet because of how crazy everything had been, but looking at it now, it really didn\’t seem all that great."

    "All of nature was basically dead."
    
    "The trees and grass had the life sucked out of them, leaving white husks of foliage, and it looked and smelt like the feeling of death."
    
    "The air was cold, stale, and much like Spring had said, empty of life."

    "I made myself comfortable. It was going to be a long wait, after all."

    "..."

    "......"

    with fade

    play music "audio/buzz.mp3"

    "Several years have passed since then. I died, of course. You can\’t survive that long without food."

    "But legends say, if you look back into the empty soulless fields,"
    
    "you can spot a skeleton lying below a dead tree,"
    
    "and a small colourful porcupine doing their absolute best,"
    
    "scuttling back and forth to bring their friends back,"
    
    "day after day,"
    
    "though to no avail..."

    "BAD END"

    return
    with fade
