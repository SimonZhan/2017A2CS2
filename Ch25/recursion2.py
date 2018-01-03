def groupsum(i,X,y):
    if y == 0:
        return True
    if i == len(X):
        return (y==0)
    return groupsum(i+1,X,y-X[i]) or groupsum(i+1,X,y)

def groupnoAdj(i,X,y):
    if y == 0:
        return True
    if i == len(X):
        return (y==0)
    return groupnoAdj(i+2,X,y) or groupnoAdj(i+2,X,y-X[i])

def groupsum5(i,X,y):
    if i == len(X):
        return (y==0)
    if X[i] % 5==0:
        return groupsum5(i+1,X,y-X[i])
    else:
        return groupsum5(i+1,X,y) or groupsum5(i+1,X,y-X[i])


def groupSum6(i,X,y):
    if X[i]==6:
        y = y -6
        if y == 0:
            return True
        if i == len(X):
            return False
        return groupSum6(i+1,X,y-X[i])
    else:
        if y == 0:
            return True
        if i == len(X):
            return False
        return groupSum6(i+1,X,y) or groupSum6(i+1,X,y-X[i])

def groupSumclump(start,array,target,x=1):
    if target==0:
        return True
    if start >= len(array):
        return False
    while array[start+1]==array[start]:
        x = x+1
        start+=1
    return groupSumclump(start+x,array,target-array[start]*x) or groupSumclump(start+x,array,target)


def spiltArray(i,X,x,y):
    if i == len(X):
        if x == y:
            return True
        else:
            return False
    return spiltArray(i+1,X,x=x+X[i],y=0) or spiltArray(i+1,X,x=0,y=y+X[i])

def spiltOdd10(i,X,x,y):
    if i == len(X):
        if x%10==0:
            if y%2 != 0:
                return True
            else:
                return False
    return spiltOdd10(i+1,X,x=x+X[i],y) or spiltOdd10(i+1,X,x,y=y+X[i])

def spilt53(i,X,x,y):
    if X[i]%5==0:
        return spilt53(i+1,X,x=x+X[i],y=0)
    elif:
        return spilt53(i+1,X,x=0,y=y+X[i])
    elif i == len(X):
        if x == y:
            return True
        else:
            return False
    return spilt53(i+1,X,x=x+X[i],y=0) or spilt53(i+1,X,x=0,y=y+X[i])







