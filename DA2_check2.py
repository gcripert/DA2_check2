#importing pandas module to read in csv file

import pandas as pd
df = pd.read_csv('Salary_Data.csv')
print (df)

#taking a look at the data

print (df.shape)

print (df.head())

print (df.columns)


#changing names of columns to be more readable at a glance

df = df.rename(columns = {'How old are you?':'Age',
                          'What industry do you work in?': 'Industry',
                          'If your job title needs additional context, please clarify here:':'Job Context',
                          "What is your annual salary? (You'll indicate the currency in a later question. If you are part-time or hourly, please enter an annualized equivalent -- what you would earn if you worked the job 40 hours a week, 52 weeks a year.)":'Salary',
                          'How much additional monetary compensation do you get, if any (for example, bonuses or overtime in an average year)? Please only include monetary compensation here, not the value of benefits.':'Additional Compensation',
                          'Please indicate the currency':'Currency',
                          'If "Other," please indicate the currency here: ':'Other Currency',
                          'If your income needs additional context, please provide it here:':'Income Context',
                          'What country do you work in?':'Country',
                          "If you're in the U.S., what state do you work in?":'US State',
                          'What city do you work in?':'City',
                          'How many years of professional work experience do you have overall?':'Overall Experience',
                          'How many years of professional work experience do you have in your field?':'Field Experience',
                          'What is your highest level of education completed?':'Education',
                          'What is your gender?':'Gender',
                          'What is your race? (Choose all that apply.)':'Race'
                          })

print (df.columns)




#changing entries with no additional monetary compensation to all be the same value (zero)

df['Additional Compensation'] = df['Additional Compensation'].fillna(0)




#Isolating entries with a college degree or higher

df = df[df['Education'].isin(['College degree', "Master's degree", 'PhD'])]



#Saving cleaned CSV


df.to_csv('cleaned_salary_data.csv')