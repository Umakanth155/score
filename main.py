from fastapi import FastAPI
from cricbuzz_scraper import fetch_live_scores
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()
cached_data = []

def update_scores():
    global cached_data
    cached_data = fetch_live_scores()
    print("✅ Live scores updated.")

# Start background scheduler to update every 30 seconds
scheduler = BackgroundScheduler()
scheduler.add_job(update_scores, "interval", seconds=30)
scheduler.start()

# Call once at startup
update_scores()

@app.get("/live-scores")
def get_scores():
    return {"matches": cached_data}
