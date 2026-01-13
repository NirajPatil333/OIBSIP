# BMI Calculator

def bmi_calculate(weight_kg , height_cm):

    height_m = height_cm / 100
    bmi = weight_kg / (height_m **2)
    return bmi


def bmi_category(bmi):
    if bmi < 18.5 :
        return "Underweight"
    elif  18.5 <= bmi <25:
        return "Normal weight"
    elif  25 <= bmi < 30 :
        return "Overweight"
    else:
        return "Obese"
    
#  Main 
def main():
    print("----BMI Calculator----")
    print("Enter the details :")


    try:
        weight =float(input("Enter your weight (in kg) :"))
        height =float(input("Enter your height (in cm) :"))


        if weight <= 0 or height <= 0 :
            print("weght and height must be positive numbers.")
            return
    
        bmi = bmi_calculate(weight , height)
        category = bmi_category(bmi)

        print("--Result--")
        print(f"Your Bmi is :{bmi :.2f}")
        print(f"category : {category}")
    
    except ValueError:
        print("Enter the valid numeric values :")


if __name__ == "__main__":
    main()




