# your code goes here!
import time

# number = 10
def countdown(number=10):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number=10):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")
