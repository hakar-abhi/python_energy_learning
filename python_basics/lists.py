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