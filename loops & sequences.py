# the lists the iterable .

developer = "Abhishek"
print(list(developer)) # this case is used to split a word in small chunks

# to remove an element from a list .
developer_1 = ['jane doe', 23 ,'python developer']
del developer_1[1]
print(developer)

# the in operator to determine whether the value exists or not in the list.
print(23 in developer_1)# the case of indexing in the nested list which is inside a list .

engineer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(engineer[2])
print(engineer[2][2]) # that's the case of nested list.

# the unpacking of a list.
fruits = ['Alice', 34, 'Rust Developer']
name, age, job = fruits
print(name)
print(age)
print(job)

# if we have to unpack the remaining values(*)

developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

# The slice operator.(:)
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(desserts[1:4]) # ['Cookies', 'Ice Cream', 'Pie']

# the case in which we have to find list of even num from a list using (::) operator

numbers = [1,2,3,4,5,6,7,8]
print(numbers[1::2])

# the use of append() for adding a list into a another list.

numbers = [1,2,3,4,5,6,7,8]
even_numbers = [10,12,14]
numbers.append(even_numbers)
print(numbers)

# adding elements from one list to another( extend())

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]

numbers = [11,3,6,8,2,5]

# the tuples

# The count() operator use for no of times occurrence of a string

programming_languages = ('rust','python', 'c++','java','rust')
print(programming_languages.count('rust'))

# index() this is use to define the position of a string

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(programming_languages.index('Python'))
print(programming_languages.index("Python",2,5))

# the sorted function in tuples.

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, key=len))

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']

# if we wanna sort our tuples in reverse order we can use reverse function.

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages, reverse=True))

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']
print(tuple("hi"))

# how the loops work..........
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
           break
    else:
        print(f"{word} not have vowels" )

# the range function in the loops .

for number in range(3):
    print(number)

# choosing numbers by using range from where to start and where end this method is also called start stop method .

for number in range(1,11):
    print(number)

for number in range(1,10,2):
    print(number)

""" The note- we have to remember one thing in range operator is 
 that we can't put floats as arguments because they will cause and 
 print error to the console and aslo remember here one thing that 
 if we don't provide any argument to our range function this will 
 also cause an error """

# the decrement case of the range function.

"""we can do this simply a negative step argument in the range function"""

for students in range(40,20,-2):
    print(students)

# the use of list converter from the sequence converted by range function.

for number in list(range(5,0,1)):
    print(number)

# the enumerate() function for the indexing of a list.

languages = ["english","Spanish","French","Italian","Hindi"]
print(list(enumerate(languages)))

""" in the above block of code we have deal with the using of enumerate() for indexing without loops we get here result
in the way tuples in there is index number mentioned with the value at that particular index like this 
[(0, 'english'), (1, 'Spanish'), (2, 'French'), (3, 'Italian'), (4, 'Hindi')]"""

# the enumearte() indexing in the for loop.

languages = ["Spanish","Italian","German","English"]
for index,language in enumerate(languages):
    print(f"Index{index} and language {language}")

# using the enumerat() function by taking the start argument in it.

languages= ["Spanish","Russian","English","French","German"]
for index, language in enumerate(languages, 2):
    print(f"index{index} and language {language}")

# the zip function.
developers = ["Abhishek","John Doe","Ramesh","Santosh"]
ids = [1,2,3,4]
for developer, dev_id in zip(developers,ids):
    print("dev:", developer)
    print("id:", dev_id)

# the list comprehensions .

even_numbers = []
for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

""" hai as we can here see that this process takes about six lines of code
we can done this whole process in just two lines of code this is called list comprehension"""

# the first way .

player_level = [level*4 for level in range(11) if level%2 != 0]
print("levels:", player_level)

# the another example.

numbers = [1,2,3,4,5,6,7,8]
result = [(num*10, "pass" ) if num*10>31 else (num*10,"fail") for num in numbers]
print(result)

# The filter function .

words = ['tree','sky','mango','banana','Megumi','Gojo']
def is_long_word(words):
    return len(words) > 4
long_words = list(filter(is_long_word,words))
print(long_words)

gun = "M416"
print(gun[::-1])
# the  lamda() function .

""" this function is generally used for writing multiple functions at once like using list filter() function at once 
we can use them in this way like in this example """
fruits = ["apple","banana","guava","Mango"]
salad = list(filter(lambda x:  len(x) >4, fruits))
print(salad)















