init offset = -1

screen buttons():
        if (map[y - 1][x] < 1 and y != 0):
            textbutton "↑" action Return(value='F') xalign .9 yalign .7 text_size 200
            key "K_UP" action Return(value='F')
        if (map[y][x + 1] < 1 and x != len(map[0]) - 1):
            textbutton "→" action Return(value='R') xalign .97 yalign .83 text_size 200
            key "K_RIGHT" action Return(value='R')
        if (map[y + 1][x] < 1 and y != len(map) - 1):
            textbutton "↓" action Return(value='B') xalign .9 yalign .96 text_size 200
            key "K_DOWN" action Return(value='B')
        if (map[y][x - 1] < 1 and x != 0):
            textbutton "←" action Return(value='L') xalign .83 yalign .83 text_size 200
            key "K_LEFT" action Return(value='L')

screen mini_map_scr(map):
    frame:
        align (0.5, 0.5)
        grid len(map) len(map[0]):
            for i in range(len(map)):
                for j in range(len(map[0])):
                    if i == y and j == x:
                        $ tile = Solid("#FF0000", xmaximum=64, ymaximum=64)
                    elif map[i][j] < 1 and knowledgemap[i][j] == 1:
                        $ tile = Solid("#ffffff", xmaximum=64, ymaximum=64)
                    elif map[i][j] == 1 and knowledgemap[i][j] == 1:
                        $ tile = Solid("#008000", xmaximum=64, ymaximum=64)
                    else:
                        $ tile = Solid("#000000", xmaximum=64, ymaximum=64)

                    add tile

screen frontman():
    text "Choose a\nFrontman" xpos 0.7 xanchor 0.5 yalign 0.5 size 90 bold True outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]

screen go(op):
    textbutton "GO!" action [Hide("go"), Hide("setupstatus"), Return(op)] xpos 0.79 xanchor 0.5 yalign 0.94 text_size 90 text_bold True text_outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]

screen setup(back):
    $ squaresize = 200
    $ spacesize = 20

    for i in range(12):
        transform:
            image "ui/shadow.png"
            anchor (0.5, 0.5)
            pos (20 + (i % 4) * (squaresize + spacesize) + squaresize / 2, 0.29 * (math.floor(i / 4.0) + 1) + 0.08)

    for i, op in enumerate(ops):
        $ portrait = Image(op.getparameter(PORTRAITS)[0])

        imagebutton:
            pos (20 + (i % 4) * (squaresize + spacesize) + squaresize / 2, 0.29 * (math.floor(i / 4.0) + 1) + 0.09)
            anchor (0.5, 1.0)
            idle Transform(portrait, fit="contain", xysize=(squaresize, 400), ypos=0)
            hover Transform(portrait, fit="contain", xysize=(squaresize + 50, 450), ypos=50)
            action [Hide("frontman"), Show("setupstatus", op=op, back=back), Show("go", op=op)]

screen setupstatus(op, back):
    image "ui/setupmenu.png"

    image "ui/classicons/" + op.getparameter(CLASS).lower() + ".png" xysize (140, 140) pos (0.915, 0.02)
    text op.getparameter(CODENAME) size 90 xpos 0.56 color "#FFF" bold True outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]
    text op.getparameter(SUBCLASS) + " " + op.getparameter(CLASS) size 50 pos (0.58, 0.1) color "#414342" bold True

    if (back):
        textbutton "Back" action [Hide("setupstatus"), Hide("go"), Jump("badmove")] xalign .65 yalign .85 xminimum 350 text_xalign .5 text_size 60 text_color "#9b5151" text_hover_color "#d03b3d" background Frame("gui/button/choice_idle_background.png")

    hbox:
        pos (0.6, 0.2)
        spacing 40
        vbox:
            spacing 20
            text "Level:" bold True size 40
            text "Health:" bold True size 40
            text "Attack:" bold True size 40
            text "Arts:" bold True size 40

        vbox:
            spacing 20
            text str(op.getparameter(LEVEL)) size 40
            text str(op.getparameter(HEALTH)) size 40
            text str(op.getparameter(ATK)) size 40
            text str(op.getparameter(ARTS)) size 40

        vbox:
            xpos 100
            spacing 20
            text "Cost:" bold True size 40
            text "Move:" bold True size 40
            text "Defense:" bold True size 40
            text "Arts Def:" bold True size 40

        vbox:
            xpos 90
            spacing 20
            text str(op.getparameter(COST)) size 40
            text str(op.getparameter(MOV)) size 40
            text str(op.getparameter(DEF)) size 40
            text str(op.getparameter(ARTSDEF)) size 40

    text "Fighting Style: " + op.getparameter(ELEMENT)[0] + "/" + op.getparameter(ELEMENT)[1] size 30 xanchor 0.5 pos (0.785, 0.51) color "#FFF" bold True

    textbutton op.getparameter(TALENT) action Show("talentblurb", id=int(op.getparameter(ID))) background Frame("gui/button/choice_idle_background.png") xanchor 0.5 xminimum 350 text_xalign .5 align (.785, .475)

    hbox:
        align(0.785, 0.69)
        xanchor 0.5
        spacing 60
        for x in op.getparameter(TECHS):
            imagebutton:
                idle Transform(x.getparameter(ICON), size=(200, 200), matrixcolor=InvertMatrix(0.0))
                hover Transform(x.getparameter(ICON), size=(200, 200), matrixcolor=InvertMatrix(1.0))
                action [Show("techblurb", op=op, id=int(x.getparameter(ID)), fullscreen=True)]

screen talentblurb(id):
    python:
        id -= 1
        talenttext = "{b}" + opdex[id][CODENAME] + "'s Talent: " + opdex[id][TALENT] + "{/b}\n"

        talentext += gettalentblurb(id + 1)

    imagebutton:
        xfill True
        yfill True
        idle "ui/empty.png"
        action [Hide("talentblurb")]

    frame:
        align (0.5, 0.5)
        margin (200, 100)
        padding (100, 50)
        text talenttext xalign 0.5

screen techblurb(op, id, fullscreen):
    python:
        id -= 1
        techtext = "{b}" + op.getparameter(CODENAME) + "'s Tech: " + techdex[id][NAME] + "{/b}\n"
        techtext += "Gain SP by " + techdex[id][GAINTYPE].lower() + ".\n"

        currentsp = 0
        for tech in op.getparameter(TECHS):
            if (tech.getparameter(ID) - 1 == id):
                currentsp = tech.getparameter(POINTS)

        techtext += "Current SP: " + str(currentsp) + "/" + str(tech.getparameter(COST)) + "."

        charges = tech.getparameter(CHARGES)
        if (charges > 1):
            techtext += " Holds " + str(charges) + "."

        techtext += "\n"

        techtext += gettechblurb(id)

    if (fullscreen):
        imagebutton:
            xfill True
            yfill True
            idle "ui/empty.png"
            action [Hide("techblurb")]

    frame:
        align (0.5, 0.5)
        margin (200, 100)
        padding (100, 50)
        text techtext xalign 0.5

screen battle():
    python:
        screenwidth = 1920
        spacesize = 20
        totalspace = spacesize * 10
        squaresize = (screenwidth - totalspace) / 9

    text str(mydp) + " DP\n{size=40}+" + str(mydpgain) + " DP p/turn{/size}" xpos 0.1 xanchor 0.5 size 90 bold True outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]
    text str(otherdp) + " D\n{size=40}+" + str(otherdpgain) + "DP p/turn{/size}" xpos 0.9 xanchor 0.5 size 90 bold True outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]

    for i, op in enumerate(battlefield):
        $ color = "#FFF"
        if (ownedfield[i] == True):
            $ color = gui.hover_color
        elif (ownedfield[i] == False):
            $ color = "#E0A366"

        add Solid(color, xpos = 20 + i * (squaresize + spacesize), ypos = 800, xysize = (squaresize, squaresize))

        text str(battlefieldPoints(i)) size 180 color (0, 0, 0, 60) xpos 60 + i * (squaresize + spacesize) ypos 800 xysize (squaresize, squaresize)

        if (op != None):
            bar:
                xpos 20 + i * (squaresize + spacesize) + squaresize / 2
                ypos 800 + squaresize / 2
                xanchor 0.5
                xsize squaresize - 20
                range int(opdex[op.getparameter(ID) - 1][HEALTH] * (10 + op.getparameter(LEVEL)) * 5)
                value op.getparameter(HEALTH)
                right_bar gui.muted_color
                left_bar "#F69122"

            if (op.getparameter(ALLY)):
                text str(op.getparameter(HEALTH)) + "HP" xanchor 0.5 xpos 20 + i * (squaresize + spacesize) + squaresize / 2 ypos 797 + squaresize / 2 outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

            bar:
                xpos 20 + i * (squaresize + spacesize) + squaresize / 2
                ypos 850 + squaresize / 2
                xanchor 0.5
                xsize squaresize - 20
                range 10
                value op.getparameter(MOVEPOINTS) * 10
                right_bar gui.muted_color
                left_bar "#459426"

            if (op.getparameter(ALLY)):
                text str(op.getparameter(MOVEPOINTS)).rstrip(".0") + "MOV" xanchor 0.5 xpos 20 + i * (squaresize + spacesize) + squaresize / 2 ypos 847 + squaresize / 2 outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

            add Transform(Image(op.getparameter(PORTRAITS)[0]),
                          fit="contain",
                          xysize=(squaresize, 1000),
                          anchor=(0.5, 1.0),
                          xpos = 20 + i * (squaresize + spacesize) + squaresize / 2,
                          ypos = 800 + squaresize / 2,
                          xzoom = 1 if op.getparameter(ALLY) else -1)

            text orderstring(actionlist.index(op)) xanchor 0.5 xpos 20 + i * (squaresize + spacesize) + squaresize / 2 ypos 800 + squaresize / 2 - 50 outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

            if (op == actor):
                add Transform(Image("ui/cursor.png"), anchor=(1.0, 1.0), xpos = 20 + i * (squaresize + spacesize) + squaresize / 2, ypos = 700, xzoom = 0.25, yzoom = 0.25)

screen battleui():
    use battle()

    vbox:
        xalign .5 yalign .3
        hbox:
            textbutton "Attack" action Return(value='attack') xminimum 350 text_xalign .5 text_size 60 text_color "#9b5151" text_hover_color "#d03b3d" background Frame("gui/button/choice_idle_background.png")
            textbutton " Tech " action Return(value='tech') xminimum 350 text_xalign .5 text_size 60 text_color "#826926" text_hover_color "#c98022" background Frame("gui/button/choice_idle_background.png")
        hbox:
            textbutton " Move " action Return(value='move') xminimum 350 text_xalign .5 text_size 60 text_color "#437128" text_hover_color "#459426" background Frame("gui/button/choice_idle_background.png")
            textbutton " Item " action Return(value='item') xminimum 350 text_xalign .5 text_size 60 text_color "#295272" text_hover_color "#256799" background Frame("gui/button/choice_idle_background.png")
        hbox:
            textbutton "Deploy" action Return(value='deploy') xminimum 350 text_xalign .5 text_size 60 text_color "#772372" text_hover_color "#B739B0" background Frame("gui/button/choice_idle_background.png")
            textbutton " Pass " action Return(value='pass') xminimum 350 text_xalign .5 text_size 60 text_color gui.accent_color text_hover_color gui.hover_color background Frame("gui/button/choice_idle_background.png")

#location is an int from 0-8
#minrange is an int
#maxrange is an int >= minrange
#aoe is a boolean
#target is one of "op", "empty", or "both"
#deploying is an int, with 0 representing not deploying
screen targeting(location, minrange, maxrange, aoe, target, deploying):
    use battle()

    python:
        screenwidth = 1920
        spacesize = 20
        totalspace = spacesize * 10
        squaresize = (screenwidth - totalspace) / 9

    textbutton "Back" action Jump("badmove") xalign .5 yalign .4 xminimum 350 text_xalign .5 text_size 60 text_color "#9b5151" text_hover_color "#d03b3d" background Frame("gui/button/choice_idle_background.png")

    if (aoe):
        $ print("HANDLE THIS!")

    for i, op in enumerate(battlefield):
        if (((target == "op" and op != None)#if we're targeting an operator, and there's an operator on this battlefield slot...
            or (target == "empty" and op == None)#or we're targeting an empty square, and there's no operator on this battlefield slot...
            or target == "both")#or if we're targeting either
            and (deploying == 0 or deploying > 0 and ownedfield[i] == True and mydp >= deploying + i * 10)#or if not deploying, or if you are deploying, and own that tile, and have enough dp to spend...
            and location + minrange <= i <= location + maxrange):#and the possible target is within our targeting range...
            imagebutton:
                pos (20 + i * (squaresize + spacesize), 800)
                xysize (squaresize, squaresize)
                idle (Solid((155, 81, 81, 200)) if target != "empty" else Solid((67, 113, 40, 200)))#choose a red color if you can target an operator
                hover (Solid((208, 59, 61, 200)) if target != "empty" else Solid((69, 148, 38, 200)))#choose a green color if you can target the ground
                action Return(value=[i])

            if (deploying > 0):
                text str(deploying + i * 10) + "\nDP" size 80 color (255, 255, 255, 255) xpos 50 + i * (squaresize + spacesize) ypos 800 xysize (squaresize, squaresize)

#source is an operator object
#target is an operator object
#hits is an int
#atkbuff is a float, with 1 as default
#elements is an array of element strings, usually just one
#effect is either zero or a tech object
screen useattack(source, targets, hits, atkbuff, elements, effect):
    use battle()

    $ damagereport = ""

    for tech in source.getparameter(TECHS):
        if (tech.getparameter(GAINTYPE) == "Attacking"):
            $ tech.setparameter(POINTS, min(tech.getparameter(COST) * tech.getparameter(CHARGES), tech.getparameter(POINTS) + tech.getparameter(GAINPER)))

    $ incapacitated = []

    for target in targets:
        python:
            for tech in target.getparameter(TECHS):
                if (tech.getparameter(GAINTYPE) == "Defending"):
                    tech.setparameter(POINTS, min(tech.getparameter(COST) * tech.getparameter(CHARGES), tech.getparameter(POINTS) + tech.getparameter(GAINPER)))

            effectiveness = effectiveness(elements, target.getparameter(ELEMENT))
            power = (source.getparameter(ARTS) if source.getparameter(USESARTS) else source.getparameter(ATK)) * 2.5 * atkbuff * effectiveness
            defense = (target.getparameter(ARTSDEF) if source.getparameter(USESARTS) else target.getparameter(DEF))

            dmg = 0
            for hit in range(hits):
                dmg += max(1, 0.05 * power, power - defense)

                if (source.getparameter(ID) == KROOS and renpy.random.random() <= 0.2):#KROOS TALENT, Kroos' talent
                    if ("{b}Kroos gets serious!{/b} " not in damagereport):
                        damagereport += "{b}Kroos gets serious!{/b} "
                    else:
                        damagereport = damagereport.replace("{b}Kroos gets serious!{/b} ", "{b}Kroos gets {i}deadly{/i} serious!{/b} ")
                    dmg *= 1.6

            dmg = int(min(target.getparameter(HEALTH), dmg))
            target.setparameter(HEALTH, target.getparameter(HEALTH) - dmg)

            damagereport += ("Ally " if source.getparameter(ALLY) else "Foe ")
            damagereport += source.getparameter(CODENAME) + " dealt " + str(dmg) + " damage to the "
            damagereport += ("ally " if target.getparameter(ALLY) else "foe ")
            damagereport += target.getparameter(CODENAME)
            damagereport += hitsStrings(hits)
            damagereport += "! "
            damagereport += effectivestring(effectiveness, elements, target.getparameter(ELEMENT))

            if (effect != 0):
                effectnum = effect.getparameter(EFFECT)
                if (effectnum == 1):#draining health, used by rocklaw. Uses effectpower1 as percentage of damage done.
                    max = maxhp(source)
                    source.setparameter(HEALTH, min(max, source.getparameter(HEALTH) + dmg * effect.getparameter(EFFECTPOWER1)))
                    damagereport += source.getparameter(CODENAME) + " drains " + str(dmg) + " health! "

            if (target.getparameter(HEALTH) <= 0):
                damagereport += ("Ally " if target.getparameter(ALLY) else "Foe ") + target.getparameter(CODENAME) + " incapacitated!"
                incapacitated.append(target)

        use showmessage(damagereport, incapacitated)

screen showmessage(message, val=None):
    use battle()

    imagebutton:
        xfill True
        yfill True
        idle "ui/empty.png"
        action ([Return(val)] if val != "badmove" else [Jump("badmove")])

    frame:
        align (0.5, 0.3)
        margin (200, 100)
        padding (100, 50)
        text message xalign 0.5

#source is an operator object
#target is an operator object
screen usetech(op):
    use battle()

    hbox:
        spacing 50
        align (0.5, 0.1)
        for tech in op.getparameter(TECHS):
            $ ready = tech.getparameter(POINTS) >= tech.getparameter(COST)
            imagebutton:
                idle Transform(tech.getparameter(ICON), size=(200, 200), matrixcolor=(InvertMatrix(0) if ready else SaturationMatrix(0)))
                hover Transform(tech.getparameter(ICON), size=(200, 200), matrixcolor=InvertMatrix(1) if ready else SaturationMatrix(0))
                hovered Show("techblurb", op=op, id=int(tech.getparameter(ID)), fullscreen=False)
                unhovered Hide("techblurb")
                action ([Return(value=tech), Hide("techblurb")] if ready else NullAction())

    textbutton "Back" action Jump("badmove") xalign .5 yalign .4 xminimum 350 text_xalign .5 text_size 60 text_color "#9b5151" text_hover_color "#d03b3d" background Frame("gui/button/choice_idle_background.png")

screen useitem():
    use battle()

    if (len(inventory) == 0):
        use showmessage("You don't have any items!", "badmove")

screen deploy():
    use battle()

    $ opsinbank = 0

    for op in ops:
        if op not in battlefield:
            $ opsinbank += 1

    if (opsinbank == 0):
        use showmessage("You have no undeployed operators!", "badmove")

    else:
        image Transform("bgs/tactics.png", matrixcolor=SaturationMatrix(0), xsize=1920, ysize=1080)
        use setup(back=True)

#op is an operator object
#statgains is a five-element array that's ordered "health, atk, def, arts, artsdef"
screen levelup(op, statgains):

    frame:
        margin (150, 75)
        align (0.5, 0.5)

    text op.getparameter(CODENAME).upper() + " LEVELED UP!" bold True size 90 align (0.5, 0.15)

    hbox:
        align (0.5, 0.6)
        vbox:
            spacing 120
            text "Level:" bold True size 40
            text "Health:" bold True size 40
            text "Attack:" bold True size 40
            text "Arts:" bold True size 40

        vbox:
            xsize 20

        vbox:
            spacing 120
            text str(op.getparameter(LEVEL)) + " ⇑1" size 40
            text str(op.getparameter(HEALTH)) + (" ⇑" + str(statgains[0]) if statgains[0] != 0 else "") size 40
            text str(op.getparameter(ATK)) + (" ⇑" + str(statgains[1]) if statgains[1] != 0 else "") size 40
            text str(op.getparameter(ARTS)) + (" ⇑" + str(statgains[3]) if statgains[3] != 0 else "") size 40

        vbox:
            xsize 800

        vbox:
            spacing 120
            text "Cost:" bold True size 40
            text "Move:" bold True size 40
            text "Defense:" bold True size 40
            text "Arts Def:" bold True size 40

        vbox:
            xsize 20

        vbox:
            spacing 120
            text str(op.getparameter(COST)) size 40
            text str(op.getparameter(MOV)) size 40
            text str(op.getparameter(DEF)) + (" ⇑" + str(statgains[2]) if statgains[2] != 0 else "") size 40
            text str(op.getparameter(ARTSDEF)) + (" ⇑" + str(statgains[4]) if statgains[4] != 0 else "") size 40

    image op.getparameter(PORTRAITS)[0] xalign 0.5 ypos 0.25

    imagebutton:
        xfill True
        yfill True
        idle "ui/empty.png"
        action [Return()]
