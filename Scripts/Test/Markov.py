
import numpy as np  

#nth state:
def n_state(n, transition, initial):
    P_rows, P_cols = transition.shape
    new = np.identity((P_rows), dtype=np.float64)
    for x in range(n):
        new = np.dot(new,transition)
    return np.dot(new, initial)

#change based on situtaion
S0 = np.matrix('1;0', dtype=np.float64)
P = np.matrix('0.75, 0.4 ; 0.25, 0.6', dtype=np.float64)

n = input("What State:\t")

print(f"{n} state:\n{n_state(int(n), P, S0)}")