
def play_fizz_buzz():
    """
    Plays the FizzBuzz game from 1 to 20.

    For each number from 1 to 20, prints:
    - "FizzBuzz" if the number is divisible by both 3 and 5.
    - "Fizz" if the number is divisible by 3 but not by 5.
    - "Buzz" if the number is divisible by 5 but not by 3.
    - The number itself if it is not divisible by either 3 or 5.
    """
    for i in range(1, 21):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':
    play_fizz_buzz()
