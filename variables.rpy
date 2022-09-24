#-----------------Effects-----------------
define flashbang = Fade(0.2, 0.0, 0.2, color="#fff")
define damage = Fade(0.2, 0.0, 0.2, color='#ad0011')

#-----------------Characters-----------------
define s = Character(_("???"), color="#fec29f") #SPRING
define me = Character(_("ME"), color="#c5f4fb") #ME
define aw = Character(_("???"), color="#9e62e7") #ALISON
define al = Character(_("???"), color="#FF8674") #ALLY
define j = Character(_("???"), color="#76ba68") #JASON
define ez = Character(_("???"), color="#e8814d") #EDWARD
define em = Character(_("???"), color="#ac7241") #EVE
define lg = Character(_("???"), color="#295cd4") #LUCAS
define ld = Character(_("???"), color = "#cecece") #LINH
define g = Character(_("???"), color="#c11d1f") #GOGI
define ew = Character(_("???"), color="#af91d4") #ELAINE
define mys = Character(_("???"), color="#ffffff") #MYSTERY
define wl = Character(_("???"), color="#ffffff") #WiLLIAM LEWIS 
define both = Character(_("BOTH"), color="#ffffff")

#-----------------Background Images-----------------
image bg street evening = "bg/street evening.png"
image bw street evening = "bg/bw street evening.png"
image bg black = "bg/black.png"
image bg kitchen = "bg/kitchen.png"
image bg kitchenleft = "bg/kitchenleft.png"
image bg kitchenright = "bg/kitchenright.png"
image bg burgervault = "bg/burgervault.png"
image bg officestart = "bg/officestart.png"
image bg officemessy = "bg/officemessy.png"
image bg bookshelf = "bg/bookshelf.png"
image bg bowlnofish = "bg/bowlnofish.png"
image bg officenofire = "bg/officenofirestart.png"
image bg courtroomlobby = "bg/courtroom lobby.png"
image bg courtroom = "bg/courtroom.png"
image bg sidebench = "bg/sidebench.png"
image bg sidebenchlook = "bg/sidebenchlook.png"
image bg judgechair = "bg/judgechair.png"
image bg witness = "bg/witnessstand.png"
image bg dimsidebench = "bg/dimsidebench.png"
image bg dimjudgechair = "bg/dimjudgechair.png"
image bg prison = "bg/prison.png"

#-----------------Assets-----------------
image ast holdit:
    "assets/HOLD IT.png"
    ycenter 0.4
image ast objection:
    "assets/OBJECTION.png"
    ycenter 0.4
image ast jimmysus = "assets/susjimmy.png"
image ast fish = "assets/origamifish.png"
image ast wtaccount:
    "assets/witnessaccount.png"
    ycenter 0.45
image ast wtendaccount:
    "assets/endwitnessaccount.png"
    ycenter 0.45
image ast crossexam:
    "assets/begincrossexamination.png"
    ycenter 0.4


#-----------------Movement-----------------
transform flip:
    xzoom -1.0
transform flipreverse:
    xzoom 1
#-----------------Sprites-----------------
#--Spring--
image spring neutral:
    "sprites/sping.png"
    xsize 1750 ysize 1750
    xalign 0.495 yalign 0.6
image spring popcorn:
    "sprites/sping popcorn.png"
    xsize 1750 ysize 1750
    xalign 0.495 yalign 0.6
image spring judge:
    "sprites/sping judge.png"
    xsize 1750 ysize 1750
    xalign 0.495 yalign 0.6
#--Edward--
image edward smirk:
    "sprites/edward smirk.png"
    zoom 0.55
image edward neutral:
    "sprites/edward neutral.png"
    zoom 0.55
image edward mc:
    "sprites/edward awh man.png"
    zoom 0.55
#--Gogi--
image gogi angry:
    "sprites/gogi anger.png"
    zoom 0.4
image gogi concerned:
    "sprites/gogi concerned.png"
    zoom 0.4
image gogi vconcerned:
    "sprites/gogi concerned 3.png"
    zoom 0.4
image gogi plead:
    "sprites/gogi concerned 2.png"
    zoom 0.4
image gogi confused:
    "sprites/gogi confused.png"
    zoom 0.4
image gogi happy:
    "sprites/gogi happy.png"
    zoom 0.4
image gogi neutral:
    "sprites/gogi neutral.png"
    zoom 0.4
image gogi shock:
    "sprites/gogi shock.png"
    zoom 0.4
image gogi wtf:
    "sprites/gogi roblox.png"
    zoom 0.4
#William Lewis 
image william neutral:
    "sprites/william lewis.png"
    ycenter 0.7
image william angry:
    "sprites/wl angry.png"
    ycenter 0.7