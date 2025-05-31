
def estimated_price(mileage):
    est_price  = theta0 + (theta1 * mileage)
    return est_price

def main():
    value = input("> Please entre your mileage: ")
    if type(value) != float or type(value) != int:
        print("You should pass int or float")
        exit()
    else:
        print("good")

if __name__ == "__main__":
    main()