'''
Created on Apr 19, 2023

@author: Jarrett
'''
import unittest
import rubik.model.cube as Cube
import rubik.controller.upFaceCross as upFaceCross


class upFaceCrossTest(unittest.TestCase):
# Analysis of solveUpFaceCross
#        
#    solveUpFaceCross:    method, takes in an instantiated cube and returns a string of rotations 
#                            required to solve the up face cross of the cube 
#
#    inputs:
#        cube:    54 character long string representing cube to be solved.
#
#    outputs:
#        side-effects:    no external effects, internal state change
#        nominal:
#                return string representing moves required to solve middle layer of cube.
#
#        abnormal:
#                return dict for ['status']: string, 'error: invalid cube'
#
#
#         Happy path:
#            test 010:    solved cube
#            test 020:    unsolved cube, solved up face cross
#            test 030:    find all tiles of up face cross, unsolved cube
#            test 040:    resolve whether up face cross is empty, in a line, or half solved.
#            test 050:    position up face, based on its configuration, to receive FURurf
#            test 060:    solve cube with an unsolved up face cross.
#
#        Sad path:
#            test 910:    invalid cube.
#            test 920:    empty cube.
#

#        Happy Path:

    def test010_upFaceCross_solvedCube(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedRotations = ''
        
        actualRotations = upFaceCross.solveUpCross(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)

    def test020_upFaceCross_unsolvedCube_solvedUpFaceCross(self):
        cube = 'bbbwbwbobyrwbroyrwgggbgbgrgyowrogyowryryyyoyorgrwwwogo'
        theCube = Cube.Cube(cube)
        
        expectedRotations = ''
        
        actualRotations = upFaceCross.solveUpCross(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test030_upFaceCross_unsolvedCube_findAllTiles(self):
        cube = 'yyrbbbbbbgbyrrrrrrgyoggggggborooooooygoyyybrywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedTiles = [1, 19, 39, 41]
        
        actualTiles = upFaceCross._findAllTiles(theCube)
        
        self.assertEqual(expectedTiles, actualTiles)
        
    def test040_upFaceCross_unsolvedCube_determineUpConfiguration(self):
        cube = 'yyrbbbbbbgbyrrrrrrgyoggggggborooooooygoyyybrywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedResult = 'WE'
        
        allKeyTiles = upFaceCross._findAllTiles(theCube)
        
        actualResult = upFaceCross._determineUpConfiguration(allKeyTiles)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test050_upFaceCross_unsolvedCube_prepForFURurf(self):
        cube = 'yyrbbbbbbgbyrrrrrrgyoggggggborooooooygoyyybrywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'U'
        
        allKeyTiles = upFaceCross._findAllTiles(theCube)
        configuration = upFaceCross._determineUpConfiguration(allKeyTiles)
        
        actualRotations = upFaceCross._prepForFURurf(configuration)
        
        self.assertEqual(expectedRotations, actualRotations)
    
    def test060_upFaceCross_unsolvedCube_solveCube(self):
        cube = 'yyrbbbbbbgbyrrrrrrgyoggggggborooooooygoyyybrywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'UFURurfUUFURurf'
        
        actualRotations = upFaceCross.solveUpCross(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test910_upFaceCross_invalidCube_tooManyFaces(self):
        cube = 'bbbbbbbfbrrrrrrrrrgggggvmggoooooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedResult = 'error: invalid cube'
        
        actualResult = upFaceCross.solveUpCross(theCube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test920_upFaceCross_invalidCube_emptyCube(self):
        cube = ''
        theCube = Cube.Cube(cube)
        
        expectedResult = 'error: invalid cube'
        
        actualResult = upFaceCross.solveUpCross(theCube)
        
        self.assertEqual(expectedResult, actualResult)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

