#This is the code for the Support or Oppose Chart
#It plots party support or opposition to the President, based on whether their party is in power. It looks at each party's support of the President when the President is from their part and opposition when the President is not
#It also charts Trump's tweets about his own agenda, so as to compare his tweets and overall Republican tweets
#This chart is a bargraph
#!/usr/bin/env python3
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('Pro Dems', 'Oppose Repubs', 'Pro Repubs', 'Oppose Dems', 'Trump Agenda')
y_pos = np.arange(len(objects))
performance = [4816,3788,664,952,77] 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of Tweets')
plt.title("Supporting or Opposing the President's Agenda")


# Save the plot into a PDF file
plt.savefig("supportOrOppose.pdf")
