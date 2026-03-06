import numpy as np

# S.U.M.A.I.Y.A Algorithm v1.0
# Developed by: Sumaiya Akter Tuli
# Objective: Stellar Signal Recovery from Interstellar Dust

def analyze_star(wavelength_nm, radius_solar, mass_solar):
    G = 6.674e-11
    sigma = 5.67e-8
    M_solar = 1.989e30
    R_solar = 6.957e8
    
    # 1. Wien’s Displacement Law
    temperature = 2,900,000 / wavelength_nm
    
    # 2. Stefan-Boltzmann Law
    radius_meters = radius_solar * R_solar
    luminosity = 4 * np.pi * (radius_meters**2) * sigma * (temperature**4)
    
    # 3. Surface Gravity
    mass_kg = mass_solar * M_solar
    gravity = (G * mass_kg) / (radius_meters**2)
    
    return temperature, luminosity, gravity

# Testing the algorithm with a Blue Giant dataset
temp, lum, g = analyze_star(wavelength_nm=450, radius_solar=10, mass_solar=20)
print(f"Results -> Temp: {temp}K, Luminosity: {lum}W, Gravity: {g}m/s^2")
