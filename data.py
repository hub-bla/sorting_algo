import statistics
import random
def create_random_list(length):
    return [(random.randrange(length)) for x in range (length)]


def A_shaped_data(length):
    n = length//2
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    for j in range(length-n, 0, -1):
        arr.append(j)

    return arr

def V_shaped_data(length):
    n = length//2
    arr = []
    for j in range(length-n, 0, -1):
        arr.append(j)
    for i in range(1, n+1):
        arr.append(i)

    return arr


def increasing_data(length):
    return [x for x in range(1, length+1)]

def decreasing_data(length):
    return [x for x in range(length, 0, -1)]


l1 = increasing_data(1021)

l2 = [3,2,1,4,6,1,2,6,3,1]



def measure_time(arr, f):
    std = []
    for i in range(10):
        new_arr = [*arr]
        k = f(new_arr)
        std.append(k)
    
    return statistics.fmean(std), statistics.pstdev(std)

def generate_data(ns, func):
    arr = []
    for i in range(len(ns)):
        arr.append(func(ns[i]))
    return arr








def run_measurments(data, func, ns):
    tm_arr = []
    std_arr = []
    for i in range(len(ns)):
        tm, std = measure_time(data[i], func)
        tm_arr.append(tm)
        std_arr.append(std)
    return tm_arr, std_arr