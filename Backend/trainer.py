import pandas as pd
import pickle


weather_df = pd.read_csv("")

file_path = ""

with open(file_path, 'wb') as f:
    pickle.dump(nameofFile, f)

print("Dataset saved as", file_path)
