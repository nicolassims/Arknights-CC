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
