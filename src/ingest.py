import os
import pandas as pd
import json

def load_logs(log_dir):
    logs = []
    for f in os.listdir(log_dir):
        if f.endswith('.csv') or f.endswith('.json'):
            df = pd.read_csv(os.path.join(log_dir, f)) if f.endswith('.csv') \
                 else pd.json_normalize(json.load(open(os.path.join(log_dir, f))))
            logs.append(df)
    return pd.concat(logs, ignore_index=True) if logs else pd.DataFrame()

def load_threat_feeds(feed_dir):
    feeds = []
    for f in os.listdir(feed_dir):
        if f.endswith('.json'):
            with open(os.path.join(feed_dir, f)) as jf:
                feeds.append(pd.json_normalize(json.load(jf)))
    return pd.concat(feeds, ignore_index=True) if feeds else pd.DataFrame()

def load_business_events(biz_dir):
    # Similar to load_logs
    pass

if __name__ == "__main__":
    logs = load_logs('data/logs')
    threats = load_threat_feeds('data/threat_feeds')
    biz = load_business_events('data/business')
    pd.concat([logs, threats, biz], axis=0).to_csv('processed/merged_data.csv', index=False)
