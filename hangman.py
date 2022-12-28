
import random
from test_2 import stages



# generování náhodného slova
words = ["harry", "ron", "albus", "hermiona", "draco"]

random_word = words[random.randint(0, len(words))]



# generování podtržítek
hidden_word = []

for one_letter in random_word:
    hidden_word.append("_")

# životy

lives = 6
print(stages[lives])



printedWord = "".join(hidden_word)

print(printedWord)

while "_" in hidden_word:
    guess = input("Zadejte hádané písmeno\n").lower()

    for index in range(0, len(random_word)):
        if guess == random_word[index]:
            hidden_word[index] = guess
        
# kontrola životů
    if guess not in random_word:
        lives -= 1
        print(stages[lives])
    print("Počet vašich životů je", lives)
    if lives == 0:
        print("Prohráli jste.")
        break

    printedWord = "".join(hidden_word)

    print(printedWord)


    if "_" not in hidden_word:
     print("Vyhráli jste!!!")








