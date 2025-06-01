import pandas as pd
import re
import sys
from pathlib import Path
from PredictPrice import isthere, estimated_price
import numpy as np

def get_thetat():
    tmpzero = 0.0
    tmpone = 0.0
    
    # try:
    data = np.loadtxt("data.csv", delimiter=",", skiprows=1)
    km_data = data[:, 0]
    price_data = data[:, 1]
		# return mileages, prices
    # except:
	# 	print('⛔ Error: Invalid Data')
	# 	exit()
          
    # df = pd.read_csv("data.csv")
    # km_data = df['km'].tolist()
    # price_data = df['price'].tolist()

    # print("KM data:", km_data)
    # print("Price data:", price_data)
    # with open("data.csv", "r") as file:
    #     tmpzero, tmpone = file.read([tmpzero, tmpone])
    # print(tmpone, tmpone)
    learning_rate = 0.001
    m = km_data.__len__()
    # print(m)
    isthere("theta")
    with open("theta", "r") as f:
        file = f.read()
        f.close()
        # print(file)
        file = file.split("\n")
        tmpzero = float(file[0])
        tmpone = float(file[1])
    # print("hello",tmpzero, "m = ", m)
    # tmpzero = 
    # thataa = 0
    delta0 = 0.0
    delta1 = 0.0
    precision = 1000
    for i in range(precision):
        # print("type is", type(km_data))
        pred = (estimated_price(km_data, delta0,delta1))
        tmpzero = pred - price_data
        delta0 -=  (learning_rate * (1.0/ m)) * np.sum(tmpzero)
        delta1 -= (learning_rate * (1.0/ m)) * np.sum(tmpzero * km_data)
        # PrintedThetaOne =  -((learning_rate * (1/ m)) * tmpone)
        # PrintedThetaZero = -((learning_rate * (1/ m)) * tmpzero)
        # print(tmpzero)
    # print(tmpone)
    print("theta",delta0)
    print("tcd heta",delta1)
    with open("theta", "w") as file:
        file.write(delta0.__str__())
        file.write('\n')  # Add newline between them
        file.write(delta1.__str__())
    # with open("output.txt", "w") as file:
    #     file.write([PrintedThetaZero.__str__(), PrintedThetaOne.__str__()])


def main():
    # precision = 1000
    # for i in range(precision):
    get_thetat()

if __name__=="__main__":
    main()