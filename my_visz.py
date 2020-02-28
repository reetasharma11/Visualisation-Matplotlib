import pandas as pd
import matplotlib.pyplot as plt
import os


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


admsn = pd.read_csv(filepath_or_buffer='/home/reeta/Python-Visualization/graduate_admissions/Admission_Predict.csv',
                      sep=',',
                      header=0)

pretty_print("Admission dataframe", admsn.to_string())
pretty_print("Admission columns", admsn.columns)

os.makedirs('plots', exist_ok=True)

# Plotting line chart
plt.plot(admsn['GRE Score'], color='red')
plt.title('GRE Score')
plt.ylabel('GRE Score')
plt.savefig(f'plots/GRE_plot.png', format='png')
plt.clf()

# Plotting histogram
plt.hist(admsn['Chance of Admit '], bins=8, color='g')
plt.title('Chance of Admit ')
plt.xlabel('Chance of Admit ')
plt.ylabel('TOEFL Score')
plt.savefig(f'plots/Chance of Admit_hist.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(admsn['GRE Score'], admsn['Chance of Admit '], color='g')
plt.title('GRE Score to Chance of Admit')
plt.xlabel('GRE Score')
plt.ylabel('Chance of Admit')
plt.savefig(f'plots/GRE_Score_to_Chance_of_Admit.png', format='png')

plt.close()

