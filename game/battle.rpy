label Battle(ops, otherops):
    python:
        firstOp = ops[0]
        theirFirstOp = otherops[0]
        myMaxHP = 10
        theirMaxHP = 10
        myHP = 7
        theirHP = 3
        mostleft = 0
        mostright = 8
        battlefield = [firstOp, None, None, None, None, None, None, None, theirFirstOp]
    
    window hide#Ren'Py function that hides the built-in gui
    show screen battleui()
    
    pause(5.0)