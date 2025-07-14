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
    match_blocks = soup.select(".cb-col.cb-col-100.cb-ltst-wgt-hdr")

    for block in match_blocks:
        team_tags = block.select(".cb-ovr-flo.cb-hmscg-tm-nm")
        score_tag = block.select_one(".cb-ovr-flo.cb-text-live")
        status_tag = block.select_one(".cb-text-complete, .cb-text-live")

        if len(team_tags) == 2:
            match_title = f"{team_tags[0].text.strip()} vs {team_tags[1].text.strip()}"
        else:
            continue

        match_info = {
            "match": match_title,
            "score": score_tag.text.strip() if score_tag else "Score not available",
            "status": status_tag.text.strip() if status_tag else "Status not available"
        }

        matches.append(match_info)

    return matches
