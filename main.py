# import random
# numbers =[1,2,3,4,5,6,7,8,9,10]

# length = int(input("Enter the length that you want of your password."))

# password = ""
# for i in range(length-1) :
#     random_word = str(random.choice(numbers))
    
#     password += random_word;
    
# print(password)


# =====================truthy and falsly value===========
# name = input("Enter your userName")
# pass_word = input("Enter your password")


# if name and pass_word: 
#     print("true")
# else:
#     print("Please enter valid details.")


# =========================ternary operator============================

# name = "uman"
# # condition if true condition if false
# print(f"Hello {name}" if name == "Suman" else "Hello Stranger")

# helo = "Hello Hello"
# print(helo or "Nothing")


print(True ==1) #true
print('' == 1) #false as "" is 0
print([] == 1) #false as [] is empty
print(10 == 10.0) # false as data types are different
print([] == []) # true