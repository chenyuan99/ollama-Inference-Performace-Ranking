import json
import os
from datetime import datetime
import time

# Set the TZ environment variable to PST
os.environ['TZ'] = 'America/Los_Angeles'
time.tzset()

def getResultsFromJSON(filename=".github/scripts/results.json"):
    with open(filename) as f:
        listings = json.load(f)
        print(f"Received {len(results)} results from results.json")
        return results
