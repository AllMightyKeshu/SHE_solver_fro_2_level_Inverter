import numpy as np  # For numerical operations like sin and pi
from scipy.optimize import minimize  # For optimization using minimize function

def objective(alfa, N, m):
    """
    Calculates the absolute difference between the sine of the firing angle (alfa)
    and the sine of the harmonic elimination equation for the m-th harmonic.
    
    Arguments:
    alfa -- the firing angle in radians
    N -- total number of harmonics
    m -- the harmonic to be eliminated
    
    Returns:
    The absolute difference between the two sine values.
    """
    return np.abs(np.sin(alfa) - np.sin((2*m - 1) * np.pi / (2 * N)))

def solve_she_equations(initial_guess, N, m, max_iter):
    """
    Solves the Selective Harmonic Elimination (SHE) equations using the minimize function
    to find the optimal firing angle that eliminates the m-th harmonic out of N total harmonics.
    
    Arguments:
    initial_guess -- the initial guess for the firing angle
    N -- total number of harmonics
    m -- the harmonic to be eliminated
    max_iter -- maximum number of iterations for the solver to find a solution
    
    Returns:
    The optimal firing angle if the solution converges; otherwise, None.
    """
    result = minimize(objective, initial_guess, args=(N, m), bounds=[(0, 2 * np.pi)], options={'maxiter': max_iter})
    
    if result.success:
        return result.x[0]
    else:
        return None

# Collect user input for the initial guess, total number of harmonics, harmonic to eliminate, and max iterations
initial_guess = float(input("Enter initial guess (in radians): "))
N = int(input("Enter total number of harmonics (N): "))
m = int(input("Enter number of desired harmonics to eliminate (m): "))
max_iter = int(input("Enter maximum number of iterations: "))

# Solve the SHE equations using the provided input values
result = solve_she_equations(initial_guess, N, m, max_iter)

# Display the result or inform the user if the solution was not found
if result is not None:
    print(f"The firing angle (in radians) to eliminate {m} harmonics out of {N} is: {result:.6f}")
else:
    print("Failed to converge to a solution within the specified iterations.")
