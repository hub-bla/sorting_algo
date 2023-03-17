import random
import time
import matplotlib.pyplot as plt
import statistics
def show_data(sort_time, prev_arr, arr, ilosc_porownan, zamiana_elementow = None):
    if (len(arr) <= 10):
        print("lista przed sortowaniem: ", prev_arr)
        print("lista po sortowaniu: ", arr)
    # if(zamiana_elementow):
    #     print("zamiana elementow", zamiana_elementow)
    # print("ilosc porownan: ", ilosc_porownan)
    # print("czas sortowania: ", sort_time)

#
#INSERTION SORT
#

def insertion_sort(arr):
    arr = arr.copy()
    ilosc_porownan = 0
    zamiana_elementow = 0
    prev_arr = [*arr]
    start_time = time.time()
    for i in range(1, len(arr)):
        sprawdzany = arr[i]
        j =i-1
        while j>=0 and sprawdzany < arr[j]:
            arr[j+1] = arr[j]
            zamiana_elementow+=1
            ilosc_porownan +=1
            j-=1
        if (j == (i-1)):
            ilosc_porownan +=1

            
        arr[j+1] = sprawdzany
    end_time = time.time()
    show_data((end_time-start_time), prev_arr, arr, ilosc_porownan, zamiana_elementow)
    return (end_time-start_time)

def insertion_sort(array):
    now = time.time()
    if (n := len(array)) <= 1:
        return
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return time.time()-now

#
#SELECTION SORT
#

def selection_sort(arr):
    ilosc_porownan = 0
    zamiana_elementow = 0
    prev_arr = [*arr]
    start_time = time.time()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if (arr[min_idx]> arr[j]):
                min_idx = j
            ilosc_porownan+=1
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
        if(arr[min_idx] != arr[i]):
            zamiana_elementow +=1
    end_time = time.time()
    show_data((end_time-start_time), prev_arr, arr, ilosc_porownan, zamiana_elementow)
    return (end_time-start_time)



#
#BUBBLE SORT
#


def bubble_sort(arr):
    ilosc_porownan = 0
    zamiana_elementow = 0
    prev_arr = [*arr]
    start_time = time.time()
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if(arr[j+1]<arr[j]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                zamiana_elementow +=1
            ilosc_porownan +=1
    end_time = time.time()
    show_data((end_time-start_time), prev_arr, arr, ilosc_porownan, zamiana_elementow)
    return (end_time-start_time)



#
#HEAP SORT
#

def max_heap(arr, n, i, ilosc_porownan, zamiana_elementow):
    max_idx = i
    left_child_idx = 2*i +1
    right_child_idx = 2*i +2
    if(left_child_idx <n):
        if arr[max_idx] < arr[left_child_idx] and left_child_idx <n :
            max_idx = left_child_idx
        ilosc_porownan +=1
        
    if(right_child_idx < n):
        if arr[max_idx] < arr[right_child_idx]:
            max_idx = right_child_idx
        ilosc_porownan +=1
    #important part for cutting last element
    if max_idx != i:
        arr[max_idx], arr[i] = arr[i], arr[max_idx]
        zamiana_elementow+=1
        ilosc_porownan, zamiana_elementow = max_heap(arr, n, max_idx, ilosc_porownan, zamiana_elementow)
    return ilosc_porownan, zamiana_elementow

def heap_sort(arr):
    ilosc_porownan = 0
    zamiana_elementow = 0
    # prev_arr = [*arr]
    
    n = len(arr)

    for i in range(n//2 -1, -1, -1):
        ilosc_porownan, zamiana_elementow = max_heap(arr, n, i, ilosc_porownan, zamiana_elementow)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        zamiana_elementow +=1
        ilosc_porownan, zamiana_elementow = max_heap(arr, i, 0, ilosc_porownan, zamiana_elementow)

    
    
    

#
#QUICK SORT
#



def partition(arr, start, end,  piv_arr, ilosc_porownan_quick, zamiana_elementow_quick):
    pivot = arr[end]
    piv_arr.append(pivot)
    i = start - 1
  
    
    for j in range(start, end):
        if arr[j] <= pivot:
           
            i += 1
            arr[i], arr[j] = arr[j], arr[i]


            if (i!=j):
                zamiana_elementow_quick[0] +=1
        ilosc_porownan_quick[0] +=1

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    if (i!=j):
                zamiana_elementow_quick[0] +=1

    return i + 1


def quick_sort(arr, start, end, piv_arr, ilosc_porownan_quick, zamiana_elementow_quick):
    if start < end:
        
        q= partition(arr, start, end,  piv_arr,ilosc_porownan_quick, zamiana_elementow_quick)

        quick_sort(arr, start, (q-1), piv_arr, ilosc_porownan_quick, zamiana_elementow_quick)
        quick_sort(arr, (q+1), end,  piv_arr, ilosc_porownan_quick, zamiana_elementow_quick)



def run_quick_sort(arr, start=0):
    prev_arr = [*arr]
    end = len(arr)-1
    ilosc_porownan_quick = [0]
    zamiana_elementow_quick = [0]
    start_time = time.time()
    piv_arr= []
    quick_sort(arr, start, end,  piv_arr, ilosc_porownan_quick, zamiana_elementow_quick)

    end_time = time.time()
    show_data((end_time-start_time), prev_arr, arr, ilosc_porownan_quick[0], zamiana_elementow_quick[0])
    print("pivots: ", piv_arr)
    return (end_time-start_time)

#
#MERGE SORT
#

def merge_sort(arr, ilosc_porownan,scalanie):
    if len(arr) > 1:
  
        mid = len(arr)//2
  
        L = arr[:mid]
  
        R = arr[mid:]

        merge_sort(L, ilosc_porownan, scalanie)
  
        merge_sort(R, ilosc_porownan,scalanie)
        scalanie[0] +=1
        i =  0 #left arr
        j = 0  #right arr
        k = 0 #for index of our arr
        
        # Copy data to arrays L and R
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            ilosc_porownan[0] +=1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def run_merge(arr):
    ilosc_porownan = [0]
    scalanie =[0]
    prev_arr = [*arr]
    start_time = time.time()
    merge_sort(arr, ilosc_porownan, scalanie)
    end_time = time.time()
    # show_data((end_time-start_time), prev_arr, arr, ilosc_porownan[0])
    # print("ilosc scalan:", scalanie[0])

    return (end_time-start_time)



random.seed(1)



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


l1 = create_random_list(10)

l2 = [3,2,1,4,6,1,2,6,3,1]




ns = [1000*i for i in range(1,11)]
def measure_time(arr, f):
    std = []
    for i in range(10):
        start_time = time.time()
        f(arr)
        end_time = time.time()
        std.append((end_time -start_time))
    
    return statistics.fmean(std), statistics.pstdev(std)

def generate_data(ns, func):
    arr = []
    for i in range(len(ns)):
        arr.append(func(ns[i]))
    return arr


v_shaped = generate_data(ns, V_shaped_data)
a_shaped = generate_data(ns, A_shaped_data)
increasing = generate_data(ns, increasing_data)
decreasing = generate_data(ns, decreasing_data)
random = generate_data(ns, create_random_list)




def run_measurments(data, func):
    tm_arr = []
    std_arr = []
    for i in range(len(ns)):
        tm, std = measure_time(data[i], func)
        print(std)
        tm_arr.append(tm)
        std_arr.append(std)
    return tm_arr, std_arr



measured_vshape_time,  measured_vshape_std = run_measurments(v_shaped, heap_sort)

measured_ashape_time, measured_ashape_std = run_measurments(a_shaped, heap_sort)

measured_random_time, measured_random_std= run_measurments(random, heap_sort)

measured_increasing_time, measured_increasing_std = run_measurments(increasing, heap_sort)

measured_decreasing_time, measured_decreasing_std = run_measurments(decreasing, heap_sort)



plt.title("Czas heap sort")
plt.xlabel("n")
plt.ylabel("czas")
v = plt.errorbar(ns, measured_vshape_time, yerr=measured_vshape_std)
a = plt.errorbar(ns, measured_ashape_time, yerr=measured_ashape_std)
r = plt.errorbar(ns, measured_random_time, yerr=measured_random_std)
i = plt.errorbar(ns, measured_increasing_time, yerr=measured_increasing_std)
d = plt.errorbar(ns, measured_decreasing_time, yerr=measured_decreasing_std)


plt.scatter(ns, measured_vshape_time)
plt.scatter(ns, measured_ashape_time)
plt.scatter(ns, measured_random_time)
plt.scatter(ns, measured_increasing_time)
plt.scatter(ns, measured_decreasing_time)
plt.legend(['v kształtne', 'a-kształtne', 'losowe', 'rosnące', 'malejące'])
plt.show()