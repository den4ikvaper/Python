current_age = input("What is your current age?\n")

life_age_expectation = input("\nHow many years you expect to live?\n")

left_days = int(life_age_expectation)*365-(int(life_age_expectation)*365-int(current_age)*365)
left_weeks = int(life_age_expectation)*52-(int(life_age_expectation)*52-int(current_age)*52)
left_month = int(life_age_expectation)*12-(int(life_age_expectation)*12-int(current_age)*12)

all_days = int(life_age_expectation)*365
all_weeks = int(life_age_expectation)*52
all_month = int(life_age_expectation)*12

life_percent_left = round(int(current_age)*365/((int(life_age_expectation)*365)/100), 1)

print(f"\nYou left {left_days} days from {all_days}, {left_weeks} weeks from {all_weeks}, and {left_month} from {all_month} month.")

print(f"\nYou already left {life_percent_left}% of your life")