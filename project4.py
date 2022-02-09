bill = float(input("Enter the bill to pay:\n"))
people = int(input("input the number of people:\n"))
tip = int(input("Enter the tip to be added "))
tip=1+(tip/100)
answer = (bill/people)*tip

print(round(answer,2))