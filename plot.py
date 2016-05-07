import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

#[EDIT filepath] import the data from file
data = pd.read_csv('test.txt',sep='\t',header=0)

#[EDIT figure dimensions] define the figure
fig, ax = plt.subplots(figsize=(9,5)) #size
#[EDIT] remove gray frame outside of the axes and turns it into white
fig.set_facecolor("white")

# remove border figure
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

#create an auxiliary variable to keep the data's length
samples_size = len(data)

#grid lines
#[EDIT range of lines] horizontal grid lines
min_horizontal = -50
max_horizontal = 110
step_horizontal = 10
for y in range(min_horizontal, max_horizontal, step_horizontal):
    plt.plot(range(-1, samples_size+1), [y] * len(range(-1, samples_size+1)), "--", lw=0.5, color="black", alpha=0.2)
#[EDIT range of lines] vertical grid lines
min_vertical = -50
max_vertical = 111
step_vertical = 10
for x in range(0,samples_size):
    plt.plot([x] * len(range(min_vertical,max_vertical,step_vertical)), range(min_vertical,max_vertical,step_vertical), "--", lw=0.5, color="black", alpha=0.2)

#set x ticks - [EDIT fontsize and opacity of x ticks]
plt.xticks(range(len(list(data.index))), list(data.index), fontsize=18, alpha=0.6)
#set y ticks - [EDIT values that will appear on y axis, the min, the max value and the step; fontsize and opacity too]
min_y_value = -50
max_y_value = 110
step_y_value = 10
plt.yticks(range(min_y_value,max_y_value,step_y_value), range(min_y_value,max_y_value,step_y_value), fontsize=18, alpha=0.6)

#set y label [EDIT text, fontsize and opacity of y label]
plt.ylabel('percentage (%)',fontsize=16, alpha=0.7)

#axis borders
#[EDIT plot's y range, uncomment if you like to specify it]
#ax.set_ylim(0,110)
#[EDIT plot's x range, default is the samples' size]
ax.set_xlim(-1,samples_size+1)

cols = data.columns
#[EDIT add the colors of your preference (divided by 255. to ensure rgb)]
colors = [(158/255., 218/255., 229/255.), (31/255., 119/255., 180/255.), (255/255., 152/255., 150/255.),(255/255., 152/255., 150/255.)]

#plot each line separately with colors from colors
for i, column in enumerate(cols):
    plt.plot(list(range(0,samples_size,1)),data[column.replace("\n", " ")].values, lw=2.5,
             color=colors[i], markersize=12, linewidth=3.0, label=column)
    y_pos = data[column].values[-1] - 0.5

    #[EDIT]if you prefer labels next to values
    if column == data.columns[0]:
        y_pos += 0.5
    elif column == data.columns[1]:
        y_pos -= 0.5
    elif column == data.columns[2]:
        y_pos += 0.75
    elif column == data.columns[3]:
        y_pos -= 0.25
    plt.text(samples_size-0.5, y_pos, column, fontsize=16, color=colors[i]) #create label next to value

plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

#[EDIT] in case you prefer a legend, uncomment all this block
#linewidth = 10
#l1 = Line2D([], [], color=colors[0], linewidth = linewidth)
#l2 = Line2D([], [], color=colors[1], linewidth = linewidth)
#l3 = Line2D([], [], color=colors[2], linewidth = linewidth)
#leg = plt.legend([l1, l2, l3], (cols[0],cols[1],cols[2]), ncol=1, frameon=False, fontsize=20,
 #          bbox_to_anchor=[1, 0.5], handlelength=2, handletextpad=1, columnspacing=2)
#change opacity of legend text
#for text in leg.get_texts():
 #   plt.setp(text, alpha=0.5)

#[EDIT the color of your plot]
ax.patch.set_facecolor('white')
#ensure the layout is tight
plt.tight_layout()
#enjoy your plot
plt.show()
