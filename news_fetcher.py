import requests
import pandas as pd

API_KEY = "6209d404a6564efea0e69195d71f3472"  # Replace with your actual key

def fetch_news(query="India", max_articles=10):
    url = (
        f"https://newsapi.org/v2/everything?q={query}&pageSize={max_articles}"
        f"&language=en&sortBy=publishedAt&apiKey={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()
    
    if data["status"] != "ok":
        raise Exception("Failed to fetch news")

    articles = data["articles"]
    df = pd.DataFrame([{
        "title": article["title"],
        "description": article["description"],
        "content": article["content"],
        "url": article["url"]
    } for article in articles])
    
    return df

if __name__ == "__main__":
    df = fetch_news()
    print(df.head())
    df.to_csv("news_articles.csv", index=False)
    print("Saved to news_articles.csv")