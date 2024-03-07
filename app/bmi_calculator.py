def calculate_bmi(height_feet, height_inches, weight_pounds):
    # Convert height to inches
    height_total_inches = (height_feet * 12) + height_inches
    # Convert height in inches to meters (1 inch = 0.0254 meters)
    height_meters = height_total_inches * 0.0254
    # Convert weight in pounds to kilograms (1 pound = 0.453592 kilograms)
    weight_kg = weight_pounds * 0.453592
    # Calculate BMI
    bmi = weight_kg / (height_meters ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

def main():
    height_feet = int(input("Enter height (feet): "))
    height_inches = int(input("Enter height (inches): "))
    weight_pounds = int(input("Enter weight (pounds): "))
    
    bmi = calculate_bmi(height_feet, height_inches, weight_pounds)
    category = bmi_category(bmi)
    
    print(f"BMI: {bmi:.2f}, Category: {category}")

if __name__ == "__main__":
    main()
