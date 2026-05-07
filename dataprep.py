import os
import pandas as pd

root = "SisFall_dataset/SisFall_dataset"

# uncomment to convert all files to .csv
for subject_folder in os.listdir( root ):
    subject_path = os.path.join(root, subject_folder)
    for filename in os.listdir( subject_path ):
        if filename.endswith(".txt"):
            old_path = os.path.join(subject_path, filename)
            new_path = os.path.join(subject_path, filename.replace(".txt", ".csv"))
            os.rename(old_path, new_path)

# uncomment to remove colums 6, 7, 8
for subject_folder in os.listdir( root ):
    subject_path = os.path.join(root, subject_folder)
    for filename in os.listdir( subject_path ):
        if filename.endswith(".csv"):
            df = pd.read_csv(subject_path + "/" + filename, header=None)
            df = df.drop(columns=[6, 7, 8])
            df.to_csv(subject_path + "/" + filename, index = False, header = False)
        
#uncomment to add timestamp col then add headers
for subject_folder in os.listdir( root ):
    subject_path = os.path.join(root, subject_folder)
    for filename in os.listdir( subject_path ):
        if filename.endswith(".csv"):
            df = pd.read_csv(subject_path + "/" + filename, header=None)
            df.insert(0, "timestamp", df.index * 5)
            df.columns = ["timestamp", "acc_x", "acc_y", "acc_z", "gyro_x", "gyro_y", "gyro_z"]
            df.to_csv(subject_path + "/" + filename, index = False)