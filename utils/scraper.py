from os import path
from typing import Any, Union
from pandas import json_normalize

import dotenv, requests

DIR_PATH = path.dirname(__file__)
DOTENV_PATH = path.join(DIR_PATH, "../.env")
KEY = dotenv.get_key(DOTENV_PATH, "API_KEY")
OUTPUT_CSV_PATH = path.join(DIR_PATH, "../data/news.csv")

def get_training_data_from_api(query: str = "python") -> Union[list[dict[str, Any]], dict[str, str]]:
    try:
        r = requests.get(f"https://newsapi.org/v2/everything?q={query}&apiKey={KEY}").json()

    except Exception as E:
        return { "error": E }

    # Successful
    if r["status"] == "ok":
        relevant = []

        for i in r["articles"]:
            relevant.append({
                "title": i["title"],
                "author": i["author"],
                "url": i["url"],
                "content": i["content"]
            })

        return relevant
    
    return { "status": r["status"] }

if __name__ == "__main__":
    data = get_training_data_from_api()

    # Writes to csv
    data_normalized = json_normalize(data)
    data_normalized.to_csv(OUTPUT_CSV_PATH, index = False)
    print(f"Wrote {len(data_normalized)} articles!")