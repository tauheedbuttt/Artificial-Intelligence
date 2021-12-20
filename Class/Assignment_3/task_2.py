import pandas as pd

from task_1 import *
import matplotlib.pyplot as plt

import numpy as np
from sklearn.decomposition import PCA


print(f'-----------------------[Built-In] PCA-----------------------')
pca = PCA(n_components=attributes)
built_in = pca.fit_transform(table)

print(pd.DataFrame(built_in, columns=columns).to_string(index=False))


# display graph
fig = plt.figure()
sub1 = fig.add_subplot(211)
sub2 = fig.add_subplot(212)

sub1.scatter(user_defined[:, 0], user_defined[:, 1])
sub2.scatter(built_in[:, 0], built_in[:, 1])

plt.show()
