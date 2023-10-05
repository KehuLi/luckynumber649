import random

def lucky_numbers():
    # creating a pool (1~49)
    # pick 6 samples from the pool
    # put them in the list
    # print it if it is correct
    pool = list(range(1, 50))
    lucky_numbers = random.sample(pool, 6)
    print("Lucky numbers: ", lucky_numbers)

lucky_numbers()