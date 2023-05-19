from rubik.model.constants import *
from rubik.model.cube import Cube

def solveMiddleLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the middle layer is solved.
        
        input:  an instance of the cube class with the bottom layer solved
        output: the rotations required to solve the middle layer  
    '''  
    rotations = ''
    cube = theCube
    cubeAsString = theCube.get()
    loopBreaker = 0
    
    if (not theCube.isValidCube()): return 'error: invalid cube'
    
    if (_solvedMiddleLayerCheck(cubeAsString)): return rotations
    
    while (not _solvedMiddleLayerCheck(cubeAsString)):
        singleRotation = ''
        allKeyTiles = []
        allKeyTiles = _findAllTiles(cube, 'F')
        edgeMates = _findEdgeMates(allKeyTiles, cube)
        allEdges = dict(zip(allKeyTiles, edgeMates))
        tileToSolve = _findTileToSolve(allEdges, cube)
        if (not (tileToSolve)):
            allKeyTiles = _findAllTiles(cube, 'B')
            edgeMates = _findEdgeMates(allKeyTiles, cube)
            allEdges = dict(zip(allKeyTiles, edgeMates))
            tileToSolve = _findTileToSolve(allEdges, cube)
        [(tile, mate)] = tileToSolve.items()
        if cubeAsString[tile] == cubeAsString[FMM]:
            singleRotation = _solveFrontFaceTile(tileToSolve, cube)
        else: singleRotation = _solveBackFaceTile(tileToSolve, cube)
        
        cube.rotate(singleRotation)
        cubeAsString = cube.get()
        rotations += singleRotation
        
        loopBreaker = loopBreaker + 1
        if loopBreaker > 50: return rotations + 'error: infinite loop'
        
    return rotations
#LOC: 29
        
    
def _solvedMiddleLayerCheck(cube):
    if ((cube[FML] != cube[FMM]) or (cube[LMR] != cube[LMM])): return False
    
    if ((cube[FMR] != cube[FMM]) or (cube[RML] != cube[RMM])): return False
    
    if ((cube[RMR] != cube[RMM]) or (cube[BML] != cube[BMM])): return False
    
    if ((cube[BMR] != cube[BMM]) or (cube[LML] != cube[LMM])): return False
    
    else: return True
#LOC: 6
        
        
def _findAllTiles(cube, face = ''):
    keyTiles = []
    allFaceTiles = []
    cubeStr = cube.get()
    
    match face:
        case 'F':
            mid = cubeStr[FMM]
            allFaceTiles = [pos+INDEX_OFFSET for pos, char in enumerate(cubeStr) if char == mid]
        case 'R':
            mid = cubeStr[RMM]
            allFaceTiles = [pos+INDEX_OFFSET for pos, char in enumerate(cubeStr) if char == mid]
        case 'B':
            mid = cubeStr[BMM]
            allFaceTiles = [pos+INDEX_OFFSET for pos, char in enumerate(cubeStr) if char == mid]
        case 'L':
            mid = cubeStr[LMM]
            allFaceTiles = [pos+INDEX_OFFSET for pos, char in enumerate(cubeStr) if char == mid]

    
    for eachTile in allFaceTiles:
        if ((eachTile % NUM_OF_TILES) == (TOP_MIDDLE_OS) or
            (eachTile % NUM_OF_TILES) == (MIDDLE_LEFT_OS) or
            (eachTile % NUM_OF_TILES) == (MIDDLE_RIGHT_OS)):
            keyTiles.append(eachTile - INDEX_OFFSET)
        if ((eachTile // NUM_OF_TILES) == 4) and ((eachTile % NUM_OF_TILES) == BOTTOM_MIDDLE_OS):
            keyTiles.append(eachTile - INDEX_OFFSET)
    
    return keyTiles
#LOC: 25


def _findEdgeMates(keyTiles, cube):
    edgeMates = []
    cubeStr = cube.get()
    for eachTile in keyTiles:
        caseNumber = eachTile // NUM_OF_TILES
        position = (eachTile + INDEX_OFFSET) % NUM_OF_TILES
        match caseNumber:
            case 0:
                if position == TOP_MIDDLE_OS: edgeMates.append(cubeStr[UBM])
                elif position == MIDDLE_LEFT_OS: edgeMates.append(cubeStr[LMR])
                else: edgeMates.append(cubeStr[RML])
            case 1:
                if position == TOP_MIDDLE_OS: edgeMates.append(cubeStr[UMR])
                elif position == MIDDLE_LEFT_OS: edgeMates.append(cubeStr[FMR])
                else: edgeMates.append(cubeStr[BML])   
            case 2:
                if position == TOP_MIDDLE_OS: edgeMates.append(cubeStr[UTM])
                elif position == MIDDLE_LEFT_OS: edgeMates.append(cubeStr[RMR])
                else: edgeMates.append(cubeStr[LML])
            case 3:
                if position == TOP_MIDDLE_OS: edgeMates.append(cubeStr[UML])
                elif position == MIDDLE_LEFT_OS: edgeMates.append(cubeStr[BMR])
                else: edgeMates.append(cubeStr[FML])
            case 4:
                if position == TOP_MIDDLE_OS: edgeMates.append(cubeStr[BTM])
                elif position == MIDDLE_LEFT_OS: edgeMates.append(cubeStr[LTM])
                elif position == MIDDLE_RIGHT_OS: edgeMates.append(cubeStr[RTM])
                else: edgeMates.append(cubeStr[FTM])
        
    return edgeMates
#LOC: 29

def _findTileToSolve(allEdges, cube):
    cube = cube.get()
    result = {}
    
    for key in allEdges:
        face = key // NUM_OF_TILES
        position = key % NUM_OF_TILES
        if allEdges[key] == cube[UMM]: continue
        match face:
            case 0:
                if (position == TOP_MIDDLE) and (allEdges[key] != cube[UMM]):
                    return {key : allEdges[key]}
                if ((position == MIDDLE_LEFT) and (allEdges[key] != cube[LMM])):
                    return {key : allEdges[key]}
                if ((position == MIDDLE_RIGHT) and (allEdges[key] != cube[RMM])): 
                    return {key : allEdges[key]}
            case 1:
                if (position == TOP_MIDDLE) and (allEdges[key] != cube[UMM]):
                    return {key : allEdges[key]}
                if ((position == MIDDLE_LEFT) and (allEdges[key] != cube[FMM])):
                    return {key : allEdges[key]}
                if ((position == MIDDLE_RIGHT) and (allEdges[key] != cube[BMM])):
                    return {key : allEdges[key]}
            case 2:
                if (position == TOP_MIDDLE) and (allEdges[key] != cube[UMM]):
                    return {key : allEdges[key]}
                if ((position == MIDDLE_LEFT) and (allEdges[key] != cube[RMM])):
                    return {key : allEdges[key]}
                if ((position == MIDDLE_RIGHT) and allEdges[key] != cube [LMM]):
                    return {key : allEdges[key]}
            case 3:
                if (position == TOP_MIDDLE) and (allEdges[key] != cube[UMM]):
                    return {key : allEdges[key]}
                if ((position == MIDDLE_LEFT) and (allEdges[key] != cube[BMM])):
                    return {key : allEdges[key]}
                if ((position == MIDDLE_RIGHT) and allEdges[key] != cube [FMM]):
                    return {key : allEdges[key]}
            case 4:
                if (allEdges[key] != cube[UMM]): return {key : allEdges[key]}
                
#LOC: 37
    
def _solveFrontFaceTile(edgeToSolve, cube):
    rotns = ''
    theCube = cube
    cube = cube.get()
    [(tileToSolve, mate)] = edgeToSolve.items()
    face = (tileToSolve // NUM_OF_TILES)
    position = (tileToSolve %  NUM_OF_TILES)
    
    if face == UP_FACE:
        rotns = _solveTileOnUpFace(edgeToSolve, theCube)
        return rotns
    
    if position != TOP_MIDDLE: rotns = _moveToTop(tileToSolve, theCube)
    
    if (position == TOP_MIDDLE) and (cube[tileToSolve] == cube[FMM]):
        match face:
            case 0: rotns = ''
            case 1: rotns = 'U'
            case 2: rotns = 'UU'
            case 3: rotns = 'u'
            
        if mate == cube[RMM]: 
            rotns += theCube.modRightTrigger('F') + 'u'
            rotns += theCube.leftTrigger('R')
        if mate == cube[LMM]:
            rotns += theCube.modLeftTrigger('F') + 'U'
            rotns += theCube.rightTrigger('L')
    return rotns
#LOC: 24
                    
def _solveBackFaceTile(edgeToSolve, cube):
    rotns = ''
    theCube = cube
    cube = cube.get()
    [(tileToSolve, mate)] = edgeToSolve.items()
    face = (tileToSolve // NUM_OF_TILES)
    position = (tileToSolve %  NUM_OF_TILES)
    
    if face == UP_FACE: 
        rotns = _solveTileOnUpFace(edgeToSolve, theCube)
        return rotns
    
    if position != TOP_MIDDLE: rotns = _moveToTop(tileToSolve, theCube)
    
    if (position == TOP_MIDDLE) and (cube[tileToSolve] == cube[BMM]):
        match face:
            case 0: rotns = 'UU'
            case 1: rotns = 'u'
            case 2: rotns = ''
            case 3: rotns = 'U'
            
        if mate == cube[RMM]: 
            rotns += theCube.modLeftTrigger('B') + 'U'
            rotns += theCube.rightTrigger('R')
        if mate == cube[LMM]:
            rotns += theCube.modRightTrigger('B') + 'u'
            rotns += theCube.leftTrigger('L')
    return rotns
#LOC: 24

def _solveTileOnUpFace(edgeToSolve, cube):
    rotns = ''
    theCube = cube
    cube = cube.get()
    [(tileToSolve, mate)] = edgeToSolve.items()
    position = (tileToSolve %  NUM_OF_TILES)
    if (mate == cube[RMM]):
        match position:
            case 1: rotns += 'U'
            case 3: rotns += 'UU'
            case 5: rotns += ''
            case 7: rotns += 'u'
    elif (mate == cube[LMM]):
        match position:
            case 1: rotns += 'u'
            case 3: rotns += ''
            case 5: rotns += 'UU'
            case 7: rotns += 'U'
    if (cube[tileToSolve] == cube[FMM]):
        if mate == cube[RMM]: 
            rotns += theCube.modLeftTrigger('R') + 'U' 
            rotns += theCube.rightTrigger('F')
        else:
            rotns += theCube.modRightTrigger('L') + 'u'
            rotns += theCube.leftTrigger('F')
    elif (cube[tileToSolve] == cube[BMM]):
        if mate == cube[RMM]:
            rotns += theCube.modRightTrigger('R') + 'u'
            rotns += theCube.leftTrigger('B')
        else:
            rotns += theCube.modLeftTrigger('L') + 'U'
            rotns += theCube.rightTrigger('B')
    return rotns
#LOC: 34

def _moveToTop(tileToSolve, cube):
    rotns = ''
    theCube = cube
    cube = cube.get()
    face = (tileToSolve // NUM_OF_TILES)
    position = (tileToSolve % NUM_OF_TILES)
    
    if position == MIDDLE_LEFT:
        match face:
            case 0: rotns = 'FUfu' + theCube.leftTrigger('F') + 'U'
            case 1: rotns = 'RUru' + theCube.leftTrigger('R') + 'U'
            case 2: rotns = 'BUbu' + theCube.leftTrigger('B') + 'U'
            case 3: rotns = 'LUlu' + theCube.leftTrigger('L') + 'U'
    if position == MIDDLE_RIGHT:
        match face:
            case 0: rotns = 'fuFU' + theCube.rightTrigger('F') + 'u'
            case 1: rotns = 'ruRU' + theCube.rightTrigger('R') + 'u'
            case 2: rotns = 'buBU' + theCube.rightTrigger('B') + 'u'
            case 3: rotns = 'luLU' + theCube.rightTrigger('L') + 'u'
    return rotns
#LOC: 19
    






