'''
Created on Feb 2, 2023

@author: Jarrett
'''
import unittest 
import rubik.model.cube as cube


class CubeTest(unittest.TestCase):

# Analysis of Cube
#
#    Cube:    class, instance of a state machine, maintain internal state
#    Methods:    __init__    constructs cube from a serialized string 
#                get         yields serialized string of internal representation
#                rotate      performs rotations on the cube per the 'dir' key
#
#    Analysis of Cube.rotate
#        inputs:
#            directions: string, len .GE. 0, [FfRrBbLlUu]; optional, defaulting to F if missing;
#                        unvalidated
#        outputs:
#            side-effects:    no external effects; internal state change
#            nominal:
#                return serialized rotated cube
#            abnormal:
#                raise DirException
#
#        happy path:
#            test 010:    F rotation
#            test 020:    f rotation
#            test 030:    R rotation
#            test 040:    r rotation
#            test 050:    B rotation
#            test 060:    b rotation
#            test 070:    L rotation
#            test 080:    l rotation
#            test 090:    U rotation
#            test 100:    u rotation
#            test 110:    missing direction
#            test 120:    empty direction ""
#            test 130:    multi-string rotation
#            test 140:    right trigger test
#            test 150:    left trigger test
#            test 160:    modified right trigger test
#            test 170:    modified left trigger test
#            test 180:    FURurf test
#            test 190:    RUrURUUr test
#            test 200:    lURuLUr test
#            test 210:    modified RUrURUUr test
#            test 220:    modified FFUrLFFlRUFF test
#
#        sad path:
#            test 910:    invalid direction
#            test 920:    Invalid cube.
#            test 930:    empty cube.
#            test 950:    invalid cube. >9 tiles of one face
#        
#        evil path: 
#            none
#
#
#
#
#    Happy path:

    def test_rotate_010ShouldRotateCubeInFDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo' 
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F')
        self.assertEqual(rotatedCube, 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo')

    def test_rotate_020ShouldRotateCubeInfDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo' 
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('f')
        self.assertEqual(rotatedCube, 'rgggbgywyyoboryorwobrggrgwywywyowbbbgwwbyybrrrrgowbooo')
        
    def test_rotate_030ShouldRotateCubeInRDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo' 
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('R')
        self.assertEqual(rotatedCube, 'ygywbbygorrbrrowybwbrygrwwywyryorbbggwrbygbwgoogowgooo')
        
    def test_rotate_040ShouldRotateCubeInrDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo' 
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('r')
        self.assertEqual(rotatedCube, 'ygwwbyygwbyworrbrrobrbgrywywyryorbbggwgbygbwooorowgoog')
        
    def test_rotate_050ShouldRotateCubeInBDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo' 
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('B')
        self.assertEqual(rotatedCube, 'ygrwbgyggboorrorroggowgbyrrwyrworgbgbywbyybwwooyowbwyb')
    
    def test_rotate_060ShouldRotateCubeInbDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo' 
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('b')
        self.assertEqual(rotatedCube, 'ygrwbgyggbogrrwrrwrrybgwoggoyroorobgbywbyybwwooyowbwyb')
        
    def test_rotate_070ShouldRotateCubeInLDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo' 
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('L')
        self.assertEqual(rotatedCube, 'ggrbbgbggbobrryrrwoboggogwobywboygrrywwryyrwwyoywwbyoo')
        
    def test_rotate_080ShouldRotateCubeInlDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo' 
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('l')
        self.assertEqual(rotatedCube, 'ogrobgoggbobrryrrwobbggbgwgrrgyobwybywwwyyywwyoyrwbroo')
        
    def test_rotate_090ShouldRotateCubeInUDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo' 
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('U')
        self.assertEqual(rotatedCube, 'bobwbgyggobrrryrrwwyrggrgwyygryorbbgbbgwywwywooyowbooo')
    
    def test_rotate_100ShouldRotateCubeInuDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo' 
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('u')
        self.assertEqual(rotatedCube, 'wyrwbgyggygrrryrrwbobggrgwyobryorbbgwywwywgbbooyowbooo')
        
    def test_rotate_110ShouldRotateCubeInMissingDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo' 
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate()
        self.assertEqual(rotatedCube, 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo')
        
    def test_rotate_120ShouldRotateCubeInEmptyDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo' 
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('')
        self.assertEqual(rotatedCube, 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo')
        
    def test_rotate_130ShouldRotateCubeInMultipleDirections(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo' 
        theCubeTwo = cube.Cube(cubeToRotate)
        rotatedCubeTwo = theCubeTwo.rotate('FRBLU')
        self.assertEqual(rotatedCubeTwo, 'wwobbbggowywrrowyogwywgoyrrbwbboyyoorbrryorgbyrggwggyb') 
        
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('FfRrBbLlUu')
        self.assertEqual(rotatedCube, 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo')  
        
    def test_rotate_140RightTriggerTest(self):
        cubeToRotate = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'  
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rightTrigger('L')
        
        self.assertEqual(rotatedCube, 'FUf')
        
    def test_rotate_150LeftTriggerTest(self):
        cubeToRotate = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'  
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.leftTrigger('F')
        
        self.assertEqual(rotatedCube, 'luL')
        
    def test_rotate_160ModRightTriggerTest(self):
        cubeToRotate = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.modRightTrigger('F')
        
        self.assertEqual(rotatedCube, 'URUr')
        
    def test_rotate_170ModLeftTriggerTest(self):
        cubeToRotate = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.modLeftTrigger('F')
        
        self.assertEqual(rotatedCube, 'uluL')
        
    def test_rotate_180FURurfTest(self):
        cubeToRotate = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.FURurf()
        
        self.assertEqual(rotatedCube, 'FURurf')
        
    def test_rotate_190RUrURUUrTest(self):
        cubeToRotate = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.RUrURUUr()
        
        self.assertEqual(rotatedCube, 'RUrURUUr')
        
    def test_rotate_200lURuLUrTest(self):
        cubeToRotate = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.lURuLUr('F')
        
        self.assertEqual(rotatedCube, 'fUBuFUb')
        
    def test_rotate_210modRUrURUUrTest(self):
        cubeToRotate = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.modRUrURUUr('R')
        
        self.assertEqual(rotatedCube, 'LUlULUUl')
        
        
    def test_rotate_210modFFUrLFFlRUFFTest(self):
        cubeToRotate = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.modFFUrLFFlRUFF('B')
        
        self.assertEqual(rotatedCube, 'FFUrLFFlRUFF')   
        
#    Sad path:
        
    def test_rotate_910InvalidDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo' 
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('2')
        self.assertEqual(rotatedCube, 'error: invalid rotation') 
    
    def test_rotate_920InvalidCube(self):
        cubeToRotate = '123456789abcdefghijklmnopqrstuvwxyz'
        theCube = cube.Cube(cubeToRotate)
        result = theCube.isValidCube()
        
        self.assertEqual(result, False)
        
    def test_rotate_930emptyCube(self):
        cubeToRotate = ''
        theCube = cube.Cube(cubeToRotate)
        result = theCube.isValidCube()
        
        self.assertEqual(result, False)
        
    def test_rotate_940invalidCube_tooManyTilesOfOneFace(self):
        cubeToRotate = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwb'
        theCube = cube.Cube(cubeToRotate)
        result = theCube.isValidCube()
        
        self.assertEqual(result, False)
 
        
        
        
        
        
        
        
        
        
        
        
        
