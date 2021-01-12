#Middle-Square method for random num generation.

seed = int(input("Please enter the number used as a seed : "))
length= len(str(seed))
while length % 2 != 0:
    seed = int(input("Please enter an even digit number as a seed : "))
    length= len(str(seed))
number = seed
seenNumber = set()

upperBound = length + length//2
lowerBound = length//2
counter = 0


while number not in seenNumber:
    counter +=1
    seenNumber.add(int(number))
    number = str(number * number).zfill(len(str(seed))*2)
    
    number = int(number[lowerBound:upperBound])
    print(number)
