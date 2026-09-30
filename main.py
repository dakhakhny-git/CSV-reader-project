import pandas as pd

def main():
    file_path = input("Enter the path to your CSV file: ").strip()
    
    try:
        df = pd.read_csv(file_path)
        
        print("\nFirst 3 rows of the CSV:")
        print(df.head(3))
        
    except FileNotFoundError:
        print("Error: File not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()