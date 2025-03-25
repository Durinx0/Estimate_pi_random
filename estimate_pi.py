# Estimate pi, given that you have random (0,1)

import random

def N():
    while True:

        n = input("n = ")
        if n.isdigit():
            n = int(n)
            break
        else:
            print("Please enter a number.")
    return n

def main():
    n = N()
    num_points_circle = 0
    num_points_total = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            num_points_circle += 1
        num_points_total += 1

    print("Pi =", 4 * num_points_circle/num_points_total) 

main()