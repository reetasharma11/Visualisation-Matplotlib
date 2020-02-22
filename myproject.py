import pandas as pd
  

def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')




# We're now creating a dataframe straight from a data file
admission= pd.read_csv(filepath_or_buffer='/home/reeta/python-notebook/graduate_admissions/Admission_Predict.csv',
                      sep=',',
                      header=0)

#pretty_print("Printing an entire dataframe", admission.to_string())
#pretty_print("Summarized info on dataframe", admission.info())

c = admission.corr(method='pearson')
#print(c)

# Question:
# 1. What is the most important factor to get admitted.
# 2. How the GRE and TOEFL correlated?
# 3. Is there any correlation between CGPA and GRE score?
##
#1. The most important factor to get admitted is cgpa because it has highest correlation with chance of admit.
# after that GRE Score and TOEFL Score.
#2.GRE score and TOEFL are also strongly correlated.
#3.Yes they are also correlated. 

#pretty_print("Show all column names for a dataframe", admission.columns)
#pretty_print("Show all index names for a dataframe", admission.head(1))

#print(admission['Research Experience'].max())


##### summary statistics on dataset
#The dataset contains several parameters which are considered important during the application for Masters Programs.
#The parameters included are :

#GRE Scores ( out of 340 )
#TOEFL Scores ( out of 120 )
#University Rating ( out of 5 )
#Statement of Purpose and Letter of Recommendation Strength ( out of 5 )
#Undergraduate GPA ( out of 10 )
#Research Experience ( either 0 or 1 )
#Chance of Admit ( ranging from 0 to 1 )



