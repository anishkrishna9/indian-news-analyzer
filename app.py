import os
import pandas as pd
import streamlit as st
import plotly.express as px


# Load the final analyzed data
@st.cache_data
def load_data():
    return pd.read_csv("final_news_analysis.csv")

st.set_page_config(page_title="📰 Indian News Analyzer", layout="wide")

st.title("Indian News Summarizer & Sentiment Analyzer")
st.markdown("Summarizes latest Indian news and shows sentiment using AI models")

# Refresh button
if st.button("🔄 Refresh News (May Take 1–2 Minutes)"):
    with st.spinner("Fetching, summarizing and analyzing latest news..."):
        os.system("python analyze_news.py")
        st.success("News updated successfully! Please scroll down to see latest results.")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("final_news_analysis.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("Filter News")
sentiment_filter = st.sidebar.multiselect(
    "Select Sentiments:",
    options=["POSITIVE", "NEGATIVE"],
    default=["POSITIVE", "NEGATIVE"]
)

df_filtered = df[df["sentiment"].isin(sentiment_filter)]

# Download CSV Button
st.download_button(
    label="Download as CSV",
    data=df_filtered.to_csv(index=False),
    file_name="analyzed_news.csv",
    mime="text/csv"
)

# Count sentiments
sentiment_counts = df_filtered["sentiment"].value_counts().reset_index()
sentiment_counts.columns = ["Sentiment", "Count"]

# Enhanced sentiment summary
sentiment_group = df_filtered.groupby("sentiment").agg({
    "title": lambda x: "; ".join(x.tolist()[:3]),  # Show 3 titles max
    "sentiment_score": "mean",
    "summary": "count"
}).reset_index()

sentiment_group.columns = ["Sentiment", "Top Titles", "Avg Score", "Count"]

# Sentiment Summary Bar Chart
st.subheader("📊 Sentiment Summary")
fig = px.pie(
    sentiment_counts,
    names="Sentiment",
    values="Count",
    color="Sentiment",
    color_discrete_map={"POSITIVE": "green", "NEGATIVE": "red"},
    title="Sentiment Distribution of News Articles",
    hole=0.4  # Makes it a donut chart (optional)
)
fig.update_traces(textposition='inside', textinfo='percent+label')

st.plotly_chart(fig, use_container_width=True)

# Display articles
for index, row in df_filtered.iterrows():
    st.markdown(f"### {row['title']}")
    st.markdown(f"**URL:** [{row['url']}]({row['url']})")
    st.markdown(f"**Summary:** {row['summary']}")
    
    st.markdown(
        f"**Sentiment:** `{row['sentiment']}` | "
        f"**Score:** `{row['sentiment_score']}`"
    )
    st.markdown("---")