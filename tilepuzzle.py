#Name:Ranxin Li
#Date: Apr.14th.2022
import copy
listbeingreturn=[]
def tilepuzzle(init, final, maxdepth):
    initcopy=copy.deepcopy(init)
    listbeingreturn.append(initcopy)
    changestatus(init,final, 0, maxdepth)
        
    return listbeingreturn

def changestatus(current, final,depth, maxdepth):
    if depth == maxdepth:
        return False

    if current==final:
        return True

    zerocoor_i=0
    zerocoor_j=0
    findzero=False
    for i in range(0,3):
        for j in range(0,3):
            if current[i][j]== 0:
                zerocoor_i=i
                zerocoor_j=j
                findzero=True
        if findzero:
            break

    if zerocoor_i !=0:
        
        current[zerocoor_i][zerocoor_j],current[zerocoor_i-1][zerocoor_j]=current[zerocoor_i-1][zerocoor_j],current[zerocoor_i][zerocoor_j]
        currentcopy=copy.deepcopy(current)
        listbeingreturn.append(currentcopy)
        if changestatus(current, final, depth+1, maxdepth):
            
            return True
        else:
            current[zerocoor_i][zerocoor_j],current[zerocoor_i-1][zerocoor_j]=current[zerocoor_i-1][zerocoor_j],current[zerocoor_i][zerocoor_j]
            listbeingreturn.pop()

    if zerocoor_j !=0:
        
        current[zerocoor_i][zerocoor_j],current[zerocoor_i][zerocoor_j-1]=current[zerocoor_i][zerocoor_j-1],current[zerocoor_i][zerocoor_j]
        currentcopy=copy.deepcopy(current)
        listbeingreturn.append(currentcopy)
        if changestatus(current, final, depth+1, maxdepth):
            
            return True
        else:
            current[zerocoor_i][zerocoor_j],current[zerocoor_i][zerocoor_j-1]=current[zerocoor_i][zerocoor_j-1],current[zerocoor_i][zerocoor_j]
            listbeingreturn.pop()
            
    if zerocoor_i !=2:
        
        current[zerocoor_i][zerocoor_j],current[zerocoor_i+1][zerocoor_j]=current[zerocoor_i+1][zerocoor_j],current[zerocoor_i][zerocoor_j]
        currentcopy=copy.deepcopy(current)
        listbeingreturn.append(currentcopy)
        if changestatus(current, final, depth+1, maxdepth):
            
            return True
        else:
            current[zerocoor_i][zerocoor_j],current[zerocoor_i+1][zerocoor_j]=current[zerocoor_i+1][zerocoor_j],current[zerocoor_i][zerocoor_j]
            listbeingreturn.pop()
            
    if zerocoor_j !=2:
        
        current[zerocoor_i][zerocoor_j],current[zerocoor_i][zerocoor_j+1]=current[zerocoor_i][zerocoor_j+1],current[zerocoor_i][zerocoor_j]
        currentcopy=copy.deepcopy(current)
        listbeingreturn.append(currentcopy)
        if changestatus(current, final, depth+1, maxdepth):
            
            return True
        else:
            current[zerocoor_i][zerocoor_j],current[zerocoor_i][zerocoor_j+1]=current[zerocoor_i][zerocoor_j+1],current[zerocoor_i][zerocoor_j]
            listbeingreturn.pop()
    return False

