import random
import time
import matplotlib.pyplot as plt
import statistics
import sys

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
        if arr[max_idx] < arr[left_child_idx] :
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
    start_time = time.time()
    n = len(arr)

    for i in range(n//2 -1, -1, -1):
        ilosc_porownan, zamiana_elementow = max_heap(arr, n, i, ilosc_porownan, zamiana_elementow)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        zamiana_elementow +=1
        ilosc_porownan, zamiana_elementow = max_heap(arr, i, 0, ilosc_porownan, zamiana_elementow)

    end_time = time.time()
    show_data((end_time-start_time), [], arr, ilosc_porownan, zamiana_elementow)
    return (end_time-start_time)


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
    #dopoki tablica ma dl wieksza niz 1 dzieli tablice
    while start < end:
        
        q= partition(arr, start, end,  piv_arr,ilosc_porownan_quick, zamiana_elementow_quick)
        # wywolaj dla krotszej czesci a potem zajmij sie wieksza
        if q - start < end - q: 
            
            quick_sort(arr, start, (q-1), piv_arr, ilosc_porownan_quick, zamiana_elementow_quick)
            start = q+1
        else:    

            quick_sort(arr, (q+1), end,  piv_arr, ilosc_porownan_quick, zamiana_elementow_quick)
            end = q-1
    



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
    # print("pivots: ", piv_arr)
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
  
        # Check if any element was left
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


ns = [1000*x for x in range(1, 11)]

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
        tm_arr.append(tm)
        std_arr.append(std)
    return tm_arr, std_arr



# measured_merge_time,  measured_merge_std = run_measurments(v_shaped, run_merge)
# measured_heap_time,  measured_heap_std = run_measurments(v_shaped, heap_sort)
# measured_quick_time,  measured_quick_std = run_measurments(v_shaped, run_quick_sort)
# measured_selection_time,  measured_selection_std = run_measurments(v_shaped, selection_sort)
# measured_bubble_time,  measured_bubble_std = run_measurments(v_shaped, bubble_sort)
# measured_insertion_time,  measured_insertion_std = run_measurments(v_shaped, insertion_sort)

# v = plt.errorbar(ns, measured_merge_time, yerr=measured_merge_std)
# a = plt.errorbar(ns, measured_heap_time, yerr=measured_heap_std)
# r = plt.errorbar(ns, measured_quick_time, yerr=measured_quick_std)
# i = plt.errorbar(ns, measured_selection_time, yerr=measured_selection_std)
# d = plt.errorbar(ns, measured_bubble_time, yerr=measured_bubble_std)
# k = plt.errorbar(ns, measured_insertion_time, yerr=measured_insertion_std)

# plt.figure()
# plt.title("Czas dla sortowania dla danych V-kształtnych")
# plt.xlabel("n")
# plt.ylabel("czas")

# plt.scatter(ns, measured_merge_time)
# plt.scatter(ns, measured_heap_time)
# plt.scatter(ns, measured_quick_time)
# plt.scatter(ns, measured_selection_time)
# plt.scatter(ns, measured_bubble_time)
# plt.scatter(ns, measured_insertion_time)
# plt.legend(['merge sort', 'heap sort', 'quick sort', 'selection sort', 'bubble sort', 'insertion sort'])
# plt.show()


# measured_vshape_time,  measured_vshape_std = run_measurments(v_shaped, run_quick_sort)

# measured_ashape_time, measured_ashape_std = run_measurments(a_shaped, run_quick_sort)

# measured_random_time, measured_random_std= run_measurments(random, run_quick_sort)

# measured_increasing_time, measured_increasing_std = run_measurments(increasing, run_quick_sort)

# measured_decreasing_time, measured_decreasing_std = run_measurments(decreasing, run_quick_sort)



# plt.title("Czas quick sort")
# plt.xlabel("n")
# plt.ylabel("czas")
# v = plt.errorbar(ns, measured_vshape_time, yerr=measured_vshape_std)
# a = plt.errorbar(ns, measured_ashape_time, yerr=measured_ashape_std)
# r = plt.errorbar(ns, measured_random_time, yerr=measured_random_std)
# i = plt.errorbar(ns, measured_increasing_time, yerr=measured_increasing_std)
# d = plt.errorbar(ns, measured_decreasing_time, yerr=measured_decreasing_std)


# plt.scatter(ns, measured_vshape_time)
# plt.scatter(ns, measured_ashape_time)
# plt.scatter(ns, measured_random_time)
# plt.scatter(ns, measured_increasing_time)
# plt.scatter(ns, measured_decreasing_time)
# plt.legend(['v kształtne', 'a-kształtne', 'losowe', 'rosnące', 'malejące'])
# plt.show()

#  a dluzsza podziel i wroc do warunku