import time

#list runtime testing functions
    #inserting
def insert_list(n, x):
    my_list = [ ]

    for i in range(n):
        my_list.append(i)

    start_time = time.time()
    my_list.insert(x, n + 1)
    end_time = time.time()

    total_time = end_time - start_time
    return total_time

def insert_beginning_list(n):
    return insert_list(n, 0)

def insert_middle_list(n):
    return insert_list(n, n//2)

def insert_end_list(n):
    return insert_list(n, n-1)

    #deleting
def delete_list(n, x):
    my_list = [ ]

    for i in range(n):
        my_list.append(i)

    start_time = time.time()
    del my_list[x]
    end_time = time.time()

    total_time = end_time - start_time
    return total_time

def delete_beginning_list(n):
    return delete_list(n, 0)

def delete_middle_list(n):
    return delete_list(n, n//2)

def delete_end_list(n):
    return delete_list(n, n-1)

    #checking if element is in lsit
def element_in_list(n, x):
    my_list = [ ]

    for i in range(n):
        my_list.append(i)

    start_time = time.time()
    for i in my_list:
        if x == i:
            break
    end_time = time.time()

    total_time = end_time - start_time
    return total_time

#dictionary runtime testing functions
def insert_dict(n, x):
    my_dict = { }

    for i in range(n):
        my_dict[str(i)] = i

    start_time = time.time()
    my_dict[str(n)] = n
    end_time = time.time()

    total_time = end_time - start_time
    return total_time

def delete_dict(n, x):
    my_dict = { }

    for i in range(n):
        my_dict[str(i)] = i

    start_time = time.time()
    del my_dict[str(n-1)]
    end_time = time.time()

    total_time = end_time - start_time
    return total_time

def element_in_dict(n, x):
    my_dict = { }

    for i in range(n):
        my_dict[str(i)] = i

    start_time = time.time()
    if str(x) in my_dict:
        end_time = time.time()
        total_time = end_time - start_time
        return total_time
    else:
        end_time = time.time()
        total_time = end_time - start_time
        return total_time


n = 10000000
n2 = 10000

my_insert_list = [ ]
dummy_list = [ ]

for i in range(0, n, n2):
    for i in range(5):
        dummy_list.append(insert_beginning_list(n))

    sum = 0
    for i in range(5):
        sum = sum + dummy_list[i]
    sum / len(dummy_list)

    my_insert_list.append(sum)


file_path = "my_list.csv"

# Open the file in 'w' mode with newline='' to prevent extra newline characters
with open(file_path, 'w', newline='') as csv_file:
    # Create a CSV writer
    csv_writer = csv.writer(csv_file)

    # Write the list as a row in the CSV file
    csv_writer.writerow(my_insert_list)
