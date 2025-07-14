import requests
from bs4 import BeautifulSoup

def fetch_live_scores():
    url = "https://www.cricbuzz.com/cricket-match/live-scores"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    matches = []
    match_cards = soup.select(".cb-mtch-lst.cb-col.cb-col-100.cb-tms-itm")

    for card in match_cards:
        try:
            title = card.select_one(".cb-ovr-flo.cb-hmscg-tm-nm").text.strip()
            score = card.select_one(".cb-ovr-flo.cb-text-live") or card.select_one(".cb-ovr-flo.cb-text-inprogress")
            status = card.select_one(".cb-text-complete, .cb-text-live, .cb-text-inprogress")

            match_info = {
                "match": title,
                "score": score.text.strip() if score else "Not Available",
                "status": status.text.strip() if status else "Not Available"
            }

            matches.append(match_info)
        except Exception as e:
            continue  # skip any card that fails

    return matches
