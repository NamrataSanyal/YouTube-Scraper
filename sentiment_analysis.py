import pandas as pd
from textblob import TextBlob
import re
def getPolarity(text):
    return TextBlob(text).sentiment.polarity
def getSubjectivity(text):
   return TextBlob(text).sentiment.subjectivity

df=pd.read_csv('Covid News Latest.csv')
dict={'title':[],'subjectivity':[],'polarity':[]}
for i in df['Video Title']:
    result = re.sub(r"\W+|_", " ", i)
    dict['title'].append(result)
    dict['subjectivity'].append(getSubjectivity(result))
    dict['polarity'].append(getPolarity(result))
df2=pd.DataFrame(dict)
print(df2)
df.to_csv('sentiment_data.csv')
