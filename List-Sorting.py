#Group members: Katelyn Juhl, Kyle Longaker

Katelyn:
def insertion_sort(list_of_items):
     for i in range(1, len(list_of_items)):
        cur_val = list_of_items[i]
        cur_pos = i

        while cur_pos > 0 and list_of_items[cur_pos - 1] > cur_val:
            list_of_items[cur_pos] = list_of_items[cur_pos - 1]
            cur_pos = cur_pos - 1
        list_of_items[cur_pos] = cur_val
          
#Big O runtime: O(n^2), worst case O(n^3) due to possible extra O(n) time it takes to look thoguh values. 

##Test code:
list_of_items = [4, 2, 3, 17, 7, 1, 34, 5, 20]
bubble_sort(list_of_items)
print(list_of_items)

Katelyn:
def bubble_sort(list_of_items):
    n = len(list_of_items)
    for i in range(n):
        for j in range(0, n-i-1):
            if list_of_items[j] > list_of_items[j+1]:
                list_of_items[j], list_of_items[j+1] = list_of_items[j+1], list_of_items[j]
    return list_of_items
     
#Big O runtime: O(n^2), worst case O(n^3) due to every comparison causing an exchange. 

##Test code:
list_of_items = [7, 32, 33, 17, 47]
bubble_sort(list_of_items)
print(list_of_items)
