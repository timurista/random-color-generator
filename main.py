
import secrets
from time import sleep
import numpy as np

def get_random_hex_color():
    # get a random number 0-100
    random_number = secrets.randbelow(100)
    # convert hex to rgb
    return random_number

def main():
    # get a random hex color
    random_hex = get_random_hex_color()
    return random_hex

if __name__ == '__main__':
    nums = []
    try:
        while True:
            num = main()
            nums.append(num)
            print(num)
            if len(nums) > 50:
                print(np.average(nums))

            sleep(1)
    except KeyboardInterrupt:
        print("AVERAGE")
        print(np.average(nums))
