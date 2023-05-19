'''
Created on April 13, 2023

@author: Jarrett
'''
from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''  
    rotations = ''
    cube = theCube
    cubeAsString = theCube.get()
    
    loopBreaker = 0
    
    if (not theCube.isValidCube()):
        return 'error: invalid cube'
    
    if (_solvedBottomLayerCheck(cubeAsString)):
        return rotations
    while (not _solvedBottomLayerCheck(cubeAsString)):
        
        singleRotation = ''
        tileToSolve = _findTileToSolve(cube)
        edgeMates = _findEdgeMates(tileToSolve, cube)
        edgeToSolve = {tileToSolve : edgeMates}
        tileCase = tileToSolve // NUM_OF_TILES
        if loopBreaker > 50: return  rotations + ' error: infinite loop'
        match tileCase:
            case 0:
                singleRotation = _solveTileOnFrontFace(edgeToSolve, cube)
            case 1:
                singleRotation = _solveTileOnRightFace(edgeToSolve, cube)
            case 2:
                singleRotation = _solveTileOnBackFace(edgeToSolve, cube)
            case 3:
                singleRotation = _solveTileOnLeftFace(edgeToSolve, cube)
            case 4:
                singleRotation = _solveTileOnUpFace(edgeToSolve, cube)
            case 5:
                singleRotation = _moveToTop(tileToSolve, face = 'D')
        
        cube.rotate(singleRotation)
        cubeAsString = cube.get()
        loopBreaker = loopBreaker + 1
        
        rotations += singleRotation
        
    return rotations
#33 LOC
    
    
    
def _solvedBottomLayerCheck(cube):
    if ((cube[DTL] != cube[DMM]) or (cube[FBL] != cube[FMM]) or (cube[LBR] != cube[LMM])):
        return False
    if ((cube[DTR] != cube[DMM]) or (cube[FBR] != cube[FMM]) or (cube[RBL] != cube[RMM])):
        return False
    if ((cube[DBL] != cube[DMM]) or (cube[BBR] != cube[BMM]) or (cube[LBL] != cube[LMM])):
        return False
    if ((cube[DBR] != cube[DMM]) or (cube[BBL] != cube[BMM]) or (cube[RBR] != cube[RMM])):
        return False
    else:
        return True
#11 LOC
    
def _findAllTiles(cube):
    
    keyBottomTiles = []

    cubeAsString = cube.get()
    downFaceTile = cubeAsString[DMM]
    allKeyTiles = [pos+INDEX_OFFSET for pos, char in enumerate(cubeAsString) if char == downFaceTile]
    
    for eachTile in allKeyTiles:
        if ((eachTile % NUM_OF_TILES) == (TOP_LEFT_OS) or 
            (eachTile % NUM_OF_TILES) == (TOP_RIGHT_OS) or
            (eachTile % NUM_OF_TILES) == (BOTTOM_LEFT_OS) or 
            (eachTile % NUM_OF_TILES) == (BOTTOM_RIGHT_OS)):
            keyBottomTiles.append(eachTile - INDEX_OFFSET)
    
    return keyBottomTiles
#12 LOC

def _findEdgeMates(tile, cube):
    cube = cube.get()
    caseNumber = tile // NUM_OF_TILES
    remainder = (tile + INDEX_OFFSET) % NUM_OF_TILES
    
    match caseNumber:
        case 0:
            result = _findFrontMates(remainder, cube)
            return result
        case 1:
            result = _findRightMates(remainder, cube)
            return result
        case 2:
            result = _findBackMates(remainder, cube)
            return result
        case 3:
            result = _findLeftMates(remainder, cube)
            return result
        case 4:
            result = _findUpMates(remainder, cube)
            return result
        case 5:
            result = _findDownMates(remainder, cube)
            return result
            
    return 'error: bad mates'
#24 LOC

def _findFrontMates(remainder, cube):
    result = ''
    edgeMates = []
    if remainder == TOP_LEFT_OS:
        edgeMates.append(cube[UBL])
        edgeMates.append(cube[LTR])
        result = ''.join(edgeMates)
        return result
    if remainder == TOP_RIGHT_OS:
        edgeMates.append(cube[UBR])
        edgeMates.append(cube[RTL])
        result = ''.join(edgeMates)
        return result
    if remainder == BOTTOM_LEFT_OS:
        edgeMates.append(cube[DTL])
        edgeMates.append(cube[LBR])
        result = ''.join(edgeMates)
        return result
    if remainder == BOTTOM_RIGHT_OS:
        edgeMates.append(cube[DTR])
        edgeMates.append(cube[RBL])
        result = ''.join(edgeMates)
        return result
#23 LOC

def _findRightMates(remainder, cube):
    result = ''
    edgeMates = []
    if remainder == TOP_LEFT_OS:
        edgeMates.append(cube[UBR])
        edgeMates.append(cube[FTR])
        result = ''.join(edgeMates)
        return result
    if remainder == TOP_RIGHT_OS:
        edgeMates.append(cube[UTR])
        edgeMates.append(cube[BTL])
        result = ''.join(edgeMates)
        return result
    if remainder == BOTTOM_LEFT_OS:
        edgeMates.append(cube[FBR])
        edgeMates.append(cube[DTR]) 
        result = ''.join(edgeMates)
        return result
    if remainder == BOTTOM_RIGHT_OS:
        edgeMates.append(cube[BBL])
        edgeMates.append(cube[DBR])
        result = ''.join(edgeMates)
        return result
#23 LOC
 
def _findBackMates(remainder, cube):
    result = ''
    edgeMates = []
    if remainder == TOP_LEFT_OS:
        edgeMates.append(cube[UTR])
        edgeMates.append(cube[RTR])
        result = ''.join(edgeMates)
        return result
    if remainder == TOP_RIGHT_OS:
        edgeMates.append(cube[UTL])
        edgeMates.append(cube[LTL])
        result = ''.join(edgeMates)
        return result
    if remainder == BOTTOM_LEFT_OS:
        edgeMates.append(cube[RBR])
        edgeMates.append(cube[DBR])
        result = ''.join(edgeMates)
        return result
    if remainder == BOTTOM_RIGHT_OS:
        edgeMates.append(cube[DBL])
        edgeMates.append(cube[LBL])
        result = ''.join(edgeMates)
        return result
#23 LOC
  
def _findLeftMates(remainder, cube):
    result = ''
    edgeMates = []
    if remainder == TOP_LEFT_OS:
        edgeMates.append(cube[UTL])
        edgeMates.append(cube[BTR])
        result = ''.join(edgeMates)
        return result
    if remainder == TOP_RIGHT_OS:
        edgeMates.append(cube[UBL])
        edgeMates.append(cube[FTL])
        result = ''.join(edgeMates)
        return result
    if remainder == BOTTOM_LEFT_OS:
        edgeMates.append(cube[BBR])
        edgeMates.append(cube[DBL])
        result = ''.join(edgeMates)
        return result
    if remainder == BOTTOM_RIGHT_OS:
        edgeMates.append(cube[FBL])
        edgeMates.append(cube[DTL])
        result = ''.join(edgeMates)
        return result
#23 LOC
    
def _findUpMates(remainder, cube):
    result = ''
    edgeMates = []
    if remainder == TOP_LEFT_OS:
        edgeMates.append(cube[BTR])
        edgeMates.append(cube[LTL])
        result = ''.join(edgeMates)
        return result
    if remainder == TOP_RIGHT_OS:
        edgeMates.append(cube[BTL])
        edgeMates.append(cube[RTR])
        result = ''.join(edgeMates)
        return result
    if remainder == BOTTOM_LEFT_OS:
        edgeMates.append(cube[FTL])
        edgeMates.append(cube[LTR])
        result = ''.join(edgeMates)
        return result
    if remainder == BOTTOM_RIGHT_OS:
        edgeMates.append(cube[FTR])
        edgeMates.append(cube[RTL])
        result = ''.join(edgeMates)
        return result
#23 LOC
    
def _findDownMates(remainder, cube):
    result = ''
    edgeMates = []
    if remainder == TOP_LEFT_OS:
        edgeMates.append(cube[FBL])
        edgeMates.append(cube[LBR])
        result = ''.join(edgeMates)
        return result
    if remainder == TOP_RIGHT_OS:
        edgeMates.append(cube[FBR])
        edgeMates.append(cube[RBL])
        result = ''.join(edgeMates)
        return result
    if remainder == BOTTOM_LEFT_OS:
        edgeMates.append(cube[BBR])
        edgeMates.append(cube[LBL])
        result = ''.join(edgeMates)
        return result
    if remainder == BOTTOM_RIGHT_OS:
        edgeMates.append(cube[BBL])
        edgeMates.append(cube[RBR])
        result = ''.join(edgeMates)
        return result
#23 LOC
    
def _findTileToSolve(cube):
    allKeyTiles = _findAllTiles(cube)
    allKeyTilesSorted = sorted(allKeyTiles)
    cube = cube.get()
    for eachTile in allKeyTilesSorted:
        if eachTile not in [DTL, DTR, DBL, DBR]:
            return eachTile
        elif eachTile == DTL:
            if (cube[FBL] != cube[FMM]) and (cube[LBR] != cube[LMM]):
                return eachTile
        elif eachTile == DTR:
            if (cube[FBR] != cube[FMM]) and (cube[RBL] != cube[RMM]):
                return eachTile
        elif eachTile == DBL:
            if (cube[BBR] != cube[BMM]) and (cube[LBL] != cube[LMM]):
                return eachTile
        elif eachTile == DBR:
            if (cube[BBL] != cube[BMM]) and (cube[RBR] != cube[RMM]):
                return eachTile
        else:
            return -1
    return -1
#22 LOC

def _moveToTop(tile, face = ''):
    rotns = ''
    position = tile % NUM_OF_TILES
    match face:
        case 'F':
            if position == BOTTOM_LEFT:
                rotns += 'lUL'
            else:
                rotns += 'Rur'
        case 'R':
            if position == BOTTOM_LEFT:
                rotns += 'fUF'
            elif position == BOTTOM_RIGHT:
                return 'Bub'
            else: return 'error in move to top R'
        case 'B':
            if position == BOTTOM_LEFT:
                rotns += 'rUR'
            else:
                rotns += 'Lul'
        case 'L':
            if position == BOTTOM_LEFT:
                rotns += 'bUB'
            else:
                rotns += 'Fuf'
        case 'D':
            if position == TOP_LEFT: rotns += 'luL'
            elif position == TOP_RIGHT: rotns += 'RUr'
            elif position == BOTTOM_LEFT: rotns += 'LUl'
            else: rotns += 'ruR'
    return rotns
#31 LOC
    
def _solveTileOnFrontFace(edgeToSolve, theCube):
    rotns = ''
    cube = theCube.get()
    [(tileToSolve, mates)] = edgeToSolve.items()
    frontFace = cube[FMM]
    rightFace = cube[RMM]
    leftFace = cube[LMM]
    solvableSet = (frontFace in mates) and ((rightFace in mates) or (leftFace in mates))
    position = tileToSolve % NUM_OF_TILES
    
    if (position < MIDDLE) and (solvableSet):
        if position == TOP_LEFT:
            if leftFace in mates:
                rotns += theCube.rightTrigger('L')
            else:
                rotns += 'u'
                rotns += theCube.rightTrigger('F')
        elif position == TOP_RIGHT:
            if leftFace in mates:
                rotns += 'U'
                rotns += theCube.leftTrigger('F')
            else:
                rotns += theCube.leftTrigger('R')
        else:
            return 'error'
    elif (position == TOP_LEFT):
        if leftFace in mates: rotns += 'u'
        rotns += 'u'
    elif (position == TOP_RIGHT): 
        if rightFace in mates: rotns += 'U'
        rotns += 'U'
    else:
        rotns += _moveToTop(tileToSolve, 'F')
        
    return rotns
#27 LOC

def _solveTileOnRightFace(edgeToSolve, theCube):
    rotns = ''
    cube = theCube.get()
    [(tileToSolve, mates)] = edgeToSolve.items()
    frontFace = cube[FMM]
    rightFace = cube[RMM]
    backFace = cube[BMM]
    solvableSet = (rightFace in mates) and ((frontFace in mates) or (backFace in mates))
    position = tileToSolve % NUM_OF_TILES
    
    if (position < MIDDLE) and (solvableSet):
        if position == TOP_LEFT:
            if frontFace in mates:
                rotns += theCube.rightTrigger('F')
            else:
                rotns += 'u'
                rotns += theCube.rightTrigger('R')
        elif position == TOP_RIGHT:
            if frontFace in mates:
                rotns += 'U'
                rotns += theCube.leftTrigger('R')
            else:
                rotns += theCube.leftTrigger('B')
        else:
            return 'error'
    elif (position < MIDDLE):
        if frontFace in mates: rotns += 'U'
        if backFace in mates: rotns += 'u'
        elif (frontFace not in mates) and (backFace not in mates): rotns = 'solveRight error'
    else:
        rotns = _moveToTop(tileToSolve, 'R')
        
    return rotns
#31  LOC
            
def _solveTileOnBackFace(edgeToSolve, theCube):
    rotns = ''
    cube = theCube.get()
    [(tileToSolve, mates)] = edgeToSolve.items()
    backFace = cube[BMM]
    rightFace = cube[RMM]
    leftFace = cube[LMM]
    solvableSet = (backFace in mates) and ((rightFace in mates) or (leftFace in mates))
    position = tileToSolve % NUM_OF_TILES
    
    if (position < MIDDLE) and (solvableSet):
        if position == TOP_LEFT:
            if rightFace in mates:
                rotns += theCube.rightTrigger('R')
            else:
                rotns += 'u'
                rotns += theCube.rightTrigger('B')
        elif position == TOP_RIGHT:
            if rightFace in mates:
                rotns += 'U'
                rotns += theCube.leftTrigger('B')
            else:
                rotns += theCube.leftTrigger('L')
        else:
            return 'error'
    elif (position == TOP_LEFT): 
        if leftFace in mates: rotns += 'u'
        rotns += 'u'
    elif (position == TOP_RIGHT): 
        if rightFace in mates: rotns += 'U'
        rotns += 'U'              
    else:
        rotns = _moveToTop(tileToSolve, 'B')
        
    return rotns
#27 LOC
    
def _solveTileOnLeftFace(edgeToSolve, theCube):
    rotns = ''
    cube = theCube.get()
    [(tileToSolve, mates)] = edgeToSolve.items()
    leftFace = cube[LMM]
    backFace = cube[BMM]
    frontFace = cube[FMM]
    solvableSet = (leftFace in mates) and ((backFace in mates) or (frontFace in mates))
    position = tileToSolve % NUM_OF_TILES
    
    if (position < MIDDLE) and (solvableSet):
        if position == TOP_LEFT:
            if backFace in mates:
                rotns += theCube.rightTrigger('B')
            else:
                rotns += 'u'
                rotns += theCube.rightTrigger('L')
        elif position == TOP_RIGHT:
            if backFace in mates:
                rotns += 'U'
                rotns += theCube.leftTrigger('L')
            else:
                rotns += theCube.leftTrigger('F')
        else:
            return 'error'
    elif (position < MIDDLE):
        if frontFace in mates: rotns += 'u'
        if backFace in mates: rotns += 'U'
        elif (frontFace not in mates) and (backFace not in mates): rotns = 'solveLeft error'    
    else:
        rotns = _moveToTop(tileToSolve, 'L')
        
    return rotns
#27 LOC

def _solveTileOnUpFace(edgeToSolve, theCube):
    rotns = ''
    cube = theCube.get()
    [(tileToSolve, mates)] = edgeToSolve.items()
    frontFace = cube[FMM]
    rightFace = cube[RMM]
    backFace = cube[BMM]
    leftFace = cube[LMM]
    frontSolvableSet = (frontFace in mates) and ((leftFace in mates) or (rightFace in mates))
    backSolvableSet = (backFace in mates) and ((leftFace in mates) or (rightFace in mates))
    position = tileToSolve % NUM_OF_TILES
    
    if (frontSolvableSet):
        if leftFace in mates:
            match position:
                case 0:
                    rotns += 'U'
                case 6:
                    rotns += 'UU'
                case 8:
                    rotns += 'u'
            rotns += 'luL' + theCube.rightTrigger('L')
        elif rightFace in mates:
            match position:
                case 2:
                    rotns += 'u'
                case 6:
                    rotns += 'U'
                case 8:
                    rotns += 'UU'
            rotns += 'RUr' + theCube.leftTrigger('R')
    elif (backSolvableSet):
        if leftFace in mates:
            match position:
                case 0:
                    rotns += 'UU'
                case 2:
                    rotns += 'U'
                case 6:
                    rotns += 'u'
            rotns += 'LUl' + theCube.leftTrigger('L')
        elif rightFace in mates:
            match position:
                case 0:
                    rotns += 'u'
                case 2:
                    rotns += 'UU'
                case 8:
                    rotns += 'U'
            rotns += 'ruR' + theCube.rightTrigger('R')
        
    return rotns

#50 LOC

    
    
    
    
    
    
    
    