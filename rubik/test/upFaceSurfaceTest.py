'''
Created on Apr 19, 2023

@author: Jarrett
'''
import unittest
import rubik.model.cube as Cube
import rubik.controller.upFaceSurface as upFaceSurface


class upperSurfaceTest(unittest.TestCase):
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
#                return string representing moves required to solve up face cross of cube.
#
#        abnormal:
#                return dict for ['status']: string, 'error: invalid cube'
#
#
#         Happy path:
#            test 010:    solved cube
#            test 020:    unsolved cube, solved up face surface
#            test 030:    find all tiles of up face corners, unsolved cube
#            test 040:    resolve whether upper surface is in a fish configuration or not.
#            test 050:    if not a fish then move an up face tile into LTR then RUrURUUr.
#            test 060:    if yes it is a fish, position fish into lower left corner.
#            test 070:    solve cube with an unsolved up face.
#
#        Sad path:
#            test 910:    solve invalid cube. should return 'error:...'
#            test 920:    solve empty cube. should return 'error:...'
#

#        Happy Path:

    def test010_upFaceSurface_solvedCube(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedRotations = ''
        
        actualRotations = upFaceSurface.solveUpSurface(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test020_upFaceSurface_unsolvedCube_solvedUpperSurface(self):
        cube = 'bbgbbbbbborbrrrrrrrgrgggggggooooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedRotations = ''
        
        actualRotations = upFaceSurface.solveUpSurface(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test030_upFaceSurface_unsolvedCube_findAllTiles(self):
        cube = 'brrbbbbbbygrrrrrrrgbygggggggoooooooooyyyyyyybwwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedTiles = [9, 20, 38, 42]
        
        actualTiles = upFaceSurface._findAllTiles(theCube)
        
        self.assertEqual(expectedTiles, actualTiles)
        
    def test040_upFaceSurface_unsolvedCube_isFish(self):
        cube = 'ooybbbbbbogyrrrrrrbbyggggggrrgoooooogyryyyyybwwwwwwwww'
        cubeTwo = 'yrybbbbbbooorrrrrrygyggggggrbroooooogygyyybybwwwwwwwww'
        
        theCube = Cube.Cube(cube)
        theCubeTwo = Cube.Cube(cubeTwo)
        
        allKeyTiles = upFaceSurface._findAllTiles(theCube)
        allKeyTilesTwo = upFaceSurface._findAllTiles(theCubeTwo)
        
        expectedResult = True
        expectedResultTwo = False
        
        actualResult = upFaceSurface._isFish(allKeyTiles)
        actualResultTwo = upFaceSurface._isFish(allKeyTilesTwo)
        
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual(expectedResultTwo, actualResultTwo)
        
    def test050_upFaceSurface_unsolvedCube_notAFish(self):
        cube = 'yrybbbbbbooorrrrrrygyggggggrbroooooogygyyybybwwwwwwwww'
        theCube = Cube.Cube(cube)
        
        allKeyTiles = upFaceSurface._findAllTiles(theCube)
        
        expectedRotations = 'U'
        
        actualRotations = upFaceSurface._notAFish(allKeyTiles)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test060_upperSurface_unsolvedCube_yesAFish(self):
        cube = 'ygrbbbbbbgbyrrrrrrgooggggggbrrooooooyyoyyybyywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        allKeyTiles = upFaceSurface._findAllTiles(theCube)
        
        expectedRotations = 'u'
        
        actualRotations = upFaceSurface._yesAFish(allKeyTiles)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test070_upperSurface_unsolvedCube_solveCube(self):
        cube = 'ygrbbbbbbgbyrrrrrrgooggggggbrrooooooyyoyyybyywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'UURUrURUUrRUrURUUrRUrURUUr'
        
        actualRotations = upFaceSurface.solveUpSurface(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test910_upperSurface_invalidCube(self):
        cube = 'STdSSTTssTdeed33desSsTeeTeSe3ds3333dds3sTTsSSe'
        theCube = Cube.Cube(cube)
        
        expectedResult = 'error: invalid cube'
        
        actualResult = upFaceSurface.solveUpSurface(theCube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test920_upperSurface_missingCube(self):
        cube = ''
        theCube = Cube.Cube(cube)
        
        expectedResult = 'error: invalid cube'
        
        actualResult = upFaceSurface.solveUpSurface(theCube)
        
        self.assertEqual(expectedResult, actualResult)
        
        
        
        

