import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from colors import bcolors as bc

# Create arrays of data
X = np.array([6, 3, 4, 6, 6, 5, 1, 3, 6, 3, 5, 4])
Z = np.array([3, 4, 6, 2, 4, 3, 5, 5, 5, 5, 3, 5])
Y = X + Z

# Pretty print the data
#print(f"{bc.PINK}🎲 X: {str(X)}{bc.ENDC}")
#print(f"{bc.BLUE}🎲 Z: {str(Z)}{bc.ENDC}")
#print(f"\n{bc.GREEN}➕ Y: {str(Y)}{bc.ENDC} \n\n")

## Use pandas to create dataframe
X.tolist(), Z.tolist(), Y.tolist()

df = pd.DataFrame({
    'roll': list(range(1, 13)),
    'die 1': X,
    'die 2': Z,
    'sum': Y
}).set_index('roll')

# Display the dataframe
print(df)

# Compute mean, variance, and SD
print(f"\n\n{bc.PURPLE}{bc.UNDERLINE}Mean:{bc.ENDC} \n{str(df.mean())}")
print(f"\n\n{bc.PURPLE}{bc.UNDERLINE}Variance:{bc.ENDC} \n{str(df.var())}")
print(
    f"\n\n{bc.PURPLE}{bc.UNDERLINE}Standard Deviation:{bc.ENDC}\n{str(df.std())}"
)

# Compute covariance
X = pd.Series(X)
Z = pd.Series(Z)
Y = pd.Series(Y)

covXZ = X.cov(Z)
covXY = X.cov(Y)

print(f"\n\n{bc.PURPLE}{bc.UNDERLINE}Cov(X,Z):{bc.ENDC} {str(covXZ)}")
print(f"{bc.PURPLE}{bc.UNDERLINE}Cov(X,Y):{bc.ENDC} {str(covXY)}")

# Compute correlation
corrXZ = X.corr(Z)
corrXY = X.corr(Y)

print(f"\n\n{bc.PURPLE}{bc.UNDERLINE}Corr(X,Z):{bc.ENDC} {str(corrXZ)}")
print(f"{bc.PURPLE}{bc.UNDERLINE}Corr(X,Y):{bc.ENDC} {str(corrXY)}")

# Plot the data
df.plot(x="die 1", y="sum", kind="scatter")
plt.show()