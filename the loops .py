# the loops we are going to do

# the for loop .

programming_languages = ['python','java','c++','ruby']
for language in programming_languages:
    print(language)
# for loops for strings .
for char in "code":
    print(char)

# the nested for loop inside a for loop.
categories = ["fruit","vegetables"]
foods = ["apple","banana","carrot","potato"]

for category in categories:
    for food in foods:
        print(category,food)

# the while loop .
secret_number = 3
guess = 0
while guess != secret_number:
    guess = int(input("guess the no (1-5):"))
    if guess != secret_number:
        print("wrong! try again")
print("you got it")

# the use of the continue statement in the loops .
developer_names = ['jess','abhi','Ritesh']
for developer in developer_names:
    if developer == "jess":
        continue
    print(developer)      # <-- Lined up with 'if'!



word = ['background','bad','ugly','ich''bibliothek','apple']
for words in word:
    for letters in words:
        if letters.lower() in "aeiou":
           print(f"{word} contains the vowels {letters}")
        else:
            print("has no vowels")

developer_names = ['jess','abhi','Ritesh']
for developer in developer_names:
    if developer == "jess":
        continue
    print(developer)      # <-- Lined up with 'if'!
words = ['background','bad','ugly','ich','bibliothek','apple']
for word in words:
    for letter in word:
        if letter.lower() in "aeiou":
           print(f"{word} contains the vowel {letter}")
    else:
        print(f"{word}has no vowels")











