#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Novem. 11, 2023
# This is program calculate the power of 2 of of 1 to your number.


def main():
    user_num = str(input("Enter your number:\n"))
    try:
        user_num = int(user_num)
    except ValueError:
        print(f"{user_num} is invalid")
    else:
        if user_num >= 0:
            for count in range(user_num):
                num_power = count**2
                print(f"{count}^2 = {num_power}")
        else:
            print("Cannot be a negative.")
    finally:
        print("Thank you for using the code.")


if __name__ == "__main__":
    main()
