import hashlib

cube = 'rggobwrobogybrywwwobrggbgbgygwrowrrwbybwyrboygyoywryoo'
rotations = ('RUrFFfUFLLRRUFrfBURbruufUFRUrUbuBFUfUruRuURUrufuFUuluLUFUfUUULUlubuB'
    + 'uuruRUBUbUUFURurfuRUrURUUrURUrURUUruRUrURUUrFFUrLFFlRUFFFFUrLFFlRUFF')
auburnId = 'jwh0100'


itemToTokenize = cube + rotations + auburnId


sha256Hash = hashlib.sha256()

sha256Hash.update(itemToTokenize.encode())

fullToken = sha256Hash.hexdigest()

print(fullToken)