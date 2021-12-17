from numpy import linalg as LA
import numpy as np
import random

def print_table(table):
    """

    :param table: a 2D matrix
    :return: none
    """
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(f'{table[j][i]: 4.2f}', end='\t')
        print()


def print_list(List):
    """
    :param List: a 1D Matrix
    :return:
    """
    for item in List:
        print(f'{item: 4.2f}', end='\t')
    print()


def get_means(table):
    """
    :param table: a 2D Matrix
    :return: mean of all the attributes in a list
    """
    means = []
    for row in table:
        means.append(sum(row)/len(row))
    return means


def means_centered(table, means):
    """
    :param table: a 2D Matrix
    :param means: mean of all the attributes in a list
    :return: a list of attribute - their mean
    """
    centered = []
    for i in range(len(table)):
        centered.append([item-means[i] for item in table[i]])
    return centered

def cov(var1, var2):
    """
    :param var1: mean-centered values of attribtue 1
    :param var2: mean-centered values of attribtue 2
    :return: covariance of attribute 1 and attribute 2
    """
    prod = [var1[i]*var2[i] for i in range(len(var1))]
    return (sum(prod)/(len(var1)-1))

def get_cov_matrix(centered):
    """
    :param centered: the centered values (X - X')
    :return: covarience matrix
    """
    attributes = len(centered)
    cov_matrix = [[0 for i in range(attributes)] for i in range(attributes)]
    for i in range(attributes):
        for j in range(attributes):
            cov_matrix[i][j] = cov(centered[i], centered[j])
    return cov_matrix

def dot_product(centered, eigen_vector):
    """

    :param centered: the centered values (X - X')
    :param eigen_vector: eigen vector
    :return: reduced values
    """
    reduced = []
    for i in range(len(centered[0])):
        set = [centered[j][i] for j in range(len(centered))]
        reduced.append(np.dot(np.array(set), np.array(eigen_vector)))
    return reduced


attributes = int(input('Enter Total Attributes: '))
samples = int(input('Enter Total Samples: '))

# attributes = 6
# samples = 10

# generating table
table = list(np.random.randint(10, 50, attributes*samples).reshape(attributes, samples))

# calculate mean
means = get_means(table)

# subtract mean from each attribute
centered = means_centered(table, means)

# add subtracted values in the table
for item in centered:
    table.append(item)

print('-----------------------Table-----------------------')
print(f" A\t\t B\t\t C\t\t D\t\t E\t\t F\t\t A-A'\t B-B'\t C-C'\t D-D'\t E-E'\t F-F'")
print_table(table)

# calculate covariance matrix
print('-----------------------Covarience Matrix-----------------------')
cov_matrix = get_cov_matrix(centered)
print()
print_table(cov_matrix)
print()

print('-----------------------Eigen Values and Vectors-----------------------')
# find eigen values and eigen vectors
eigen_vals, eigen_vectors = LA.eig(np.array(cov_matrix))
eigen_vals = sorted(eigen_vals,reverse=True)
print(f'Eigen Values: {[f"{value: 4.2f}" for value in eigen_vals]}')
print_table(eigen_vectors)
print()

print('-----------------------Selected Eigen Vector-----------------------')
# select an eigen vector subset (selecting randomly)
P = random.randint(0, len(eigen_vectors)-1)
eigen_vector = eigen_vectors[P]
print_list(eigen_vector)


print(f'-----------------------PCA USER DEFINED (PC{P+1})-----------------------')
# do dot product
user_defined = dot_product(centered, eigen_vector)
print_list(user_defined)
