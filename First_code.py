# # print ("hello world")
# first_name = "Bolutife"
# last_name = "Ilori"
# # age = "22"
# # origin = "Nigeria"
# # statement = f"{first_name} {last_name} is {age} years old and comes from {origin}"
# # print(statement)
# product1 = "apple"
# product2 = "banana"
# buyer = f"{first_name} {last_name}"
# price1 = 200
# price2 = 300
# quantity1 = 4
# quantity2 = 6
# total1 = price1 * quantity1
# total2 = price2 * quantity2
# statement = f"Hello {buyer}, you have purchased {quantity1} {product1} at {price1} each and {quantity2} {product2} at {price2} each and your total is {total1} and {total2} respectively"
# print(statement)
# var1 = input("enter first number: ")
# var2 = input("enter second number: ")
# var3 = input("enter third number: ")
# sum_of_var = int(var1) + int(var2) + int(var3)
# print(sum_of_var)

# product = input ("what do you want to buy? ")
# quantity = input ("how many do you want to purchase? ")
# price = input ("what is the price? ")
# buyer = input ("what is your name? ")
# total = int(price)* int(quantity)
# statement = f" Hello {buyer}, you have purchased {quantity} {product} at {price} each and total is {total}"
# print(statement)

# radius = input(" what is the radius? ")
# pie = 3.142
# circumference = 2 *pie*int(radius)
# print (round(circumference))
# statement = f" the circumference of a circle with radius {radius} is {circumference}"
# print(statement)
# 
# pass_mark = 70
# score = int(input("what is your score? "))

# response = f"Pass : {score >= pass_mark}"
# print(response) 

# text = input ("Say anything: ")
# value = input ("Any word in text: ")
# statement = f" Word in text : {value in text}"
# print(statement)

# experiment = input ("Word: ")
# sample = experiment[::-1]
# sentence = f" Palindrome {sample == experiment}"
# print(sentence)

# new_file = open("sample.txt", "a")
# new_file.writelines("Hello You")
# new_file.close()

# new_file = open("sample.txt", "r")
# line = new_file.readlines()
# print(line)
# range (0,20)
# help(range)
# variable = input("What is ur date of birth? ")
# new_value = variable.replace (" ", "-")
# print(new_value)
# variable2 = input ("Say Anything: ")
# new_value2 = variable2.split(",")
# print(new_value2)
# # variable2 = input("Say Anything: ")
# new_value1= "-".join(new_value2)
# print(new_value1)

# variable_3 = input("Anything: ").lower()
# variable_4 = variable_3.count("a")
# print(variable_4)
 
# sample = ["boy", "girl", "house"]
# sample_2 = map(lambda x:len(x), sample)
# print(list(sample_2))
# sample = ["boy", "girl", "house"]
# sample_2 = map(lambda x:(len(x),x), sample)
# print(list(sample_2))

# sample = input("Anything: ")
# sample_1 = sample.split(" ")
# sample_2 = map(lambda x:len(x), sample_1)
# sample_3 = max (sample_2)
# print(sample_3)
# scores = [30,20,60,70,45,70,75,50]
# sum_nums = sum(scores)
# no_of_vals = len(scores)

# mean = sum_nums/no_of_vals
# mean_deviation = map(lambda score : score - mean, scores)
# print(list(mean_deviation))
# print(16**0.5)

# new_file2 = open("new_file.txt", "a")
# name = input("Name:  ")
# note = input ("Note: ")
# # response = name + ' : ' + note  or
# response = f"{name} : {note}\n"
# new_file2.writelines(response)
# new_file2.close()

# opposite = int(input("b: "))
# adjacent = int(input ("a: "))
# opposite_2 = opposite * opposite
# adjacent_2 = adjacent * adjacent
# sum_values = opposite_2 + adjacent_2
# hypotenus = sum_values ** 0.5
# print(hypotenus)

# mean = sum_nums/no_of_vals
# mean_deviation = map(lambda score : score - mean, scores)
# print(list(mean_deviation))

variable_x = (input("Values for x: "))
variable_y = (input("Values for y: "))
split_x = variable_x.split(" ")
split_y = variable_y.split(" ")
total_x = sum(variable_x)
print(total_x)
total_y = sum(variable_y)
mean_x = f"{total_x/len(variable_x)}"
mean_y = f"sum{variable_y}/len{variable_y}"
mean_deviation_x = map(lambda variable_x: variable_x - mean_x, variable_x)
mean_deviation_y = map(lambda variable_y: variable_y - mean_y, variable_y)
print(list(mean_deviation_x))
print(list(mean_deviation_y))
print(sum(variable_x))
print(sum(variable_y))