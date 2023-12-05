#Puzzle: Day 03 ____________________
#Gear Ratios
file = open("03-Puzzle_Inputs.txt","r")
import re

def symbolIndex(line,symbol,refpoint): #Find Columns Index of Symbols
    index = line.find(symbol,refpoint[0])
    refpoint[0] = index+1
    return index

def mapCoordinates(data): #Find Coordinates of All Symbols: [rows,columns]
    map_gear = list(map(lambda x: list(filter(lambda y: y != '' , re.findall('[^0-9.]',x))), data)) #Find All Symbols
    map_index = list(filter(lambda x: x[1]!=[], enumerate(map_gear))) #Find Rows Index of Symbols
    
    refpoint = [0]
    coords = list(map(lambda x: [x[0],
                               list(map(lambda y: symbolIndex(data[x[0]],y,refpoint),x[1])),
                               refpoint.pop(),
                               refpoint.append(0)][:2], map_index))
    return coords

def partsValue(data,row,col): #Find and Remove Parts from Schematics
    if len(re.findall(r'\d+',data[row][col-1:col+2])) == 2:
        part1 = re.split(r'\D+',data[row][:col])[-1]
        part2 = re.split(r'\D+',data[row][col+1:])[0]
        data[row] = data[row][:col-len(part1)]+'.'*len(part1)+data[row][col]+'.'*len(part2)+data[row][col+len(part2)+1:]
        
        return part1+' '+part2
    
    elif len(re.findall(r'\d+',data[row][col-1:col+2])) == 1:
        index = data[row][:col+2].rfind(re.findall(r'\d+',data[row][:col+2])[-1])
        part1 =re.split(r'\D+',data[row][index:])[0]
        data[row] = data[row][:index]+'.'*len(part1)+data[row][index+len(part1):]
  
        return part1
    
    return ''

#Part1_____
def engineParts(data):
    coords = mapCoordinates(data)
    
    parts = list(map(lambda x: ' '.join(map(lambda y: scanEngine(data,x[0],y),x[1])), coords))
    parts = list(map(int,' '.join(parts).split()))
    
    return sum(parts)

def scanEngine(data,row,col):
    area = list(map(lambda x: partsValue(data,row+x,col),range(-1,2))) #AREA SCANNED: top,middle,bottom
    
    return ' '.join(area)


#Part2_____
def gearParts(data):
    coords = mapCoordinates(data)
    parts = list(map(lambda x: sum(list(map(lambda y: scanGears(data,x[0],y),x[1]))), coords))
 
    return sum(parts)

def scanGears(data,row,col):
    area = list(map(lambda x: re.findall(r'\d+',data[row+x][col-1:col+2]),range(-1,2)))
    if len(area[0])+len(area[1])+len(area[2]) == 2:
        area = list(map(lambda x: partsValue(data,row+x,col),range(-1,2)))
        part1,part2 = list(map(int,' '.join(area).split()))

        return part1*part2
    
    return 0
        

if __name__ == '__main__':    
    data = list(map(lambda x: '.'+x.split()[0]+'.',file)) #Add Borders Left/Right
    data = ['.'*len(data[0])]+data+['.'*len(data[0])] #Add Borders Up/Down
    datacopy = []
    
    datacopy[:] = data[:]
    print('Sum of All Parts:',engineParts(datacopy))
    
    datacopy[:] = data[:]
    print('Sum of All Gear Ratios:',gearParts(datacopy))

