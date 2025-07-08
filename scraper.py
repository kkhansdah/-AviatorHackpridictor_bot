import requests
import json
from bs4 import BeautifulSoup

def update_data():
    url = "https://kwgvip5.com"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
  
    rounds = []
    multipliers = []

    table = soup.find("table", class_="aviator-table")
    if table:
        rows = table.find_all("tr")[1:11] 

        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                round_id = cols[0].text.strip()
                multiplier = cols[1].text.strip().replace("x", "")
                rounds.append(f"R-{round_id}")
                try:
                    multipliers.append(float(multiplier))
                except:
                    multipliers.append(0.0)

    with open("data.json", "w") as f:
        json.dump({
            "rounds": rounds,
            "multipliers": multipliers
        }, f)
