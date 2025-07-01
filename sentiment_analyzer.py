from transformers import pipeline

# Load sentiment pipeline (this will download model)
sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment(text):
    result = sentiment_pipeline(text[:512])[0]  # Truncate to 512 tokens
    return result['label'], round(result['score'], 3)
