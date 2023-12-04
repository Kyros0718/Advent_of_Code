#Puzzle: Day 03 ____________________
#Gear Ratios
file = open("03-Puzzle_Inputs.txt","r")
import re

def mapDigits(data):
    return list(map(lambda x: list(filter(lambda y: y != '', re.split(r'\D+',x))), data))

def scanSymbols(val, index, data, digit_map, ref_index, ref_point, ratio):
    #reset reference points for find()
    if ref_index[0] != index: #Incase of repeating values within the same lines
        ref_index[0] = index
        ref_point[0] = 0
        
    #set vision above/below current line
    current = data[index]
    above = '.'*len(data[0])
    below = '.'*len(data[0])
    
    if index > 0:
        above = data[index-1]
    if index < len(data)-1:
        below = data[index+1]
    
    
    #set focused vision range
    index1 = current.find(val,ref_point[0])
    index2 = index1+len(val)
    ref_point[0] = index2
    
    if index1 > 0:
        index1-=1
    if index2 < len(data[0])+1:
        index2+=1
        
    if any([re.search('[^0-9.]',below[index1:index2]), re.search('[^0-9.]',current[index1:index2]), re.search('[^0-9.]',above[index1:index2])]):
        
        if ratio and any([re.search('[*]',below[index1:index2]), re.search('[*]',current[index1:index2]), re.search('[*]',above[index1:index2])]):
            #print(val)
            print(above[index1:index2].find('*'),current[index1:index2].find('*'),below[index1:index2].find('*'))
        else:
            return val

#Part 1_____
def engineParts(data):
    digit_map = mapDigits(data)
    
    ref_point = [0]
    ref_index = [0]
    
    parts = list(map(lambda x:
                 list(filter(lambda y: y!=None,
                             list(map(lambda z: scanSymbols(z,x,data,digit_map,ref_index,ref_point, False),digit_map[x])))), range(len(data))))
    engine_parts = []
    list(map(lambda x: engine_parts.extend(x), parts))
    return sum(map(int,engine_parts))

#Part 2_____
def gearRatio(data):
    digit_map = mapDigits(data)
    
    ref_point = [0]
    ref_index = [0]
    
    parts = list(map(lambda x:
                 list(filter(lambda y: y!=None,
                             list(map(lambda z: scanSymbols(z,x,data,digit_map,ref_index,ref_point, True),digit_map[x])))), range(len(data))))
    print(parts)
    return ''


if __name__ == '__main__':    
    data = list(map(lambda x: x.split()[0],file))
    #print(engineParts(data))
    print(gearRatio(data))
