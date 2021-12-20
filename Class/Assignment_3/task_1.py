from numpy import linalg as LA
import numpy as np
import pandas as pd
import random
from sklearn.datasets import load_iris


# attributes = int(input('Enter Total Attributes: '))
# samples = int(input('Enter Total Samples: '))

attributes = 2
samples = 10

# Load Iris dataset
# max attributes with iris = 4
# table = load_iris().data[:samples, :attributes]

# generating table
table = np.random.randint(10, 50, attributes*samples).reshape(samples, attributes)

# calculate mean
means = np.mean(table, axis=0)

# subtract mean from each attribute
centered = table-means

print('-----------------------Original Data-----------------------')
columns = [chr(i+1) for i in range(64, (attributes-1)+65)] #generates list of A,B,C...n
print(pd.DataFrame(table, columns=columns).to_string(index=False))
print(f'Means = {means}')


print('----------------------- Mean-Centered Data -----------------------')
columns = [f"{chr(i + 1)} - {chr(i + 1)}'" for i in range(64, (attributes-1)+65)] #generates list of A-A',B-B',C-C'...n
print(pd.DataFrame(centered, columns=columns).to_string(index=False))

# calculate covariance matrix
print('-----------------------Covarience Matrix-----------------------')
cov_matrix = np.cov(centered.T)
print(pd.DataFrame(cov_matrix, columns=[' ' for i in range(attributes)]).to_string(index=False))
print()

print('-----------------------Eigen Values and Vectors-----------------------')
# find eigen values and eigen vectors
eigen_vals, eigen_vectors = LA.eig(np.array(cov_matrix))
# sort eigen values and eigen vectors
idx = eigen_vals.argsort()[::-1]
eigen_vals = eigen_vals[idx]
eigen_vectors = eigen_vectors[:,idx]
#print them
print(f'Eigen Values: {[f"{value: 4.2f}" for value in eigen_vals]}')
print(pd.DataFrame(eigen_vectors, columns=[' ' for i in range(attributes)]).to_string(index=False))
print()

print(f'-----------------------[User-Defined] PCA -----------------------')
# do dot product
user_defined = np.dot(eigen_vectors.T, centered.T).T

columns = [chr(i) for i in range(97, attributes+97)] #generates list of a,b,c...n
print(pd.DataFrame(user_defined, columns=columns).to_string(index=False))
