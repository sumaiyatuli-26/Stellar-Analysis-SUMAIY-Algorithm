import math

# S.U.M.A.I.Y.A Algorithm: Phase 1, 2 & 3
# Developed by: Sumaiya Akter Tuli
# Objective: Signal Recovery, Luminosity Analysis & Temperature Detection

def initial_research_phases():
    print("--- S.U.M.A.I.Y.A Algorithm: Initial Analysis ---")
    
    # Phase 1: Signal Recovery from Dust Interference
    raw_signal = 0.55
    dust_density = 2.4
    recovered_brightness = raw_signal + (dust_density * 0.15)
    print(f"Step 1: Recovered Brightness: {round(recovered_brightness, 3)}")

    # Phase 2: Inverse Square Law for Source Energy
    distance_ly = 10.0
    source_energy = recovered_brightness * (distance_ly ** 2)
    print(f"Step 2: Source Energy (Luminosity): {round(source_energy, 2)} Units")

    # Phase 3: Surface Temperature (Wien's Law)
    peak_wavelength_nm = 500 
    wien_constant = 2900000
    temperature = int(wien_constant / peak_wavelength_nm)
    print(f"Step 3: Star Temperature: {temperature} Kelvin")

    # Classification by Temperature
    if temperature > 10000:
        star_type = "Blue Star (Hot)"
    elif temperature > 5000:
        star_type = "Yellow Star (Sun-like)"
    else:
        star_type = "Red Dwarf (Cool)"
    
    print(f"Result: Classified as {star_type}")

if __name__ == "__main__":
    initial_research_phases()
