## FIX SLIDING MOCAP BONE v0.1 BY GUANHUA-VFX ##
## https://guanhua-vfx.format.com ##

#IMPORTANT: RUN SCRIPT ON FRAME BEFORE SLIDING STARTS# 

import maya.cmds

#create fix locator
cmds.spaceLocator(name="fixLoc")
cmds.scale (10,10,10, "fixLoc")

#FIND AND REPLACE "Character1_Hips" with Sliding Bone Name#

#parent constraint fix locator to sliding bone, unparent to get bone location before sliding
cmds.parentConstraint ("Character1_Hips","fixLoc")
cmds.parent ("fixLoc_parentConstraint1", removeObject= True)

#constraint sliding bone to locator to fix sliding
cmds.parentConstraint ("fixLoc","Character1_Hips", sr=["x","y","z"])

#set weight from current frame to "1", weight from previous frame to "0"
cmds.disconnectAttr ("Character1_Hips.blendParent1","pairBlend1.weight") 
cmds.select ("pairBlend1")
cmds.setKeyframe (v=1, at="weight")
currTime = cmds.currentTime(q=1)
cmds.select ("pairBlend1")
cmds.setKeyframe (v=0, at="weight",t=currTime-1)

##remember to Bake Animation after script and delete locator##