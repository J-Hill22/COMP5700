'''
Created on Feb 2, 2023

@author: Jarrett
'''
from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self._cube = encodedCube
        
    def get(self):
        return self._cube
    
    def rotate(self, directions=''):
        validRotations = set('FfRrBbLlUu')
        if set(directions) <= validRotations:
            if (directions):
                for eachCharacter in directions:
                    match eachCharacter:
                        case 'F': 
                            self._rotateF()
                        case 'f':
                            self._rotatef()
                        case 'R':
                            self._rotateR()
                        case 'r':
                            self._rotater()
                        case 'B':
                            self._rotateB()
                        case 'b':
                            self._rotateb()
                        case 'L':
                            self._rotateL()
                        case 'l':
                            self._rotatel()
                        case 'U':
                            self._rotateU()
                        case 'u':
                            self._rotateu()
                        case _:
                            self._rotateF()
            else:
                self._rotateF()
            return self._cube
        else:
            return 'error: invalid rotation'
        
    

    def _rotateF(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotated the front face clockwise
        rotatedCubeList[FTR] = cubeList[FTL]
        rotatedCubeList[FMR] = cubeList[FTM]
        rotatedCubeList[FBR] = cubeList[FTR]
        rotatedCubeList[FTM] = cubeList[FML]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FBM] = cubeList[FMR]
        rotatedCubeList[FTL] = cubeList[FBL]
        rotatedCubeList[FML] = cubeList[FBM]
        rotatedCubeList[FBL] = cubeList[FBR]
    
        #rotate up to right
        rotatedCubeList[RTL] = cubeList[UBL]
        rotatedCubeList[RML] = cubeList[UBM]
        rotatedCubeList[RBL] = cubeList[UBR]
    
        #rotate right to down
        rotatedCubeList[DTR] = cubeList[RTL]
        rotatedCubeList[DTM] = cubeList[RML]
        rotatedCubeList[DTL] = cubeList[RBL]
    
        #rotate down to left
        rotatedCubeList[LTR] = cubeList[DTL]
        rotatedCubeList[LMR] = cubeList[DTM]
        rotatedCubeList[LBR] = cubeList[DTR]
    
        #rotate left to up
        rotatedCubeList[UBR] = cubeList[LTR]
        rotatedCubeList[UBM] = cubeList[LMR]
        rotatedCubeList[UBL] = cubeList[LBR]
        
        self._cube = "".join(rotatedCubeList)

    def _rotatef(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotated the front face
        rotatedCubeList[FBL] = cubeList[FTL]
        rotatedCubeList[FML] = cubeList[FTM]
        rotatedCubeList[FTL] = cubeList[FTR]
        rotatedCubeList[FBM] = cubeList[FML]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FTM] = cubeList[FMR]
        rotatedCubeList[FBR] = cubeList[FBL]
        rotatedCubeList[FMR] = cubeList[FBM]
        rotatedCubeList[FTR] = cubeList[FBR]
    
        #rotate up to left
        rotatedCubeList[LBR] = cubeList[UBL]
        rotatedCubeList[LMR] = cubeList[UBM]
        rotatedCubeList[LTR] = cubeList[UBR]
     
        #rotate right to top
        rotatedCubeList[UBL] = cubeList[RTL]
        rotatedCubeList[UBM] = cubeList[RML]
        rotatedCubeList[UBR] = cubeList[RBL]
     
        #rotate bottom to right
        rotatedCubeList[RBL] = cubeList[DTL]
        rotatedCubeList[RML] = cubeList[DTM]
        rotatedCubeList[RTL] = cubeList[DTR]
     
        #rotate left to bottom
        rotatedCubeList[DTL] = cubeList[LTR]
        rotatedCubeList[DTM] = cubeList[LMR]
        rotatedCubeList[DTR] = cubeList[LBR]
        
        self._cube = "".join(rotatedCubeList)
        
    def _rotateR(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate the right face clockwise
        rotatedCubeList[RTR] = cubeList[RTL]
        rotatedCubeList[RMR] = cubeList[RTM]
        rotatedCubeList[RBR] = cubeList[RTR]
        rotatedCubeList[RTM] = cubeList[RML]
        rotatedCubeList[RMM] = cubeList[RMM]
        rotatedCubeList[RBM] = cubeList[RMR]
        rotatedCubeList[RTL] = cubeList[RBL]
        rotatedCubeList[RML] = cubeList[RBM]
        rotatedCubeList[RBL] = cubeList[RBR]
    
        #rotate up to back 
        rotatedCubeList[BTL] = cubeList[UBR]
        rotatedCubeList[BML] = cubeList[UMR]
        rotatedCubeList[BBL] = cubeList[UTR]
    
        #rotate back to down
        rotatedCubeList[DBR] = cubeList[BTL]
        rotatedCubeList[DMR] = cubeList[BML]
        rotatedCubeList[DTR] = cubeList[BBL]
    
        #rotate down to front
        rotatedCubeList[FTR] = cubeList[DTR]
        rotatedCubeList[FMR] = cubeList[DMR]
        rotatedCubeList[FBR] = cubeList[DBR]
    
        #rotate front to up
        rotatedCubeList[UTR] = cubeList[FTR]
        rotatedCubeList[UMR] = cubeList[FMR]
        rotatedCubeList[UBR] = cubeList[FBR]
        
        self._cube = "".join(rotatedCubeList)
        
    def _rotater(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate the right face counter clockwise
        rotatedCubeList[RBL] = cubeList[RTL]
        rotatedCubeList[RML] = cubeList[RTM]
        rotatedCubeList[RTL] = cubeList[RTR]
        rotatedCubeList[RBM] = cubeList[RML]
        rotatedCubeList[RMM] = cubeList[RMM]
        rotatedCubeList[RTM] = cubeList[RMR]
        rotatedCubeList[RBR] = cubeList[RBL]
        rotatedCubeList[RMR] = cubeList[RBM]
        rotatedCubeList[RTR] = cubeList[RBR]
    
        #rotate up to front 
        rotatedCubeList[FBR] = cubeList[UBR]
        rotatedCubeList[FMR] = cubeList[UMR]
        rotatedCubeList[FTR] = cubeList[UTR]
    
        #rotate front to down
        rotatedCubeList[DTR] = cubeList[FTR]
        rotatedCubeList[DMR] = cubeList[FMR]
        rotatedCubeList[DBR] = cubeList[FBR]
    
        #rotate down to back
        rotatedCubeList[BBL] = cubeList[DTR]
        rotatedCubeList[BML] = cubeList[DMR]
        rotatedCubeList[BTL] = cubeList[DBR]
    
        #rotate back to up
        rotatedCubeList[UBR] = cubeList[BTL]
        rotatedCubeList[UMR] = cubeList[BML]
        rotatedCubeList[UTR] = cubeList[BBL]
        
        self._cube = "".join(rotatedCubeList)
        
    def _rotateB(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate back clockwise
        rotatedCubeList[BTR] = cubeList[BTL]
        rotatedCubeList[BMR] = cubeList[BTM]
        rotatedCubeList[BBR] = cubeList[BTR]
        rotatedCubeList[BTM] = cubeList[BML]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BBM] = cubeList[BMR]
        rotatedCubeList[BTL] = cubeList[BBL]
        rotatedCubeList[BML] = cubeList[BBM]
        rotatedCubeList[BBL] = cubeList[BBR]
    
        #rotate up to left
        rotatedCubeList[LBL] = cubeList[UTL]
        rotatedCubeList[LML] = cubeList[UTM]
        rotatedCubeList[LTL] = cubeList[UTR]
    
        #rotate left to down
        rotatedCubeList[DBL] = cubeList[LTL]
        rotatedCubeList[DBM] = cubeList[LML]
        rotatedCubeList[DBR] = cubeList[LBL]
    
        #rotate down to right
        rotatedCubeList[RBR] = cubeList[DBL]
        rotatedCubeList[RMR] = cubeList[DBM]
        rotatedCubeList[RTR] = cubeList[DBR]
    
        #rotate right to up
        rotatedCubeList[UTL] = cubeList[RTR]
        rotatedCubeList[UTM] = cubeList[RMR]
        rotatedCubeList[UTR] = cubeList[RBR]
        
        self._cube = "".join(rotatedCubeList)
        
    def _rotateb(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate back counter clockwise
        rotatedCubeList[BBL] = cubeList[BTL]
        rotatedCubeList[BML] = cubeList[BTM]
        rotatedCubeList[BTL] = cubeList[BTR]
        rotatedCubeList[BBM] = cubeList[BML]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BTM] = cubeList[BMR]
        rotatedCubeList[BBR] = cubeList[BBL]
        rotatedCubeList[BMR] = cubeList[BBM]
        rotatedCubeList[BTR] = cubeList[BBR]
    
        #rotate up to right
        rotatedCubeList[RTR] = cubeList[UTL]
        rotatedCubeList[RMR] = cubeList[UTM]
        rotatedCubeList[RBR] = cubeList[UTR]
    
        #rotate left to up
        rotatedCubeList[UTR] = cubeList[LTL]
        rotatedCubeList[UTM] = cubeList[LML]
        rotatedCubeList[UTL] = cubeList[LBL]
    
        #rotate down to left
        rotatedCubeList[LTL] = cubeList[DBL]
        rotatedCubeList[LML] = cubeList[DBM]
        rotatedCubeList[LBL] = cubeList[DBR]
    
        #rotate right to down
        rotatedCubeList[DBR] = cubeList[RTR]
        rotatedCubeList[DBM] = cubeList[RMR]
        rotatedCubeList[DBL] = cubeList[RBR]
        
        self._cube = "".join(rotatedCubeList)
    
    def _rotateL(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate left face clockwise
        rotatedCubeList[LTR] = cubeList[LTL]
        rotatedCubeList[LMR] = cubeList[LTM]
        rotatedCubeList[LBR] = cubeList[LTR]
        rotatedCubeList[LTM] = cubeList[LML]
        rotatedCubeList[LMM] = cubeList[LMM]
        rotatedCubeList[LBM] = cubeList[LMR]
        rotatedCubeList[LTL] = cubeList[LBL]
        rotatedCubeList[LML] = cubeList[LBM]
        rotatedCubeList[LBL] = cubeList[LBR]
    
        #rotate up to front
        rotatedCubeList[FTL] = cubeList[UTL]
        rotatedCubeList[FML] = cubeList[UML]
        rotatedCubeList[FBL] = cubeList[UBL]
    
        #rotate front to down
        rotatedCubeList[DTL] = cubeList[FTL]
        rotatedCubeList[DML] = cubeList[FML]
        rotatedCubeList[DBL] = cubeList[FBL]
    
        #rotate down to back
        rotatedCubeList[BBR] = cubeList[DTL]
        rotatedCubeList[BMR] = cubeList[DML]
        rotatedCubeList[BTR] = cubeList[DBL]
    
        #rotate back to up
        rotatedCubeList[UBL] = cubeList[BTR]
        rotatedCubeList[UML] = cubeList[BMR]
        rotatedCubeList[UTL] = cubeList[BBR]
        
        self._cube = "".join(rotatedCubeList)    
        
    def _rotatel(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate left face counter clockwise
        rotatedCubeList[LBL] = cubeList[LTL]
        rotatedCubeList[LML] = cubeList[LTM]
        rotatedCubeList[LTL] = cubeList[LTR]
        rotatedCubeList[LBM] = cubeList[LML]
        rotatedCubeList[LMM] = cubeList[LMM]
        rotatedCubeList[LTM] = cubeList[LMR]
        rotatedCubeList[LBR] = cubeList[LBL]
        rotatedCubeList[LMR] = cubeList[LBM]
        rotatedCubeList[LTR] = cubeList[LBR]
    
        #rotate up to back
        rotatedCubeList[BBR] = cubeList[UTL]
        rotatedCubeList[BMR] = cubeList[UML]
        rotatedCubeList[BTR] = cubeList[UBL]
    
        #rotate front to up
        rotatedCubeList[UTL] = cubeList[FTL]
        rotatedCubeList[UML] = cubeList[FML]
        rotatedCubeList[UBL] = cubeList[FBL]
    
        #rotate down to front
        rotatedCubeList[FTL] = cubeList[DTL]
        rotatedCubeList[FML] = cubeList[DML]
        rotatedCubeList[FBL] = cubeList[DBL]
    
        #rotate back to down
        rotatedCubeList[DBL] = cubeList[BTR]
        rotatedCubeList[DML] = cubeList[BMR]
        rotatedCubeList[DTL] = cubeList[BBR]
        
        self._cube = "".join(rotatedCubeList)    
               
    def _rotateU(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate up face clockwise
        rotatedCubeList[UTR] = cubeList[UTL]
        rotatedCubeList[UMR] = cubeList[UTM]
        rotatedCubeList[UBR] = cubeList[UTR]
        rotatedCubeList[UTM] = cubeList[UML]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UBM] = cubeList[UMR]
        rotatedCubeList[UTL] = cubeList[UBL]
        rotatedCubeList[UML] = cubeList[UBM]
        rotatedCubeList[UBL] = cubeList[UBR]
    
        #rotate back to right
        rotatedCubeList[RTR] = cubeList[BTR]
        rotatedCubeList[RTM] = cubeList[BTM]
        rotatedCubeList[RTL] = cubeList[BTL]
    
        #rotate right to front
        rotatedCubeList[FTR] = cubeList[RTR]
        rotatedCubeList[FTM] = cubeList[RTM]
        rotatedCubeList[FTL] = cubeList[RTL]
    
        #rotate front left
        rotatedCubeList[LTR] = cubeList[FTR]
        rotatedCubeList[LTM] = cubeList[FTM]
        rotatedCubeList[LTL] = cubeList[FTL]
    
        #rotate left back
        rotatedCubeList[BTR] = cubeList[LTR]
        rotatedCubeList[BTM] = cubeList[LTM]
        rotatedCubeList[BTL] = cubeList[LTL]
        
        self._cube = "".join(rotatedCubeList)
        
    def _rotateu(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate up face counter clockwise
        rotatedCubeList[UBL] = cubeList[UTL]
        rotatedCubeList[UML] = cubeList[UTM]
        rotatedCubeList[UTL] = cubeList[UTR]
        rotatedCubeList[UBM] = cubeList[UML]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UTM] = cubeList[UMR]
        rotatedCubeList[UBR] = cubeList[UBL]
        rotatedCubeList[UMR] = cubeList[UBM]
        rotatedCubeList[UTR] = cubeList[UBR]
    
        #rotate back to left
        rotatedCubeList[LTR] = cubeList[BTR]
        rotatedCubeList[LTM] = cubeList[BTM]
        rotatedCubeList[LTL] = cubeList[BTL]
    
        #rotate right to back
        rotatedCubeList[BTR] = cubeList[RTR]
        rotatedCubeList[BTM] = cubeList[RTM]
        rotatedCubeList[BTL] = cubeList[RTL]
    
        #rotate front to right
        rotatedCubeList[RTR] = cubeList[FTR]
        rotatedCubeList[RTM] = cubeList[FTM]
        rotatedCubeList[RTL] = cubeList[FTL]
    
        #rotate left to front
        rotatedCubeList[FTR] = cubeList[LTR]
        rotatedCubeList[FTM] = cubeList[LTM]
        rotatedCubeList[FTL] = cubeList[LTL]
        
        self._cube = "".join(rotatedCubeList)
        
        
    def isValidCube(self):
        cubeToValidate = self._cube
        cubeList = list(self._cube)
        validCubeSet = set('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        validCubeLength = 54
        validUniquesList = cubeList[4::9]
        validUniques = len(validUniquesList) == len(set(validUniquesList))
        
        for eachUnique in validUniquesList:
            if cubeToValidate.count(eachUnique) != 9:
                return False
        
        if set(cubeToValidate) <= validCubeSet:
            if len(cubeToValidate) == validCubeLength:
                if validUniques:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def rightTrigger(self, face=''):
        match face:
            case 'F':
                return 'RUr'
            case 'R':
                return 'BUb'
            case 'B':
                return 'LUl'
            case 'L':
                return 'FUf'
#10 LOC
    
    def leftTrigger(self, face=''):
        match face:
            case 'F':
                return 'luL'
            case 'R':
                return 'fuF'
            case 'B':
                return 'ruR'
            case 'L':
                return 'buB'
            
#10 LOC

    def modRightTrigger(self, face=''):
        match face:
            case 'F':
                return 'URUr'
            case 'R':
                return 'UBUb'
            case 'B':
                return 'ULUl'
            case 'L':
                return 'UFUf'
            
    def modLeftTrigger(self, face=''):
        match face:
            case 'F':
                return 'uluL'
            case 'R':
                return 'ufuF'
            case 'B':
                return 'uruR'
            case 'L':
                return 'ubuB'
            
    def FURurf(self):
        return 'FURurf'
    
    def RUrURUUr(self):
        return 'RUrURUUr'
    
    def lURuLUr(self, face = ''):
        match face:
            case 'L':
                return 'lURuLUr'
            case 'F':
                return 'fUBuFUb'
            case 'R':
                return 'rULuRUl'
            case 'B':
                return 'bUFuBUf'
            case _:
                return ''
            
    def modRUrURUUr(self, face = ''):
        match face:
            case 'L':
                return 'RUrURUUr'
            case 'F':
                return 'BUbUBUUb'
            case 'R':
                return 'LUlULUUl'
            case 'B':
                return 'FUfUFUUf'
            case _:
                return ''
            
    def modFFUrLFFlRUFF(self, face = ''):
        match face:
            case 'B':
                return 'FFUrLFFlRUFF'
            case 'L':
                return 'RRUbFRRfBURR'
            case 'F':
                return 'BBUlRBBrLUBB'
            case 'R':
                return 'LLUfBLLbFULL'
            case _:
                return 'FFUrLFFlRUFF'
#I1: 249 LOC
#I2: 20 LOC     
#I3: 20 LOC
#I4: 20 LOC
#I5: 4 LOC 
#I6: 36
        
#change test 123

    def _testingForGit(self):
        return None
        
        
        
        
        
        
        
        