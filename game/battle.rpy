label Battle(ops, otherOps):
    window hide#Ren'Py function that hides the built-in gui

    scene tactics with dissolve

    python:
        battlefield = [None, None, None, None, None, None, None, None, None]

        renpy.show_screen("frontman")
        first = renpy.call_screen("setup")


    #show screen battleui()
    #show screen frontman()

    pause(5.0)
