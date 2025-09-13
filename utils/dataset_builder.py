from typing import Any, List, Dict, Union

from os import path, getcwd
from pandas import DataFrame

import dotenv, requests

DIR_PATH = getcwd()
DOTENV_PATH = path.join(DIR_PATH, "../.env")

KEY = dotenv.get_key(DOTENV_PATH, "API_KEY")
OUTPUT_CSV_PATH = path.join(DIR_PATH, "../data/news.csv")

def get_training_data_from_api(query: str = "python") -> Union[List[Dict[str, Any]], Dict[str, str]]:
    """ Makes GET request to API to fetch news articles matching query """

    if not query:
        return { "error": "Query cannot be empty!" }
    
    try:
        r = requests.get(f"https://newsapi.org/v2/everything?q={query}&apiKey={KEY}").json()

    except Exception as E:
        return { "error": E }

    # Successful
    if r["status"] == "ok":
        relevant = []

        for i in r["articles"]:
            relevant.append({
                "content": i["content"].strip()
            })

        return relevant
    
    return { "status": r["status"] }

def save_to_csv(data: List[Dict[str, Any]]) -> int:
    """ Writes JSON data from request to CSV """

    if not data:
        return -1

    try :
        df = DataFrame(data)
        df.to_csv(OUTPUT_CSV_PATH, index = False)

    except:
        return -1

    return len(df)

if __name__ == "__main__":
    from preprocessing import clean_text

    data = get_training_data_from_api(query = "world")
    data = [{ k: clean_text(v) for k, v in article.items() } for article in data]

    n_data = save_to_csv(data)
    print(f"Wrote {n_data} articles!")