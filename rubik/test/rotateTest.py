from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):


# Analysis of Rotate    
#
#    rotate:    method, validates the 'dir' and 'cube' keys, instantiates the cube, rotates the 
#               cube, and returns a string value of the cube
#
#        inputs: 
#            parms:    a parsed query string expected to contain keys 'dir' and 'cube'
#                'dir':    string, len .GE. 0, [FfRrBbLlUu]; optional, defaults to "F" if missing;
#                          unvalidated
#                'cube':   string, len 54, 6 unique chars from [a-zA-Z0-9], 5th 14th 23rd 32nd 41st 
#                          and 50th chars must be unique; mandatory; unvalidated
#        outputs:  
#            side-effects:    applies rotation directions to an instanced cube
#            nominal:
#                return dict containing: if input 'cube' and 'dir' is valid:
#                                        {'cube':'bbb...www':'status':'ok'}
#                                        where contents of 'cube' describes the encoded cube
#            abnormal:
#                return dict contating: if input 'cube' or 'dir' is invalid:
#                                       {'status':'error:xxx'} 
#                                       where 'xxx' is an error message 
#
#
#        happy path:
#            test 010:    parms contains valid 'cube' and 'dir' key
#            test 100:    should rotate nominal cube in F direction
#            test 105:    should rotate nominal cube in f direction
#            test 110:    should rotate nominal cube in R direction
#            test 115:    should rotate nominal cube in r direction
#            test 120:    should rotate nominal cube in B direction
#            test 125:    should rotate nominal cube in b direction
#            test 130:    should rotate nominal cube in L direction
#            test 135:    should rotate nominal cube in l direction
#            test 140:    should rotate nominal cube in U direction
#            test 145:    should rotate nominal cube in u direction
#            test 150:    should rotate nominal cube with empty direction
#            test 155:    should rotate nominal cube with missing direciton
#            test 160:    should rotate nominal cube with multi-string direction
#
#        sad path:
#            test 910:    'cube' key has invalid characters
#            test 920:    'cube' key is an invalid length
#            test 930:    'cube' key does not have unique chars in 
#                             5th 14th 23rd 32nd 41st 50th place
#            test 940:    'dir' key is invalid
#            test 950:    'cube' key is empty string.
#            test 960:    'cube' is an invalid cube. cube with != 9 occurrences of legal characters. 
#            test 970:    'cube' is missing from URL
#            
#        evil path:
#            none
#
#
#
    def test010_rotate_ValidKey(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        
        expectedResult = 'bbbbbbbbbyrryrryrroooooooooggwggwggwyyyyyygggrrrwwwwww'
    
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(expectedResult, result.get('cube'))
        
    def test100_rotate_rotateNominalCubeInFDirection(self):
        encodedCube = '4dJBssBsVVVBJdV4dVsJsBV4dBd44BdBsssVdVJBJ4sVB4dd44JJJJ'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        
        expectedResult = 'BB4ssdVsJsVBVdVBdVsJsBV4dBd444dBdssddVJBJ4VsB4JV44JJJJ'
    
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(expectedResult, result.get('cube'))
    
    def test105_rotate_rotateNominalCubeInfDirection(self):
        encodedCube = 'ccyc9HH9c9QQyy9x99ccxyxxQxxQ99HcQHxcyx9HQyHHHxcQQHQyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'f'
        
        expectedResult = 'yHcc99ccHQQQcy9x99ccxyxxQxxQ9HHcHHxHyx9HQy9yx9QcQHQyyy'
    
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(expectedResult, result.get('cube'))
        
    def test110_rotate_rotateNominalCubeInRDirection(self):
        encodedCube = 'gFxyqjxqyyjqxyyggqjFygggjFFFqyFjxjqjqyxxFgFqqgjxyxxgjF'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'R'
        
        expectedResult = 'gFxyqxxqFgxygyjqyqqFygggxFFFqyFjxjqjqyxxFjFqygjjyxggjj'
    
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(expectedResult, result.get('cube'))
        
    def test115_rotate_rotateNominalCubeInrDirection(self):
        encodedCube = 'qNfgfgNNg5f5NVq5fNffgVggqVg5ffqN5qgqV5Vq5VVqNf5NVqNV5g'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'r'
        
        expectedResult = 'qNVgfVNNN5qNfVf5N5gfgNggNVg5ffqN5qgqV5qq5VVqff5fVqgV5g'
    
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(expectedResult, result.get('cube'))
        
    def test120_rotate_rotateNominalCubeInBDirection(self):
        encodedCube = '3PaP3aJ3JPxP3xP8JxxJPxJx833J8a8aa8PPx83a8J833a8aJPaxxJ'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'B'
        
        expectedResult = '3PaP3aJ3JPxJ3xx8Jx8xx3JJ3xP38a8aaxPPPPxa8J833a8aJPaJ88'
    
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(expectedResult, result.get('cube'))
        
    def test125_rotate_rotateNominalCubeInbDirection(self):
        encodedCube = 'WUttccS6U6WWWW6St6ccUS6UStUSUUcSSWWtcStSU666Wct6UtWcct'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'b'
        
        expectedResult = 'WUttccS6U6WcWWSSttUUUc6tcSScUUcSStWtWcSSU666Wct6UtW66W'
    
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(expectedResult, result.get('cube'))
        
    def test130_rotate_rotateNominalCubeInLDirection(self):
        encodedCube = 'yy621Dy1D261yu2yuD216yDDuD1Dyu62Duu2u26uy211D1626616uy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'L'
        
        expectedResult = 'uy6u1D11D261yu2yuD216yD6uD1u6Du2y2Du126Dy261Dy62261yuy'
    
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(expectedResult, result.get('cube'))
        
    def test135_rotate_rotateNominalCubeInlDirection(self):
        encodedCube = 'VigViVXiXXlilXXuVVXgVglluiggllgVulXgiVuuuXuuilXlugiVgi'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'l'
        
        expectedResult = 'liguiVViXXlilXXuVVXgugluuiiluglVXgglVVuVuXXuigXllgiVgi'
    
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(expectedResult, result.get('cube'))
        
    def test140_rotate_rotateNominalCubeInUDirection(self):
        encodedCube = 'QOQT9LQROR9RTRRLLTO99TQR99LLLRQLQOOTTT9OOLOQTLOQ9TQ9RR'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'U'
        
        expectedResult = 'R9RT9LQROO99TRRLLTLLRTQR99LQOQQLQOOTOOTQOTTL9LOQ9TQ9RR'
    
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(expectedResult, result.get('cube'))
        
    def test145_rotate_rotateNominalCubeInuDirection(self):
        encodedCube = '9sKuu9sKKuw9KKwu9wwwwuWssWs99KWwKwWKuWWussWu9WssK9wW9u'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'u'
        
        expectedResult = '99Kuu9sKK9sKKKwu9wuw9uWssWswwwWwKwWKWs9WsuuuWWssK9wW9u'
    
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(expectedResult, result.get('cube'))
        
    def test150_rotate_rotateNominalCubeInEmptyDirection(self):
        encodedCube = 'wv7XXXevewXXt777tXtwwve77evtttwtw77vXevwwveeXttwXvee7v'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = ''
        
        expectedResult = 'eXwvXveX7eXXe77XtXtwwve77evtttwtt77wXevwwvvwt7twXvee7v'
    
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(expectedResult, result.get('cube'))
        
    def test155_rotate_rotateNominalCubeInMissingDirection(self):
        encodedCube = 'yOOywwJJjJOSJSjSSOwSOyySwOOyjSwOJJSwjJjwJyJjySOyyjjwwj'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = None
        
        expectedResult = 'JyyJwOjwOJOSjSjySOwSOyySwOOyjSwOOJSyjJjwJywJSSJJyjjwwj'
    
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(expectedResult, result.get('cube'))
        
    def test160_rotate_rotateNominalCubeInMuiltiStringDirection(self):
        encodedCube = 'NOJNONN9OOOJOJJ9NPNPKPPO99NPPPKKJK9K9NOKNJJ99OKKP9KPJJ'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'Lfrb'
        
        expectedResult = 'JNOOOJ9K9JJNOJNKK9PPOPP9JKPNK9JK9JJKK9KONPOONPPON99NNP'
    
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(expectedResult, result.get('cube'))
        
    def test910_rotate_InvalidCharactersCubeKey(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooo12345gggggggggyyyyyyyyywwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test920_rotate_InvalidLengthCubeKey(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwwwbbbbbbbbbbbb'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test930_rotate_InvalidUniquesCubeKey(self):
        encodedCube = 'bbbbbbbbbrrrrbrrrroooobooooggggbggggyyyybyyyywwwwbwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test940_rotate_InvalidDirKey(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'Forget about it'
        
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid rotation', result['status'])
        
    def test950_rotate_emptyCube(self):
        encodedCube = ''
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FFFFFF'
        
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test960_rotate_illegalCube_notNineUniqueCharacters(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwb'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRUurf'
        
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test970_rotate_cubeMissingFromParms(self):
        parms = {}
        parms['cube'] = None
        parms['dir'] = 'FFFFFF'
        
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: cube is missing', result['status'])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
