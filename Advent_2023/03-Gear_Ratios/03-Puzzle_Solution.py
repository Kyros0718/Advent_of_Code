#Puzzle: Day 03 ____________________
#Gear Ratios
file = open("03-Puzzle_Inputs.txt","r")

import re
def mapDigits(data):
    if type(data) == type(str()):
        return list(filter(lambda x: x != '', re.split(r'\D+',data) ))
    else:
        return list(map(lambda x: list(filter(lambda y: y != '' , re.split(r'\D+',x))), data))

def lineVision(data,index): #Give Vision Above & Below Line
    current = data[index]
    above = '.'*len(data[0])
    below = '.'*len(data[0])
    
    if index > 0:
        above = data[index-1]
    if index < len(data)-1:
        below = data[index+1]
        
    return [above,current,below]

def focusVision(line,val,refpoint): #set focused vision range around the value
    index1 = line.find(val,refpoint)
    index2 = index1+len(val)
    newrefpoint = index2
    
    if index1 > 0:
        index1-=1
    if index2 < len(line)+1:
        index2+=1
    
    return [index1,index2,newrefpoint]
    
def scanSymbols(val, index, data, ref_index, ref_point, ratio):
    #reset reference points for find()
    if ref_index[0] != index: #Incase of repeating values within the same lines
        ref_index[0] = index
        ref_point[0] = 0
        
    above,current,below = lineVision(data,index)
    
    index1,index2, ref_point[0] = focusVision(current,val,ref_point[0])
    
        
    if any([re.search('[^0-9.]',below[index1:index2]), re.search('[^0-9.]',current[index1:index2]), re.search('[^0-9.]',above[index1:index2])]):
        #Part 2_____
        if ratio and any([re.search('[*]',below[index1:index2]), re.search('[*]',current[index1:index2]), re.search('[*]',above[index1:index2])]):
            
            #Set Vision Above & Below '*'
            if above[index1:index2].find('*')>=0:
                gabove,gcurrent,gbelow = lineVision(data,index-1)
                
            elif current[index1:index2].find('*')>=0:
                gabove,gcurrent,gbelow = above,current,below
                
            elif below[index1:index2].find('*')>=0:
                gabove,gcurrent,gbelow = lineVision(data,index+1)
            
            #Set Focused Vision around '*'
            gindex1, gindex2 = focusVision(gcurrent,'*',index1)[:2]
            
            #Find Digits Around '*'
            fabove = mapDigits(gabove[gindex1:gindex2])
            fcurrent = mapDigits(gcurrent[gindex1:gindex2])
            fbelow = mapDigits(gbelow[gindex1:gindex2])
            
            
            if len(fabove+fcurrent+fbelow)==2: #
                if any([len(fabove)==2,len(fcurrent)==2,len(fbelow)==2]):
                    ratio_index = index
                    fline = current
                    
                elif (fabove and fcurrent) or (fcurrent and fbelow):
                    ratio_index = index+1
                    fline = below
                    
                else:
                    ratio_index = index+2
                    fline = gbelow
                    
                findex = fline[:gindex2].rfind(list(filter(lambda x: x!='', re.split(r'\D+',fline[:gindex2])))[-1])
                val2 = re.split(r'\D+',fline[findex:])[0]
                val = int(val)*int(val2)
                data[ratio_index] = fline[0:findex]+'.'*len(val2)+fline[findex+len(val2):]
                
                return val
            
        
        #Part 1_____       
        elif not ratio:
            return val


def engineParts(data):
    digit_map = mapDigits(data)
    
    ref_point = [0]
    ref_index = [0]
    
    parts = list(map(lambda x:
                 list(filter(lambda y: y!=None,
                             list(map(lambda z: scanSymbols(z,x,data,ref_index,ref_point, False),digit_map[x])))), range(len(data))))
    engine_parts = []
    list(map(lambda x: engine_parts.extend(x), parts))
    return sum(map(int,engine_parts))


def gearRatio(data):
    digit_map = mapDigits(data)

    ref_point = [0]
    ref_index = [0]
    
    parts = list(map(lambda x:
                 list(filter(lambda y: y!=None,
                             list(map(lambda z: scanSymbols(z,x,data,ref_index,ref_point, True),digit_map[x])))), range(len(data))))

    engine_parts = []
    list(map(lambda x: engine_parts.extend(x), parts))
    return sum(map(int,engine_parts))


if __name__ == '__main__':    
    data = list(map(lambda x: x.split()[0],file))
    #print(engineParts(data))
    print(gearRatio(data))
    
    
    

    


