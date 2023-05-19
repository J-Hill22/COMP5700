'''
Created on Apr 15, 2023

@author: Jarrett
'''
import unittest
import rubik.model.cube as Cube
import rubik.controller.middleLayer as middleLayer


class middleLayerTest(unittest.TestCase):
# Analysis of solveMiddleLayer
#        
#    solveMiddleLayer:    method, takes in an instantiated cube and returns a string of rotations 
#                            required to solve the middle layer of the cube (assuming downFaceCross
#                            and bottomLayer are already solved)
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
#            test 020:    unsolved cube, solved middle
#            test 030:    find all tiles of middle layer, unsolved cube
#            test 040:    find edge mates of middle layer, unsolved cube
#            test 050:    find tiles that need to be solved on middle layer
#            test 060:    solve cube with out of place tile on top row of Front face.
#            test 070:    solve cube with out of place tile on top row of back face.
#            test 080:    move a tile on middle row to top row to be solved by any face.
#            test 090:    solve tile with front or back tile on the up face of cube.
#            test 100:    solve completely scrambled cube.
#
#        Sad path:
#            test 910:    invalid cube - should be caught by cube.py
#            test 920:    empty cube.
#

#        Happy Path:


    def test010_middleLayer_solvedCube(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        expectedRotations = ''
        
        actualRotations = middleLayer.solveMiddleLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test020_middleLayer_unsolvedCube_solvedBottomAndMiddleLayer(self):
        cube = 'gggbbbbbbooorrrrrrbbbggggggrrrooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        expectedRotations = ''
        
        actualRotations = middleLayer.solveMiddleLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test030_middleLayer_unsolvedCube_findAllTiles(self):
        cube = 'gggbbbbbbooorrrrrrbbbggggggrrrooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedTiles = [3, 5, 19]
        expectedTilesTwo = [12, 14, 28]
        expectedTilesThree = [1, 21, 23]
        expectedTilesFour = [10, 30, 32]
        
        actualTiles = middleLayer._findAllTiles(theCube, 'F')
        actualTilesTwo = middleLayer._findAllTiles(theCube, 'R')
        actualTilesThree = middleLayer._findAllTiles(theCube, 'B')
        actualTilesFour = middleLayer._findAllTiles(theCube, 'L')
        
        
        self.assertEqual(expectedTiles, actualTiles)
        self.assertEqual(expectedTilesTwo, actualTilesTwo)
        self.assertEqual(expectedTilesThree, actualTilesThree)
        self.assertEqual(expectedTilesFour, actualTilesFour)
        
    def test040_middleLayer_unsolvedCube_findEdgeMates(self):
        cube = 'ybygbrbbbrybgrorrrroobgygggbroboyoooygyyyogrgwwwwwwwww'
        theCube = Cube.Cube(cube)
        
        keyTilesFront = middleLayer._findAllTiles(theCube, 'F') #[1, 21, 30]
        keyTilesRight = middleLayer._findAllTiles(theCube, 'R') #[5, 28, 43]
        keyTilesBack = middleLayer._findAllTiles(theCube, 'B') #[3, 12, 37]
        keyTilesLeft = middleLayer._findAllTiles(theCube, 'L') #[14, 19, 41]
        
        expectedMatesFront = ['r', 'o', 'y']
        expectedMatesRight = ['g', 'y', 'b']
        expectedMatesBack = ['y', 'r', 'o']
        expectedMatesLeft = ['b', 'g', 'y']
        
        actualMatesFront = middleLayer._findEdgeMates(keyTilesFront, theCube)
        actualMatesRight = middleLayer._findEdgeMates(keyTilesRight, theCube)
        actualMatesBack = middleLayer._findEdgeMates(keyTilesBack, theCube)
        actualMatesLeft = middleLayer._findEdgeMates(keyTilesLeft, theCube)
        
        self.assertEqual(expectedMatesFront, actualMatesFront)
        self.assertEqual(expectedMatesRight, actualMatesRight)
        self.assertEqual(expectedMatesBack, actualMatesBack)
        self.assertEqual(expectedMatesLeft, actualMatesLeft)
        
    def test050_middleLayer_unsolvedCube_findTilesToSolve(self):
        cube = 'ybygbrbbbrybgrorrrroobgygggbroboyoooygyyyogrgwwwwwwwww'
        theCube = Cube.Cube(cube)
        
        allKeyTilesFront = middleLayer._findAllTiles(theCube, 'F')
        edgeMatesFront = middleLayer._findEdgeMates(allKeyTilesFront, theCube)
        
        allKeyTilesBack = middleLayer._findAllTiles(theCube, 'B')
        edgeMatesBack = middleLayer._findEdgeMates(allKeyTilesBack, theCube)
        
        allKeyTiles = allKeyTilesFront + allKeyTilesBack #[1, 21, 30, 3, 12, 37]
        allEdgeMates = edgeMatesFront + edgeMatesBack   #[r, o, y, y, r, o]
        allEdges = dict(zip(allKeyTiles, allEdgeMates))
        
        
        tilesToSolve = middleLayer._findTileToSolve(allEdges, theCube)
        
        expectedTiles = {1: 'r'} #{1, 21, 12, 37 : 'r', 'o', 'r', 'o'}
        
        self.assertEqual(expectedTiles, tilesToSolve)
        
    def test060_middleLayer_unsolvedCube_solveFrontFaceTile(self):
        cube = 'ybygbrbbbrybgrorrrroobgygggbroboyoooygyyyogrgwwwwwwwww'
        theCube = Cube.Cube(cube)
        
        allKeyTilesFront = middleLayer._findAllTiles(theCube, 'F')
        edgeMatesFront = middleLayer._findEdgeMates(allKeyTilesFront, theCube)
        
        allEdges = dict(zip(allKeyTilesFront, edgeMatesFront)) 
        
        tileToSolve = middleLayer._findTileToSolve(allEdges, theCube)
        
        actualRotations = middleLayer._solveFrontFaceTile(tileToSolve, theCube)
        expectedRotations = 'URUrufuF'
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test070_middleLayer_unsolvedCube_solveBackFaceTile(self):
        cube = 'ygoobgbbbbbyyrbrrrrybogogggryogoyoooybgryrgrywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        allKeyTilesBack = middleLayer._findAllTiles(theCube, 'B')
        edgeMatesBack = middleLayer._findEdgeMates(allKeyTilesBack, theCube)
        
        allEdges = dict(zip(allKeyTilesBack, edgeMatesBack))
        
        tileToSolve = middleLayer._findTileToSolve(allEdges, theCube)
        
        actualRotations = middleLayer._solveBackFaceTile(tileToSolve, theCube)
        expectedRotations = 'UUuruRUBUb'
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test080_middleLayer_unsolvedCube_moveMiddleTileToTop(self):
        cube = 'rrobbobbbbbygryrrrgygggggggybbroroooroooyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        allKeyTilesFront = middleLayer._findAllTiles(theCube, 'F')
        edgeMatesFront = middleLayer._findEdgeMates(allKeyTilesFront, theCube)
        
        allKeyTilesBack = middleLayer._findAllTiles(theCube, 'B')
        edgeMatesBack = middleLayer._findEdgeMates(allKeyTilesBack, theCube)
        
        allEdgesFront = dict(zip(allKeyTilesFront, edgeMatesFront))
        allEdgesBack = dict(zip(allKeyTilesBack, edgeMatesBack))
        
        tileToSolveFront = middleLayer._findTileToSolve(allEdgesFront, theCube)
        tileToSolveBack = middleLayer._findTileToSolve(allEdgesBack, theCube)
        
        actualRotationsFront = middleLayer._solveFrontFaceTile(tileToSolveFront, theCube)
        expectedRotationsFront = 'FUfuluLU'
        
        actualRotationsBack = middleLayer._solveBackFaceTile(tileToSolveBack, theCube)
        expectedRotationsBack = 'RUrufuFU'
        
        self.assertEqual(expectedRotationsFront, actualRotationsFront)
        self.assertEqual(expectedRotationsBack, actualRotationsBack)
        
    def test090_middleLayer_unsolvedCube_solveTileOnUpFace(self):
        cube = 'grobbbbbbbyyrryrrrbbyggggggrryoooooogyryyoogywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        allKeyTilesUp = middleLayer._findAllTiles(theCube, 'B')
        edgeMatesUp = middleLayer._findEdgeMates(allKeyTilesUp, theCube)
        
        allEdgesUp = dict(zip(allKeyTilesUp, edgeMatesUp))
        
        tileToSolveUp = middleLayer._findTileToSolve(allEdgesUp, theCube)
        
        actualRotationsRight = middleLayer._solveTileOnUpFace(tileToSolveUp, theCube)
        expectedRotationsRight = 'uUBUburuR'
        
        self.assertEqual(expectedRotationsRight, actualRotationsRight)
        
    def test100_middleLayer_unsolvedCube_solveMiddleLayer(self):
        cube = 'rrobbobbbbbygryrrrgygggggggybbroroooroooyyyyywwwwwwwww'
        cubeTwo = 'grrobybbbyrybrrrrroygbgygggyoygobooorobgyyogbwwwwwwwww'
        theCube = Cube.Cube(cube)
        theCubeTwo = Cube.Cube(cubeTwo)
        
        self.maxDiff = None
        
        expectedRotations = 'FUfuluLUURUrufuFuuluLUFUfUUULUlubuBuUBUburuR'
        expectedRotationsTwo = 'luLUFUfuuuluLUFUfUBUburuRuURUrufuFUUubuBULUl'
        
        actualRotations = middleLayer.solveMiddleLayer(theCube)
        actualRotationsTwo = middleLayer.solveMiddleLayer(theCubeTwo)
        
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedRotationsTwo, actualRotationsTwo)
        
    def test910_middleLayer_invalidCube(self):
        cube = ';alksjdbf'
        
        theCube = Cube.Cube(cube)
        
        actualResult = middleLayer.solveMiddleLayer(theCube)
        
        expectedResult = 'error: invalid cube'
        
        self.assertEqual(expectedResult, actualResult)
        
    def test920_middleLayer_emptyCube(self):
        cube = ''
        
        theCube = Cube.Cube(cube)
        
        actualResult = middleLayer.solveMiddleLayer(theCube)
        
        expectedResult = 'error: invalid cube'
        
        self.assertEqual(expectedResult, actualResult)






















