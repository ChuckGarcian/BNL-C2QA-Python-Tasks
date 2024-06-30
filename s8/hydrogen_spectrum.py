# Title: hydrogen_spectrum.py
# Author: Charles 'Chuck' Garcia 

# Note to grader: I struggled with this task and intend/hope to go back and give
# it the proper focus it needs. 

def main ():
  rydberg_constant = 1.0967757e7
  
  # Pfund series
  print("Pfund Series:")
  k = 5
  for j in range(6, 11):
      wave_length = 1 / (rydberg_constant * (1 / pow(k, 2) - 1 / pow(j, 2))) * 1e9
      print(f"\t{j:>2} -> {k:>2}{wave_length:8.0f} nm")

  # Humphreys series
  print("\nHumphreys Series:")
  k = 6
  for j in range(7, 12):
      wave_length = 1 / (rydberg_constant * (1 / pow(k, 2) - 1 / pow(j, 2))) * 1e9
      print(f"\t{j:>2} -> {k:>2}{wave_length:8.0f} nm")

main()