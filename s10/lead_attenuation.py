# Title: lead_attenuation.py
# Author: Charles "Chuck" Garcia

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d


def main():
    # Extract Sample data
    file_name = "lead_attenuation.csv"
    file_path = Path(file_name).parent / file_name
    samples = np.genfromtxt(file_path, delimiter=",", skip_header=0)
    energy, attenuation = samples.T

    # Interpolation Logic
    atten_f = interp1d(energy, attenuation, kind="cubic")
    min_energy, max_energy = np.min(energy), np.max(energy)
    energy_est = np.linspace(min_energy, max_energy, 1000)
    attenuation_est = atten_f(energy_est)

    # Plotting Logic
    plt.figure(Path(__file__).name)
    plt.title("Lead Attenuation Coefficient")
    plt.xlabel("Energy [MeV]")
    plt.ylabel(r"$\mu (cm^{-1})$")
    plt.scatter(energy, attenuation, zorder=3)
    plt.plot(energy_est, attenuation_est)
    plt.yscale("log")
    plt.show()

    # Computing Percent of photons
    energy_x = 4.65
    distance = 2
    atten_val = atten_f(energy_x)
    percent = np.exp(-1 * atten_val * distance) * 100

    print(f"Attenuation cofficient for a photon with {energy_x} Mev: {atten_val: >.04f}")
    print(f"Percentage: {percent: >.02f}%")


main()
