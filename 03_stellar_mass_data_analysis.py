import random

# S.U.M.A.I.Y.A Algorithm: Phase 11
# Developed by: Sumaiya Akter Tuli
# Objective: Massive Data Classification and Statistical Analysis (100,000 Objects)

def massive_data_analysis(num_stars):
    print(f"--- S.U.M.A.I.Y.A Algorithm: Big Data Analysis ---")
    print(f"Processing Survey Data of {num_stars} Stars...")
    print("-" * 55)

    blue, yellow, red = 0, 0, 0
    
    # Simulating massive dataset analysis
    for _ in range(num_stars):
        # Assigning random temperatures to simulate a real-world star survey
        temp = random.randint(3000, 30000)
        
        if temp > 10000: 
            blue += 1
        elif temp > 5000: 
            yellow += 1
        else: 
            red += 1

    # Statistical Output
    print(f"Analysis Status: 100% Completed")
    print(f"1. Blue Stars (Very Hot): {blue}")
    print(f"2. Yellow Stars (Sun-like): {yellow}")
    print(f"3. Red Dwarfs (Cool): {red}")
    print("-" * 55)
    print("Statistical survey of extragalactic objects is successful.")

if __name__ == "__main__":
    # Analyzing 100,000 stars
    massive_data_analysis(100000)

