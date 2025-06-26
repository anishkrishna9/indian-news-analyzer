# Indian News Summarizer & Sentiment Analyzer

This is an AI-powered Streamlit web app that **fetches the latest Indian news**, **summarizes each article using a T5 model**, and **performs sentiment analysis** using a fine-tuned BERT model. It provides an intuitive dashboard that allows you to explore summaries, filter by sentiment, and download results.

[![View in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-link-here.streamlit.app/)

---

## Features

- Fetches real-time Indian news using NewsAPI
- Summarizes content using HuggingFace's `t5-small` model
- Analyzes sentiment with `distilbert-base-uncased-finetuned-sst-2-english`
- Visual summary using interactive **pie chart**
- Download filtered results as CSV
- One-click refresh to fetch new data and rerun analysis

---

## Screenshot

![App Screenshot](https://your-screenshot-link-if-any.png)

---

## Tech Stack

| Component         | Tool / Library |
|------------------|----------------|
| App Framework     | Streamlit      |
| NLP Models        | HuggingFace Transformers (`t5`, `bert`) |
| Visualization     | Plotly         |
| News Source       | NewsAPI.org    |
| Data Handling     | Pandas         |

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/indian-news-analyzer.git
   cd indian-news-analyzer

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
4. **Set your NewsAPI key**
   For Streamlit Cloud, use st.secrets["NEWS_API_KEY"]. In local development, add your key to news_fetcher.py:
   ```python
   API_KEY = "YOUR_NEWS_API_KEY"
   
## Run the app
streamlit run app.py
