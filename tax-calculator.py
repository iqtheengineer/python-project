#ACME Corporation needs a simple payroll program written in Python.
#The Input Items are the following:
#Employee Name
#Hours worked
#Pay Rate (hourly)

#Employees are to receive 1.5x pay rate for hours over 40
#Fed Tax = 10%
#State tax = 3%
#FICA rate = 7%

#The program output should be the following:
#Name Hours Rate Grosspay Fed Tax State Tax FICA Netpay
#** Bonus: Bonus points if program can process 5 employees inputs before program ends

#Gathers employee's info
employee_name = input("Employee Name:")

hours_worked = int(input("Hours Worked:"))

pay_rate = int(input("Pay Rate:"))

fed_tax = .90

state_tax = .97

fica_rate = .93


#Calculates input
if (hours_worked) > 40:
    net_pay = (pay_rate * 1.5 * hours_worked)
    print(net_pay * fed_tax * state_tax * fica_rate)

elif (hours_worked) <= 40:
    net_pay2 = (pay_rate * hours_worked) 
    print(net_pay2 * fed_tax * state_tax * fica_rate)

else:
    print("Please Work") 
