# HW5
# Use one or three of the built-in variables in your code base
# isinstance
# id()
# split(0)
# Examples:
# Give each user a unique id
# Convert the date of birth format from MM/DD/YYYY to "Month, Day, Year"


valid_states = ("FL", "NY", "CA", "TX", "NC")

expected_salaries = {"FL": 50000, "NY": 70000, "CA": 70000, "TX": 60000, "NC": 50000}


def calculate_expected_salary(number_of_experience_years, user_information, number_of_edu_years):
    try:

        expected_salary = expected_salaries[user_information["State"].upper()]
        number_of_education_years_as_an_integer = int(number_of_edu_years)
      
    except KeyError:
        print("******* INPUT ERROR: Please enter a valid state *******")
    except ValueError:
        print("******* INPUT ERROR: Please enter a valid number for years of learning experience *******")    
    else: #this else only gets executed if the exception is not raised/called

        if number_of_experience_years == 1:
            new_expected_salary = expected_salary - 5000       # 70,000 - 5,000 = $65,000
        elif number_of_experience_years == 2:
            new_expected_salary = expected_salary - 3000
        elif number_of_experience_years == 3:
            new_expected_salary = expected_salary + 1000
        elif number_of_experience_years == 4:
            new_expected_salary = expected_salary + 5000
        else:
            print("******* Sorry. Please enter one of the valid options. *******")

        

        if len(users_coding_languages) < 3:
            new_expected_salary = new_expected_salary - 10000        # 65,000 - 10,000= $55,000
            print("learn some more languages; $10k deduct from the expected salary.")
        elif len (users_coding_languages) > 3:
            new_expected_salary = new_expected_salary + 10000
            print("Your in good shape! $10k added to expected salary.")
        else:
            new_expected_salary = new_expected_salary + 5000

        if int(number_of_education_years) < 3:
            new_expected_salary = new_expected_salary - 5000

        if int(number_of_education_years) > 3:
            new_expected_salary = new_expected_salary + 5000
        else:
            new_expected_salary = new_expected_salary - 5000   

            

    print("Expect $" + str(new_expected_salary) + " for your level of experience")

    for state in expected_salaries:
            salary = expected_salaries[state]
            print("Your starting salary living in " + state + " could have been $" + str(salary) + ".")


while True:
    try:
        users_experience = input("How many years of experience do you have?\n"
        "[1] less than 1 year\n"
        "[2] 1-3 years of experience\n"
        "[3] 3-8 years of experience\n"
        "[4] 8+ years of experience")

        users_experience = int(users_experience)

        users_coding_languages = input("What coding languages do you know? (Separate each language by a comma)")

        if users_coding_languages == '':
            raise ValueError

        users_coding_languages = users_coding_languages.split(",")

        #Ask the user to insert personal info: dob, full_name, country, state, is_active
        user_name = input("What is your Full Name?: \n")

        age = input("Please enter your age: \n")

        try:
            age_as_an_integer = int(age)

        except ValueError:
            print("*******INPUT ERROR: Please enter an integer******* \n") 

        dob = input("Enter Date of Birth (MM/DD/YYYY): \n")

        for state in valid_states:
            print(state)

        #print(valid_states[0]) ****The While loop handles these tasks
        #print(valid_states[1])
        #print(valid_states[2])
        #print(valid_states[3])
        #print(valid_states[4])

        user_state = input("Choose your State (Use the 2 letter abbreviation): \n")


        user_country = input("Country: \n")

        user_is_active = input("Active Developer: \n")

        number_of_education_years = input("Please enter how many years you have been learning to code: \n")

        users_personal_info = {"Full Name": user_name,
                            "Date of Birth": dob,
                            "State": user_state,
                            "Country": user_country,
                            "Active Developer": user_is_active,
                            "Number of education years": number_of_education_years,
                            "Age": age}   
        
        user_id = ("users_personal_info")
        unique_number = id(user_id)
        print(unique_number) 
        
        break
    except ValueError:
        print("Please enter all valid values.")

calculate_expected_salary(users_experience, users_personal_info, number_of_education_years)
