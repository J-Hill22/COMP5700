'''
Constants used across the microservice 
'''

#-----------------------------------
#  Mapping of cube element positions to mnemonic names
#  Each mnemonic is a three-character pattern, frc, where
#       f indicates the face and is one of F, R, B, L, U, D
#       r indicates the row and is one of T, M, B (for top, middle, bottom, respectively)
#       c indicates the column and is one of L, M, R (for left, middle, right, repectively)
#  The regex for the pattern is r'[FRBLUD][TMB][LMR]'
#
# Front face
FTL = 0
FTM = 1
FTR = 2
FML = 3
FMM = 4
FMR = 5
FBL = 6
FBM = 7
FBR = 8

# Right face
RTL = 9
RTM = 10
RTR = 11
RML = 12
RMM = 13
RMR = 14
RBL = 15
RBM = 16
RBR = 17

# Back face
BTL = 18
BTM = 19
BTR = 20
BML = 21
BMM = 22
BMR = 23
BBL = 24
BBM = 25
BBR = 26

# Left face
LTL = 27
LTM = 28
LTR = 29
LML = 30
LMM = 31
LMR = 32
LBL = 33
LBM = 34
LBR = 35

# Up face
UTL = 36
UTM = 37
UTR = 38
UML = 39
UMM = 40
UMR = 41
UBL = 42
UBM = 43
UBR = 44

#Down face
DTL = 45
DTM = 46
DTR = 47
DML = 48
DMM = 49
DMR = 50
DBL = 51
DBM = 52
DBR = 53

#Constants of any cube face
NUM_OF_TILES = 9
TOP_LEFT = 0
TOP_MIDDLE = 1
TOP_RIGHT = 2
MIDDLE_LEFT = 3
MIDDLE = 4
MIDDLE_RIGHT = 5
BOTTOM_LEFT = 6
BOTTOM_MIDDLE = 7
BOTTOM_RIGHT = 8

#Constants of any cube face offset by for easier indexing
TOP_LEFT_OS = 1
TOP_MIDDLE_OS = 2
TOP_RIGHT_OS = 3
MIDDLE_LEFT_OS = 4
MIDDLE_OS = 5
MIDDLE_RIGHT_OS = 6
BOTTOM_LEFT_OS = 7
BOTTOM_MIDDLE_OS = 8
BOTTOM_RIGHT_OS = 0

INDEX_OFFSET = 1

#Constants for which face is which
FRONT_FACE = 0
RIGHT_FACE = 1
BACK_FACE = 2
LEFT_FACE = 3
UP_FACE = 4
DOWN_FACE = 5

