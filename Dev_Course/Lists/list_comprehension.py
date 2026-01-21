#List Comprehensions
#syntax: [expression for item in iterable]

clicks = [10 , 5 , 15 , 20]

#printing a list where all elements are doubled:
doubled_clicks = [c * 2 for c in clicks]
print(doubled_clicks)

#eg 2:

contributors = ['alice' , 'bob' , 'charlie']
formatted_names = [name.capitalize() for name in contributors]
print(formatted_names)

#[expression for item in iterable if condition]:
nums = [1 , 7 , 8 , 14 , 21 , 30 , 50]
divisible_by_seven = [n for n in nums if n % 7 == 0]
print(divisible_by_seven)

#
ai_team = ['alice', 'bob' , 'charlie']
data_team = ['alice' , 'david' , 'charlie']
shared_skills = [name for name in ai_team if name in data_team]
print(shared_skills)