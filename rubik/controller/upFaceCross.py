from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the up-face cross configuration.
        
        input:  an instance of the cube class with the middle layer solved
        output: the rotations required to solve the up-face cross  
    '''  
    rotations = ''
    cube = theCube
    cubeAsString = theCube.get()
    loopBreaker = 0
    
    if (not theCube.isValidCube()): return 'error: invalid cube'
    
    if (_solvedUpCrossCheck(cubeAsString)): return rotations
    
    while (not _solvedUpCrossCheck(cubeAsString)):
        singleRotation = ''
        allKeyTiles = _findAllTiles(cube)
        configuration = _determineUpConfiguration(allKeyTiles)
        
        singleRotation = _prepForFURurf(configuration)
        singleRotation += cube.FURurf()
        
        cube.rotate(singleRotation)
        cubeAsString = cube.get()
        rotations += singleRotation
        
        loopBreaker = loopBreaker + 1
        if loopBreaker > 25: return rotations + 'error: infinite loop in solveUpCross'
    
    return rotations
#LOC: 19

def _solvedUpCrossCheck(cube):
    if (cube[UTM] != cube[UMM]): return False
    
    if (cube[UML] != cube[UMM]): return False
    
    if (cube[UMR] != cube[UMM]): return False
    
    if (cube[UBM] != cube[UMM]): return False
    
    else: return True
#LOC: 6
    
def _findAllTiles(cube):
    cubeStr = cube.get()
    allKeyTiles = []
    
    allUpTiles = [pos for pos, char in enumerate(cubeStr) if char == cubeStr[UMM]]
    
    for eachTile in allUpTiles:
        remainder = eachTile % NUM_OF_TILES
        keyTile = remainder % 2
        if (keyTile == 1): allKeyTiles.append(eachTile)
    
    return allKeyTiles
#LOC: 9

def _determineUpConfiguration(allKeyTiles):
    configuration = ''
    if (UTM in allKeyTiles):
        configuration += 'N'
        
    if (UML in allKeyTiles):
        configuration += 'W'

    if (UMR in allKeyTiles):
        configuration += 'E'
        
    if (UBM in allKeyTiles):
        configuration += 'S'
        
    return configuration
#LOC: 11

def _prepForFURurf(configuration):
    rotns = ''

    if configuration == 'WE':
        rotns += 'U'
        return rotns
    
    if configuration == 'NE':
        rotns += 'u'
        return rotns
    
    if configuration == 'ES':
        rotns += 'UU'
        return rotns
    
    if configuration == 'WS':
        rotns += 'U'
        return rotns
    
    if configuration == 'EWS':
        rotns += 'U'
        
    else: return ''
#LOC: 17
    
        
    
    
        

