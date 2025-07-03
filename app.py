import os
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="📰 Indian News Analyzer", layout="wide")

# Automatically run analysis if CSV missing
if not os.path.exists("final_news_analysis.csv"):
    st.warning("Data file not found. Running analysis pipeline, please wait...")
    os.system("python analyze_news.py")
    st.success("Data generated successfully!")

# Function to load data safely
@st.cache_data
def load_data():
    try:
        return pd.read_csv("final_news_analysis.csv")
    except FileNotFoundError:
        st.error("Data file still not found. Please click '🔄 Refresh News' to generate it.")
        return pd.DataFrame()

# Load data
df = load_data()

# Refresh button to re-run pipeline
if st.button("🔄 Refresh News (May Take 1–2 Minutes)"):
    with st.spinner("Fetching, summarizing and analyzing latest news..."):
        os.system("python analyze_news.py")
        df = load_data()
    st.success("✅ News updated successfully! Scroll down to see latest results.")

# If data loaded, show UI
if not df.empty:
    # Sidebar filters
    st.sidebar.header("🔍 Filter News")
    sentiment_filter = st.sidebar.multiselect(
        "Select Sentiments:",
        options=["POSITIVE", "NEGATIVE"],
        default=["POSITIVE", "NEGATIVE"]
    )

    # Filter dataframe
    df_filtered = df[df["sentiment"].isin(sentiment_filter)]

    # Download filtered data
    st.download_button(
        label="📥 Download as CSV",
        data=df_filtered.to_csv(index=False),
        file_name="analyzed_news.csv",
        mime="text/csv"
    )

    # Sentiment summary pie chart
    st.subheader("🥧 Sentiment Summary")
    sentiment_counts = df_filtered["sentiment"].value_counts().reset_index()
    sentiment_counts.columns = ["Sentiment", "Count"]

    if not sentiment_counts.empty:
        fig = px.pie(
            sentiment_counts,
            names="Sentiment",
            values="Count",
            color="Sentiment",
            color_discrete_map={"POSITIVE": "green", "NEGATIVE": "red"},
            title="Sentiment Distribution of News Articles",
            hole=0.4
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data matches the current filters.")

    # Show articles
    st.subheader("📰 News Articles")
    for index, row in df_filtered.iterrows():
        st.markdown(f"### 🗞️ {row['title']}")
        st.markdown(f"**URL:** [{row['url']}]({row['url']})")
        st.markdown(f"**Summary:** {row['summary']}")
        st.markdown(
            f"**Sentiment:** `{row['sentiment']}` | "
            f"**Score:** `{row['sentiment_score']}`"
        )
        st.markdown("---")
else:
    st.info("No data available. Please refresh to try again.")
