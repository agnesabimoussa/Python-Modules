

# This function checks if all dependencies are available
# and prints helpful messages to the user

def check_dependencies() -> bool:
    dependencies = ['pandas', 'requests', 'matplotlib', 'numpy']
    all_available = True

    for dep in dependencies:
        try:
            module = __import__(dep)
            version = getattr(module, '__version__', 'unknown')
            print(f"[ok] {dep} ({version})")
        except ImportError:
            print(f"[ko] {dep} is not available")
            all_available = False

    return all_available


# Guide the user to install dependencies needed for this exercise
def print_instructions() -> None:
    print("\nTo install dependencies with pip:")
    print("python -m venv venv")
    print("source venv/bin/activate")
    print("pip install -r requirements.txt")
    print("\nTo install dependencies with Poetry:")
    print("poetry install")
    print("poetry run python loading.py")


# Main logic that executes when all dependencies are available
def load_program() -> None:
    import pandas as pd
    import requests
    import matplotlib.pyplot as plt
    import numpy as np

    print("\nAnalyzing Matrix data...")
    print("Fetching data with requests...")
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users_data = response.json()
    print("Creating matrix with pandas...")
    user_ids = np.array([u['id'] for u in users_data])
    lat = np.array([float(u['address']['geo']['lat']) for u in users_data])
    lng = np.array([float(u['address']['geo']['lng']) for u in users_data])
    matrix = np.column_stack((user_ids, lat, lng))
    df = pd.DataFrame(matrix, columns=['User_ID', 'Latitude', 'Longitude'])
    print(f"Matrix shape: {df.shape}")
    print("Computing with numpy...")
    matrix_mean = np.mean(matrix, axis=0)
    print(f"Mean values [ID, Lat, Lng]: {matrix_mean}")
    print("Visualizing with matplotlib...")
    plt.figure(figsize=(10, 5))
    plt.scatter(df['Longitude'], df['Latitude'],
                c=df['User_ID'], cmap='viridis', s=100)
    plt.colorbar(label='User ID')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Matrix Data: User Locations')
    plt.savefig('matrix_analysis.png', dpi=100)
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    available = check_dependencies()
    if available is False:
        print_instructions()
    else:
        load_program()


if __name__ == "__main__":
    main()
