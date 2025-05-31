import pandas as pd

theta0 = 0
theta1 = 0
def estimated_price(mileage):
    est_price  = theta0 + (theta1 * mileage)
    return est_price
data = pd.read_csv("data.csv")
print(data.__len__())

def get_thetat():
    tmpzero = {}
    tmpone = {}
    with open("data.csv", "r") as file:
        tmpzero, tmpone = file.read([tmpzero, tmpone])
    print(tmpone, tmpone)
    # learning_rate = 1
    # m = 5
    # thata = 0
    # thataa = 0
    # for i in m:
    #     thata += (estimated_price(mileage[i]) - price[i])
    #     thataa += (estimated_price(mileage[i]) - price[i]) * mileage[i]
    # tmpzero = learning_rate * (1/ m) * thata
    # tmpone =  learning_rate * (1/ m) * thataa
    # with open("output.txt", "w") as file:
    #     file.write([tmpzero, tmpone])    

# index  = 0 
def main():
    precision = 30000
    for i in range(precision):
        get_thetat()

if __name__=="__main__":
    main()