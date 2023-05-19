'''
Created on April 7, 2023

@author: Jarrett
'''

import unittest
import rubik.controller.bottomCross as bottomCross


class bottomCrossTestTwo(unittest.TestCase):

# Analysis of bottomCross
#
#    solveBottomCross:  method, takes in an instantiated cube and returns a string of rotations
#                        required to transform the cube into the down-face cross.
#    
#        inputs:
#            cube: a 54 character string representing a cube to be solved.  
#            
#        outputs:
#            side-effects:    no external effects; internal state change
#            nominal:
#                return string representing moves required to transform cube into a down-face cross
#            abnormal:
#                return dict for ['status']: string, 'error: some error message here'
#
#        happy path:
#            test 010:    
#            test 020:    
#            test 030:    
#            test 040:    
#            test 050:    
#            test 060:    
#            test 070:    solve cube with out of place tile on Front face.
#            test 080:    
#            test 090:    
#
#        sad path:
#            test 910:    invalid cube - should be caught by cube.py
#        
#        evil path: 
#            none
#
#
#

    def test070_bottomCross_testingForFrozenModule(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedRotations = ''
        
        actualRotations = bottomCross.solveBottomCross(cube)
        
        self.assertEqual(expectedRotations, actualRotations)        
        

        