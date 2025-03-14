f_name = "eva"
l_name = "ndegwa"
age = 100
place = "Nairobi"
is_stay = True
km = 50.8
print(km)
print(is_stay)
print(age)
print(f_name,l_name)
print("name: ",f_name, l_name)
print(1, place, age)

print("  ")
temperature = 25

if temperature >= 25:
    print("It’s a hot day! ☀️")
else:
    print("It’s a cool day! ❄️")


 # Control flow example for grading student marks
# This will ask the user for input and grade the student's performance

# Prompt the user for student marks
#50.7marks = int(input("Enter the student's marks (0-100): "))
# marks1 = float(input("Enter the student's marks (0-100): "))
marks1 = 100
# Grading system based on the marks
if marks1 > 70:
    print("Grade: Distinction 🏆")
elif marks1 >= 60:
    print("Grade: Credit 🎖️")
elif marks1 >= 50:
    print("Grade: Pass 👍")
else:
    print("Grade: Fail ❌")


# Print numbers 0 to 4
for i in range(5):
    print(i)

countdown = 5

while countdown > 0:
    print("Counting down:", countdown)
    countdown -= 1  
 
   