from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    if (parms.get('cube') == None):
        result['status'] ='error: cube is missing'
        return result
    
    encodedCube = parms.get('cube')
    
    theCube = Cube(encodedCube)
    if (not theCube.isValidCube()):
        result['status'] = 'error: invalid cube'
        return result
    
    directions = parms.get('dir')
    
    if (directions == None):
        directions = ''
    
    validRotations = set('FfRrBbLlUu')
    
    if set(directions) <= validRotations:
        theCube.rotate(directions)
    else:
        result['status'] = 'error: invalid rotation'
        return result
    
    result['cube'] = theCube.get()
    result['status'] = 'ok'                     
    return result