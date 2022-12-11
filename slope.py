#!/usr/bin/env python3

# Created By: Peter Sobowale
# Date: December 8, 2022
# This program is a linear calculator, it solves linear equations
import os
import time


# ------------------- Functions ------------------------
# function solves for y
def solve_for_y(m, x, b):
    solve_y = m * x + b
    return solve_y


# function solves for y if b is a negative
def solve_for_y2(m, x, b):
    solve_y2 = m * x - b
    return solve_y2


# function solves for x
def solve_for_x(y, b, m):
    solve_x = (y - b) / m
    return solve_x


# function solves for x if b is negative
def solve_for_x2(y, b, m):
    solve_x2 = (y + b) / m
    return solve_x2


# function solves for m
def solve_for_m(y, b, x):
    m = (y - b) / x
    return m


# function solves for m if b is a negative
def solve_for_m2(y, b, x):
    m2 = (y + b) / x
    return m2


# function that solve for y int
def solve_y_int(x1, x2, y1, y2, m):
    b = m * x2
    b = y2 - b
    return b


# function solves for b
def solve_for_b(y, m, x):
    solve_b = y - (m * x)
    return solve_b


# function that solves for m
def solve_m1(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    return m


# function that solves for m (negative y1)
def solve_m2(x1, x2, y1, y2):
    m = (y2 + abs(y1)) / (x2 - x1)
    return m


# function that solves for m (negative y2)
def solve_m3(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 + abs(x1))
    return m


# ------------------- Main ---------------------------
def main():
    # set use again to y
    use_again = "y"

    # make while loop and make it run as long as use again is y
    while use_again == "y":

        # set operation check to false and stop time to display message
        operation_check = False
        os.system("clear")
        print("Welcome to the world's greatest calculator!")
        time.sleep(2.5)

        # while loop that runs as long as operation check is false
        while operation_check == False:
            os.system("clear")

            # display choices to the user
            print("Choose from one of the following options:")
            print(
                "\t [1] Solve for y -- y=mx+b \n \t"
                + "[2] Solve for x -- x=(y-b)/m \n \t"
                + " [3] Solve for m -- m=(y-b)/x \n \t "
                + "[4] Solve for b -- b=y-mx \n \t"
                + "[5] Solve for m -- m=(y2-y1)/(x2-x1)"
            )

            # get operation from user
            operation = input("Enter your selection: ")

            # try to make sure no value or operation other than 1-5 is accepted
            try:
                check = int(operation)
                if check >= 1 and check <= 5:
                    operation_check = True
                else:
                    operation_check = False
            except ValueError:
                operation_check = False

        # If else if to determine what code should run
        if check == 1:
            os.system("clear")
            print("******************")
            print("To solve for y, you need m, x and b.")

            # get values for m, x and b
            m_as_a_string = input("Enter a value for m: ")

            # nested try catch to make sure inputs show no errors
            try:
                m_float = float(m_as_a_string)
                x_as_a_string = input("Enter a value for x: ")
                try:
                    x_float = float(x_as_a_string)
                    b_as_a_string = input("Enter a value for b: ")
                    try:
                        b_float = float(b_as_a_string)

                        # if statement to check if 0 is greater than b
                        if 0 > b_float:
                            y2 = solve_for_y2(m_float, x_float, b_float)
                            print(
                                "The value of y is "
                                + str(y2)
                                + "."
                                + "\n"
                                + "The equation is y = "
                                + str(m_float)
                                + "x - "
                                + str(abs(b_float))
                                + "."
                                + "\n"
                            )
                        else:
                            y = solve_for_y(m_float, x_float, b_float)
                            print(
                                "The value of y is "
                                + str(y)
                                + "."
                                + "\n"
                                + "The equation is y = "
                                + str(m_float)
                                + "x + "
                                + str(b_float)
                                + "."
                                + "\n"
                            )

                    except ValueError:
                        print("\nEnter a valid b value.")
                except ValueError:
                    print("\nEnter a valid m value.")
            except ValueError:
                print("\nEnter a valid x value.")

        # case #2
        elif check == 2:
            os.system("clear")
            print("******************")
            print("To solve for x, you need y, b and m.")

            # Get input for y, b and m
            y_as_a_string = input("Enter a value for y: ")

            # nested try catch to make sure inputs show no errors
            try:
                y_float = float(y_as_a_string)
                b_as_a_string = input("Enter a value for b: ")
                try:
                    b_float = float(b_as_a_string)
                    m_as_a_string = input("Enter a value for m: ")
                    try:
                        m_float = float(m_as_a_string)
                        # if statement to make sure m = 0 as thats an error
                        if m_float == 0:
                            print("\nYour m cannot be 0.")
                        else:

                            # if statement to check if b is negative or positive
                            if 0 > b_float:
                                x2 = solve_for_x2(y_float, b_float, m_float)
                                print(
                                    "The value of x is "
                                    + str(x2)
                                    + "."
                                    + "\n"
                                    + "The equation is y = "
                                    + str(m_float)
                                    + "x + "
                                    + str(abs(b_float))
                                    + "."
                                    + "\n"
                                )
                            else:
                                x = solve_for_x(y_float, b_float, m_float)
                                print(
                                    "The value of x is "
                                    + str(x)
                                    + "."
                                    + "\n"
                                    + "The equation is y = "
                                    + str(m_float)
                                    + "x + "
                                    + str(b_float)
                                    + "."
                                    + "\n"
                                )

                    except ValueError:
                        print("\nEnter a valid m value.")
                except ValueError:
                    print("\nEnter a valid b value.")
            except ValueError:
                print("\nEnter a valid y value.")

        # case #3
        elif check == 3:
            os.system("clear")
            print("******************")
            print("To solve for m, you need y, b and x.")

            # get user input for value y, b and x
            y_as_a_string = input("Enter a value for y: ")

            # nested try catch to make sure values have no errors
            try:
                y_float = float(y_as_a_string)
                b_as_a_string = input("Enter a value for b: ")
                try:
                    b_float = float(b_as_a_string)
                    x_as_a_string = input("Enter a value for x: ")
                    try:
                        x_float = float(x_as_a_string)
                        # if statement to make sure x doesn't equal 0
                        if x_float == 0:
                            print("\nYour x cannot be 0.")
                        else:
                            # if statement to check if b is negative or positive
                            if 0 > b_float:
                                m2 = solve_for_m2(y_float, b_float, x_float)
                                print(
                                    "The value of m is "
                                    + str(m2)
                                    + "."
                                    + "\n"
                                    + "The equation is y = "
                                    + str(m2)
                                    + "x + "
                                    + str(abs(b_float))
                                    + "."
                                    + "\n"
                                )

                            else:
                                m = solve_for_m(y_float, b_float, x_float)
                                print(
                                    "The value of m is "
                                    + str(m)
                                    + "."
                                    + "\n"
                                    + "The equation is y = "
                                    + str(m)
                                    + "x + "
                                    + str(b_float)
                                    + "."
                                    + "\n"
                                )

                    except ValueError:
                        print("\nEnter a valid x value.")
                except ValueError:
                    print("\nEnter a valid b value.")
            except ValueError:
                print("\nEnter a valid y value.")

        # case #4
        elif check == 4:
            os.system("clear")
            print("******************")
            print("To solve for b, you need y, m and x.")

            # get input for values y, m and x
            y_as_a_string = input("Enter a value for y: ")

            # Nested try catch to make sure no errors in values
            try:
                y_float = float(y_as_a_string)
                m_as_a_string = input("Enter a value for m: ")
                try:
                    m_float = float(m_as_a_string)
                    x_as_a_string = input("Enter a value for x: ")
                    try:
                        x_float = float(x_as_a_string)

                        # function to solve for b
                        solve_b = solve_for_b(y_float, m_float, x_float)

                        if 0 <= solve_b:
                            print(
                                "The value of b is "
                                + str(solve_b)
                                + "."
                                + "\n"
                                + "The equation is y = "
                                + str(m_float)
                                + "x + "
                                + str(solve_b)
                                + "."
                                + "\n"
                            )
                        else:
                            print(
                                "The value of b is "
                                + str(solve_b)
                                + "."
                                + "\n"
                                + "The equation is y = "
                                + str(m_float)
                                + "x - "
                                + str(abs(solve_b))
                                + "."
                                + "\n"
                            )
                    except ValueError:
                        print("\nEnter a valid x value.")
                except ValueError:
                    print("\nEnter a valid m value.")
            except ValueError:
                print("\nEnter a valid y value.")

        # case 5
        elif check == 5:
            os.system("clear")
            print("******************")
            print("To solve for m, you need x1, x2, y1 and y2.")
            x1_string = input("Enter a value for x1: ")
            try:
                x1_float = float(x1_string)
                x2_string = input("Enter a value for x2: ")
                try:
                    x2_float = float(x2_string)
                    y1_string = "Enter a value for y1: "
                    try:
                        y1_float = float(y1_string)
                        y2_string = input("Enter a value for y2: ")
                        try:
                            y2_float = float(y2_string)
                            if -1 >= y1_float:
                                m = solve_m2(x1_float, x2_float, y1_float, y2_float)
                                b = solve_y_int(
                                    x1_float, x2_float, y1_float, y2_float, m
                                )
                                if b >= 0:
                                    print(
                                        "The value of b is "
                                        + str(b)
                                        + "."
                                        + "\n"
                                        + "The equation is y = "
                                        + str(m)
                                        + "x + "
                                        + str(b)
                                        + "\n" * 2
                                    )
                                else:
                                    print(
                                        "The value of b is "
                                        + str(b)
                                        + "."
                                        + "\n"
                                        + "The equation is y = "
                                        + str(m)
                                        + "x - "
                                        + str(abs(b))
                                        + "\n" * 2
                                    )

                            if -1 >= x1_float:
                                m = solve_m3(x1_float, x2_float, y1_float, y2_float)
                                b = solve_y_int(
                                    x1_float, x2_float, y1_float, y2_float, m
                                )
                                if b >= 0:
                                    print(
                                        "The value of b is "
                                        + str(b)
                                        + "."
                                        + "\n"
                                        + "The equation is y = "
                                        + str(m)
                                        + "x + "
                                        + str(b)
                                        + "\n" * 2
                                    )
                                else:
                                    print(
                                        "The value of b is "
                                        + str(b)
                                        + "."
                                        + "\n"
                                        + "The equation is y = "
                                        + str(m)
                                        + "x - "
                                        + str(abs(b))
                                        + "\n" * 2
                                    )

                            if -1 <= x1_float:
                                m = solve_m1(x1_float, x2_float, y1_float, y2_float)
                                b = solve_y_int(
                                    x1_float, x2_float, y1_float, y2_float, m
                                )
                                if b >= 0:
                                    print(
                                        "The value of b is "
                                        + str(b)
                                        + "."
                                        + "\n"
                                        + "The equation is y = "
                                        + str(m)
                                        + "x + "
                                        + str(b)
                                        + "\n" * 2
                                    )
                                else:
                                    print(
                                        "The value of b is "
                                        + str(b)
                                        + "."
                                        + "\n"
                                        + "The equation is y = "
                                        + str(m)
                                        + "x - "
                                        + str(abs(b))
                                        + "\n" * 2
                                    )

                        except ValueError:
                            print("\nEnter a valid y2 value.")
                    except ValueError:
                        print("\nEnter a valid y1 value.")
                except ValueError:
                    print("\nEnter a valid x2 value.")
            except ValueError:
                print("\nEnter a valid x1 value.")

        # defining use_again to see if user wants to use again or stop
        use_again = input("\n" + "Do you want to use it again? (y/n): ")

        # if statement that stops the program if use again != y
        if not use_again == "y":
            os.system("clear")
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
