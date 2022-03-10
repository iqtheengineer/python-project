def calc_and_show_pay():
    rate = input("How much is your hourly rate?: ")     
    hours = input("How many hours did you work?: ")     
    gross_pay = float(rate) * float(hours)  
    print("Payroll Information:")           
    print("Your pay is %f"%(gross_pay))     
    return gross_pay 
calc_and_show_pay()
