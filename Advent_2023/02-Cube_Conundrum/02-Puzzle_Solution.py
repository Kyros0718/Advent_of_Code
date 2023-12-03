#Puzzle: Day 02 ____________________
#Cube Conundrum
file = open("02-Puzzle_Inputs.txt","r")

#Data Conversion_____
def dictAssign(key,val,dic):
    dic[key] = val

def rgbFormat(rgblist):
    rgb = {'red':0,'green':0,'blue':0}
    list(map(lambda x: dictAssign(x.split()[1],int(x.split()[0]),rgb), rgblist))
    
    return [rgb['red'],rgb['green'],rgb['blue']]

def rgbDict(data):
    cubes = {}
    rgblist = list(map(lambda x: [x[0]]+list(map(lambda y: y.split(', '),x[1:])), data))
    stuff = list(map(lambda x: dictAssign(x[0],list(map(lambda y: rgbFormat(y), x[1:])), cubes), rgblist))
    return cubes

    
#Part 1_____
def possibleGame(rgblist, datadict):
    max_rgb = {}
    list(map(lambda x: dictAssign(x,list(map(lambda y: max(y),list(zip(*datadict[x])))) ,max_rgb), datadict))
    possible = list(filter(lambda x: all([max_rgb[x][0]<=rgblist[0],max_rgb[x][1]<=rgblist[1],max_rgb[x][2]<=rgblist[2]]),max_rgb))
    
    return sum(map(int,possible))

#Part 2_____
def cubePower(datadict):
    max_rgb = {}
    list(map(lambda x: dictAssign(x,list(map(lambda y: max(y),list(zip(*datadict[x])))) ,max_rgb), datadict))
    power = list(map(lambda x: max_rgb[x][0]*max_rgb[x][1]*max_rgb[x][2], max_rgb))
    
    return sum(power)


if __name__ == '__main__':    
    data = list(map(lambda x: [x.split()[1][:-1]]+' '.join(x.split()[2:]).split('; '), file))
    data = rgbDict(data)
    
    print("Sum Of Possible Game's ID:", possibleGame([12,13,14],data))
    print("Sum of Power Sets:", cubePower(data))
    

