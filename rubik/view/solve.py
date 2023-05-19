from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
import hashlib
import random

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    auburnId = 'jwh0100'
    
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    
    if (parms.get('cube') == None):
        result['status'] ='error: cube is missing'
        return result
    
    
    
    
    if theCube.isValidCube():   
        rotations = ""
        rotations += solveBottomCross(theCube)      #iteration 2
        rotations += solveBottomLayer(theCube)      #iteration 3
        rotations += solveMiddleLayer(theCube)      #iteration 4
        rotations += solveUpCross(theCube)          #iteration 5
        rotations += solveUpSurface(theCube)        #iteration 5
        rotations += solveUpperLayer(theCube)       #iteration 6
        
        sliceOfToken = _generateIntegrityKey(encodedCube, rotations, auburnId)
        
        result['solution'] = rotations
        result['status'] = 'ok'    
        result['integrity'] = sliceOfToken                    #iteration 5
    else:
        result = {'status' : 'error: invalid cube'}
                     
    return result


def _generateIntegrityKey(cubeAsString, rotations, auburnId):
    itemToTokenize = cubeAsString + rotations + auburnId
    sha256Hash = hashlib.sha256()
    sha256Hash.update(itemToTokenize.encode())
    
    fullToken = sha256Hash.hexdigest()
    startHashIndex = random.randint(0, len(fullToken) - 8)
    endHashIndex = startHashIndex + 8
    sliceOfToken = fullToken[startHashIndex : endHashIndex]
    
    return sliceOfToken
# I2: 4 LOC
# I5: 11 LOC
# I6: 4 LOC













