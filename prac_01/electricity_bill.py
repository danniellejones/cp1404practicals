"""CP1404 | Prac_01 Electricity Bill Estimator | Dannielle Jones"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

# print("Electricity bill estimator")
# cents_per_kwh = int(input("Enter cents per kWh: "))
# daily_use_in_kwh = float(input("Enter daily use in kWh: "))
# billing_days = int(input("Enter number of billing days: "))
# total = (daily_use_in_kwh * (cents_per_kwh / 100)) * billing_days
# print(f"Estimated bill ${total}")

cents_per_kwh = 0
print("Electricity bill estimator 2.0")
tariff = int(input("Which tariff? 11 or 31: "))
daily_use_in_kwh = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
if tariff == 11:
    cents_per_kwh = TARIFF_11
elif tariff == 31:
    cents_per_kwh = TARIFF_31
else:
    print("Select tariff is invalid, result will be incorrect")
total = (daily_use_in_kwh * cents_per_kwh) * billing_days
print(f"Estimated bill ${total:.2f}")
