import numpy as np
import os

# Define the conversion folder
conversion_folder = "../textEvalFile"
os.makedirs(conversion_folder, exist_ok=True)  # Create the folder if it doesn't exist

########################################################################################################

# Load the beta.dat file
dat_file_path = "mmMesh/mmMesh.beta.dat"
data = np.load(dat_file_path)

# Create the .txt file path inside the conversion folder
base_name = os.path.basename(dat_file_path).replace('.dat', '.txt')  # Extract file name and change extension
txt_file_path = os.path.join(conversion_folder, base_name)

# Save the data with NumPy-like structure to the .txt file
with open(txt_file_path, 'w') as txt_file:
    txt_file.write(np.array2string(data, separator=', ', formatter={'float_kind': lambda x: f"{x:.6f}"}))

print(f"{dat_file_path} data has been saved to {txt_file_path}")

########################################################################################################

# Load the delta.dat file
dat_file_path = "mmMesh/mmMesh.delta.dat"
data = np.load(dat_file_path)

# Create the .txt file path inside the conversion folder
base_name = os.path.basename(dat_file_path).replace('.dat', '.txt')  # Extract file name and change extension
txt_file_path = os.path.join(conversion_folder, base_name)

# Save the data with NumPy-like structure to the .txt file
with open(txt_file_path, 'w') as txt_file:
    txt_file.write(np.array2string(data, separator=', ', formatter={'float_kind': lambda x: f"{x:.6f}"}))

print(f"{dat_file_path} data has been saved to {txt_file_path}")

########################################################################################################

# Load the gender.dat file
dat_file_path = "mmMesh/mmMesh.gender.dat"
data = np.load(dat_file_path)

# Create the .txt file path inside the conversion folder
base_name = os.path.basename(dat_file_path).replace('.dat', '.txt')  # Extract file name and change extension
txt_file_path = os.path.join(conversion_folder, base_name)

# Save the data with NumPy-like structure to the .txt file
with open(txt_file_path, 'w') as txt_file:
    txt_file.write(np.array2string(data, separator=', ', formatter={'float_kind': lambda x: f"{x:.6f}"}))

print(f"{dat_file_path} data has been saved to {txt_file_path}")

########################################################################################################

# Load the pmat.dat file
dat_file_path = "mmMesh/mmMesh.pmat.dat"
data = np.load(dat_file_path)

# Create the .txt file path inside the conversion folder
base_name = os.path.basename(dat_file_path).replace('.dat', '.txt')  # Extract file name and change extension
txt_file_path = os.path.join(conversion_folder, base_name)

# Save the data with NumPy-like structure to the .txt file
with open(txt_file_path, 'w') as txt_file:
    txt_file.write(np.array2string(data, separator=', ', formatter={'float_kind': lambda x: f"{x:.6f}"}))

print(f"{dat_file_path} data has been saved to {txt_file_path}")

########################################################################################################

# Load the skeleton.dat file
dat_file_path = "mmMesh/mmMesh.skeleton.dat"
data = np.load(dat_file_path)

# Create the .txt file path inside the conversion folder
base_name = os.path.basename(dat_file_path).replace('.dat', '.txt')  # Extract file name and change extension
txt_file_path = os.path.join(conversion_folder, base_name)

# Save the data with NumPy-like structure to the .txt file
with open(txt_file_path, 'w') as txt_file:
    txt_file.write(np.array2string(data, separator=', ', formatter={'float_kind': lambda x: f"{x:.6f}"}))

print(f"{dat_file_path} data has been saved to {txt_file_path}")

########################################################################################################

# Load the test_pc.dat file
dat_file_path = "mmMesh/mmMesh.test_pc.dat"
data = np.load(dat_file_path)

# Create the .txt file path inside the conversion folder
base_name = os.path.basename(dat_file_path).replace('.dat', '.txt')  # Extract file name and change extension
txt_file_path = os.path.join(conversion_folder, base_name)

# Save the data with NumPy-like structure to the .txt file
with open(txt_file_path, 'w') as txt_file:
    txt_file.write(np.array2string(data, separator=', ', formatter={'float_kind': lambda x: f"{x:.6f}"}))

print(f"{dat_file_path} data has been saved to {txt_file_path}")

########################################################################################################

# Load the trans.dat file
dat_file_path = "mmMesh/mmMesh.trans.dat"
data = np.load(dat_file_path)

# Create the .txt file path inside the conversion folder
base_name = os.path.basename(dat_file_path).replace('.dat', '.txt')  # Extract file name and change extension
txt_file_path = os.path.join(conversion_folder, base_name)

# Save the data with NumPy-like structure to the .txt file
with open(txt_file_path, 'w') as txt_file:
    txt_file.write(np.array2string(data, separator=', ', formatter={'float_kind': lambda x: f"{x:.6f}"}))

print(f"{dat_file_path} data has been saved to {txt_file_path}")

########################################################################################################

# Load the vertices.dat file
dat_file_path = "mmMesh/mmMesh.vertices.dat"
data = np.load(dat_file_path)

# Create the .txt file path inside the conversion folder
base_name = os.path.basename(dat_file_path).replace('.dat', '.txt')  # Extract file name and change extension
txt_file_path = os.path.join(conversion_folder, base_name)

# Save the data with NumPy-like structure to the .txt file
with open(txt_file_path, 'w') as txt_file:
    txt_file.write(np.array2string(data, separator=', ', formatter={'float_kind': lambda x: f"{x:.6f}"}))

print(f"{dat_file_path} data has been saved to {txt_file_path}")