import sys

def fizzbuzz(num, fizz=3, buzz=5):
    '''
    INPUT: int, int, int
    OUTPUT: string
    Return "Fizz" if num is divisible by fizz,
           "Buzz" if num is divisible by buzz,
           "FizzBuzz" if num is dibisible by both fizz and buzz, and
           "" otherwise
    '''

    if num % fizz == 0 and num % buzz ==0:
      return "FizzBuzz"
    elif num % fizz == 0:
      return "Fizz"
    elif num % buzz == 0:
      return "Buzz"
    else: return ""

    pass



if __name__ == '__main__':
    print fizzbuzz(int(sys.argv[1]), 3, 5)