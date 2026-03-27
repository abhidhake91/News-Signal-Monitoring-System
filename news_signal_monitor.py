import feedparser
import pandas as pd
import os
from datetime import datetime

# -----------------------------
# RSS SOURCES
# -----------------------------

RSS_FEEDS = [
    "https://news.google.com/rss/search?q=artificial+intelligence",
    "https://news.google.com/rss/search?q=technology",
    "https://news.google.com/rss/search?q=startup"
]

# -----------------------------
# SIGNAL KEYWORDS
# -----------------------------

SIGNALS = {
    "Funding": ["funding", "raises", "raised", "investment", "funded"],
    "Acquisition": ["acquire", "acquires", "acquisition", "buy"],
    "Partnership": ["partnership", "collaboration", "alliance"],
    "Launch": ["launch", "released", "introduces"],
    "Hiring": ["hiring", "expands team"],
    "Leadership": ["appoints", "ceo", "joins", "leadership"]
}


# -----------------------------
# SIGNAL DETECTION
# -----------------------------

def detect_signal(title):

    title_lower = title.lower()

    for signal_type, keywords in SIGNALS.items():
        for word in keywords:
            if word in title_lower:
                return signal_type

    return "General"


# -----------------------------
# FETCH NEWS
# -----------------------------

def fetch_news():

    articles = []

    for url in RSS_FEEDS:

        feed = feedparser.parse(url)

        for entry in feed.entries[:10]:

            signal = detect_signal(entry.title)

            articles.append({
                "Title": entry.title,
                "Signal": signal,
                "Link": entry.link,
                "Published": entry.published,
                "Captured_Date": datetime.today().strftime("%Y-%m-%d")
            })

    return articles


# -----------------------------
# MAIN
# -----------------------------

if __name__ == "__main__":

    news = fetch_news()

    df = pd.DataFrame(news)

    # Keep only meaningful signals
    df = df[df["Signal"] != "General"]

    file_name = "signals_dataset.csv"

    if os.path.exists(file_name):

        existing_df = pd.read_csv(file_name)

        combined_df = pd.concat([existing_df, df])

        combined_df.drop_duplicates(subset=["Title"], inplace=True)

        combined_df.to_csv(file_name, index=False)

        print("\nExisting dataset found.")
        print("New signals added. Duplicates removed.")

    else:

        df.to_csv(file_name, index=False)

        print("\nNew dataset created.")

    print("\nTotal signals stored:", len(pd.read_csv(file_name)))