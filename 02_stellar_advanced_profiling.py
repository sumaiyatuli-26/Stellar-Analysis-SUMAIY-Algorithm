import math
import random

# S.U.M.A.I.Y.A Algorithm: Phase 8 & 10
# Developed by: Sumaiya Akter Tuli
# Objective: Advanced Calculation of Stellar Mass, Gravity, and Lifespan

def advanced_stellar_profiling():
    print("--- S.U.M.A.I.Y.A Algorithm: Advanced Profiling ---")
    print("-" * 55)

    # Simulating data for an observed star
    temperature = 12000  # Kelvin
    distance_ly = 5.5    # Million Light Years
    
    # 1. Mass Estimation (Relative to the Sun)
    # Using the Mass-Luminosity relation logic
    stellar_mass = (temperature / 5800) ** 2  
    
    # 2. Radius and Gravity Calculation
    stellar_radius = math.sqrt(stellar_mass)
    surface_gravity = stellar_mass / (stellar_radius ** 2) 

    # 3. Estimated Lifespan (Based on nuclear fuel consumption rate)
    # T = 10 / M^2.5 (Billion Years)
    lifespan = 10 / (stellar_mass ** 2.5) 
    
    # 4. Age simulation (How much of its life has passed)
    current_age = random.uniform(0.01, lifespan)

    # Output Results
    print(f"Stellar Mass: {round(stellar_mass, 2)} Solar Masses")
    print(f"Surface Gravity: {round(surface_gravity, 2)} G (Relative to Sun)")
    print(f"Estimated Lifespan: {round(lifespan, 3)} Billion Years")
    print(f"Current Estimated Age: {round(current_age, 3)} Billion Years")
    print("-" * 55)
    print("Advanced Profiling Successful.")

if __name__ == "__main__":
    advanced_stellar_profiling()
