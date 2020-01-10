class Person:
    name = "John"
    lastname = "Doe"
    age = 35
    gender = "male"
    lucky_numbers = [ 7, 11, 13, 17]

class Person_2:
    name = "Jane"
    lastname = "Doe"
    age = 38
    gender = "female"
    lucky_numbers = [ 2, 4, 6, 8]

class Family:
    lastname = "Doe"
    members = [Person, Person_2]       #Array of objects, don't forget to add Jimmy

# STEP 1 Change the fourth lucky number of John Doe to 33
# Your code here

Person.lucky_numbers[3] = 33
print(Person.lucky_numbers)



# STEP 2 Create Little Jimmy's object and then add it to the family object
# Your code here

obj = Person()
obj.name = "Jimmy"
obj.lastname = "Doe"
obj.gender = "male"
obj.lucky_numbers = [ 1, 2, 3, 4, 5]
obj.significant_other = None

Family.members.insert(2,obj.name)


print(Family.members)

def add_allFamilyLuckyNumbers(an_array):
    sum_ofAllLuckyNumbers = 0 # sum_ofAllLuckyNumbers is a number, the sum of all lucky numbers.

    # STEP 3 Loop through all the family members to get all the lucky numbers
    # Your code here
   

    return sum_ofAllLuckyNumbers

def get_lucky_numbers():
    for i in range(1):
        print(Person.lucky_numbers, Person_2.lucky_numbers)
    return i
get_lucky_numbers()


# STEP 4 Print the sum of all the lucky numbers of the Doe's family
# Your code here

