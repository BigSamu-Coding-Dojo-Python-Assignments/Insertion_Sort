import time

a = [2,3,5,6,8,1,4,7]
b = [6,3,7,4,8,2,5,1]
c = [8,2,5,7,1,4,3,6]

def insertion_sort(someList):
    start_time = time.time()
    for i in range(1,len(someList),1):
        j=i-1
        temp = someList[i]
        while temp < someList[j] and j>=0:     
            someList[j+1]= someList[j]
            j -=1
        someList[j+1] = temp
    end_time = time.time()
    print(end_time-start_time)
    return someList

print(insertion_sort(a))
print(insertion_sort(b))
print(insertion_sort(c))