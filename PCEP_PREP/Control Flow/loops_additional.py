#pass instruction:
for i in range(1, 6):
    pass #placeholder for future code. The loop will run without doing anything.
print("Loop has ended.")

#loops with else statement:
for i in range(1, 6):
    print("Counter:", i)
else:
    print("Loop has ended. This is the else block.") #the else block will be executed after the loop finishes normally (without a break statement)