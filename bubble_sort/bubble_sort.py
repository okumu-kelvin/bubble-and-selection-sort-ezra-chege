def bubble_sort(unsorted_list):
    indexing_length = len(unsorted_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length): 
            if unsorted_list[i] > unsorted_list[i+1]:
                sorted = False
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]

    return unsorted_list