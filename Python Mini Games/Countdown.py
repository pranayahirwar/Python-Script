import datetime

print("Enter your goal and dealine date, seperated with colon")
user_input = input("Example - Learn Docker:26.12.2023\n>>>")
user_input_list = user_input.split(":")

if len(user_input_list) > 3:
    print("You have entered in wrong formate. Please correct it !!!")
else:
    usergoal = user_input_list[0]
    deadline = user_input_list[1]

#! Converting userinput data in datetime formate.
# In strptime method, then 2nd parameter talks about how our date is passed and seperated with what value.
#! if date = 12/10/2022 -> strptime(date, "%d/%m/%Y")
# if year is 22 insted of 2022, use small "y"

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
todays_date = datetime.datetime.today()

time_left = (deadline_date - todays_date)
remain_in_day = time_left.days
remain_in_hours = int(time_left.total_seconds() // 3600)
# print(remain_in_day, remain_in_hours)

#* Telling User how much time left.
if remain_in_day > 3:
    print(f"Dear User, you deadline is in {remain_in_day} days to complete your Goal '{usergoal}'. You can relax :)")
else:
    print(f"Dear User, you deadline is in {remain_in_hours} hours to complete your Goal '{usergoal}', Please build it FAST!!!")
