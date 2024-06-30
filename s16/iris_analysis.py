# Title: iris_analysis.py
# Author: Charles "Chuck" Garcia

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Extract Iris Data
    file_name = "iris.csv"
    file_path = Path(__file__).parent / file_name
    data = np.genfromtxt(file_path, delimiter=",", skip_header=True, dtype=None, encoding=None)

    # Create a dictionary to store data for each variety
    flower_dic = {}
    
    for flower in data:
        petal_length = float(flower[2])
        petal_width = float(flower[3])
        variety = flower[4]
        
        if variety in flower_dic:
            flower_dic[variety].append((petal_length, petal_width))
        else:
            flower_dic[variety] = [(petal_length, petal_width)]

    # Convert lists to numpy arrays for easier plotting
    for variety in flower_dic:
        flower_dic[variety] = np.array(flower_dic[variety])

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    colors = ['red', 'green', 'blue']
    
    for (variety, data), color in zip(flower_dic.items(), colors):
        plt.scatter(data[:, 0], data[:, 1], c=color, label=variety, alpha=0.7)

    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Petal Width (cm)')
    plt.title('Iris Flower Data: Petal Length vs Petal Width')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()