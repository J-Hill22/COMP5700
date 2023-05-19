'''
Created on Apr 13, 2023

@author: Jarrett
'''
import unittest
import rubik.model.cube as Cube
import rubik.controller.bottomLayer as bottomLayer
from test.test_set import cube
from rubik.controller.bottomCross import _findEdgeMate


class bottomLayerTest(unittest.TestCase):
# Analysis of solveBottomLayer
#        
#    solveBottomLayer:    method, takes in an instantiated cube and returns a string of rotations 
#                            required to solve the bottom layer of the cube (assuming downFaceCross
#                            is already solved)
#
#    inputs:
#        cube: 54 character long string representing cube to be solved.
#
#    outputs:
#        side-effects:    no external effects, internal state change
#        nominal:
#                return string representing moves required to solve bottom layer of cube.
#
#        abnormal:
#                return dict for ['status']: string, 'error: some error message here'
#
#
#         Happy path:
#            test 010:    solved cube
#            test 020:    unsolved cube, solved bottom cross
#            test 030:    find all tiles of bottom layer, unsolved cube
#            test 040:    find edge mates of bottom layer, unsolved cube
#            test 050:    find tiles that need to be solved on bottom layer (only for corners)
#            test 060:    move tiles that are in the bottom portion of the face to the top layer
#            test 070:    solve cube with out of place tile on top row of Front face.
#            test 075:    solve cube with out of place tile on bottom row of Front face.
#            test 080:    solve cube with out of place tile on top row of right face.
#            test 085:    solve cube with out of place tile on bottom row of right face.
#            test 090:    solve cube with out of place tile on top row of back face.
#            test 095:    solve cube with out of place tile on bottom row of back face.
#            test 100:    solve cube with out of place tile on top row of Left face.
#            test 105:    solve cube with out of place tile on bottom row of Left face.
#            test 110:    solve cube with out of place tile on top row of UP face.
#            test 120:    solve completely scrambled cube.
#            test 130:    solve cube with unsolved down face
#
#        Sad path:
#            test 910:    invalid cube - should be caught by cube.py
#            test 920:    empty cube.
#

#        Happy Path:


    def test010_bottomLayer_solvedCube(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        expectedRotations = ''
        
        actualRotations = bottomLayer.solveBottomLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations) 
        
    def test020_bottomLayer_unsolvedCubeSolvedBottomLayer(self):
        cube = 'oboobybbbbybgrrrrrryrggrggggggyoboooyoyoybyrywwwwwwwww'
        theCube = Cube.Cube(cube)
        expectedRotations = ''
        
        actualRotations = bottomLayer.solveBottomLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test030_bottomLayer_unsolvedBottom_findAllTiles(self):
        cube = 'bybgboobywbygrorryrbwygyogbgbogorwogrrgoyyyrrwwbwwwowg'
        theCube = Cube.Cube(cube)
        
        expectedTiles = [9, 20, 33, 45]
        
        actualTiles = bottomLayer._findAllTiles(theCube)
        
        self.assertEqual(expectedTiles, actualTiles)
        
    def test040_bottomLayer_unsolvedBottom_findEdgeMates(self):
        cube = 'bybgboobywbygrorryrbwygyogbgbogorwogrrgoyyyrrwwbwwwowg'
        theCube = Cube.Cube(cube)
        
        expectedMates = ['bo', 'br', 'gr', 'go']
        expectedStr = ''.join(expectedMates)
        expectedStrSorted = ''.join(sorted(expectedStr))
        
        allKeyTiles = bottomLayer._findAllTiles(theCube)
        actualMates = []
        for eachTile in allKeyTiles:
            edgeMates = bottomLayer._findEdgeMates(eachTile, theCube)
            actualMates.append(edgeMates)
        actualStr = ''.join(actualMates)
        actualStrSorted = ''.join(sorted(actualStr))
        
        self.assertEqual(expectedStrSorted, actualStrSorted)
        
    def test050_bottomLayer_unsolvedBottom_findTileToSolve(self):
        cube = 'bybgboobywbygrorryrbwygyogbgbogorwogrrgoyyyrrwwbwwwowg'
        cubeTwo = 'bbbbbbrrrrrrrrrgggggggggooooooooobbbyyyyyyyyywwwwwwwww'
        cubeThree = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        theCube = Cube.Cube(cube)
        theCubeTwo = Cube.Cube(cubeTwo)
        theCubeThree = Cube.Cube(cubeThree)
        
        expectedTile = 9
        expectedTileTwo = 45
        expectedTileThree = -1
        
        actualTile = bottomLayer._findTileToSolve(theCube)
        actualTileTwo = bottomLayer._findTileToSolve(theCubeTwo)
        actualTileThree = bottomLayer._findTileToSolve(theCubeThree)
        
        self.assertEqual(expectedTile, actualTile)
        self.assertEqual(expectedTileTwo, actualTileTwo)
        self.assertEqual(expectedTileThree, actualTileThree)
        
    def test060_bottomLayer_unsolvedBottom_moveToTop(self):
        cube = 'rbgybbwbboybrrrrrryorggggggggbooroobyyoyybyoyowwwwwwww'
        
        theCube = Cube.Cube(cube)
        
        tile = bottomLayer._findTileToSolve(theCube)
        
        
        expectedRotations = 'lUL'
        
        actualRotations = bottomLayer._moveToTop(tile, 'F')
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test070_bottomLayer_unsolvedBottom_solveOutOfPlaceFrontTileOnTopRow(self):
        cube = 'oowrbbybbbbyrrrrrrrbbggggggrggooyoooyygyyoyyobwwwwwwww'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'UluL'
        
        actualRotations = bottomLayer.solveBottomLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test075_bottomLayer_unsolvedBottom_solveOutOfPlaceFrontTileOnBottomRow(self):
        cube = 'rbgybbwbboybrrrrrryorggggggggbooroobyyoyybyoyowwwwwwww'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'lULFUf'
        
        actualRotations = bottomLayer.solveBottomLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test080_bottomLayer_unsolvedBottom_solveOutOfPlaceRightTileOnTopRow(self):
        cube = 'goobbybbbbbwgrryrrrrygggggggrrooooooobbyyyyyywwrwwwwww'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'UfuF'
        
        actualRotations = bottomLayer.solveBottomLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test085_bottomLayer_unsolvedBottom_solveOutOfPlaceRightTileOnBottomRow(self):
        cube = 'ogybbgbbbbrgrrrrrwyogyggrggobyooooooyyryybbyrwwwwwwwwg'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'BubruR'
        
        actualRotations = bottomLayer.solveBottomLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test090_bottomLayer_unsolvedBottom_solveOutOfPlaceBackTileOnTopRow(self):
        cube = 'yoobbbbbbbbrrryrrywggrggrggoggooooooyygryyryywwwwwwwwb'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'BUb'
        
        actualRotations = bottomLayer.solveBottomLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test095_bottomLayer_unsolvedBottom_solveOutOfPlaceBackTileOnBottomRow(self):
        cube = 'oobbbbbbbyrrrrrrrgybyyggwggrggoooooogybyygyyowwwwwwwwr'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'rURBUb'
        
        actualRotations = bottomLayer.solveBottomLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test100_bottomLayer_unsolvedBottom_solveOutOfPlaceLeftTileOnTopRow(self):
        cube = 'ooybbbbbbboorrrrrrbrrggygggggwbooyooyyyyyyggrwwwwwwoww'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'UbuB'
        
        actualRotations = bottomLayer.solveBottomLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test105_bottomLayer_unsolvedBottom_solveOutOfPlaceLeftTileOnBottomRow(self):
        cube = 'bbybbbobbrggrrrrrroobggggggyryooyoowoyyyyyrogbwwwwwwww'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'FufluL'
        
        actualRotations = bottomLayer.solveBottomLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test110_bottomLayer_unsolvedBottom_solveOutOfPlaceUpTile(self):
        cube = 'rrrobbobbgybrrrrrrogyggggggoobooyooybywbybyyygwwwwwwww'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'luLFUf'
        
        actualRotations = bottomLayer.solveBottomLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test120_bottomLayer_scrambledCube_solveCube(self):
        cube = 'orwgbygbbgyobrorrgworbgyogygbyoorrooygbrygbyrywwwwwbww'
        cubeTwo = 'ooogbbybrwgrorrwrggybbggwgbyywyooyogorybyrgybowbwwwrwr'
        cubeThree = 'rrgybgybgwyrrroyrwbybbggrgbyrboooworogwbybyyogwowwwowg'
        infCubeOne = 'ggwbbrbbygoryrobryybbggoggowyoyoygoorrbgybwrrwwowwwywr'
        
        self.maxDiff = None
        
        theCube = Cube.Cube(cube)
        theCubeTwo = Cube.Cube(cubeTwo)
        theCubeThree = Cube.Cube(cubeThree)
        theInfOne = Cube.Cube(infCubeOne)
        
        expectedRotations = 'UUFUfruRLUl'
        expectedRotationsTwo = 'UFUfufUFRUrubuBrURBUb'
        expectedRotationsThree = 'uBubruRbUBuFUfbUBuuRUrUULUlbuB'
        expectedRotationsInfOne = 'UURUruBUbUULUlbuB'
        
        actualRotations = bottomLayer.solveBottomLayer(theCube)
        actualRotationsTwo = bottomLayer.solveBottomLayer(theCubeTwo)
        actualRotationsThree = bottomLayer.solveBottomLayer(theCubeThree)
        actualRotationsInfOne = bottomLayer.solveBottomLayer(theInfOne)
        
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedRotationsTwo, actualRotationsTwo)
        self.assertEqual(expectedRotationsThree, actualRotationsThree)
        self.assertEqual(expectedRotationsInfOne, actualRotationsInfOne)
        
    def test130_bottomLayer_unsolvedBottom_solveCube(self):
        cube = 'bbbbbbooorrrrrrbbbggggggrrroooooogggyyyyyyyyywwwwwwwww'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'luLuuLUlruRuuRUrluL'
        
        actualRotations = bottomLayer.solveBottomLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
    
    def test910_bottomCross_invalidCube(self):
        cube = '12345676lajkhbf'
        
        theCube = Cube.Cube(cube)
        
        expectedResult = 'error: invalid cube'
        
        actualResult = bottomLayer.solveBottomLayer(theCube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test920_bottomCross_emptyCube(self):
        cube = ''
        
        theCube = Cube.Cube(cube)
        
        expectedResult = 'error: invalid cube'
        
        actualResult = bottomLayer.solveBottomLayer(theCube)
        
        self.assertEqual(expectedResult, actualResult)
    
    
    
    
    
    
    
    
    
    
    
    
    