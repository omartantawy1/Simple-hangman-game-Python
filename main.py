
import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word=random.choice(hangman_words.word_list)
print(f' chosen word is {chosen_word}')


display=[]
lives=6

for letter in range(len(chosen_word)):
    display+="_"

print(display)        

end_of_game=False

while not end_of_game:
    guess=input('guess a letter ?').lower()

   
    for letter in range(len(chosen_word)):
        if chosen_word[letter]==guess:
           display[letter] =chosen_word[letter] 
           
    if guess not in chosen_word[letter]:
        print(f" you have entered letter {guess} and that's not in the word")
        lives-=1
        print(f" numbers of lives available is {lives}")
        if lives==0:
            end_of_game=True
            print('you lose')
              
                    
    print(f"{' '.join(display)}")
    if "_" not in display :
        end_of_game=True
        print("you win")

    print(hangman_art.stages[lives])  
    