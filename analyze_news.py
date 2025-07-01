import pandas as pd
from news_fetcher import fetch_news
from summarizer import summarize_text
from sentiment_analyzer import get_sentiment

def analyze_news():
    df = fetch_news()
    df = df.dropna(subset=["content"])

    print("Summarizing and analyzing sentiment...")

    summaries = []
    sentiments = []
    sentiment_scores = []

    for content in df["content"]:
        summary = summarize_text(content[:1000])
        label, score = get_sentiment(summary)

        summaries.append(summary)
        sentiments.append(label)
        sentiment_scores.append(score)

    df["summary"] = summaries
    df["sentiment"] = sentiments
    df["sentiment_score"] = sentiment_scores

    df.to_csv("final_news_analysis.csv", index=False)
    print("Analysis saved to final_news_analysis.csv")

if __name__ == "__main__":
    analyze_news()