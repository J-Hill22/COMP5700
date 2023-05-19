'''
Created on Apr 21, 2023

@author: Jarrett
'''
import unittest
import rubik.model.cube as Cube
import rubik.controller.upperLayer as upperLayer

class upperLayerTest(unittest.TestCase):
    
# Analysis of solveUpperLayer
#        
#    solveUpFaceCross:    method, takes in an instantiated cube and returns a string of rotations 
#                            required to solve the upper layer of the cube 
#
#    inputs:
#        cube:    54 character long string representing cube to be solved.
#
#    outputs:
#        side-effects:    no external effects, internal state change
#        nominal:
#                return string representing moves required to solve upper layer of cube.
#
#        abnormal:
#                return dict for ['status']: string, 'error: invalid cube'
#
#
#         Happy path:
#            test 010:    check if upper layer is solved
#            test 015:    check if upper corners are solved
#            test 020:    find all corner tiles of upper layer, unsolved cube.
#            test 030:    resolve whether upper layer has matching corners solved on any face.
#            test 040:    if there are matching corners move them to the appropriate face.
#            test 045:    solve the upper layer corners
#            test 050:    resolve whether there is a fully solved face in the upper layer.
#            test 060:    solve a cube with an unsolved upper layer.
#
#        Sad path:
#            test 910:    solve invalid cube. should return 'error:...'
#            test 920:    solve empty cube. should return 'error:...'
#

#        Happy Path:

    def test010_upperLayer_solvedCube_solvedUpperLayerCheck(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedRotations = ''
        
        actualRotations = upperLayer.solveUpperLayer(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test015_upperLayer_unsolvedCubeSolvedCorners_solvedUpperCornersCheck(self):
        cube = 'bgbbbbbbbrrrrrrrrrgogggggggoboooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        cubeStr = theCube.get()
        
        expectedResult = True
        
        actualResult = upperLayer._solvedUpperCornersCheck(cubeStr)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test020_upperLayer_findCornersToSolve_unsolvedCube(self):
        cube = 'rrrbbbbbbgggrrrrrroooggggggbbbooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
         
        expectedTiles = {'b': [27, 29], 'r': [0, 2], 'g': [9, 11], 'o': [18, 20]} 
         
        actualTiles = upperLayer._findCornersToSolve(theCube)
         
        self.assertEqual(expectedTiles, actualTiles)
        
    def test030_upperLayer_checkForMatchingCorners(self):
        cube = 'rrrbbbbbbgggrrrrrroooggggggbbbooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        cornersToSolve = upperLayer._findCornersToSolve(theCube)
        
        expectedResult = {'F' : 'r'}
        
        actualResult = upperLayer._checkForMatchingCorners(cornersToSolve, theCube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test040_upperLayer_alignMatchingCorners(self):
        cube = 'rrrbbbbbbgggrrrrrroooggggggbbbooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        cornersToSolve = upperLayer._findCornersToSolve(theCube)
        matchingCorners = upperLayer._checkForMatchingCorners(cornersToSolve, theCube)
         
        expectedRotation = 'u'
        
        actualRotation = upperLayer._alignMatchingCorners(matchingCorners, theCube)
        
        self.assertEqual(expectedRotation, actualRotation)
        
    def test045_upperLayer_unsolvedCube_solveUpperCorners(self):
        cube = 'bbgbbbbbboorrrrrrrggbggggggrroooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'lURuLUrRUrURUUrubUFuBUfFUfUFUUf'
        
        actualRotations = upperLayer.solveUpperLayer(theCube)
        
        self.assertIn(expectedRotations, actualRotations)
        
        
        
    def test050_upperLayer_unsolvedCube_checkForSolvedFace(self):
        cube = 'bgbbbbbbbrorrrrrrrgbgggggggoroooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedResult = ''
        
        actualResult = upperLayer._checkForSolvedFace(theCube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test060_upperLayer_unsolvedCube_solveUpperLayer(self):
        cube = 'rrgbbbbbbogorrrrrrborgggggggbbooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'UUlURuLUrRUrURUUrBBUlRBBrLUBB'
        
        actualRotations = upperLayer.solveUpperLayer(theCube)
        
        self.assertIn(expectedRotations, actualRotations)
    
#    Sad Path:
        
    def test910_upperLayer_invalidCube(self):
        cube = 'STdSSTTssTdeed33desSsTeeTeSe3ds3333dds3sTTsSSe'
        theCube = Cube.Cube(cube)
        
        expectedResult = 'error: invalid cube'
        
        actualResult = upperLayer.solveUpperLayer(theCube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test920_upperLayer_emptyCube(self):
        cube = ''
        theCube = Cube.Cube(cube)
        
        expectedResult = 'error: invalid cube'
        
        actualResult = upperLayer.solveUpperLayer(theCube)
        
        self.assertEqual(expectedResult, actualResult)
        

        
        
        
        
        
        
        
        

