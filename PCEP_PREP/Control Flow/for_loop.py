#for loop:

for i in range(1, 6): #range() function generates a sequence of numbers from 1 to 5
    print("Counter:", i)
print("For loop has ended.")


#break statement:
for i in range(1, 11):
    if i == 5:
        break #exit the loop when i is equal to 5
    print("Counter:", i)
print("Loop has ended.")

#continue statement:
for i in range(1, 11):
    if i % 2 == 0:
        continue #skip the rest of the loop body and move to the next iteration if i is even
    print("Counter:", i)
print("Loop has ended.")