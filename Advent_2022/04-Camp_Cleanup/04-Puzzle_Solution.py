#Puzzle: Day 03 ____________________
#Rucksack Reorganization

def dataConverter(data):
    data = list(map(lambda x: list(map(int,'-'.join(x.split()[0].split(',')).split('-'))), open(data,'r')))
    return list(map(lambda x: (set(range(x[0],x[1]+1)), set(range(x[2],x[3]+1)))  ,data))

#PART 1 _____
def fullOverlap(data):
    return list(map(lambda x: not bool(x[0]-x[1]) or not bool(x[1]-x[0]) ,data)).count(True) 

#PART 2 _____
def anyOverlap(data):
    return list(map(lambda x: bool(x[0]&x[1]) ,data)).count(True)


if __name__ == '__main__':
    data = dataConverter('04-Puzzle_Inputs.txt')
    
    print(f'Full Overlaps Amount: {fullOverlap(data)}')
    print(f'Any Overlaps Amount:  {anyOverlap(data)}')
 

    
