import sys
from pathlib import Path

def isthere(path):
    my_file = Path(path)
    if not my_file.exists():
        print(f"Can't find {path}")
        sys.exit(1)

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
    normalized_mileage = (mileage - km_min) / (km_max - km_min)
    return theta0 + (theta1 * normalized_mileage)

def main():
    try:
        mileage = float(input("Enter mileage (km): "))
        price = estimated_price(mileage)
        print(f"Estimated price: €{price:.2f}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
