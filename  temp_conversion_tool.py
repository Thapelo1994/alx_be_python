# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Handles user interaction for temperature conversion.
    """
    while True:
        try:
            temp_input = input("Enter the temperature value: ")
            temperature = float(temp_input)
            break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

    while True:
        unit_input = input("Is this temperature in Celsius (C) or Fahrenheit (F)? ").upper()
        if unit_input in ('C', 'F'):
            break
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    if unit_input == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
    elif unit_input == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temp:.2f}°C")

if __name__ == "__main__":
    main()