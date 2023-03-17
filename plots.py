import matplotlib.pyplot as plt
from plotsandmeasurments import  run_quick_sort, run_merge, heap_sort, selection_sort, insertion_sort, bubble_sort, v_shaped
from data import generate_data, V_shaped_data, A_shaped_data, increasing_data, decreasing_data, create_random_list, run_measurments
sorts ={
    'merge': run_merge,
    'quick': run_quick_sort,
    'heap': heap_sort,
    'selection': selection_sort,
    'insertion': insertion_sort,
    'bubble': bubble_sort
}


data_types = {
    'V kształtnych': V_shaped_data,
    'A kształtnych': A_shaped_data,
    'rosnących': increasing_data,
    'malejących': decreasing_data,
    'losowych': create_random_list
}

ns = [1000*x for x in range(1, 11)]



v_shaped = generate_data(ns, V_shaped_data)
a_shaped = generate_data(ns, A_shaped_data)
increasing = generate_data(ns, increasing_data)
decreasing = generate_data(ns, decreasing_data)
random = generate_data(ns, create_random_list)




for data_type in data_types.keys():
    arr = generate_data(ns, data_types[data_type])
    plt.figure()
    plt.xlabel("n")
    plt.ylabel("czas")
    plt.title(f"Czasy sortowania dla danych {data_type}")
    for sort in sorts.keys():
       measured_time,  measured_std = run_measurments([*arr], sorts[sort], ns)
       plt.errorbar(ns, measured_time, yerr=measured_std)
       plt.scatter(ns, measured_time)

    plt.legend(['merge sort', 'quick sort', 'heap sort', 'selection sort', 'insertion sort'])
    plt.savefig(f"{data_type}_plot.png")
    plt.cla()