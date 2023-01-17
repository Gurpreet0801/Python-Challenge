#Create and Read file 

import os
import csv

#Path for the CSV file in Resources
File = "C:\\Users\\surbh\\Downloads\\Gurpreet\\Gurpreet DA Study\\Module3\\Pybank\\Resources\\budget_data.csv"

#Create the list for sorting
list_data= []


#open the file 
with open(File) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        list_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]),"change": 0})

#Calculating Total Months
TotalMonths = len(list_data)

#Calculate changes in amount
Old_amount = list_data[0]["amount"]
for i in range(TotalMonths):
    list_data[i]["change"] = list_data[i]["amount"] - Old_amount
    change_amount = list_data[i]["amount"]

#Calculate total amount

TotalAmount = sum(row["amount"] for row in list_data)

#calculating Average 


TotalChange = sum(row["change"] for row in list_data)
avg = round(TotalChange/(TotalMonths+1),2)

#Getting Increase and Decrease , key= Lambda x:x function was used to return the output,it takes more arguments
# It have only one expression which can be evaluated.
 
Maximum = max(list_data, key = lambda x:x["change"])
Minimum = min(list_data, key= lambda x:x["change"])


#Print the output

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${TotalAmount}")
print(f"Average Change: ${avg}")
print(f'Greatest Increase in Profits: {Maximum["month"]} (${Maximum["change"]})')
print(f'Greatest Decrease in Profits: {Minimum["month"]} (${Minimum["change"]})')

#Print and Export the .txt file
File = "C:\\Users\\surbh\\Downloads\\Gurpreet\\Gurpreet DA Study\\Python-Challenge\\Pybank\\Resources\\Pybank.txt"
with open(File,"w") as text_file:
    print("Final Analysis" , file=text_file)
    print("----------------------------", file=text_file)
    print(f"Total Months: {TotalMonths}",file=text_file)
    print(f"Total: ${TotalAmount}",file=text_file)
    print(f"Average Change: ${avg}",file=text_file)
