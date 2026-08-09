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