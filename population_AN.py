import sqlite3
import matplotlib.pyplot as plt

# Function to create a database and a table
def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('population_SM.db')
    cursor = conn.cursor()
    
    # Create the population table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()

# Function to insert initial population data for 10 cities
def insert_initial_data():
    cities_data = [
        ('Miami', 2023, 470000),
        ('Orlando', 2023, 300000),
        ('Tampa', 2023, 400000),
        ('Jacksonville', 2023, 900000),
        ('Fort Lauderdale', 2023, 183000),
        ('Tallahassee', 2023, 200000),
        ('St. Petersburg', 2023, 265000),
        ('Hialeah', 2023, 235000),
        ('Port St. Lucie', 2023, 210000),
        ('Cape Coral', 2023, 200000)
    ]
    
    conn = sqlite3.connect('population_SM.db')
    cursor = conn.cursor()
    
    # Insert data into the population table
    cursor.executemany('''
        INSERT INTO population (city, year, population) VALUES (?, ?, ?)
    ''', cities_data)
    
    conn.commit()
    conn.close()

# Function to simulate population growth over 20 years at a 2% growth rate
def simulate_population_growth():
    conn = sqlite3.connect('population_SM.db')
    cursor = conn.cursor()
    
    # Get the cities from the population table
    cursor.execute("SELECT DISTINCT city FROM population")
    cities = cursor.fetchall()
    
    # Simulate growth for each city
    for city in cities:
        city_name = city[0]
        cursor.execute("SELECT population FROM population WHERE city = ? AND year = 2023", (city_name,))
        initial_population = cursor.fetchone()[0]
        
        # Simulate for 20 years
        for year in range(2024, 2044):
            population = int(initial_population * (1.02) ** (year - 2023))
            cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)", (city_name, year, population))
    
    conn.commit()
    conn.close()

# Function to plot population growth for a chosen city
def plot_population_growth():
    conn = sqlite3.connect('population_SM.db')
    cursor = conn.cursor()
    
    # Get the list of cities
    cursor.execute("SELECT DISTINCT city FROM population")
    cities = cursor.fetchall()
    city_names = [city[0] for city in cities]
    
    # Show cities to the user and let them choose
    print("Available cities:")
    for idx, city in enumerate(city_names, 1):
        print(f"{idx}. {city}")
    
    while True:
        city_choice = input("Choose a city by number to see its population growth (or type 'exit' to quit): ")
        if city_choice.lower() == 'exit':
            break
        
        if city_choice.isdigit() and 1 <= int(city_choice) <= len(city_names):
            city_name = city_names[int(city_choice) - 1]
            cursor.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year", (city_name,))
            data = cursor.fetchall()
            
            years = [year for year, _ in data]
            populations = [population for _, population in data]
            
            # Plot the population growth
            plt.plot(years, populations, label=city_name)
            plt.xlabel("Year")
            plt.ylabel("Population")
            plt.title(f"Population Growth in {city_name}")
            plt.grid(True)
            plt.legend()
            plt.show()
        else:
            print("Invalid choice. Please select a valid city or type 'exit'.")
    
    conn.close()

# Main function to control the program flow
def main():
    create_database()
    insert_initial_data()
    simulate_population_growth()
    plot_population_growth()

# Run the program
if __name__ == "__main__":
    main()
