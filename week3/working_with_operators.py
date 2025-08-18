a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= 10)
print(b <= 25)


score = 75

print(score >= 50)
print(score < 50)  
print(score == 100)

x = 10
print("Initial value:", x)

x += 5
print("After x += 5:", x)

x -= 2
print("After x -= 2:", x)

x *= 3
print("After x *= 3:", x)

x /= 4
print("After x /= 4:", x)


x %= 3
print("After x %= 3:", x)

x = 4
x **= 2
print("After x **= 2:", x)

x //= 3
print("After x //= 3:", x)



print(not(x == 10)) 


age = 17
score = 85

# Must be younger than 18 AND score above 80
eligible = (age < 18) and (score > 80)

print("Scholarship Eligible:", eligible) 

age = 22
has_ticket = False

can_enter = (age >= 18) and (has_ticket or age < 25)

print("Access Granted:", can_enter) 