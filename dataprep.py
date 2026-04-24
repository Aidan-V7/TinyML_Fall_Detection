import os
import pandas as pd

root = "Not_Fall"

# uncomment to convert all files to .csv
for filename in os.listdir( root ):
    if filename.endswith(".txt"):
        old_path = os.path.join(root, filename)
        new_path = os.path.join(root, filename.replace(".txt", ".csv"))
        os.rename(old_path, new_path)

# uncomment to remove colums 6, 7, 8
for filename in os.listdir( root ):
    if filename.endswith(".csv"):
        df = pd.read_csv(root + "/" + filename, header=None)
        df = df.drop(columns=[6, 7, 8])
        df.to_csv(root + "/" + filename, index = False, header = False)
        
#uncomment to add timestamp col then add headers
for filename in os.listdir( root ):
    if filename.endswith(".csv"):
        df = pd.read_csv(root + "/" + filename, header=None)
        df.insert(0, "timestamp", df.index * 5)
        df.columns = ["timestamp", "acc_x", "acc_y", "acc_z", "gyro_x", "gyro_y", "gyro_z"]
        df.to_csv(root + "/" + filename, index = False)
            
            
            
            


