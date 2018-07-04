import json
import time
import matplotlib.pyplot as plt
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, SentimentOptions # Custom options vary on application


with open("datasheet.txt",'r') as file: # Read datasheet
    data_main = file.readlines()

data_main = [x.strip() for x in data_main] 

for i in (0,len(data_main)-1): # Cleanup
    if (data_main[i] == "None"):
        data_main.pop(i)
      
# Enter your IBM cloud credentials and current version
natural_language_understanding = NaturalLanguageUnderstandingV1(
  username = "username",
  password = "password",
  version = "version",
  url = "url")

positive_count = 0 
negative_count = 0

# Limited data_main size for relevance and better server response
data_rel = [] 
for i in range(0,15):
    data_rel.append(data_main[i])


for i in data_rel:
    response = natural_language_understanding.analyze(
    url = i,
    features = Features(
    sentiment = SentimentOptions()))

    pasre_data = (json.dumps(response, indent=2)) # Score and overall sentiment can be retreived, all depends on your analysis method
    label_data = (((pasre_data).split(',')[4]).strip()).split() # Retreive sentiment label
    label_value = str(label_data[1][1:9])
    print(label_value)
    time.sleep(7) # Needed for correct processing speed with the server (variable)
    if ((label_value) == "positive"):
        positive_count += 1

    else:
        negative_count += 1

 
# Data to plot

labels = 'Negative', 'Positive'
sizes = [negative_count,positive_count]
colors = ['lightskyblue', 'lightcoral']
explode = (0,0)
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
    



