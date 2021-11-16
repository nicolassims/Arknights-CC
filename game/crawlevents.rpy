label CrawlEvent(map, eventcode):
    if (map == "guerroforest"):
        if eventcode == -2:
            show forest behind ace with dissolve

            a "This place can actually look kinda pretty. When it's not covered in burnt shit, anyway."

        elif type == -3 and crawlMoveCommand == 'R':
            hide forest with dissolve

    elif (map == "piccinocity"):
        if eventcode == -2:
            a "Huh? I think I hear voices... Headhunters!"

            hide screen buttons
            hide screen mini_map_scr

            python:
                enemyparty = []
                enemycount = renpy.random.randint(1, 7)
                for i in range(enemycount):
                    enemyparty.append(Operator(HEADHUNTER, renpy.random.randint(4, 8), False, [ Tech(4) ]))

            call Battle(party, enemyparty)

            call Crawl(piccinocity, y, x, piccinoknowledge, False)
