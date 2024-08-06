import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = 'Lab Session Data.xlsx'
sheet = 'IRCTC Stock Price'

df = pd.read_excel(file,sheet_name=sheet)

df.columns=df.columns.str.strip()
column_A = 'Date'
column_B = 'Month'
column_C = 'Day'
column_D ='Price'
column_E = 'Open'
column_F = 'High'
column_G = 'Low'
column_H = 'Volume'
column_I = 'Chg%'

B = df[column_B].values
C = df[column_C].values
D = df[column_D].values
I = df[column_I].values
mean_D = np.mean(D)
std_D = np.std(D)


mean_Wed = np.mean(D[C == 'Wed']) 

mean_Apr = np.mean(D[B =='Apr'])



neg_chg = df[column_I].apply(lambda x: x < 0)

prob_loss = neg_chg.sum()/len(df)

pos_chg = df[column_I].apply(lambda x: x > 0)

prob_prof = pos_chg.sum()/len(df)

prob_wed = (C == 'Wed').sum()/len(df)
prob_prof_Wed = pos_chg[C == 'Wed'].sum()/len(df[C == 'Wed'])

prob_prof_and_wed = (pos_chg & (C == 'Wed')).sum() / len(df)

prob_prof_given_wed = prob_prof_and_wed / prob_wed

plt.scatter(C,I)

plt.xlabel('Day')
plt.ylabel('Change in %')
plt.title('Change in % vs Day')


        
print('Mean of D:',mean_D)
print('Standard Deviation of D:',std_D)
print('Mean of Wednesday:',mean_Wed)
print('Mean of April:',mean_Apr)
print('Probability of Loss:',prob_loss)
print('Probability of Profit on Wednesday:',prob_prof_Wed)
print('The Conditional Probability is',prob_prof_given_wed)
plt.show()
