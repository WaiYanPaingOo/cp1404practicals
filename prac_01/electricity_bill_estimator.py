"""Electricity Bill Estimator"""

cents_per_kWh = float(input("Enter cents per kWh: "))
daily_kWh_use = float(input("Enter daily use is kWh: "))
number_of_billing_days = float(input("Enter number of billing days: "))
estimated_bill = (daily_kWh_use * number_of_billing_days) * cents_per_kWh

print("Estimated bill: ${}".format(estimated_bill))
