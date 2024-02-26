def insertion_sort(list_of_items):
     for i in range(1, len(list_of_items)):
        cur_val = list_of_items[i]
        cur_pos = i

        while cur_pos > 0 and list_of_items[cur_pos - 1] > cur_val:
            list_of_items[cur_pos] = list_of_items[cur_pos - 1]
            cur_pos = cur_pos - 1
        list_of_items[cur_pos] = cur_val

list_of_items = [4, 2, 3, 17, 7, 1, 34, 5, 20]
bubble_sort(list_of_items)
print(list_of_items)
       
##def bubble_sort(list_of_items):
    







##list_of_items = [47, 12, 33, 17, 7, 51, 34, 5, 20]
##bubble_sort(list_of_items)
##print(list_of_items)
