#Create and Read file 
import os
import csv

#Providing Path

File = "C:\\Users\\surbh\\Downloads\\Gurpreet\\Gurpreet DA Study\\Python-Challenge\\Pybank\\Resources\\budget_data.csv"
#C:\Users\surbh\Downloads\Gurpreet\Gurpreet DA Study\Module3\Pybank\Resources\budget_data.csv

#Create the list for iteration
TotalMonths = []
Profit = []
MonthlyProfit = []


#open the file 
with open(File, encoding="utf-8") as FileOne:
    csvreader = csv.reader(FileOne,delimiter=",") 
    header = next(csvreader) 

#Calculating Total Months
    for row in csvreader: 

        # Appending Total Months and Profit
        TotalMonths.append(row[0])
        Profit.append(int(row[1]))
    for i in range(len(Profit)-1):
        MonthlyProfit.append(Profit[i+1]-Profit[i])

#Calculate changes in amount
    Maximum = max(MonthlyProfit)
    Minimum = min(MonthlyProfit)

#Considering Months value has changed to next month when icrementing

MaxMonth = MonthlyProfit.index(max(MonthlyProfit)) + 1
MinMonth = MonthlyProfit.index(min(MonthlyProfit)) + 1 

#Print the output

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(TotalMonths)}")
print(f"Total: ${sum(Profit)}")
print(f"Average Change: {round(sum(MonthlyProfit)/len(MonthlyProfit),2)}")
print(f"Greatest Increase in Profits: {TotalMonths[MaxMonth]} (${(str(Maximum))})")
print(f"Greatest Decrease in Profits: {TotalMonths[MinMonth]} (${(str(Minimum))})")


#Print and Export the .txt filr
File = "C:\\Users\\surbh\\Downloads\\Gurpreet\\Gurpreet DA Study\\Python-Challenge\\Pybank\\Resources\\Pybank.txt"
with open(File,"w") as text_file:
    print("Final Analysis" , file=text_file)
    print("----------------------------", file=text_file)
    print(f"Total Months: {len(TotalMonths)}",file=text_file)
    print(f"Total: ${sum(Profit)}",file=text_file)
    print(f"Average Change: {round(sum(MonthlyProfit)/len(MonthlyProfit),2)}",file=text_file)
    print(f"Greatest Increase in Profits: {TotalMonths[MaxMonth]} (${(str(Maximum))})",file=text_file)
    print(f"Greatest Decrease in Profits: {TotalMonths[MinMonth]} (${(str(Minimum))})",file=text_file) 

