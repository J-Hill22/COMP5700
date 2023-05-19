from unittest import TestCase
from rubik.view.solve import solve
 

class SolveTest(TestCase):

# Analysis of solve
#        
#    solve: method, takes in a dictionary containing 'cube' : 54 char long string representing
#            an instantiated cube to be solved.
#
#    inputs:
#        parms: a dictionary containing a 'cube' represented by a 54 character long string
#
#    outputs:
#        side-effects:    no external effects, internal state change
#        nominal:
#            return a dictionary containing: a string of rotations describing how to solve an
#                an input cube, a status to show whether there was an error or not,
#                and integrity to describe something from increment 3
#        abnormal:
#            return dict with ['status']: string, 'error: some message here'
#                            ['integrity']: string, 'some integrity here'
#
#
#         Happy path:
#            test 010:    solved cube
#            test 020:    unsolved cube, solved bottom cross.
#            test 030:    unsolved cube with "daisy" on Up face.
#            test 040:    unsolved cube, scrambled.
#            test 050:    unsolved bottom, rest of cube is solved.
#            test 060:    test for integrity key, input unsolved/scrambled cube
#            test 070:    test generateIntegrityKey function in solve class.
#
#        Sad path:
#            test 910:    invalid cube:    random string of letters and numbers
#            test 920:    invalid cube:    empty cube.
#            test 930:    invalid cube:    too many unique characters
#            test 940:    invalid cube:    not enough unique characters
#            test 950:    invalid cube:    too many characters
#            test 960:    invalid cube:    not enough characters
#            test 970:    invalid cube:    missing cube parameter
#

#        Happy Path:

    def test010_solve_solvedCube(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('', result.get('solution'))
        
    def test020_solve_unsolvedCube_solvedBottomCross(self):
        parms = {}
        parms['cube'] = 'bybgboobywbygrorryrbwygyogbgbogorwogrrgoyyyrrwwbwwwowg'
        result = solve(parms)
        expectedRotations = ('RUruBUbbUBuFUfbuBRUrufuFUUURUrufuFBUburuRUUUuluLUFUf' 
                             + 'ruRUBUbuuULUlubuBuruRUBUbRUrURUUrRUrURUUrRUrURUUr'
                             + 'ufUBuFUbBUbUBUUbRRUbFRRfBURR')
        
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual(expectedRotations, result.get('solution'))
        
    def test030_solve_unsolvedDaisy(self):
        parms = {}
        parms['cube'] = 'obwgbbyoggryrryrgybgoggbbyrwowooowygbwrwywgwroyybwrbro'
        result = solve(parms)
        expectedRotations = ('BBLLRRFFrURBUbUUfuFbUBLUlFufluLFUfuluLUURUrufuFluL' 
                             + 'UFUfuuuluLUFUfuubuBULUluUBUburuRUFURurfRUrURUUrRUrURUUr'
                             + 'ULLUfBLLbFULLLLUfBLLbFULL')
        
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual(expectedRotations, result.get('solution'))
    
    def test040_solve_unsolvedCube_scrambled(self):
        parms = {}
        parms['cube'] = 'obggbwrroroobryyobywwggyyrrorboowwbggoggybwywyybrwgbwr'
        result = solve(parms)
        expectedRotations = ('RUrFFfUUFBBFUfLLRRUUluLuuLUluuBUbUfuFRUrufuFUUuluL'
                             + 'UFUfLUlubuBUuURUrufuFuULUlubuBUUuruRUBUbUFURurfURUrURUUruRUrURUUr'
                             + 'UUrULuRUlLUlULUUlBBUlRBBrLUBB')
        
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual(expectedRotations, result.get('solution'))
        
    def test050_solve_unsolvedBottom_solveCube(self):
        parms = {}
        parms['cube'] = 'bbbbbbooorrrrrrbbbggggggrrroooooogggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        expectedRotations = ('FFULLuffFFUUBBuuffFFuRRUffURUrfuFUFUfruRLUlLUlubuB'
                             + 'UuURUrufuFLUlubuBUuuluLUFUfUUULUlubuBUUUBUburuRFURurf'
                             + 'UrULuRUlLUlULUUlRRUbFRRfBURRRRUbFRRfBURR')
        
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual(expectedRotations, result.get('solution'))
        
    def test060_solve_unsolvedCube_solveCubeWithIntegrityKey(self):
        parms = {}
        parms['cube'] = 'robbbwworwborryywwbbyrgyorybgggoroworyyoywwyrgbgowgggb'
        result = solve(parms)
        expectedRotation = ('RfUUFBBLUlFFLLUBlblUULRRluLFFRurUUUruRRUrfuFUFUfbuBUURUrufuFUUULUl'
                            + 'ubuBUUFUfuluLUuruRUBUbFURurfUURUrURUUrURUrURUUruRUrURUUr'
                            + 'UUfUBuFUbBUbUBUUbRRUbFRRfBURR')
        
        
        expectedHash = '1549fa29ba6021a4aaea45ca40c03b20b010bbd682669f6f13d5fe8e90f6f626'
        actualHash = result['integrity']
        
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual(expectedRotation, result.get('solution'))
        self.assertIsNot(actualHash, '')
        self.assertIn(actualHash, expectedHash)
        
    def test070_solve_unsolvedCube_generateIntegrityKeyTest(self):
        parms = {}
        parms['cube'] = 'rggobwrobogybrywwwobrggbgbgygwrowrrwbybwyrboygyoywryoo'
        result = solve(parms)
        
        expectedHash = 'b3827e1a9fdd7e0c7eccbe27cb86f0a2055ff76d6b810d5ca8da7f8f8339d550'
        actualHash = result['integrity']
        
        self.assertIn('integrity', result)
        self.assertIsNot(actualHash, '')
        self.assertIn(actualHash, expectedHash)
        
    
#        Sad Path:
    
    def test910_solve_invalidCube(self):
        parms = {}
        parms['cube'] = '12345676lajkhbf'
        result = solve(parms)
        
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        self.assertEqual('error: invalid cube', result.get('status'))
        
    def test920_solve_emptyCube(self):
        parms = {}
        parms['cube'] = ''
        result = solve(parms)
        
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        self.assertEqual('error: invalid cube', result.get('status'))
            
    def test930_solve_invalidCube_tooManyUniques(self):
        parms = {}
        parms['cube'] = 'bbbbbbfbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwp'
        result = solve(parms)
        
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test940_solve_invalidCube_notEnoughUniques(self):
        parms = {}
        parms['cube'] = 'wwwwwwwwwrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        result = solve(parms)
        
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test950_solve_invalidCube_tooManyCharacters(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwww'
        result = solve(parms)
        
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test960_solve_invalidCube_notEnoughCharacters(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwww'
        result = solve(parms)
        
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test970_solve_emptyCube(self):
        parms = {}
        parms['cube'] = None
        result = solve(parms)
        
        self.assertIn('status', result)
        self.assertEqual('error: cube is missing', result['status'])
        self.assertEqual('error: cube is missing', result.get('status'))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
