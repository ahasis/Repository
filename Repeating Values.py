def repeating_values():
    word = input("Enter Any Word: ")
    word_dic = {}

    for char in word:
        if char in word_dic:
            print(f"{char} is the repeating value, memory adress: {id (char)}")
        else:
            word_dic[char] = 1
        return None 

repeating_values()