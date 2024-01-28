import time
import csv

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
def insert_dict(n):

    my_dict = { }

    for i in range(n):
        my_dict[str(i)] = i

    start_time = time.time()
    my_dict[str(n)] = n
    end_time = time.time()

    total_time = end_time - start_time
    return total_time

def delete_dict(n):
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

def avg_calc():
    sum = 0
    for s in range(5):
        sum = sum + dummy_list[s]
    avg = sum / len(dummy_list)

    return avg











n = 1000000
n2 = 100000

#List - insert beginning
my_insert_beginning_list = [ ]
my_insert_beginning_list.append("list insert beginning")

for i in range(0, n, n2):
    dummy_list = [ ]

    for j in range(5):
        dummy_list.append(insert_beginning_list(i + n2))

    my_insert_beginning_list.append(avg_calc())

#List - insert middle
my_insert_middle_list = [ ]
my_insert_middle_list.append("list insert middle")

for i in range(0, n, n2):
    dummy_list = [ ]

    for j in range(5):
        dummy_list.append(insert_middle_list(i + n2))

    my_insert_middle_list.append(avg_calc())

#List - insert end
my_insert_end_list = [ ]
my_insert_end_list.append("list insert end")

for i in range(0, n, n2):
    dummy_list = [ ]

    for j in range(5):
        dummy_list.append(insert_end_list(i + n2))

    my_insert_end_list.append(avg_calc())

#List - delete beginning
my_delete_beginning_list = [ ]
my_delete_beginning_list.append("list delete beginning")

for i in range(0, n, n2):
    dummy_list = [ ]
    
    for j in range(5):
        dummy_list.append(delete_beginning_list(i + n2))

    my_delete_beginning_list.append(avg_calc())

#List - delete middle
my_delete_middle_list = [ ]
my_delete_middle_list.append("list delete middle")

for i in range(0, n, n2):
    dummy_list = [ ]

    for j in range(5):
        dummy_list.append(delete_middle_list(i + n2))

    my_delete_middle_list.append(avg_calc())

#List - delete end
my_delete_end_list = [ ]
my_delete_end_list.append("list delete end")

for i in range(0, n, n2):
    dummy_list = [ ]

    for j in range(5):
        dummy_list.append(delete_end_list(i + n2))

    my_delete_end_list.append(avg_calc())

#List - element within list
my_element_in_list = [ ]
my_element_in_list.append("list element in")

for i in range(0, n, n2):
    dummy_list = [ ]

    for j in range(5):
        dummy_list.append(element_in_list(i + n2, (i + n2)//2))

    my_element_in_list.append(avg_calc())

#Dict - insert    
my_insert_dict = [ ]
my_insert_dict.append("dict insert")

for i in range(0, n, n2):
    dummy_list = [ ]

    for j in range(5):
        dummy_list.append(insert_dict(i + n2))

    my_insert_dict.append(avg_calc())

#Dict - delete    
my_delete_dict = [ ]
my_delete_dict.append("dict delete")

for i in range(0, n, n2):
    dummy_list = [ ]
    for j in range(5):
        dummy_list.append(delete_dict(i + n2))

    my_delete_dict.append(avg_calc())

#Dict - element in dict    
my_element_in_dict = [ ]
my_element_in_dict.append("dict element in")

for i in range(0, n, n2):
    dummy_list = [ ]
    n_elmenent_in_dict = n2 * (i + 1)
    n_elmenent_in_dict2 = n2//2

    for j in range(5):
        dummy_list.append(element_in_dict(i + n2, (i + n2)//2))

    my_element_in_dict.append(avg_calc())

#Counter - shows the length of lists/dicts using the number of elements in each
counter = [ ]
counter.append("number of elements")
for i in range(0, n, n2):
    counter.append(i + n2)





file_path = r'C:\Users\james\OneDrive\Documents\UNC\1. Spring 2024\4. Algorithms (CS 301)\3. Big O Running Time\my_runtime_data.csv'

with open(file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(counter)

    csv_writer.writerow(my_insert_beginning_list)
    csv_writer.writerow(my_insert_middle_list)
    csv_writer.writerow(my_insert_end_list)

    csv_writer.writerow(my_delete_beginning_list)
    csv_writer.writerow(my_delete_middle_list)
    csv_writer.writerow(my_delete_end_list)

    csv_writer.writerow(my_element_in_list)

    csv_writer.writerow(my_insert_dict)
    csv_writer.writerow(my_delete_dict)
    csv_writer.writerow(my_element_in_dict)

# Plotting bar graphs (Histograms) using matpotlib.pyplot 
import matplotlib.pyplot as plot
import csv

# Loading data from CSV file
file_path = r'C:\Users\james\OneDrive\Documents\UNC\1. Spring 2024\4. Algorithms (CS 301)\3. Big O Running Time\my_runtime_data.csv'

with open(file_path, newline='') as fileName:
    data = csv.reader(fileName)
    data = list(data)

# Extracting headers and rows from the file
headers = data[0]
rows = data[1:] # reading data form all rows except 1st. 

# Function to plot histograms (bar graphs)
def plot_data(Graph_Title, xAxis, yAxis, headers, rowData):
    x_labels = headers[1:] # reading the headers from first to last
    y_data = [float(value) for value in rowData[1:]]  # Converting string data to float

    plot.bar(x_labels, y_data)
    plot.title(Graph_Title)
    plot.xlabel(xAxis)
    plot.ylabel(yAxis)
    plot.xticks(rotation=45)
    plot.tight_layout()
    plot.show()

# Ploting histograms for each data category
plot_data("Insertion Time at Beginning (List)", "Number of Elements", "Average Time (s)", headers, rows[0])
plot_data("Insertion Time in Middle (List)", "Number of Elements", "Average Time (s)", headers, rows[1])
plot_data("Insertion Time at End (List)", "Number of Elements", "Average Time (s)", headers, rows[2])
plot_data("Deletion Time at Beginning (List)", "Number of Elements", "Average Time (s)", headers, rows[3])
plot_data("Deletion Time in Middle (List)", "Number of Elements", "Average Time (s)", headers, rows[4])
plot_data("Deletion Time at End (List)", "Number of Elements", "Average Time (s)", headers, rows[5])
plot_data("Search Time in List", "Number of Elements", "Average Time (s)", headers, rows[6])
plot_data("Insertion Time in (Dictionary)", "Number of Elements", "Average Time (s)", headers, rows[7])
plot_data("Deletion Time in (Dictionary)", "Number of Elements", "Average Time (s)", headers, rows[8])
plot_data("Search Time in (Dictionary)", "Number of Elements", "Average Time (s)", headers, rows[9])
