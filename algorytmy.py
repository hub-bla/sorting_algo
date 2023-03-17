import random
from time import process_time
import time

def show_data(sort_time, prev_arr, arr, ilosc_porownan, zamiana_elementow = None):
    if (len(arr) <= 10):
        print("lista przed sortowaniem: ", prev_arr)
        print("lista po sortowaniu: ", arr)
    if(zamiana_elementow):
        print("zamiana elementow", zamiana_elementow)
    print("ilosc porownan: ", ilosc_porownan)
    print("czas sortowania: ", sort_time)

#
#INSERTION SORT
#

def insertion_sort(arr):
    ilosc_porownan = 0
    zamiana_elementow = 0
    prev_arr = [*arr]
    start_time = process_time()
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
    end_time = process_time()
    show_data(("{:.14f}".format(end_time-start_time)), prev_arr, arr, ilosc_porownan, zamiana_elementow)


#
#SELECTION SORT
#

def selection_sort(arr):
    ilosc_porownan = 0
    zamiana_elementow = 0
    prev_arr = [*arr]
    start_time = process_time()
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
    end_time = process_time()
    show_data(("{:.14f}".format(end_time-start_time)), prev_arr, arr, ilosc_porownan, zamiana_elementow)



#
#BUBBLE SORT
#


def bubble_sort(arr):
    ilosc_porownan = 0
    zamiana_elementow = 0
    prev_arr = [*arr]
    start_time = process_time()
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if(arr[j+1]<arr[j]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                zamiana_elementow +=1
            ilosc_porownan +=1
    end_time = process_time()
    show_data(("{:.14f}".format(end_time-start_time)), prev_arr, arr, ilosc_porownan, zamiana_elementow)



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
    #dla odnawiania kopca maksymalnego
    if max_idx != i:
        arr[max_idx], arr[i] = arr[i], arr[max_idx]
        zamiana_elementow+=1
        ilosc_porownan, zamiana_elementow = max_heap(arr, n, max_idx, ilosc_porownan, zamiana_elementow)
    return ilosc_porownan, zamiana_elementow

def heap_sort(arr):
    ilosc_porownan = 0
    zamiana_elementow = 0
    prev_arr = [*arr]
    start_time = process_time()
    n = len(arr)

    for i in range(n//2 -1, -1, -1):
        ilosc_porownan, zamiana_elementow = max_heap(arr, n, i, ilosc_porownan, zamiana_elementow)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        zamiana_elementow +=1
        ilosc_porownan, zamiana_elementow = max_heap(arr, i, 0, ilosc_porownan, zamiana_elementow)

    end_time = process_time()
    show_data(("{:.14f}".format(end_time-start_time)), prev_arr, arr, ilosc_porownan, zamiana_elementow)


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
    



def run_quick_sort(arr, start, end):
    prev_arr = [*arr]
    
    ilosc_porownan_quick = [0]
    zamiana_elementow_quick = [0]
    start_time = process_time()
    piv_arr= []
    quick_sort(arr, start, end,  piv_arr, ilosc_porownan_quick, zamiana_elementow_quick)

    end_time = process_time()
    show_data(("{:.14f}".format(end_time-start_time)), prev_arr, arr, ilosc_porownan_quick[0], zamiana_elementow_quick[0])
    if (len(arr)<=10):
        print("pivots: ", piv_arr)

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
    start_time = process_time()
    merge_sort(arr, ilosc_porownan, scalanie)
    end_time = process_time()
    show_data(("{:.14f}".format(end_time-start_time)), prev_arr, arr, ilosc_porownan[0])
    print("ilosc scalan:", scalanie[0])

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

l2 = create_random_list(10)




run_quick_sort([*l2], 0, len(l2)-1)
print()
run_merge([*l2])
print()

heap_sort([*l2])
print()

selection_sort([*l2])
print()

insertion_sort([*l2])
print()

bubble_sort([*l2])





# insertion_sort(l1)
# selection_sort(l1)
#bubble_sort(l1)
# run_quick_sort(l2,0, len(l2)-1)
#run_merge(l1)







#ktorki opis
#wykresiki


#wnioski
#pol tekstu storny mniej wiecej

#liczba operacji wynosi i porownan