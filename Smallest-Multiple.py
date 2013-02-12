divisor = 20

def checkDivis(checkNum):
    for i in range(1, 20):
        if(checkNum % i == 0):
            continue
        else:
            return False
    return True
    
while 1:
    if checkDivis(divisor):
        print divisor
        break
    else:
        divisor += 20