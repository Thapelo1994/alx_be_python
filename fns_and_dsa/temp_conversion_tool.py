# Global conversion factors (though not strictly "factors" in this context,
# these are the constants used in the conversion formulas)
FAHRENHEIT_OFFSET = 32
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    """
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    fahrenheit = (celsius * FAHRENHEIT_TO_CELSIUS_FACTOR) + FAHRENHEIT_OFFSET
    return fahrenheit

def main():
    """
    Handles user interaction for temperature conversion.
    """
    while True:
        try:
            temperature_input = input("Enter the temperature: ")
            temperature = float(temperature_input)
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            continue

        unit = input("Is this temperature in Celsius or Fahrenheit (C/F)? ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
            break
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
            break
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()