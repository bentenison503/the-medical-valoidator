# How Do Conditional Statements and Logical Operators Work?
 #print("Master the APIs: Learn how to seamlessly integrate APIs from OpenAI, Anthropic, or Hugging Face into Python or JavaScript applications.\nLearn Frameworks: Master tools like LangChain or LlamaIndex, which are the industry standards for connecting existing AI models to databases and user interfaces.\nUnderstand Vector Databases: Learn how to use Pinecone, Chroma, or Milvus to store data that AI tools can search through instantly.")
print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True
#if conditions
age = 12
if age >= 18:
    print("you are an adult")
elif age >= 18:
    print("you are a young child")
else:
    print("you are a teenager")
    age = 2

    if age >= 65:
        print('You are a senior citizen')
    elif age >= 30:
        print('You are an adult in your prime')
    elif age >= 18:
        print('You are a young adult')
    elif age >= 13:
        print('You are a teenager')
    elif age >= 3:
        print('You are a young child')
    else:
        print('You are a toddler or an infant')

      # some of the complex conditional statements by using and,or and not operatorss
    is_citizen = True
    age = 24
    if is_citizen and age >= 18:
        print('you are elegible to vote')
    else:
        print('You are eligible to vote')

is_citizen = True
age = 35
print(age and is_citizen)

is_Abhishek = True
age = 16
if is_citizen and age >= 18:
    print('you are eligible to vote')
else:
    print("Abhishek:",'you are not eligible to vote')

#  the or operator
age = 19
is_employed = False
print(age or is_employed )

age = 18
is_student = False
if age > 18 or is_student:
    print('you are eligible for student discount')
else:
    print('you are not eligible for student discount')
# the not operator

print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy

toxicity_score = 0.15
if toxicity_score >= 0.80:
    print('block entitrely and notify modes')
elif toxicity_score >= 0.55:
    print('hold for humnan review')
else:
    print('Approove and post comment')




