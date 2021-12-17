from task_1 import *
import matplotlib.pyplot as plt

import numpy as np
from sklearn.decomposition import PCA


print(f'-----------------------PCA BUILT IN-----------------------')
pca = PCA(n_components=samples)
pca.fit(table)
print('\t'.join([f'{item: 4.5f}' for item in pca.explained_variance_ratio_]))

built_in = pca.explained_variance_ratio_

# display graph
fig = plt.figure()
sub1 = fig.add_subplot(221)
sub2 = fig.add_subplot(222)

sub1.scatter(user_defined, np.linspace(0, 0, samples))
sub2.scatter(built_in, np.linspace(0, 0, samples))
plt.show()
