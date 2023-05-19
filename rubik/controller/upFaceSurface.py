from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpSurface(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the up face is solved.
        
        input:  an instance of the cube class with up-face cross solved
        output: the rotations required to solve the up surface  
    '''  
    rotations = ''
    cube = theCube
    cubeAsString = theCube.get()
    loopBreaker = 0
    
    if (not theCube.isValidCube()): return 'error: invalid cube'
    
    if (_solvedUpperLayerCheck(cubeAsString)): return rotations
    
    while (not _solvedUpperLayerCheck(cubeAsString)):
        singleRotation = ''
        allKeyTiles = _findAllTiles(cube)
        
        if _isFish(allKeyTiles):
            singleRotation += _yesAFish(allKeyTiles)
            singleRotation += cube.RUrURUUr()
        
        else:
            singleRotation += _notAFish(allKeyTiles)
            singleRotation += cube.RUrURUUr()
        
        cube.rotate(singleRotation)
        cubeAsString = cube.get()
        rotations += singleRotation
        
        if loopBreaker > 25: return rotations + 'error: infinite loop in solveUpperLayer'
    
    return rotations
#LOC: 21

def _solvedUpperLayerCheck(cube):
    if (cube[UTL] != cube[UMM]): return False
    
    if (cube[UTR] != cube[UMM]): return False
    
    if (cube[UBL] != cube[UMM]): return False
    
    if (cube[UBR] != cube[UMM]): return False
    
    else: return True
#LOC: 6
    
    
def _findAllTiles(cube):
    cubeStr = cube.get()
    allKeyTiles = []
    
    allUpTiles = [pos for pos, char in enumerate(cubeStr) if char == cubeStr[UMM]]
    
    for eachTile in allUpTiles:
        remainder = eachTile % NUM_OF_TILES
        keyTile = remainder % 2
        if (keyTile == 0) and (eachTile != UMM): allKeyTiles.append(eachTile)
        
    return allKeyTiles
#LOC: 9
        
def _isFish(allKeyTiles):
    if ((UTL in allKeyTiles) and 
        ((UTR not in allKeyTiles) and 
        (UBL not in allKeyTiles) and 
        (UBR not in allKeyTiles))):
        return True
    
    if ((UTR in allKeyTiles) and 
        ((UTL not in allKeyTiles) and 
        (UBL not in allKeyTiles) and 
        (UBR not in allKeyTiles))):
        return True
    
    if ((UBL in allKeyTiles) and 
        ((UTR not in allKeyTiles) and 
        (UTL not in allKeyTiles) and 
        (UBR not in allKeyTiles))):
        return True
    
    if ((UBR in allKeyTiles) and 
        ((UTR not in allKeyTiles) and 
        (UBL not in allKeyTiles) and 
        (UTL not in allKeyTiles))):
        return True
    
    else: return False
#LOC: 22
    
def _notAFish(allKeyTiles):
    rotns = ''
    if (LTR in allKeyTiles):
        return rotns
    
    if (FTR in allKeyTiles):
        rotns += 'U'
        return rotns
    
    if (RTR in allKeyTiles):
        rotns += 'UU'
        return rotns
    
    if (BTR in allKeyTiles):
        rotns = 'u'
        return rotns
#LOC: 13
        
def _yesAFish(allKeyTiles):
    rotns = ''
    
    if (UBL in allKeyTiles):
        return rotns
    
    if (UTL in allKeyTiles):
        rotns = 'u'
        return rotns
    
    if (UBR in allKeyTiles):
        rotns = 'U'
        return rotns
    
    if (UTR in allKeyTiles):
        rotns = 'UU'
        return rotns
    
    else: return 'error in yesAFish'
#LOC: 14
