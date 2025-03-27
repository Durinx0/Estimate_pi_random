# Estimate pi, given that you have random (0,1)

import random
import matplotlib.pyplot as plt

def N():
    while True:

        n = input("n = ") #Enter value of n
        if n.isdigit(): #n must be a number
            n = int(n)
            break
        else:
            print("Please enter a number.")
    return n

def main(): #Main function where we calculate pi
    n = N()
    num_points_circle = 0
    inside_x = []
    inside_y = []
    outside_x = []
    outside_y = []

    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            num_points_circle += 1
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)
        
    print("Pi =", 4 * num_points_circle/n) 


    plt.figure(figsize=(6,6))
    plt.scatter(inside_x, inside_y, color='green', s=1, label='Inside Circle')
    plt.scatter(outside_x, outside_y, color='red', s=1, label='Outside Circle')
    plt.legend()
    plt.title("Monte Carlo Estimation of π")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.show()

main()