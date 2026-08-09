# print sum of numbers till the entered num
def total_value():

    num = int(input("Enter a number: "))
    total = 0
    while num >0:
        total += num
        num = num-1
    print ("the sum is", total)

# print multiplication table for entered number

def num_multiplication():

    num2 = int(input("Enter a number: "))
    table = 1
    while table <=10:
        print(num2, "*", table , "==",num2*table)
        table +=1

def secret_number():
    secret_num = 7
    running = True
    while running:
        guess_num = int(input("enter the guess: "))
        if guess_num == secret_num:
            print("You got it!")
            running = False



def modification_secret():
    secret_num = 7
    while True:
        guess = int(input("Enter a number: "))
        if guess == secret_num:
            print("You got it!")
            break
        elif guess > secret_num:
            print("The guess is greater thn secret number")
        else:
            print("The guess is smaller")



def guess_count():
    secret_num = 7
    counter=0
    while True:
        counter+=1
        guess = int(input("Enter a number: "))
        if guess == secret_num:
            print("You got it!")
            print("You guessed it in",counter,"guesses")
            break
        elif guess > secret_num:
            print("The guess is greater thn secret number")
        else:
            print("The guess is smaller")

def number_things():
    counter=1

    list_num = []
    
    while counter<=5:
        
        num= int(input("Enter a number: "))
        list_num.append(num)
        counter+=1
       
        
    total = sum(list_num)
    average = total/len(list_num)
    largest = max(list_num)
    smallest = min(list_num)
    print("total is:", total)
    print("average is:", average)
    print("largest is:", largest)
    print("smallest is:", smallest)


def remove_duplicates():
    num_list = []
    new_list= []
   
    while len(num_list)<5:
        num = int(input("Enter a number: "))  
        num_list.append(num)
    for num in num_list:
        if num not in new_list:
            new_list.append(num)
    print("New list without repitition is",new_list)
        

def find_number_of_duplicates():
    num_list = []
    count=0
    while len(num_list)<5:
        num = int(input("Enter a number: "))
        num_list.append(num)
    guess = int(input("Enter a number of your choice: "))
    for number in num_list:
        if guess == number:
            count+=1
    print("The number u chose appears",count,"times")



def reversing_the_list():
    num_list = []
    reverse_list=[]
    while len(num_list)<5:
        num = int(input("Enter a number: "))
        num_list.append(num)
    for i in range(len(num_list)):
        reverse_list.append(num_list[(len(num_list)-1)-i])
    print("reversed list is: ",reverse_list)


def second_largest_unique():
    num_list = [4,9,2,9,7]
    new_list=[]
    largest = num_list[0]
     

    for num in num_list:
        if num > largest:
            largest = num
        
    for number in num_list:
        if number != largest:
            new_list.append(number)
    second_largest = new_list[0]
    for values in new_list:
        if values > second_largest:
            second_largest =values
            
    print("The second largest number is", second_largest)




def second_largest_unique_edit():
    num_list = [4,9,2,9,7]
    new_list=[]
    largest = None
    second_largest = None
    
    for num in num_list:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
            
        elif num!=largest and (second_largest is None or num > second_largest):
            second_largest = num

            
    print("The second largest number is", second_largest)



def check_palindrome():
    choice = input("Enter word of your choice: ").lower()
    
    reversed_word = ""

    for i in range(len(choice)):
        reversed_word = reversed_word+choice[-i-1]
    print(reversed_word)
    if reversed_word == choice:
        print("Its a palindrome")
    else:
        print("Not a palindrome")
    
def vowel_counter():
    vowel_list = "aeiou"
    vowel_count = 0
    sentence = input("Enter a sentence: ").lower()
    for character in sentence:
        if character in vowel_list:
            vowel_count+=1
    print("The vowel count is", vowel_count)

def word_counter():
    counter = 0
    sentence = input("Enter a sentence: ").lower()
    word_list = sentence.split()
    print("The number of words are:", len(word_list))

def find_longest_word():
    sentence = input("Enter a sentence: ").lower()
    word_list = sentence.split()
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            
            longest_word = word
    print("longest word is",longest_word)

def replace_vowels():

    sentence = input("Enter the sentence of your choice: ").lower()
    vowels="aeiou"
    new_sentence =""
    for character in sentence:
        if character not in vowels:
            new_sentence = new_sentence +character

    print ("The new sentence is", new_sentence)

def count_separate_vowels():
    vowels = "aeiou"
    sentence = input("Enter a sentence: ").lower()
    
    vowel_count = [0]*5
    for i,vowel in enumerate(vowels):
        
        for character in sentence:
            if vowel == character:
                vowel_count[i] +=1
        
        print("The vowel count for",vowels[i],":",vowel_count[i])
        
def onetime_counter():
    sentence = input("Enter a sentence: ").lower()
    sentence = sentence.replace(" ","")
    character_count = [0]*len(sentence)
    for i, character in enumerate(sentence):
        for characters in sentence:
            if character == characters:
                character_count[i]+=1
        if character_count[i] == 1:
            print("The character with the lowest count is: ", sentence[i],"with count: ",character_count[i])
            break

def keep_non_repeating():
    sentence = input("Enter the sentence: ").lower()
    sentence = sentence.replace(" ","")
    character_count = [0]*len(sentence)
    new_word = ""

    for i, character in enumerate(sentence):

        for characters in sentence:

            if character == characters:

                character_count[i]+=1

            if character_count[i]==1 and character not in new_word:
                new_word = new_word + sentence[i]

    print("The new word with the unique character is: ", new_word)

def keep_character_in_two():

    word1 = input("Enter first word: ").lower()
    word2 = input("Enter second word: ").lower()
    new_word = ""

    for character1 in word1:
       
        if character1 in word2 and character1 not in new_word:
                new_word += character1
    print("The new word with character in both words is: ", new_word)


def check_anagrams():
    word1 = input("Enter word 1: ").lower()
    word2 = input("Enter word 2: ").lower()

    if len(word1) != len(word2):
        print("Not anagrams")
        return

    for character in word1:
        count1 = 0
        count2 = 0

        for letter in word1:
            if letter == character:
                count1 += 1
        
        for letter in word2:
            if letter == character:
                count2 += 1
       
        if count1 != count2:
            
            print("Not anagrams")
            return

    print(word1, "and", word2, "are anagrams")

def number_of_unique():

    word = input("Enter a word: ").lower()
    count=0
    old_character =""
    

    for i, character in enumerate(word):
        count=0
        if character not in old_character:

            for letter in word:
                if character == letter:
                    count+=1
                    old_character+=character
            print(character,":", count)

def character_with_max_repeat():

    word = input("Enter the word: ").lower()
    old_character = ""
    greatest = None
    most_freq =[]

    for i, character in enumerate(word):
        count = 0

        if character not in old_character:
        
            for letter in word:
                if character == letter:
                    count+=1
            old_character+=character
                
            if greatest is None or count > greatest:

                greatest = count
                most_freq = [character]
            elif count == greatest:
                most_freq.append(character)
       

    print("The most freq character is",most_freq, greatest,"times")


def character_counter():
    word = input("Enter a word: ").lower()
    
    compressed =""
    new_word=word
    counted =0
    for character in word:        
        count=0
        new_word = word[counted:]

        for letter in new_word:
            if character == letter:
                last_repeat = character
                count+=1
                counted+=1
            else:
                break
        if count >0:
            compressed += last_repeat+str(count)
                 
    print(compressed)




def character_counter_better():
    word = input("Enter a word: ").lower()
    compressed =""
    i = 0
    while i < len(word):
        character = word[i]
        count = 1
        while (i+count)<len(word) and word[i+count]==character:
            count+=1
        compressed += character + str(count)
        i+=count
    print(compressed)

def word_generator():
    compressed_string =input("Enter a compressed string:").lower()
    expanded_string=""

    i =0
    
    while i < len(compressed_string):
        j=0
        character = compressed_string[i]
        count = int(compressed_string[i+1])
        while j < count:
            expanded_string += character
            j+=1
        i+=2
    print(expanded_string)


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

def get_mean_absolute_error(actual,predicted):
    if len(actual)==0 or (len(actual) != len(predicted)):
        return None
    total = 0
    for i in range(len(actual)):
        error = abs(actual[i]-predicted[i])
        total+=error
    result = total/len(actual)
    return result
# mean_absolute_error = get_mean_absolute_error([10,20,30],[12,18,33])
# print("Mean absolute error is: ", mean_absolute_error)

def get_mean_squared_error(actual,predicted):
    if not actual or len(actual)!=len(predicted):
        return None
    total = 0
    for i in range(len(actual)):
        error_squared = (actual[i] - predicted[i])**2
        total +=error_squared
    result = total/len(actual)
    return result
# mean_squared_error = get_mean_squared_error([10,20,30],[12,18,33])
# print("Mean squared error is: ", mean_squared_error)

def get_root_mean_squared(actual,predicted):
    if not actual or len(actual)!=len(predicted):
        return None
    total = 0
    for i in range(len(actual)):
        error_squared = (actual[i] - predicted[i])**2
        total += error_squared
    average = total/len(actual)
    result = average**0.5
    return result
# root_mean_squared_error = get_root_mean_squared([10,20,30],[12,18,33])
# print("The root mean squared error is: ", root_mean_squared_error)

def get_mean_absolute_percentage_error(actual,predicted):
    if not actual or len(actual)!=len(predicted):
        return None
    total = 0
    valid_count = 0
    for i in range(len(actual)):
        if actual[i] == 0:
            continue
        error =abs((predicted[i]-actual[i])/(actual[i]))*100
        total+=error
        valid_count+=1
    if valid_count == 0:
        return None
    result = total/valid_count
    return result
# mape =get_mean_absolute_percentage_error([10,20,30],[12,18,33])
# print("The mean absolute percentage error is: ", mape)

def get_forecast_bias(actual,predicted):
    if not actual or len(actual)!=len(predicted):
        return None
    total = 0
    for i in range(len(actual)):
        error = predicted[i]-actual[i]
        total+=error
    result = total/len(actual)
    return result
# forecast_bias = get_forecast_bias([10,20,30],[12,18,33])
# print("The forecast bias is: ",forecast_bias)

def count_forecast_direction(actual,predicted):
    if not actual or len(actual)!=len(predicted):
        return None
    over_pred = 0
    under_pred =0
    exact = 0
    for i in range(len(actual)):
        error = predicted[i]-actual[i]
        if error > 0:
            over_pred+=1
        elif error < 0:
            under_pred += 1
        else:
            exact+=1
    return over_pred, under_pred, exact
# result = count_forecast_direction([10,20,30],[12,18,33])
# over_pred, under_pred, exact = result
# if result is None:
#     print("Invalid input")
# else:
#     print("The number of over predictions are: ", over_pred)
#     print("The number of under predictions are: ",under_pred)
#     print("The exact predictions are: ", exact)

                        ## Function composition ##

def get_mean_absolute_error(actual,predicted):
    if not actual or len(actual) != len(predicted):
        return None
    total = 0
    for i in range(len(actual)):
        error = abs(actual[i]-predicted[i])
        total+=error
    result = total/len(actual)
    return result

def compare_forecasts(actual,predicted_a,predicted_b):

    mae_a = get_mean_absolute_error(actual,predicted_a)
    mae_b = get_mean_absolute_error(actual,predicted_b)

    if mae_a is None or mae_b is None:
        return None

    if mae_a < mae_b:
        return "Forecast A"
    elif mae_a > mae_b:
        return "Forecast B"
    else:
        return "Tie"

actual = [100, 120, 140, 130, 150]

predicted_a = [102, 118, 145, 128, 149]
predicted_b = [110, 125, 138, 135, 160]

# result = compare_forecasts(actual,predicted_a,predicted_b)

# print(result)

                               ## Dictionary ##

def average_energy_use(energy_data):

    if not energy_data:
        return None
    total = 0
    for energy in energy_data.values():
        total+=energy
    result = total/len(energy_data)
    return result
energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}
# avg_energy_usage = average_energy_use(energy_data)
# print("The average energy usage is: ",avg_energy_usage)

def highest_energy_data(energy_data):
    if not energy_data:
        return None
    highest = None
    for day, energy in energy_data.items():
        if highest is None or energy > highest:
            highest = energy
            highest_day = day
    return highest, highest_day
energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}

# result = highest_energy_data(energy_data)
# highest,highest_day = result
# print("The highest energy consumption is: ", highest, "on", highest_day)

def day_above_average(energy_data):
    if not energy_data:
        return None
    total = 0
    new_list =[]
    for energy in energy_data.values():
        total+=energy
    average = total/len(energy_data)
    for day, energy in energy_data.items():
        if energy > average:
            new_list.append(day)
    return new_list

energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}

# result = day_above_average(energy_data)
# print("The days above average energy use are: ", result)

def scale_energy_data(energy_data,factor):
    if not energy_data:
        return None
    new_dict ={}
    for day, energy in energy_data.items():
        scaled_energy = energy*factor
        new_dict[day] = scaled_energy
    return new_dict
energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}
factor = 1.1
# result = scale_energy_data(energy_data,factor)

# print("New sclaed energy data is: ", result)



def categorize_energy_use(energy_data):
    if not energy_data:
        return None
    new_dict = {}
    
    for day, energy in energy_data.items():
        if energy < 130:
            new_dict[day] = "Low"
            
        elif energy <=145:
            new_dict[day] = "Medium"

        else:
            new_dict[day] = "High"
    return new_dict

energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}

# result = categorize_energy_use(energy_data)
# print(result)
        
def merge_dictionaries(data_a, data_b):

    if not data_a and not data_b:
        return None
    merged_dict = {}
    for day_a, energy_a in data_a.items():
        merged_dict[day_a] = energy_a
    for day_b, energy_b in data_b.items():
        if day_b in merged_dict:
            merged_dict[day_b]+=energy_b
        else:
            merged_dict[day_b] = energy_b

    return merged_dict
data_a = {"Monday": 100, "Tuesday": 120}
data_b = {"Tuesday": 30, "Wednesday": 140}

# result = merge_dictionaries(data_a,data_b)
# print(result)
        
def find_missing_days(energy_data, expected_days):
    list_of_missing_days =[]
    for day in expected_days:
        if day not in energy_data:
            list_of_missing_days.append(day)
    return list_of_missing_days

energy_data = {
    "Monday": 100,
    "Wednesday": 130,
    "Friday": 150
}
expected_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

# result = find_missing_days(energy_data,expected_days)
# print(result)

def fill_missing_days(energy_data, expected_days):

    new_energy_data = {}
    for day in expected_days:
        if day not in energy_data:
            new_energy_data[day] = 0
        else:
            new_energy_data[day] = energy_data[day]
    return new_energy_data
energy_data = {
    "Monday": 100,
    "Wednesday": 130,
    "Friday": 150
}
expected_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]
# result = fill_missing_days(energy_data, expected_days)
# print(result)

def remove_invalid_readings(energy_data):
    new_energy_data = {}

    for day, energy in energy_data.items():
        if energy < 0:
            continue
        
        new_energy_data[day] = energy_data[day]
    return new_energy_data
energy_data = {
    "Monday": 100,
    "Tuesday": -20,
    "Wednesday": 0,
    "Thursday": 140
}
# result = remove_invalid_readings(energy_data)
# print(result)

def group_days_by_category(energy_data):

    new_data = {"Low": [],
                "Medium":[],
                "High":[]
                }


    for day, energy in energy_data.items():
        if energy < 130:
            new_data["Low"].append(day)
        elif energy <= 145:
            new_data["Medium"].append(day)
            
        else:
            new_data["High"].append(day)

    
    return new_data
energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}
# result = group_days_by_category(energy_data)
# print(result)

def count_energy_category(energy_data):

    low_count = 0
    medium_count = 0
    high_count = 0

    new_data = {"Low": low_count,
                "Medium": medium_count,
                "High": high_count
                }
    for energy in energy_data.values():
        if energy < 130:
            new_data["Low"]+=1
        elif energy <=145:
            new_data["Medium"]+=1
        else:
            new_data["High"]+=1
    return new_data
energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}
# result = count_energy_category(energy_data)
# print(result)

def energy_range(energy_data):
    highest = None
    lowest = None
    if not energy_data:
        return None
    for energy in energy_data.values():
        if highest is None or energy > highest:
            highest = energy
        if lowest is None or energy < lowest:
            lowest = energy
    return highest,lowest

energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}

# result = energy_range(energy_data)
# highest, lowest = result
# print("The range in energy consumption is highest: ",highest,"to lowest: ",lowest)

def energy_range(energy_data):
    highest = None
    lowest = None
    if not energy_data:
        return None
    for energy in energy_data.values():
        if highest is None or energy > highest:
            highest = energy
        if lowest is None or energy < lowest:
            lowest = energy
    return highest,lowest

energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}

# result = energy_range(energy_data)
# highest, lowest = result
# print("The range in energy consumption is:",highest - lowest)

def peak_demand_summary(energy_data, threshold):
    if not energy_data:
        return None
    peak_days = []
    total = 0

    for day, energy in energy_data.items():
        if energy > threshold:
            peak_days.append(day)
            total+=energy

    number_of_peak_days = len(peak_days)
    return peak_days, number_of_peak_days, total

energy_data = {
    "Monday": 120,
    "Tuesday": 155,
    "Wednesday": 128,
    "Thursday": 170,
    "Friday": 150
}

threshold = 145

# result = peak_demand_summary(energy_data, threshold)
# peak_days, number_of_peak_days, total = result
# print("The peak days are:", peak_days)
# print("The number of peak days are:", number_of_peak_days)
# print("The total peak energy consumption is:",total)
    
def invert_energy_data(energy_data):

    new_data ={}

    for day, energy in energy_data.items():
        new_data[energy] = day
    return new_data

energy_data = {
    "Monday": 120,
    "Tuesday": 155,
    "Wednesday": 128,
    "Thursday": 170,
    "Friday": 150
}

# result = invert_energy_data(energy_data)
# print(result)

def invert_energy_data(energy_data):
    new_data= {}

    for day, energy in energy_data.items():
        if energy in new_data:
            new_data[energy].append(day)

            
        else:
            new_data[energy] = [day]

    return new_data

energy_data = {
    "Monday": 120,
    "Tuesday": 150,
    "Wednesday": 120
}

# result = invert_energy_data(energy_data)
# print(result)


def count_energy_values(energy_data):
    new_data = {}
    
    for energy in energy_data.values():
        
        if energy in new_data:
            new_data[energy] +=1
        else:
            new_data[energy] = 1
          
    return new_data

energy_data = {
    "Monday": 120,
    "Tuesday": 150,
    "Wednesday": 120,
    "Thursday": 150,
    "Friday": 130
}
# result = count_energy_values(energy_data)
# print(result)
        
def most_common_energy_value(energy_data):

    if not energy_data:
        return None
    new_data = {}
    largest = None
    for energy in energy_data.values():
        if energy in new_data:
            new_data[energy]+=1
        else:
            new_data[energy]=1
    
    for energy, count in new_data.items():
        if largest is None or count > largest:
            largest = count
            max_energy = energy
    return largest, max_energy

energy_data = {
    "Monday": 120,
    "Tuesday": 150,
    "Wednesday": 120,
    "Thursday": 150,
    "Friday": 120
}

# result = most_common_energy_value(energy_data)

# largest, max_energy = result
# print(max_energy,",",largest)


def sorting_energy_values(energy_data):
    list_of_energy = []
    for energy in energy_data.values():
        list_of_energy.append(energy)
    return list_of_energy
energy_data = {
    "Monday": 120,
    "Tuesday": 150,
    "Wednesday": 130,
    "Thursday": 170,
    "Friday": 140
}
# result = sorting_energy_values(energy_data)
# print("The sorted energy data is:", sorted(result))


def rank_based_sort_experiment(energy_values):
    sorted_energy_values = [0]*len(energy_values)

    for position in range(len(energy_values)):
        count = 0
        i = 0
        check = energy_values[position]
        if check in sorted_energy_values:
            dup_posn = sorted_energy_values.index(check)
            dup_posn+=1
            sorted_energy_values[dup_posn] = check
        else:

            while i < len(energy_values):
                    
                if check > energy_values[i]:
                    count+=1

                else:
                    count = count
                i+=1
            
                
            sorted_energy_values[count] = energy_values[position]
    return sorted_energy_values
energy_values = [120, 150, 130, 170, 140]
# result = rank_based_sort_experiment(energy_values)
# print(result)    

def bubble_sort(energy_values):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(energy_values)-1):
            
            if energy_values[i]>energy_values[i+1]:
                swapped = True
                energy_values[i], energy_values[i+1]=energy_values[i+1],energy_values[i]
        
    return energy_values

energy_values = [120, 150, 130, 170, 140]
# result = bubble_sort(energy_values)
# print(result)

def bubble_sort_descending(energy_values):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(energy_values)-1):
            
            if energy_values[i]<energy_values[i+1]:
                swapped = True
                energy_values[i], energy_values[i+1]=energy_values[i+1],energy_values[i]
        
    return energy_values

energy_values = [120, 150, 130, 170, 140]

# result = bubble_sort_descending(energy_values)
# print(result)

def selection_sort(energy_values):
    if not energy_values:
        return None
    position = 0
    
    while position < len(energy_values):
        smallest_index = position
        for i in range(position+1, len(energy_values)):
            if energy_values[i]<energy_values[smallest_index]:
                
                smallest_index = i
        energy_values[position],energy_values[smallest_index]=energy_values[smallest_index],energy_values[position]
        
        
        position+=1
    return energy_values
   

def finding_the_median(energy_values):
    if energy_values is None:
        return None

    size_of_list = len(selection_sort(energy_values))
    if size_of_list % 2 == 0:
        place = size_of_list//2
        median = (energy_values[place]+energy_values[place-1])/2
    else:
        place = size_of_list//2
        median = energy_values[place]
    return median
energy_values = [120, 180, 150, 130, 170, 140]
# result = finding_the_median(energy_values)
# print(result)

def summary(energy_values):
    if energy_values is None:
        return None
    sorted_values = selection_sort(energy_values)
    median_value = finding_the_median(sorted_values)
    total_range = sorted_values[len(sorted_values)-1]-sorted_values[0]
    total = 0
    for i in range(len(sorted_values)):
        total+=sorted_values[i]
    mean_value = total/len(sorted_values)
    return median_value, total_range, mean_value
# energy_values = [120, 150, 130, 170, 140]
# result = summary(energy_values)
# median_value, total_range, mean_value = result
# print("Median:",median_value,"Mean:",mean_value,"Range:",total_range)

def get_standard_deviation(energy_values):
    if not energy_values:
        return None
    result = summary(energy_values)
    median_value, total_range, mean_value = result
    total = 0
    for energy in energy_values:
        total+=(energy-mean_value)**2
    standard_deviation = (total/len(energy_values))**(0.5)
    return standard_deviation

energy_values = [120, 150, 130, 170, 140]
# result = get_standard_deviation(energy_values)
# print(result)

def get_zscore(energy_values):
    if not energy_values:
        return None
    total = 0
    for energy in energy_values:
        total+=energy
    mean_calc = total/len(energy_values)
    squared_total = 0
    for energy in energy_values:
        squared_total+=(energy-mean_calc)**2
    standard_deviation = (squared_total/len(energy_values))**0.5
    if standard_deviation==0:
        return None
    z_score_list=[]
    for energy in energy_values:
        z_score_list.append((energy-mean_calc)/standard_deviation)
    return z_score_list
energy_values = [120, 150, 130, 170, 140]
# result = get_zscore(energy_values)
# print(result)

def find_outliers(energy_values):
    if not energy_values:
        return None
    z_score_list = get_zscore(energy_values)
    if z_score_list is None:
        return None
    outlier_list = []
    for i in range(len(z_score_list)):
        if z_score_list[i]<-2 or z_score_list[i]>2:

            outlier_list.append(energy_values[i])

    return outlier_list,z_score_list
energy_values = [120, 125, 130, 128, 127, 190]

# result = find_outliers(energy_values)
# outliers,z_scores = result
# print("The list of outliers:",outliers)

def moving_average(values,window):
    if not values or window <= 0 or window > len(values):
        return None
    position = 0
    result = []
    
    while (position+window) <= len(values):
        total=0
        for i in range(position,position+window):
            total+=values[i]
        result.append(total/window)
        position+=1
    return result
values = [10, 20, 30, 40, 50]
window_size = 3
# moving_averaged_values = moving_average(values,window_size)
# print(moving_averaged_values)

def rolling_max(values,window_size):
    if not values or window_size <=0 or window_size > len(values):
        return None
    position = 0
    result = []
    while (position+window_size)<=len(values):
        largest=values[position]
        for i in range(position,position+window_size):
            if values[i]>largest:
                largest=values[i]
        result.append(largest)
        position+=1
    return result
# values = [10, 20, 30, 40, 50]
# window_size=3
# max_values = rolling_max(values,window_size)
# print(max_values)


def rolling_min(values,window_size):
    if not values or window_size <=0 or window_size > len(values):
        return None
    position = 0
    result = []
    while (position+window_size)<=len(values):
        smallest=values[position]
        for i in range(position,position+window_size):
            if values[i]<smallest:
                smallest=values[i]
        result.append(smallest)
        position+=1
    return result
values = [10, 20, 30, 40, 50]
window_size=3
# min_values = rolling_min(values,window_size)
# print(min_values)

def rolling_range(values,window_size):
    if not values or window_size <=0 or window_size > len(values):
        return None
    min_values = rolling_min(values,window_size)
    max_values = rolling_max(values,window_size)
    result = []
    for i in range(len(min_values)):
        result.append(max_values[i]-min_values[i])
    return result
values = [10, 20, 15, 30, 25]
window_size = 3
range_values = rolling_range(values,window_size)
print(range_values)


    

        





    






  




    



















        
            
      


            

  
        




    






        
            


        





