import os
import pandas as pd

def download_and_load_dataset():
    # Ensure Kaggle credentials directory exists
    # Running this locally would require changing '/root/.kaggle' to the actual path to .kaggle on your PC
    # Running this on Google Colab is highly recommended
    os.makedirs('/root/.kaggle', exist_ok=True)

    # Move the Kaggle token to the appropriate location
    if not os.path.exists('/root/.kaggle/kaggle.json'):
        if os.path.exists('kaggle.json'):
            os.rename('kaggle.json', '/root/.kaggle/kaggle.json')
        else:
            raise FileNotFoundError("kaggle.json not found in the current directory.")

    # Set file permissions (Kaggle CLI requirement)
    os.chmod('/root/.kaggle/kaggle.json', 0o600)

    # Download the dataset
    os.system("kaggle datasets download -d 'niharika41298/nutrition-details-for-most-common-foods'")

    # Unzip it
    os.makedirs('/content/dataset', exist_ok=True)
    os.system("unzip -o nutrition-details-for-most-common-foods.zip -d /content/dataset/")

    # Load into pandas
    csv_path = '/content/dataset/nutrients_csvfile.csv'
    df = pd.read_csv(csv_path)
    return df
