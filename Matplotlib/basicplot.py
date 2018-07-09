import matplotlib as mpl
import matplotlib.pyplot as plt
#we have three layer backend layer and artist layer and scripting layer
#to get the backend of the system on web to render the graph eg in jupiter notebook we have inline
#artist layer contain container such as figure axes subplot and contain primitive such as  Line 2d,rectangle and collection such as pathcollection
#here we are using scripting layer pyplot
mpl.get_backend()
#Matplotlib's pyplot is an example of a procedural method for building visualizations while SVG, HTML are declarative methods of creating visualizations.
#D3.js is informational method
plt.plot(3,2)
plt.show()
#to show that data point
plt.plot(3,2,".")
# First let's set the backend without using mpl.use() from the scripting layer
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

# create a new figure
fig = Figure()

# associate fig with the backend
canvas = FigureCanvasAgg(fig)

# add a subplot to the fig
ax = fig.add_subplot(111)

# plot the point (3,2)
ax.plot(3, 2, '.')

# save the figure to test.png
# you can see this figure in your Jupyter workspace afterwards by going to
# https://hub.coursera-notebooks.org/
canvas.print_png('test.png')



# create a new figure
plt.figure()

# plot the point (3,2) using the circle marker
plt.plot(3, 2, 'o')
plt.plot(3,4,'o')
# get the current axes
ax = plt.gca()
#to get the current figure
temp=plt.gcf()

# Set axis properties [xmin, xmax, ymin, ymax]
ax.axis([0,6,0,10])
# get all the child objects the axes contains
ax.get_children()
# get children from current axes (the legend is the second to last item in this list)
plt.gca().get_children()
# get the legend from the current axes
legend = plt.gca().get_children()[-2]
# you can use get_children to navigate through the child artists
legend.get_children()[0].get_children()[1].get_children()[0].get_children()

# remove the frame of the chart
for spine in plt.gca().spines.values():
    spine.set_visible(False)
#Or
# TODO: remove the frame of the chart
ax = plt.gca()
ax.set_frame_on(False)