#-----------------Effects-----------------
define flashbang = Fade(0.2, 0.0, 0.2, color="#fff")
define damage = Fade(0.2, 0.0, 0.2, color='#ad0011')

#-----------------Characters-----------------
define s = Character(_("???"), color="#ffffff") 
define me = Character(_("ME"), color="#c5f4fb")
define aw = Character(_("ALISON"), color="#9e62e7")
define al = Character(_("ALLY"), color="#FF8674")
define j = Character(_("JASON"), color="#76ba68")
define ez = Character(_("EDWARD"), color="#e8814d")
define em = Character(_("EVE"), color="#ac7241")
define l = Character(_("LUCAS"), color="#295cd4")
define g = Character(_("GOGI"), color="#c11d1f")

#-----------------Background Images-----------------
image bg street evening = "bg/street evening.png"
image bw street evening = "bg/bw street evening.png"
image bg black = "bg/black.png"

#-----------------Sprites-----------------
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