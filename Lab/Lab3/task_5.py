import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# Data
feature1 = [12, 11, 8, 6, 9, 6, 10]
feature2 = [4, 5, 1, 4, 3, 6, 2]
classes = ['a', 'a', 'a', 'b', 'b', 'a', 'b']

# Add Legend
a = mlines.Line2D([], [], marker='o', linestyle='None',
                          markersize=10, label='Class: a')
b = mlines.Line2D([], [], marker='x', linestyle='None',
                          markersize=10, label='Class: b')
plt.legend(handles=[a,b])

# Scatter the Graph
for i in range(len(classes)):
    marker='o'
    if classes[i]=='b': 
        marker='x'
    plt.scatter(feature1[i], feature2[i], marker=marker)

plt.show()

