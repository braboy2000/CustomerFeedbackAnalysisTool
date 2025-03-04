import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from textblob import TextBlob  # For Sentiment Analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  # Another option
from transformers import pipeline


# Load credentials
creds = Credentials.from_service_account_file("boreal-voyager-452700-k9-22da5f88e5b0.json", scopes=["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"])

# Connect to Google Sheets
client = gspread.authorize(creds)

# Open the spreadsheet
sheet = client.open("CustomerFeedback").sheet1  

# Get data from the sheet
data = sheet.get_all_records()

# Convert to Pandas DataFrame
df = pd.DataFrame(data)

#Columns renamed for any spacing issues
df.rename(columns={
    "Timestamp": "timestamp",
    "Feedback Type": "feedback_type",
    "Feedback": "feedback",
    "Suggestions for improvement": "suggestions",
    "Name": "name",
    "Email": "email"
}, inplace=True)

df["suggestions"].fillna("", inplace=True)  # Replace NaN with an empty string
df["feedback"].fillna("", inplace=True)
df["timestamp"] = pd.to_datetime(df["timestamp"])

#Analyze Feedback column
def get_sentiment(text):
    if text.strip():  # Ensure text isn't empty
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0:
            return "Positive"
        elif polarity < 0:
            return "Negative"
        else:
            return "Neutral"
    return "Neutral"

#new column called 'Sentiment' created
df["sentiment"] = df["feedback"].apply(get_sentiment)





def get_vader_sentiment(text):
    if text.strip():  # Ensure text isn't empty
        scores = analyzer.polarity_scores(text)
        compound = scores["compound"]  # Overall sentiment score
        if compound >= 0.05:
            return "Positive"
        elif compound <= -0.05:
            return "Negative"
        else:
            return "Neutral"
    return "Neutral"

# Apply VADER analysis
df["vader_sentiment"] = df["feedback"].apply(get_vader_sentiment)

def get_bert_sentiment(text):
    if text.strip():  # Ensure the text isn't empty
        result = sentiment_pipeline(text)[0]  # Run BERT model
        return result["label"]  # Output: "POSITIVE" or "NEGATIVE"
    return "NEUTRAL"

# Apply BERT to the feedback column
df["bert_sentiment"] = df["feedback"].apply(get_bert_sentiment)
# Display DataFrame




sentiment_summary = {
    "Total Feedback Entries": len(df),
    "Most Common Feedback Type": df["feedback_type"].mode()[0],
    "TextBlob Positive": (df["textblob_sentiment"] == "Positive").sum(),
    "TextBlob Neutral": (df["textblob_sentiment"] == "Neutral").sum(),
    "TextBlob Negative": (df["textblob_sentiment"] == "Negative").sum(),
    "VADER Positive": (df["vader_sentiment"] == "Positive").sum(),
    "VADER Neutral": (df["vader_sentiment"] == "Neutral").sum(),
    "VADER Negative": (df["vader_sentiment"] == "Negative").sum(),
    "BERT Positive": (df["bert_sentiment"] == "POSITIVE").sum(),
    "BERT Negative": (df["bert_sentiment"] == "NEGATIVE").sum(),
}
print(sentiment_summary)

#Comparison of Models vs Original Feedback
print(df[["feedback", "textblob_sentiment", "vader_sentiment", "bert_sentiment"]].head(10))




