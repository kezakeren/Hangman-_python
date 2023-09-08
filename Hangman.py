# MEMBERS:
# IRASUBIZA Rebecca 223023798
#KEZA UWINEZA Keren  223019964
import random
import string

chances = 6
warning = 3


s_words = ['Pen','cat','woman','kid','ship','crisps','chips','table',
        'cartoon','star','bicycle','bag','bottle','book','phone','chair',
        'door','projector','board','chalk','window','boy','girl','computer',
        'clothes','roads','fingers','church','pin','query']


word = s_words[random.randint(0, 29)]
loop = len(word)
new_word = []
used_letter = []
breaker = 0


while loop > 0:
    new_word.append('-')
    loop -= 1

def update_data():
    
    print("Word: ","".join(str(i) for i in new_word), )
    print(f"Guess chances remaing: {chances}")
    print(f"Unused letters : {', '.join(i for i in string.ascii_lowercase if i not in used_letter)}")
    
def check_1(chr):
    global warning
    global chances
    if chr in string.ascii_lowercase or chr == ' ' :
        if chr in used_letter:
            if warning == 0:
                chances -= 1
                return False
            warning = warning - 1
            return False
        return True
    
    else:
        print("Invalid letter, please enter a valid letter")
        
        if warning == 0:
            chances -= 1
        else:
            warning -= 1
        return False

def check_2(chr, secret_word):
    global chances
    count = 0
    index_list = []
    if chr in secret_word:
        for i in secret_word:
            if i == chr:
                index_list.append(count)
            count += 1
        return index_list
    else:
        print("wrong guess")
        if chr not in "aiueo":
            chances -= 1
        else:
            chances -= 2
            return[]

def guess_check():
    if chances > 0 :
        return True
    return False

def end():
    if not (guess_check()):
        print(f"\n You loose!, You're out of guesses \n The word was: {word}")
    if breaker == len(new_word):
        score = chances * len(set(new_word))
        print(f"\n  You Won! you guessed the word\n--- The word: {word}\n Your score: {score}")
    


print("\nHangman Game ")
print("the rules of the game are :")
print("here's 6 Guesses and 3 Warning at start")
print("You must Enter one character at a time\n")




while breaker != len(new_word) :
    if guess_check():
        update_data()
        char = input("Guess any letter: ")
        if check_1(char):
            index = check_2(char, word)

            if index:
                count = 0
                for i in word:
                    if count in index and char not in used_letter:
                        new_word[count] = char
                        breaker += 1
                        count += 1
                        continue
                    count += 1
        used_letter.append(char)
    else:
        break

end()
