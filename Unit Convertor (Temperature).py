def cel_to_fah(cel):
    return (cel * 9/5) + 32

def fah_to_cel(fah):
    return (fah - 32) * 5/9

def temperature_converter():
    print("Temperature Converter")
    print("Enter your choice:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = int(input("Enter your choice (1 or 2): "))
        
        if choice not in [1, 2]:
            raise ValueError("Invalid choice. Please enter 1 or 2.")

        value = float(input("Enter the temperature value: "))

        if choice == 1:
            result = cel_to_fah(value)
            print(f"{value} Celsius is equal to {result:.2f} Fahrenheit.")
        else:
            result = fah_to_cel(value)
            print(f"{value} Fahrenheit is equal to {result:.2f} Celsius.")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid input.")

if __name__ == "__main__":
    temperature_converter()
