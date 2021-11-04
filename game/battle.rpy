label Battle(ops, otherOps):
    window hide#Ren'Py function that hides the built-in gui

    scene tactics with dissolve

    python:
        battlefield = [None, None, None, None, None, None, None, None, None]
        frontman = renpy.call_screen("setup")
        print(frontman)


    show screen battleui()

    pause(5.0)
