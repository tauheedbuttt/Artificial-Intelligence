import numpy as np
import pandas as pd
import random

# create random list in range 1 - 5
s = pd.Series([random.randrange(1, 5, 1) for i in range(10)])
print(f'Series\n{s}')
print(f'Smallest: {s.idxmin()}')
print(f'Largest: {s.idxmax()}')


