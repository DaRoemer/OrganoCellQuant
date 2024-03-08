import numpy as np
from scipy.special import ellipkinc, ellipeinc

def ellipsoid_surface_area(a, b, c):
    # Sort a, b, c so a >= b >= c
    a, b, c = reversed(sorted([a, b, c]))

    if a == c:
        # The ellipsoid is a sphere
        return 4 * np.pi * a**2

    cosphi  = c / a
    cosphi2 = cosphi**2 
    phi     = np.arccos(cosphi)
    sinphi2 = 1 - cosphi2
    k2      = a**2 * (b**2 - c**2) / b**2 / (a**2 - c**2)
    # Round to 8 decimal places to avoid an unfortunate numerical instability
    k2      = round(k2, 8)

    return 2 * np.pi * c**2  + 2 * np.pi * a * b / np.sin(phi) * (ellipkinc(phi,k2) * cosphi2 + ellipeinc(phi,k2) * sinphi2)



# Function to extract and calculate the difference for one column
def calculate_difference(entry):
    if isinstance(entry, str) and '-' in entry:
        # If the entry is a string and contains a hyphen
        a, b = map(int, entry.split('-'))
        return abs(a - b)
    else:
        return entry
