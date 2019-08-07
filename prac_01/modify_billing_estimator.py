"""Electricity Bill Estimator 2.0"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = int(input("Which traffic? 11 or 31: "))

while tariff != 11 and tariff != 31:
    print("Invalid tariff!")
    tariff = int(input("Which tariff? 11 or 31: "))

daily_kWh_use = float(input("Enter daily use is kWh: "))
number_of_billing_days = float(input("Enter number of billing days: "))

if tariff == 11:
    estimated_bill = (daily_kWh_use * number_of_billing_days) * TARIFF_11
else:
    estimated_bill = (daily_kWh_use * number_of_billing_days) * TARIFF_31

print("Estimated bill: ${:.2f}".format(estimated_bill))

