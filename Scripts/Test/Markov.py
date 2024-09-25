
import numpy as np  


# Check if all rows sum to 1 and all entries are between 0 and 1
def check_transition(x):
    x_rows, x_cols = x.shape
    for r in range(x_rows):
        row_sum = 0
        for c in range(x_cols):
            entry = x[r, c]
            if entry > 1 or entry < 0:  # Check if entry is between 0 and 1
                return False
            row_sum += entry
        if not np.isclose(row_sum, 1):  # Check if row sums to 1 (using np.isclose to avoid floating-point errors)
            return False
    return True

# Nth state:
def n_state(n, transition, initial):
    P_rows, P_cols = transition.shape
    new = np.identity((P_rows), dtype=np.float64)
    for x in range(n):
        new = np.dot(new,transition)
    return np.dot(new, initial)

# Change based on situtaion
S0 = np.matrix('1;0', dtype=np.float64)
P = np.matrix('0.75, 0.4 ; 0.25, 0.6', dtype=np.float64)

n = input("What State:\t")

print(f"{n} state:\n{n_state(int(n), P, S0)}")
