list_sort=[23,76,33,21,22]
#list_sort=[2,6,5,1,3,4]

def Selection_Sort(list_sort):
    for i in range(0, len(list_sort)-1):
        cur_min_index = i
        for j in range(i + 1, len(list_sort)):
            if list_sort[j] < list_sort[cur_min_index]:
                cur_min_index = j
        list_sort[i], list_sort[cur_min_index] = list_sort[cur_min_index], list_sort[i]




Selection_Sort(list_sort)
print(list_sort)
