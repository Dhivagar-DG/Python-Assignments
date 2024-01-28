def bubbleSort(lst, ascending=True):
    order = 'Ascending' if ascending else 'Descending'
    for i in range(len(lst)-1):
        is_sort = False
        for j in range(len(lst)-i-1):
            condition = lst[j] > lst[j + 1] if ascending else lst[j] < lst[j + 1]
            if condition:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                is_sort = True
        if not is_sort:
            break
    print(f"After sorted list elements using BUBBLE SORT in {order} order : {lst}")

lst = input("Enter the list of values ex:(1,2,3,4,5): ").split(',')
lst = list(map(int, lst))
print("Actual list elements : ", lst)
bubbleSort(lst.copy())
bubbleSort(lst.copy(), False)