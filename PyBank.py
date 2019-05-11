import os
import csv

date, revenue = ([] for i in range(2))

input_file = "budget_data.csv"
output_file = "budget_data_summary.txt"

Budget_data_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')
txt_output_path = os.path.join("summary_data", 'budget_data_summary.txt')

# /Users/GeuntaeJang/Desktop/COLNYC/homework/03-Python/Instructions/PyBank/Resources/budget_data.csv

with open(Budget_data_csv, 'r') as budget_data:
    reader = csv.reader(budget_data, delimiter=',')

    next(reader)

    row_num = 0
    for row in reader:
        date.append(row[0])
        revenue.append(row[1])
        row_num += 1


print("\nFinancial Analysis", "\n" + "-" * 50)

print("Total Months:", row_num)

revenue_sum = 0
for i in revenue:
    revenue_sum += int(i)

print("Total Revenue: $" + str(revenue_sum))

total_revenue_change = 0
for h in range(row_num):
    total_revenue_change += int(revenue[h]) - int(revenue[h - 1])

first_pass = (int(revenue[0]) - int(revenue[-1]))
total_revenue_change_adj = total_revenue_change - first_pass

avg_revenue_change = (total_revenue_change_adj + int(revenue[0])) / row_num
print("Average Revenue Change: $" + str(round(avg_revenue_change)))

high_revenue = 0
for j in range(len(revenue)):
    if int(revenue[j]) - int(revenue[j - 1]) > high_revenue:
        high_revenue = int(revenue[j]) - int(revenue[j - 1])
        high_month = date[j]

print("Greatest Increase in Revenue:", high_month, "($" + str(high_revenue) + ")")

low_revenue = 0
for k in range(len(revenue)):
    if int(revenue[k]) - int(revenue[k - 1]) < low_revenue:
        low_revenue = int(revenue[k]) - int(revenue[k - 1])
        low_month = date[k]

print("Greatest Decrease in Revenue:", low_month, "($" + str(low_revenue) + ")")

print("\n\n")

with open('budget_data_summary.txt', 'w') as text:
    text.write("Financial Analysis for: " + input_file)
    text.write("-" * 50)
    text.write("Total Months: " + str(row_num))
    text.write("Total Revenue: $" + str(revenue_sum))
    text.write("Average Revenue Change: $" + str(round(avg_revenue_change)))
    text.write("Greatest Increase in Revenue: " + str(high_month) + " ($" + str(high_revenue) + ")")
    text.write("Greatest Decrease in Revenue: " + str(low_month) + " ($" + str(low_revenue) + ")")

