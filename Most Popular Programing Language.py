
from collections import Counter

import matplotlib.pyplot as plt

import pandas as pd


plt.style.use('seaborn')


# Reading and sorting the data :
    
data = pd.read_csv('Programing Languages Used By People.csv')

responder_id = data['Responder_id']

programing_languages = data['LanguagesWorkedWith']


# Arranging the data :

language_counter = Counter()

for languages in programing_languages:
    language_counter.update(languages.split(';'))
    
languages = []

popularity = []

for items in language_counter.most_common(10):
    languages.append(items[0])
    popularity.append(items[1])
    
languages.reverse()

popularity.reverse()


# Plotting the data :
    
plt.barh(languages, popularity)

plt.title('Top 10 Most Popular Programing Languages')

plt.xlabel("Language used by >>>")

plt.tight_layout()

plt.show()


''' Created By Sourin Das '''
