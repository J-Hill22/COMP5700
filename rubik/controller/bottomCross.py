'''
Created on Mar 23, 2023

@author: Jarrett
'''
from rubik.model.cube import Cube
from rubik.model.constants import *

def solveBottomCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the down-face cross configuration.
        
        input:  an instance of the cube class
        output: the rotations required to transform the input cube into the down-face cross 
    '''  

    result = bottomCrossSolver(theCube)

    return result
         
def bottomCrossSolver(theCube):
    rotations = ''
    tileToSolve = -1
    
    instancedCube = theCube
    cubeAsString = theCube.get()
    
    loopBreaker = 0
    
    if (not theCube.isValidCube()):
        return 'error: invalid cube'
    
    while (_solvedBottomCrossCheck(cubeAsString) == False):
        if loopBreaker > 25:
            return 'error: infinite loop in bottomCross'
        
        singleRotation = ''
        
        tileToSolve = _findTileToSolve(cubeAsString)
        edgeMate = _findEdgeMate(tileToSolve, cubeAsString)
        edgeToSolve = {tileToSolve : edgeMate}
        tileCase = tileToSolve // NUM_OF_TILES
        
        match tileCase:
            case 0:
                singleRotation += _solveFrontTile(edgeToSolve, cubeAsString)
            case 1:
                singleRotation += _solveRightTile(edgeToSolve, cubeAsString)
            case 2:
                singleRotation += _solveBackTile(edgeToSolve, cubeAsString)
            case 3:
                singleRotation += _solveLeftTile(edgeToSolve, cubeAsString)
            case 4:
                singleRotation += _solveUpTile(edgeToSolve, cubeAsString)
            case 5:
                singleRotation += _solveDownTile(edgeToSolve, cubeAsString)
            
        instancedCube.rotate(singleRotation)
        cubeAsString = instancedCube.get()
        
        rotations += singleRotation
        
        loopBreaker = loopBreaker + 1
        
    return rotations
#34 LOC
    
def _solvedBottomCrossCheck(cube):
    if cube[DTM] != cube[DMM]:
        return False
    if cube[DMR] != cube[DMM]:
        return False
    if cube[DBM] != cube[DMM]:
        return False
    if cube[DML] != cube[DMM]:
        return False
    if cube[FBM] != cube[FMM]:
        return False
    if cube[LBM] != cube[LMM]:
        return False
    if cube[RBM] != cube[RMM]:
        return False
    if cube[BBM] != cube[BMM]:
        return False
    else:
        return True
    #18 LOC
    
def _findEdges(cube):
    cubeString = cube
    downFaceTile = cube[DMM]
    allKeyTiles = [pos+INDEX_OFFSET for pos, char in enumerate(cubeString) if char == downFaceTile]
    
    keyCrossTiles = []
    for eachTile in allKeyTiles:
        if ((eachTile % NUM_OF_TILES) == TOP_MIDDLE_OS or (eachTile % NUM_OF_TILES) == MIDDLE_LEFT_OS or
             (eachTile % NUM_OF_TILES) == MIDDLE_RIGHT_OS or (eachTile % NUM_OF_TILES) == BOTTOM_MIDDLE_OS):
            keyCrossTiles.append(eachTile - INDEX_OFFSET)
            
    return keyCrossTiles
    #16 LOC
    
def _findEdgeMate(edge, cube):
    caseNumber = (edge + INDEX_OFFSET) // NUM_OF_TILES
    remainder = (edge + INDEX_OFFSET) % NUM_OF_TILES
    
    match caseNumber:
        case 0:
            if remainder == TOP_MIDDLE_OS:
                return cube[UBM]
            elif remainder == MIDDLE_LEFT_OS:
                return cube[LMR]
            elif remainder == MIDDLE_RIGHT_OS:
                return cube[RML]
            else:
                return cube[DTM]
        case 1:
            if remainder == TOP_MIDDLE_OS:
                return cube[UMR]
            elif remainder == MIDDLE_LEFT_OS:
                return cube[FMR]
            elif remainder == MIDDLE_RIGHT_OS:
                return cube[BML]
            else:
                return cube[DMR]
        case 2:
            if remainder == TOP_MIDDLE_OS:
                return cube[UTM]
            elif remainder == MIDDLE_LEFT_OS:
                return cube[RMR]
            elif remainder == MIDDLE_RIGHT_OS:
                return cube[LML]
            else:
                return cube[DBM]
        case 3:
            if remainder == TOP_MIDDLE_OS:
                return cube[UML]
            elif remainder == MIDDLE_LEFT_OS:
                return cube[BMR]
            elif remainder == MIDDLE_RIGHT_OS:
                return cube[FML]
            else:
                return cube[DML]
        case 4:
            if remainder == TOP_MIDDLE_OS:
                return cube[BTM]
            elif remainder == MIDDLE_LEFT_OS:
                return cube[LTM]
            elif remainder == MIDDLE_RIGHT_OS:
                return cube[RTM]
            else:
                return cube[FTM]
        case 5:
            if remainder == TOP_MIDDLE_OS:
                return cube[FBM]
            elif remainder == MIDDLE_LEFT_OS:
                return cube[LBM]
            elif remainder == MIDDLE_RIGHT_OS:
                return cube[RBM]
            else:
                return cube[BBM]
    return 'error'
#64 LOC

def _findTileToSolve(cube):
    edges = _findEdges(cube)
    
    for eachEdge in edges:
        if eachEdge not in [DTM, DML, DMR, DBM]:
            return eachEdge
        elif eachEdge == 46:
            if cube[FBM] != cube[FMM]:
                return eachEdge
        elif eachEdge == 48:
            if cube[LBM] != cube[LMM]:
                return eachEdge
        elif eachEdge == 50:
            if cube[RBM] != cube[RMM]:
                return eachEdge
        elif eachEdge == 52:
            if cube[BBM] != cube[BMM]:
                return eachEdge
        else:
            return -1
    
    return -1
#20 LOC
    
def _solveUpTile(edgeToSolve, cube: Cube):
    rotns = ''
    
    for key in edgeToSolve:
        
        match key:
            case 37:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'UUFF'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'URR'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'BB'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'uLL'
            case 39:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'uFF'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'UURR'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'UBB'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'LL'
            case 41:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'UFF'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'RR'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'uBB'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'UULL'
            case 43:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'FF'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'uRR'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'UUBB'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'ULL'
    
    return rotns
    #41 LOC
def _solveFrontTile(edgeToSolve, cube: Cube):
    rotns = ''
    
    for key in edgeToSolve:
        match key:
            case 1:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'ULfl'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'Frf'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'UlBL'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'fLF'
            case 3:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'luLFF'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'lUULRR'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'lULBB'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'L'
            case 5:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'RUrFF'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'R'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'RurBB'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'RUUrLL'
            case 7:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'FluLFF'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'fr'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'FFUlb'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'FL'
                
    return rotns
    #41 LOC
def _solveRightTile(edgeToSolve, cube: Cube):
    rotns = ''
    
    for key in edgeToSolve:
        match key:
            case 10:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'rFR'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'UFrf'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'Rbr'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'UfLF'
            case 12:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'F'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'fuFRR'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'fUUFBB'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'fUFLL'
            case 14:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'RRFrr'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'rUFrf'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'b'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'BubLL'
            case 16:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'RF'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'RRUFrf'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'rb'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'RRUfLF'
                
    return rotns
    #41 LOC
def _solveBackTile(edgeToSolve, cube: Cube):
    rotns = ''
    
    for key in edgeToSolve:
        match key:
            case 19:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'UrFR'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'bRB'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'BLUlBB'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'Blb'
            case 21:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'rURFF'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'R'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'BURbr'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'BBlBB'
            case 23:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'LUlFF'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'BBRBB'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'LUlBB'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'l'
            case 25:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'BBUrFR'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'BR'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'BBURbr'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'bl'

    return rotns
    #41 LOC
def _solveLeftTile(edgeToSolve, cube: Cube):
    rotns = ''
    
    for key in edgeToSolve:
        match key:
            case 28:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'Lfl'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'uFrF'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'lBL'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'LFUfLL'
            case 30:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'LLfll'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'LUlbRB'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'B'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'buBLL'
            case 32:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'f'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'FufRR'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'LLBll'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'FUfLL'
            case 34:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'lf'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'LLUURR'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'LB'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'LLUBlb'
                    
    return rotns
    #41 LOC

def _solveDownTile(edgeToSolve, cube: Cube):
    rotns = ''
    
    for key in edgeToSolve:
        match key:
            case 46:
                if edgeToSolve[key] == cube[FMM]:
                    return rotns
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'FFuRRUff'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'FFUUBBuuff'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'FFULLuff'
            case 48:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'LLuFFUll'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'LLUURRuull'
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'LLUBBull'
                elif edgeToSolve[key] == cube[LMM]:
                    return rotns
            case 50:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'RRUFFurr'
                elif edgeToSolve[key] == cube[RMM]:
                    return rotns
                elif edgeToSolve[key] == cube[BMM]:
                    rotns += 'RRuBBUrr'
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'RRUULLuurr'
            case 52:
                if edgeToSolve[key] == cube[FMM]:
                    rotns += 'BBUUFFuubb'
                elif edgeToSolve[key] == cube[RMM]:
                    rotns += 'BBURRubb'
                elif edgeToSolve[key] == cube[BMM]:
                    return rotns
                elif edgeToSolve[key] == cube[LMM]:
                    rotns += 'BBuLLUbb'

    return rotns
    #41 LOC
    
    
    