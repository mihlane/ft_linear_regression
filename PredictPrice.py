import re
import sys
from pathlib import Path

def isthere(path):
    my_file = Path(path)
    if my_file.exists() == False:
        print(f'Cant find {path}')
        sys.exit(1)

def get_type(value):
    if re.fullmatch(r"\d*\.\d+", value):
        return float(value)
    elif re.fullmatch(r"\d+", value):
        return int(value)
    else:
        print('Please enter a number!')
        sys.exit(1)

def estimated_price(mileage):
    isthere("theta")
    with open("theta", "r") as f:
        file = f.read()
        f.close()
        print(file)
        file = file.split("\n")
        theta0 = float(file[0])
        theta1 = float(file[1])
    est_price  = theta0 + (theta1 * mileage)
    # print(type(est_price), type(theta0), est_price)
    # est_price = get_type(est_price)
    return est_price


def main():
    value = input("> Please entre your mileage: ")
    value = get_type(value)
    predected_price = estimated_price(value)
    if predected_price < 200:
        print("the predected price may not be reliable")
    # else:
    print(f"the estimated price is : {predected_price}")

if __name__ == "__main__":
    main()