#Puzzle: Day 05 ____________________
#Supply Stacks

def dataConverter(data):
    data = list(map(lambda x: list(map(int,'-'.join(x.split()[0].split(',')).split('-'))), open(data,'r')))
    return list(map(lambda x: (set(range(x[0],x[1]+1)), set(range(x[2],x[3]+1)))  ,data))




if __name__ == '__main__':
    data = dataConverter('05-Puzzle_Inputs.txt')
    

    
