print("Give me the intervals,seperated with "," ")
list=input()
def sumIntervals(intervals):
    numbers=set()
    for inval in intervals:#inval is one of the intervals
        for i in range(inval[0],inval[1]):
            numbers.add(i)
    return len(numbers)
print(sumIntervals(list))
