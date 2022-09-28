from operator import indexOf
import random
import matplotlib.pyplot as plt

# binary search function returning 
# number of repetitions 
def binary_search(arr, target, high = 1, low= 0, count = 1):
    if count == 1:
        high = len(arr)-1

    if high >= low:    
        mid = (high+low)//2
        if arr[mid] == target:
            return count
        elif arr[mid] > target:
            return binary_search(arr, target, mid-1, low, count+1)
        else:
            return binary_search(arr, target, high, mid+1, count+1)
    else: 
        return count

# linear search function returning 
# number of repitions
def linear_search(arr, target):
    count = 1
    for int in range(len(arr)):
        if arr[int] == target:
            return count
        count+=1
    print("failed")
    return count

# Graphing time effeciency of 
# linear vs binary search
def many_searches(accuracy):
    avg_count_l = 0
    avg_count_b = 0
    avg_count_lst_b = []
    avg_count_lst_l = []
    size_lst = []
    for x in range(100):
        size = random.randint(0, 10000)
        for y in range(accuracy):
            arr = random.sample(range(1000000), size)
            target = arr[random.randint(0, size-1)]
            avg_count_b += (binary_search(sorted(arr), target))
            avg_count_l += (linear_search(arr, target))
        avg_count_lst_b.append(avg_count_b//accuracy)
        avg_count_lst_l.append(avg_count_l//accuracy)
        size_lst.append(size)
    print(avg_count_lst_b, size_lst)
    # plt.scatter(size_lst, avg_count_lst_b, label ="Binary")
    # plt.scatter(size_lst, avg_count_lst_l, label="Linear")
    # plt.xlabel("Size of Array")
    # plt.ylabel("Avg Number of Iterations")
    # plt.legend()
    # plt.show()

many_searches(10)

# THE AVG COUNT LSTS DONT MAKE SENSE