import numpy as np  

# Check if all columns sum to 1 and all entries are between 0 and 1
def check_transition(x):
    x_rows, x_cols = x.shape
    for c in range(x_cols):
        col_sum = 0  # Reset col_sum for each column
        for r in range(x_rows):
            entry = x[r, c]
            if entry > 1 or entry < 0:  # Check if entry is between 0 and 1
                return False
            col_sum += entry  # Sum the values in the column
        if not np.isclose(col_sum, 1):  # Check if column sums to 1 (using np.isclose to avoid floating-point errors)
            return False
    return True

# Nth state:
def n_state(n, transition, initial):
    if check_transition(transition):
        P_rows, P_cols = transition.shape
        new = np.identity((P_rows), dtype=np.float64)
        for x in range(n):
            new = np.dot(new,transition)
        return np.dot(new, initial)
    else:
        return False

# Change based on situtaion
S0 = np.matrix('1;0', dtype=np.float64)
P = np.matrix('0.75, 0.4 ; 0.25, 0.6', dtype=np.float64)

n = input("What State:\t")

print(f"{n} state:\n{n_state(int(n), P, S0)}")

print(f"check: {check_transition(P)}")
