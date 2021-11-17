label CrawlEvent(mapname, eventcode):
    if (mapname == "guerroforest"):
        if eventcode == -2:
            show forest behind ace with dissolve

            a "This place can actually look kinda pretty. When it's not covered in burnt shit, anyway."

        elif eventcode == -3 and crawlMoveCommand == 'R':
            hide forest with dissolve

    elif (mapname == "piccinocity"):
        if eventcode == -2:
            if (piccinokills < 2):
                a "Huh? I think I hear voices... Headhunters!"
            elif (piccinokills <= 3):
                a "More targets."
            elif (piccinokills == 4):
                chiave "You're... you're hunting them down, aren't you?"

                a "They're practice. The Laterans will be a lot harder than these mooks."

                chiave "{size=20}Lives aren't practice, man...{/size}"

                nvl clear

                nvl show dissolve

                "Your brutality seems to disturb Chiave."

                "He clearly doesn't understand how valuable this experience is for him, too."

                "{color=FF0000}Your heart shifts towards the path of a killer.{/color}"

                $ killer += 1
            else:
                a "More."

            hide screen buttons
            hide screen mini_map_scr

            python:
                enemyparty = []
                enemycount = renpy.random.randint(1, 7)
                for i in range(enemycount):
                    enemyparty.append(Operator(HEADHUNTER, renpy.random.randint(4, 8), False, [ Tech(4) ]))

            call Battle(party, enemyparty)

            $ piccinokills += 1

            call Crawl(piccinocity, y, x, piccinoknowledge, False)

        elif (eventcode == -3):
            a "Looks like someone left some cash here... I'll take it."

            nvl clear

            "Gained 10 Dosh!"

            $ cash += 10

            $ map[y][x] = 0

    elif (mapname == "piccinocityeast"):
        if eventcode == -2:
            if crawlMoveCommand == 'L':
                if (gatedown):
                    a "There's a gate here, but the gate's open. Guess I can just walk on through."

                elif (sawstation):
                    a "There's a closed gate here. I bet that station down South would open it up."

                    $ x += 1

                else:
                    a "There's a closed gate here. Maybe there's a lever somewhere that would open it."

                    $ x += 1

        elif eventcode == -3:
            if (gatedown):
                a "There's a guard station with a lever here. The lever is off."
            else:
                a "There's a guard station with a lever here. Looks like the lever is on, right now."

                a "Should I flip it?"

                menu:
                    "Flip it.":
                        $ gatedown = True

                        who "Hey! You there, stop!"

                        $ censor(a, "Damn, I was spotted...")

                        hide screen buttons
                        hide screen mini_map_scr

                        python:
                            enemyparty = [Operator(SKULLHUNTER, 7, False, [ Tech(4) ])]

                        call Battle(party, enemyparty)

                        if (headhunterspared):
                            show headhunter at midright with dissolve

                            headhunter "Huh, that guy... I think I might be able to copy some of his fancy knife tricks."

                            a "Go ahead."

                            headhunter "...Yeah, I'll have to look into that. Maybe when I've got a bit more experience."

                            hide headhunter with dissolve

                        call Crawl(piccinocityeast, y, x, piccinoknowledgeeast, False)

                    "Don't.":
                        a "A little more information wouldn't hurt."

                        $ y -= 1

            $ sawstation = True
