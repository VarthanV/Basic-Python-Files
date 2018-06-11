current_users=['pavan','rahul','rajaram','harish','chinni']
newusers=['chinni','pavan','aa','b','cc']
for user in newusers:
    if(user in current_users):
        print(user+"re enter a new name")
    if(user not in current_users):
        print(user+"it i available")
