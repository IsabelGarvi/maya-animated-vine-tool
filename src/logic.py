import sys

import maya.cmds as cmds


def selection_is_spline():
    selection = cmds.ls(selection=True)

    if len(selection) == 0:
        sys.stderr.write('You need to have something selected in the scene.')
    else:
        for object in selection:
            pass

