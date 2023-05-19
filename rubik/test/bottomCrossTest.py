'''
Created on Mar 23, 2023

@author: Jarrett
'''

import unittest
import rubik.model.cube as Cube
import rubik.controller.bottomCross as bottomCross


class bottomCrossTest(unittest.TestCase):

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
#            test 010:    solved cube
#            test 020:    unsolved cube, solved bottom cross
#            test 030:    find edges of down cross, unsolved cube
#            test 040:    find edge mates of down cross, unsolved cube
#            test 050:    find out of place edges that need to be solved
#            test 060:    solve cube with out of place tile on Up face.
#            test 070:    solve cube with out of place tile on Front face.
#            test 080:    solve cube with out of place tile on Right Face.
#            test 090:    solve cube with out of place tile on Back Face.
#            test 100:    solve cube with out of place tile on Left Face.
#            test 110:    solve cube with out of place tile on Down Face.
#            test 120:    solve completely scrambled cube.
#
#        sad path:
#            test 910:    invalid cube - should be caught by cube.py
#            test 920:    empty cube.
#        
#        evil path: 
#            none
#
#
#

    def test010_bottomCross_solvedCube(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = Cube.Cube(cube)
        expectedRotations = ''
        
        actualRotations = bottomCross.solveBottomCross(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)        
        
    def test020_bottomCross_unsolvedCube_solvedBottomCross(self):
        cube = 'bybgboobywbygrorryrbwygyogbgbogorwogrrgoyyyrrwwbwwwowg'
        theCube = Cube.Cube(cube)
        expectedRotations = ''
        
        actualRotations = bottomCross.solveBottomCross(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)    
        
    def test030_bottomCross_unsolvedCross_findEdges(self):
        cube = 'gwygbbrbrbrgyrbyygoowroboywowyggogobrrwgyybrrwwowwgboy'
        
        expectedEdges = [1, 28, 46, 48]
        
        actualEdges = bottomCross._findEdges(cube)

        self.assertEqual(expectedEdges, actualEdges)   
    
    def test040_bottomCross_unsolvedCross_findEdgeMate(self):
        cube = 'gwygbbrbrbrgyrbyygoowroboywowyggogobrrwgyybrrwwowwgboy'
        
        expectedMates = ['r', 'g', 'b', 'o']
        
        edges = bottomCross._findEdges(cube)
        
        actualMates = []
        
        for eachEdge in edges:
            mate = bottomCross._findEdgeMate(eachEdge, cube)
            actualMates.append(mate)
        
        self.assertEqual(expectedMates, actualMates) 
        
    def test050_bottomCross_findTileToSolve(self):
        cube = 'bogobggbrygorrowrbyybygyyggororogwowwbgwyyybrowbwwbrwr'
        cubeTwo = 'gogybgbbrygorrowrbyygygoygbwowgororoobgwyyrbrwwbwwbywr'
        cubeScrambled = 'bgbwbyrggygrorbywogywwgbwbrboyroowrwobygyrrwogyoywrbog'
        cubeSolved = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        
        expectedEdges = 39
        expectedEdgesTwo = 39
        expectedEdgesScrambled = 3
        expectedEdgesSolved = -1
        
        actualEdges = bottomCross._findTileToSolve(cube)
        actualEdgesTwo = bottomCross._findTileToSolve(cubeTwo)
        actualEdgesScrambled = bottomCross._findTileToSolve(cubeScrambled)
        actualEdgesSolved = bottomCross._findTileToSolve(cubeSolved)
        
        self.assertEqual(expectedEdges, actualEdges)
        self.assertEqual(expectedEdgesTwo, actualEdgesTwo)
        self.assertEqual(expectedEdgesScrambled, actualEdgesScrambled)
        self.assertEqual(expectedEdgesSolved, actualEdgesSolved)
        
    def test060_bottomCross_outOfPlaceUpTile(self):
        cube = 'bogobggbrygorrowrbyybygyyggororogwowwbgwyyybrowbwwbrwr'
        cubeTwo = 'ygoobggbryybrrowrboroygyyggbogrogwowywwbybrygowbwwbrwr'
        cubeThree = 'ggoybgobryybrrowrborgygoygywowgorgobowwwybrygywbbwbrwr'
        
        theCube = Cube.Cube(cube)
        theCubeTwo = Cube.Cube(cubeTwo)
        theCubeThree = Cube.Cube(cubeThree)
        
        expectedRotations = 'UURR'
        expectedRotationsTwo = 'URR'
        expectedRotationsThree = 'URRuLL'
         
        actualRotations = bottomCross.solveBottomCross(theCube)
        actualRotationsTwo = bottomCross.solveBottomCross(theCubeTwo)
        actualRotationsThree = bottomCross.solveBottomCross(theCubeThree)
         
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedRotationsTwo, actualRotationsTwo)
        self.assertEqual(expectedRotationsThree, actualRotationsThree)
        
    
    def test070_bottomCross_outOfPlaceFrontTile(self):
        cube = 'wwrobbobbyyrorrorrbrrggggggggoooyooyyywyybbbbgrywwwwww'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'ULfl'
        
        actualRotations = bottomCross.solveBottomCross(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test080_bottomCross_outOfPlaceRightTile(self):
        cube = 'wobgbrgbowwwyrogrygrobggrggbyoooyooyybrbyrbyrrwywwgwwb'
        cubeTwo = 'brybbgrbybwyyrrbrrgyoggggggworooroogbboyybwyryoowwwwww'
        
        theCube = Cube.Cube(cube)
        theCubeTwo = Cube.Cube(cubeTwo)
        
        expectedRotations = 'UFrf'
        expectedRotationsTwo = 'rFR'
        
        actualRotations = bottomCross.solveBottomCross(theCube)
        actualRotationsTwo = bottomCross.solveBottomCross(theCubeTwo)
        
        
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedRotationsTwo, actualRotationsTwo)
    
    def test090_bottomCross_outOfPlaceBackTile(self):
        cube = 'obrgbbybygorrrrbrrywwggyggwbbwroybogogbyyygoyowowwwrow'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations ='BLUlBB'
        
        actualRotations = bottomCross.solveBottomCross(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test100_bottomCross_outOfPlaceLeftTile(self):
        cube = 'ybbgbowbwogwyryrrgoyrggbygygwroooboryrgbyrbywbrgwwwowo'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations ='Lfl'
        
        actualRotations = bottomCross.solveBottomCross(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
        
    def test110_bottomCross_outOfPlaceDownTile(self):
        cube = 'goobbbwrgwgrorowbrgybgggwgbyyyyoryooorybyroybgwrwwwrwb'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations ='FFuRRUff'
        
        actualRotations = bottomCross.solveBottomCross(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test120_bottomCross_unsolvedCube_scrambled(self):
        cube = 'worrbbogrbgyyrgyrwboyrgrrgygwoyowbbgoyroyobbwwwgwwboyg'
        
        theCube = Cube.Cube(cube)
        self.maxDiff = None
        
        expectedRotations = 'LFUfLLluLFFuFrFFFUlbLBB'
        
        actualRotations = bottomCross.solveBottomCross(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test130_bottomCross_unsolvedCube_solvedCubeUnsolvedBottom(self):
        cube = 'bbbbbbooorrrrrrbbbggggggrrroooooogggyyyyyyyyywwwwwwwww'
        
        theCube = Cube.Cube(cube)
        
        expectedRotations = 'FFULLuffFFUUBBuuffFFuRRUff'
        
        actualRotations = bottomCross.solveBottomCross(theCube)
        
        self.assertEqual(expectedRotations, actualRotations)
        
#        Sad Path:
    
    def test910_bottomCross_invalidCube(self):
        cube = '12345676lajkhbf'
        
        theCube = Cube.Cube(cube)
        
        expectedResult = 'error: invalid cube'
        
        actualResult = bottomCross.solveBottomCross(theCube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test920_bottomCross_emptyCube(self):
        cube = ''
        
        theCube = Cube.Cube(cube)
        
        expectedResult = 'error: invalid cube'
        
        actualResult = bottomCross.solveBottomCross(theCube)
        
        self.assertEqual(expectedResult, actualResult)
        
        
        
        
        
        
