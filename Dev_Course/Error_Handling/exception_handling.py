try:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = a / b

except ZeroDivisionError as e:
    print(f'A zero division error has occurred: {e.args}')

else: # the else block will execute if no exception was found
    print("No errors.")
    print(f'{a} / {b} : ', c)

finally:
    print('Good Bye!')