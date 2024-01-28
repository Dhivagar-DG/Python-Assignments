# INSERTION SORT USING PYTHON

def insertion_sort(lst, ascending=True):
    order = 'Ascending' if ascending else 'Descending'
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            condition = lst[j-1] > lst[j] if ascending else lst[j-1] < lst[j]
            if condition:
                lst[j-1], lst[j] = lst[j], lst[j-1]
            else:
                break
    print(f"After sorted list elements using INSERTION SORT in {order} order : {lst}")
lst = input("Enter the list of values ex:(1,2,3,4,5): ").split(',')
lst = list(map(int, lst))
print("Actual list elements : ", lst)
insertion_sort(lst.copy())
insertion_sort(lst.copy(), False)