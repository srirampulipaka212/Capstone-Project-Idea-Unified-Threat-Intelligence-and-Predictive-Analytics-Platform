import pandas as pd
import numpy as np
from geolite2 import geolite2

reader = geolite2.reader()

def geo_lookup(ip):
    try:
        match = reader.get(ip)
        return match['country']['iso_code'] if match else None
    except:
        return None

def clean_data(input_path='processed/merged_data.csv', output_path='processed/cleaned_data.csv'):
    df = pd.read_csv(input_path)
    df['country'] = df['source_ip'].apply(geo_lookup)
    df['user_id'] = df['user_id'].apply(lambda x: hash(x) % 10000)  # Anonymize
    df['threat_score'] = np.where(
        df['source_ip'].isin(df[df['is_malicious'] == 1]['source_ip']), 1, 0)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    clean_data()
