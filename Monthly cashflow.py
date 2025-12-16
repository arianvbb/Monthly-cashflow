import csv

# Creating empty lists for expenses and income
Expenses = []
Influx = []

with open('average_american_monthly_cashflow.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        if int(row[2]) > 0: # Adding condition to separate income and expenses
            Influx.append(int(row[2]))
        else:
            Expenses.append(int(row[2]))

print(sum(Influx) + sum(Expenses))