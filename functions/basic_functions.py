def count_vowels(sentence):
    vowels="aeiou"
    
    count=0
    for character in sentence.lower():
        if character in vowels:
            count+=1
    return count
#total_vowels = count_vowels("I am gay")
#print("Total vowel count: ", total_vowels)

def find_longest_word(sentence):

    words = sentence.split()
    longest_word = None
    for word in words:
        if longest_word is None or len(word)> len(longest_word):
            longest_word = word
    return longest_word
# longest = find_longest_word("I am gay")
# print("The longest word is: ",longest)

def smallest_number(numbers):
    smallest = None
    for num in numbers:
        if smallest is None or num < smallest:
            smallest = num
    return smallest
# smallest_num = smallest_number([5,4,3,2,1])
# print("The smallest number is: ",smallest_num)
    
def get_average(numbers):

    if len(numbers) == 0:
        return None
    total=0
    for num in numbers:
        total +=num
    average = total/len(numbers)
    return average
# average_found = get_average([])
# if average_found is None:
#     print("The list is empty")
# else:
#     print("The average found is: ", average_found)

def number_summary(numbers):
    smallest = None
    largest = None
    total = 0
    if len(numbers) == 0:
        return None 
           

    for num in numbers:
        if smallest is None or num < smallest:
            smallest = num
        if largest is None or num > largest:
            largest = num
        total += num
    average = total/len(numbers)
    return smallest, largest, average
# result= number_summary([1,2,3,4,5])
# if result is None:
#     print("The list givenw was empty")
# else:
#     smallest, largest, average = result
#     print("The smallest number is: ", smallest)
#     print("The largest number is: ",largest)
#     print("The average is: ",average)

def output_positive_num(numbers):
    pos_list = []
    for num in numbers:
        if num > 0:
            pos_list.append(num)
    return pos_list
# positive_number = output_positive_num([-3, 0, 5, 8, -1])
# print("The list of positive numbers is: ", positive_number)

def filter_even_num(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
# even_number_list =filter_even_num([-3, 0, 5, 8, -1])
# print("The list of even numbers is: ", even_number_list)   

def give_squares(numbers):
    squared = []
    for num in numbers:
        squared.append(num**2)
    return squared

# squared_numbers = give_squares([1,2,3,4,5])
# print("The squared number list is: ",squared_numbers)

def convert_temp(temperatures):
    fahrenheit_temp =[]
    for temp in temperatures:
        fahrenheit_temp.append(temp*9/5+32)
    return fahrenheit_temp
# temperature_in_fahrenheit =convert_temp([0, 20, 30, 100])
# print("Temperatures in Fahrenehit: ",temperature_in_fahrenheit)

def get_normalized_data(numbers):
    normalized_list =[]
    largest = None
    for num in numbers:
        if largest is None or num > largest:
            largest = num
    for num in numbers:
        normalized_list.append(num/largest)
    return normalized_list
# normalized_data = get_normalized_data([10,20,40])
# print("The normalized data is: ", normalized_data)

def get_percentage_change(old_value, new_value):
    if old_value == 0:
        return None
    result = ((new_value-old_value)/old_value)*100
    return result
# percentage_change = get_percentage_change(10,20)
# if percentage_change is None:
#     print("Old value was zero")
# else:
#     print("Percentage change is:", percentage_change,"%")