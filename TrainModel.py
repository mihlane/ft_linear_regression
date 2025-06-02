import pandas as pd
import re
import sys
from pathlib import Path

def isthere(path):
    my_file = Path(path)
    if not my_file.exists():
        print(f'Cant find {path}')
        sys.exit(1)

def normalize(x, min_x, max_x):
    return (x - min_x) / (max_x - min_x)

def estimated_price(mileage):
    isthere("theta")
    isthere("scaling_params")

    with open("theta", "r") as f:
        theta0 = float(f.readline().strip())
        theta1 = float(f.readline().strip())

    with open("scaling_params", "r") as f:
        km_min = float(f.readline().strip())
        km_max = float(f.readline().strip())

    # Normalize mileage
    mileage = (mileage - km_min) / (km_max - km_min)

    return theta0 + (theta1 * mileage)

def get_thetat():
    df = pd.read_csv("data.csv")
    price_data = df['price'].tolist()

    # Min-max normalization of km
    km_min = df['km'].min()
    km_max = df['km'].max()
    km_data = [(km - km_min) / (km_max - km_min) for km in df['km']]

    with open("scaling_params", "w") as f:
        f.write(f"{km_min}\n{km_max}")

    theta0, theta1 = 0, 0
    try:
        with open("theta", "r") as f:
            theta0 = float(f.readline().strip())
            theta1 = float(f.readline().strip())
    except FileNotFoundError:
        pass

    learning_rate = 0.01
    m = len(km_data)

    tmp0, tmp1 = 0, 0
    for i in range(m):
        pred = theta0 + (theta1 * km_data[i])
        error = pred - price_data[i]
        tmp0 += error
        tmp1 += error * km_data[i]

    theta0 -= (learning_rate * tmp0) / m
    theta1 -= (learning_rate * tmp1) / m

    with open("theta", "w") as f:
        f.write(f"{theta0}\n{theta1}")

def main():
    print("please wait our model to train")
    for _ in range(6500): 
        get_thetat()
    print("the model is trained now , you can predict prices!!")

if __name__ == "__main__":
    main()
