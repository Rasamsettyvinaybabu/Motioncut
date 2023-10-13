def kg_to_lb(weight_kg):
    # 1 kilogram is approximately 2.20462 pounds
    return weight_kg * 2.20462

def lb_to_kg(weight_lb):
    # 1 pound is approximately 0.453592 kilograms
    return weight_lb * 0.453592

def main():
    print("Weight Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        weight_kg = float(input("Enter weight in kilograms: "))
        weight_lb = kg_to_lb(weight_kg)
        print(f"{weight_kg} kilograms is approximately {weight_lb} pounds")
    elif choice == 2:
        weight_lb = float(input("Enter weight in pounds: "))
        weight_kg = lb_to_kg(weight_lb)
        print(f"{weight_lb} pounds is approximately {weight_kg} kilograms")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
