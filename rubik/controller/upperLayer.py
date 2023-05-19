from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpperLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the entire upper layer is solved.
        
        input:  an instance of the cube class with up-face surface solved
        output: the rotations required to solve the upper layer  
    '''  
    rotations = ''
    cube = theCube
    cubeAsString = theCube.get()
    loopBreaker = 0
    
    if (not theCube.isValidCube()): return 'error: invalid cube'
    
    if (_solvedUpperLayerCheck(cubeAsString)): return rotations
    
    while (not _solvedUpperLayerCheck(cubeAsString)):
        if loopBreaker > 25: return rotations + ' error: infinite loop in solve upper layer'
        singleRotation = ''
        if (_solvedUpperCornersCheck(cubeAsString)):
            solvedFace = _checkForSolvedFace(cube)
            singleRotation = cube.modFFUrLFFlRUFF(solvedFace)
        else: #(not _solvedUpperCornersCheck(cubeAsString)):
            if loopBreaker > 25: return rotations + ' error: infinite loop in solve upper corners'
            singleRotation = ''
            cornersToSolve = _findCornersToSolve(cube)
            matchingCorners = _checkForMatchingCorners(cornersToSolve, cube)
            if bool(matchingCorners):
                [(face, position)] = matchingCorners.items()
                alignmentRotation = _alignMatchingCorners(matchingCorners, cube)
                if alignmentRotation != '':
                    cube.rotate(alignmentRotation)
                    cubeAsString = cube.get()
                    rotations += alignmentRotation
                    continue
                singleRotation += cube.lURuLUr(face)
                singleRotation += cube.modRUrURUUr(face)
            else:
                singleRotation += cube.lURuLUr('L')
                singleRotation += cube.RUrURUUr()

        cube.rotate(singleRotation)
        cubeAsString = cube.get()
        rotations += singleRotation
        
        loopBreaker = loopBreaker + 1
        
    return rotations
#LOC: 35
    
def _solveUpperCorners(cube):
    rotns = ''
    singleRotation = ''
    cornersToSolve = _findCornersToSolve(cube)
    matchingCorners = _checkForMatchingCorners(cornersToSolve, cube)
    if bool(matchingCorners):
        [(face, position)] = matchingCorners.items()
        alignmentRotation = _alignMatchingCorners(matchingCorners, cube)
        if alignmentRotation != '':
            cube.rotate(alignmentRotation)
            cubeAsString = cube.get()
            rotns += alignmentRotation
            return rotns
        singleRotation += cube.lURuLUr(face)
        singleRotation += cube.modRUrURUUr(face)
    else:
        singleRotation += cube.lURuLUr('L')
        singleRotation += cube.RUrURUUr()
    
        
    cube.rotate(singleRotation)
    cubeAsString = cube.get()
    rotns += singleRotation
#LOC: 21
    
    
def _solvedUpperLayerCheck(cube):
    if ((cube[FTL] != cube[FMM]) or
        (cube[FTM] != cube[FMM]) or
        (cube[FTR] != cube[FMM])):
        return False
    
    if ((cube[RTL] != cube[RMM]) or
        (cube[RTM] != cube[RMM]) or
        (cube[RTR] != cube[RMM])):
        return False
    
    if ((cube[BTL] != cube[BMM]) or
        (cube[BTM] != cube[BMM]) or
        (cube[BTR] != cube[BMM])):
        return False
    
    if ((cube[LTL] != cube[LMM]) or
        (cube[LTM] != cube[LMM]) or
        (cube[LTR] != cube[LMM])):
        return False
    
    else: return True
#LOC: 18

def _solvedUpperCornersCheck(cube):
    if ((cube[FTL] != cube[FMM]) or
        (cube[FTR] != cube[FMM])):
        return False
    
    if ((cube[RTL] != cube[RMM]) or
        (cube[RTR] != cube[RMM])):
        return False
    
    if ((cube[BTL] != cube[BMM]) or
        (cube[BTR] != cube[BMM])):
        return False
    
    if ((cube[LTL] != cube[LMM]) or
        (cube[LTR] != cube[LMM])):
        return False
    
    else: return True
#LOC: 14
    
def _findCornersToSolve(cube):
    cubeStr = cube.get()
    cornersToSolve = {}
    
    allPossiblePositions = [FTL, FTR, RTL, RTR, BTL, BTR, LTL, LTR]
    
    for eachPosition in allPossiblePositions:
        face = ''
        faceCase = (eachPosition + INDEX_OFFSET) // NUM_OF_TILES
        match faceCase:
            case 0: face = cubeStr[FMM]
            case 1: face = cubeStr[RMM]
            case 2: face = cubeStr[BMM]
            case 3: face = cubeStr[LMM]
        if (cubeStr[eachPosition] not in cornersToSolve): 
            cornersToSolve[cubeStr[eachPosition]] = []
        cornersToSolve[cubeStr[eachPosition]].append(eachPosition)
            
    return cornersToSolve
#LOC: 16
    
    
def _checkForMatchingCorners(cornersToSolve, cube):
    cubeStr = cube.get()
    matchingCorners = {}
    for eachKey in cornersToSolve:
        face = eachKey
        position = cornersToSolve[eachKey]
        if len(position) < 2: continue
        if ((position[0] // NUM_OF_TILES) == (position[1] //NUM_OF_TILES)):
            faceCase = position[0] // NUM_OF_TILES
            match faceCase:
                case 0: matchingCorners = {'F': face}
                case 1: matchingCorners = {'R': face}
                case 2: matchingCorners = {'B': face}
                case 3: matchingCorners = {'L': face}
            return matchingCorners

    return matchingCorners
#LOC: 16

def _alignMatchingCorners(matchingCorners, cube):
    cubeStr = cube.get()
    rotns = ''
    [(positionOfTile, colorOfTile)] = matchingCorners.items()
    
    match positionOfTile:
        case 'F':
            if colorOfTile == cubeStr[FMM]: rotns = ''
            if colorOfTile == cubeStr[RMM]: rotns = 'u'
            if colorOfTile == cubeStr[BMM]: rotns = 'UU'
            if colorOfTile == cubeStr[LMM]: rotns = 'U'
            
        case 'R':
            if colorOfTile == cubeStr[FMM]: rotns = 'U'
            if colorOfTile == cubeStr[RMM]: rotns = ''
            if colorOfTile == cubeStr[BMM]: rotns = 'u'
            if colorOfTile == cubeStr[LMM]: rotns = 'UU'
            
        case 'B':
            if colorOfTile == cubeStr[FMM]: rotns = 'UU'
            if colorOfTile == cubeStr[RMM]: rotns = 'U'
            if colorOfTile == cubeStr[BMM]: rotns = ''
            if colorOfTile == cubeStr[LMM]: rotns = 'u'
            
        case 'L':
            if colorOfTile == cubeStr[FMM]: rotns = 'u'
            if colorOfTile == cubeStr[RMM]: rotns = 'UU'
            if colorOfTile == cubeStr[BMM]: rotns = 'U'
            if colorOfTile == cubeStr[LMM]: rotns = ''
            
    return rotns
#LOC: 26
            
def _checkForSolvedFace(cube):
    cubeStr = cube.get()
    
    if cubeStr[FTM] == cubeStr[FMM]: return 'F'
    
    if cubeStr[RTM] == cubeStr[RMM]: return 'R'
    
    if cubeStr[BTM] == cubeStr[BMM]: return 'B'
    
    if cubeStr[LTM] == cubeStr[LMM]: return 'L'
    
    else: return ''
#LOC: 7
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    