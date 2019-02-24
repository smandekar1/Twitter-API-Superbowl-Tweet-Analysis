import numpy as np
import matplotlib.pyplot as plt
from parse_json import counted


counts = []

for key, value in counted:
    counts.append(value)
    # counts += value
print("counts", counts)
men_means = counts

labels = []

for key, value in counted:
    labels.append(key)
    # counts += value
print("labels", labels)
# men_means = counts

# men_means = (20, 35, 30, 35, 27)
# women_means, women_std = (25, 32, 34, 20, 25), (3, 5, 2, 3, 3)

ind = np.arange(len(men_means))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, men_means, width,
                color='olivedrab', label='Count')
# rects2 = ax.bar(ind + width/2, women_means, width, yerr=women_std,
#                 color='IndianRed', label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Word Count')
ax.set_title('Most Common Words from Superbowl Tweets')
ax.set_xticks(ind)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "center")
# autolabel(rects2, "right")
print(counted)
plt.show()