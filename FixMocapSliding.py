## FIX SLIDING MOCAP BONE v0.1 BY GUANHUA-VFX ##
## https://guanhua-vfx.format.com ##

#IMPORTANT: RUN SCRIPT ON FRAME BEFORE SLIDING STARTS# 

import maya.cmds

#get selected sliding bone
selectedJoint = cmds.ls(sl=True)
cmds.select(clear=True)

#create fix locator and assign to variable
fixLoc = cmds.spaceLocator(name="fixLoc")

#scale locator's shape instead of transform (Safer)
fixLocShape = cmds.listRelatives(fixLoc)
cmds.setAttr('%s.localScaleX'%fixLocShape[0], 10)
cmds.setAttr('%s.localScaleY'%fixLocShape[0], 10)
cmds.setAttr('%s.localScaleZ'%fixLocShape[0], 10)

#parent constraint fix locator to sliding bone, unparent to get bone location before sliding
constraintTemp = cmds.parentConstraint(selectedJoint[0], fixLoc)
cmds.delete(constraintTemp)

#constraint sliding bone to locator to fix sliding
cmds.parentConstraint (fixLoc, selectedJoint[0], sr=["x","y","z"])

#set weight from current frame to "1", weight from previous frame to "0"
cmds.disconnectAttr ("%s.blendParent1"%selectedJoint[0],"pairBlend1.weight") 
cmds.select ("pairBlend1")
cmds.setKeyframe (v=1, at="weight")
currTime = cmds.currentTime(q=1)
cmds.select ("pairBlend1")
cmds.setKeyframe (v=0, at="weight",t=currTime-1)

##remember to Bake Animation after script and delete locator##
