import numpy as np 
import pandas as pd

file = 'Lab Session Data.xlsx'
sheet_name = 'Purchase data'

# Read the data from the specified sheet
df = pd.read_excel(file, sheet_name=sheet_name)

# Remove any leading or trailing spaces from column names
df.columns = df.columns.str.strip()

# Define column names for matrix A and C
column_names_A = ['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']
column_name_C = 'Payment (Rs)'

# Extract matrices
A = df[column_names_A].values
C = df[[column_name_C]].values

# Compute the rank of matrix A
rank_A = np.linalg.matrix_rank(A)

# Find the dimensionality of the vector space spanned by columns of A
dimensionality_vector_space = rank_A

# Number of vectors (rows) in matrix A
num_vectors = A.shape[0]

# Compute the pseudo-inverse of matrix A
A_pseudo_inv = np.linalg.pinv(A)

# Compute the cost matrix X
X = A_pseudo_inv @ C

df['STATUS'] = df[column_name_C].apply(lambda x: 'RICH' if x > 200 else 'POOR')

# Print the results
print("Matrix A (Candies, Mangoes, Milk Packets):")
print(A)
print("\nMatrix C (Payment):")
print(C)

print("\nDimensionality of the vector space:", dimensionality_vector_space)
print("Number of vectors in the vector space:", num_vectors)
print("Rank of Matrix A:", rank_A)

print("\nCost of each product (Matrix X):")
print(X)

print(df[['Customer', 'Payment (Rs)', 'STATUS']].head())