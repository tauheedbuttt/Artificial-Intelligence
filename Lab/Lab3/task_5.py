import matplotlib.pyplot as plt

feature1 = [12, 11, 8, 6, 9, 6, 10]
feature2 = [4, 5, 1, 4, 3, 6, 2]

plt.scatter(feature1, feature2)

plt.colorbar(ticks=[0, 1])
plt.show()

