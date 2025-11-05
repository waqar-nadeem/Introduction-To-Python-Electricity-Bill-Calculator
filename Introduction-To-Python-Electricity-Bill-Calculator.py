units_consumed = int(input("Enter the number of units consumed: "))
if units_consumed <= 100:
    total_bill = units_consumed * 10
elif units_consumed <= 200:
    total_bill = (100 * 10) + (units_consumed - 100) * 15
else:
    total_bill = (100 * 10) + (100 * 15) + (units_consumed - 200) * 20
print("The total electricity bill is Rs.", total_bill)
