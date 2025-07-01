import pandas as pd
from news_fetcher import fetch_news
from summarizer import summarize_text

def summarize_articles():
    df = fetch_news()
    df = df.dropna(subset=["content"])

    print("Summarizing articles...")

    df["summary"] = df["content"].apply(lambda x: summarize_text(x[:1000]))  # Shorten input if too long

    df.to_csv("summarized_news.csv", index=False)
    print("Summarized news saved to summarized_news.csv")

if __name__ == "__main__":
    summarize_articles()