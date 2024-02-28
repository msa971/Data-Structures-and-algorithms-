class Chocolate:
    """Class to represent a chocolate"""

    # Constructor:
    def __init__(self, weight, type, price):  # initializing attributes of the chocolate.
        self.weight = weight
        self.type = type
        self.price = price


class Student:
    """Class to represent a student"""

    # Constructor:
    def __init__(self, name):  # initializing attributes of the student.
        self.name = name
        self.chocolate = None


def Iteration(chocolates, students):  # function for iterating to distribute the chocolate to the students:
    if len(chocolates) < len(students):  # checks if the number of chocolates is less to the number of students.
        print("Error! Not enough chocolates for all students :(")  # if the number of chocolates is less than the number of students it prints the given statement.

    timer = 0
    for i, student in enumerate(students):  # iterates through the list of students and also keeps track of the number of iterations.
        student.chocolate = chocolates[i]  # Assigns the chocolates to the students.
        timer += 1
    print("\nThe time it took for the iteration: ", timer, "seconds")



def Recursion(chocolates, students, timer=0):  # function for recursion to distribute the chocolate to the students:
    if len(students) == 0 or len(chocolates) == 0:  # checks if either lists is empty
        return timer

    students[0].chocolate = chocolates[0] # Assigns the first chocolate on the list to the first student on the list.
    timer += 1
    return Recursion(chocolates[1:], students[1:], timer) # Recrusively calls the Recrusion function with the sublist of chocolates and the sublist of students starting from the second element in each and distributes the remaining chocolate to the remaining students.



# Test case:
chocolates = [Chocolate("4g", "milk chocolate", "1.99 dhs"), Chocolate("2g", "caramel chocolate", "15.5 dhs"),
              Chocolate("8g", "wafer chocolate", "3.0 dhs"), Chocolate("5g", "white chocolate", "11.0 dhs"),
              Chocolate("15g", "dark chocolate", "10.99 dhs")]
students = [Student("Mahra"), Student("Rouda"), Student("Alyazi"), Student("Zayed"), Student("Mohamed")]

Iteration(chocolates, students)  # This calls the iteration function
print("\nIteration results: ")
for student in students:  # for each student on the list of students, it prints the following statement:
    print(student.name, "received a", student.chocolate.type, "that weighs:", student.chocolate.weight, "and costs:", student.chocolate.price)


# Reset students for the recursive test
students = [Student("Mahra"), Student("Rouda"), Student("Alyazi"), Student("Zayed"), Student("Mohamed")]

Recursion(chocolates, students)  # Calls the recursion function
recursion_time = Recursion(chocolates, students)  # Calls the recursion function
print("\nThe time it took for the recursion: ", recursion_time, "seconds")
print("\nRecursive results:")
for student in students:  # for each student in the student list, it prints the following statement:
    print(student.name, "received a", student.chocolate.type, "that weighs:", student.chocolate.weight, "and costs:", student.chocolate.price)




# Sorting algorithm. I chose merge sort because it had the best time complexity in relation to the input compared to other sorting algorithms.
# Sort by weight:
def merge_sort_byweight(chocolates, timer):  # function for merge sort by weight
    if len(chocolates) <= 1:  # This is the base case meaning that if the list has 0 or 1 elements, it's already sorted
        return chocolates

    mid = len(chocolates) // 2  # divides the array of chocolates in half
    first_half = merge_sort_byweight(chocolates[:mid], timer)  # sort the first half using recrusion
    second_half = merge_sort_byweight(chocolates[mid:], timer)  # sort the second half using recrusion

    return merge(first_half, second_half, timer)  # Merge the sorted halves based on price


def merge(first, second, timer):  # function for merging the two halves
    merged = []
    first_index, second_index = 0, 0

    while first_index < len(first) and second_index < len(second):
        timer[0] += 1
        # compares the weights of the chocolates and appends the smaller one to the list
        if int(first[first_index].weight[:-1]) < int(second[second_index].weight[:-1]):
            merged.append(first[first_index])
            first_index += 1

        else:
            merged.append(second[second_index])
            second_index += 1

    # appends the elements that are left from the first and second half to the list
    merged.extend(first[first_index:])
    merged.extend(second[second_index:])

    return merged



# Sort by price:
def merge_sort_byprice(chocolates, timer):  # function to merge sort the chocolates by price
    if len(chocolates) <= 1:  # This is the base case meaning that if the list has 0 or 1 elements, it's already sorted
        return chocolates

    mid = len(chocolates) // 2  # Divide the list into two halves
    first_half = merge_sort_byprice(chocolates[:mid], timer)  # sort the first half using recrusion
    second_half = merge_sort_byprice(chocolates[mid:], timer)  # sort the second half using recrusion

    return merge_by_price(first_half, second_half, timer)  # Merge the sorted halves based on price


def merge_by_price(first, second, timer):  # function to merge the two sorted halves
    merged = []
    first_index, second_index = 0, 0

    while first_index < len(first) and second_index < len(second):
        timer[0] += 1
        # Compare the prices of chocolates and append the cheaper one to the list
        if float(first[first_index].price[:-4]) < float(second[second_index].price[:-4]):
            merged.append(first[first_index])
            first_index += 1

        else:
            merged.append(second[second_index])
            second_index += 1

    # Append the elements that are left of the first and second half to the list
    merged.extend(first[first_index:])
    merged.extend(second[second_index:])

    return merged



# Test case:
chocolates = [Chocolate("4g", "milk chocolate", "1.99 dhs"), Chocolate("2g", "caramel chocolate", "15.5 dhs"),
              Chocolate("8g", "wafer chocolate", "3.0 dhs"), Chocolate("5g", "white chocolate", "11.0 dhs"),
              Chocolate("15g", "dark chocolate", "10.99 dhs")]

#Sort counter for sort by weight
weight_sort_timer = [0]
# Step counter for sort by price
price_sort_timer = [0]

# Sorting the chocolates by weight
weight_sorted_chocolates = merge_sort_byweight(chocolates, weight_sort_timer)
# Sorting the chocolates by price
price_sorted_chocolates = merge_sort_byprice(chocolates, price_sort_timer)

# Printing sorted chocolates
print("\nThe chocolates sorted by weight:")
for chocolate in weight_sorted_chocolates:
    print(chocolate.type)
print("\nThe time it took for sorting by weight:", weight_sort_timer[0], "seconds")


# Printing sorted chocolates
print("\nThe chocolates sorted by price:")
for chocolate in price_sorted_chocolates:
    print(chocolate.type)

print("\nThe time it took for sorting by price:", price_sort_timer[0], "seconds")



#Start of the searching algorithm:
class Chocolate:
    """Class to represent a chocolate"""

    def __init__(self, weight, price): #initializing attributes for the chocolates
        self.weight = weight
        self.price = price


class Student:
    """Class to represent a student"""

    def __init__(self, name, chocolate): #initializing attributes for the students
        self.name = name
        self.chocolate = chocolate


def find_student(students, target_value, key, timer): #function to find the student that is holding the specific chocolate
    timer[0] = 0
    for student in students:
        timer[0] += 1
        if key == "price" and float(student.chocolate.price) == target_value: #for each student in the students list check the given price is equal to any price on the list.
            return student.name, timer[0]
        elif key == "weight" and int(student.chocolate.weight[:-1]) == target_value: #and do the same for each weight on the list.
            return student.name, timer[0]
    return None, timer[0]


# A list of chocolates assigned to students with weights and prices:
students = [
    Student("Mahra", Chocolate("2g", 2.5)),
    Student("Rouda", Chocolate("3g", 3.0)),
    Student("Alyazi", Chocolate("5g", 5.8)),
    Student("Zayed", Chocolate("8g", 10.2)),
    Student("Mohamed", Chocolate("12g", 15.0))
]

# Test case for finding a student by chocolate price
price_to_find = 15  # Example price to search for
search_timer = [0]
found_students_byprice = find_student(students, price_to_find, "price", search_timer) #calling the find_student function.
if found_students_byprice:
    print("\nFinding student that holds the chocolate by price:")
    print(f"A student is holding a chocolate with the price {price_to_find} dhs is : {found_students_byprice}") #prints the price with the corresponding student.
    print("Time it took for searchinh:", search_timer)
else:
    print(f"No chocolate with the price {price_to_find} dhs is found.")

# Test case for finding a student by chocolate weight
weight_to_find = 3  # Example weight to search for
search_timer = [0]
found_student_byweight = find_student(students, weight_to_find, "weight", search_timer) #calling the find_student function.
if found_student_byweight:
    print("\nFinding student that holds the chocolate by weight:")
    print(f"A student is holding a chocolate with the weight {weight_to_find} g is :  {found_student_byweight}") #prints the price with the corresponding student.
    print("Time it took for searching:", search_timer)
else:
    print(f"No chocolate with the weight {weight_to_find} g is found.")