#advent day 1

def advent_day_1_num_1():
    '''First: If a digit matches digit next to it, function adds them. 
    Works also for last and first digit.'''

    captcha = input("Type or paste captcha here for 1st solution: ").strip()

    digit_list = [int(digit) for digit in captcha]
    n = len(digit_list)
    solution = sum(d for i, d in enumerate(digit_list) if d == digit_list[(i+1) % n])

    print("First solution: ", solution)

advent_day_1_num_1()
