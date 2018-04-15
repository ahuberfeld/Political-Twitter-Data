#This is the code for the Healthcar Tags Chart
#It plots Democrats' tweets about Healthcare before and after the election, Republicans' tweets about Healthcare before and after the election, and Trump's tweets about healthcare
#The data is represented in a bargraph

#!/usr/bin/env python3
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Dems. Pre', 'Dems. Post', 'Repubs. Pre', 'Repubs. Post', 'Trump')
y_pos = np.arange(len(objects))
performance = [627,764,1631,295,0]
 
plt.bar(y_pos, performance, align='center', alpha=.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of Tweets about Healthcare')
plt.title("Tweeting about Healthcare Before and After Trump's Election")
 
plt.savefig("healthcareTags.pdf")

