import pandas as pd

#Load both CSV files into separate DataFrames.
list1 = pd.read_csv('in_flight_survey.csv')
list2 = pd.read_csv('post_flight_survey.csv')

#Identify and handle any missing values in both DataFrames. 
# Consider replacing them with the mean of the respective column.
si = list1['Satisfaction_InFlight'].mean()
fs = list1['Food_Service'].mean() 
e = list1['Entertainment'].mean()
sp = list2['Satisfaction_PostFlight'].mean()
bs = list2['Baggage_Service'].mean()
cs = list2['Customer_Support'].mean()

list1['Satisfaction_InFlight'].fillna(value=si, inplace=True)
list1['Food_Service'].fillna(value=fs, inplace=True)
list1['Entertainment'].fillna(value=e, inplace=True)
list2['Satisfaction_PostFlight'].fillna(value=sp, inplace=True)
list2['Baggage_Service'].fillna(value=bs, inplace=True)
list2['Customer_Support'].fillna(value=cs, inplace=True)

#Perform an inner join on Passenger_ID and Flight_Number to combine the two DataFrames.

df = pd.merge(list1, list2, on=['Passenger_ID', 'Flight_Number'], how='inner')

#Group the combined DataFrame by Flight_Number and 
# calculate the average satisfaction scores (Satisfaction_InFlight, Satisfaction_PostFlight).
groupby_avg = df.groupby('Flight_Number')[["Satisfaction_InFlight", "Satisfaction_PostFlight"]].mean().reset_index()

#From the combined DataFrame, 
#select passengers who gave a satisfaction score of less than 5 in either survey and analyze their feedback.

result = df[(groupby_avg['Satisfaction_InFlight'] < 5) | (groupby_avg['Satisfaction_PostFlight'] < 5)]

print(result)
