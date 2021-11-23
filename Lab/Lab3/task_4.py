import numpy as np
import pandas as pd
from math import *
import random

def euclidean_dist(p, q):
    return sqrt((sum([pow((q[i]-p[i]), 2) for i in range(len(q))])))


q = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
p = pd.Series([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])

print(f"Euclidean distance: {euclidean_dist(p, q)}")
