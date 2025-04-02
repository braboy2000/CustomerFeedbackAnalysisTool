import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from textblob import TextBlob  # For Sentiment Analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  # Another option
from transformers import pipeline
from collections import Counter

# Load credentials
creds = Credentials.from_service_account_file("boreal-voyager-452700-k9-22da5f88e5b0.json", scopes=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"])

# Connect to Google Sheets
client = gspread.authorize(creds)

# Open the spreadsheet
sheet = client.open("CustomerFeedback").sheet1

# Get data from the sheet
data = sheet.get_all_records()

# Convert to Pandas DataFrame
df = pd.DataFrame(data)

# Columns renamed for any spacing issues
df.rename(columns={
    "Timestamp": "timestamp",
    "Feedback Type": "feedback_type",
    "Feedback": "feedback",
    "Suggestions for improvement": "suggestions",
    "Name": "name",
    "Email": "email"
}, inplace=True)

# Sentiment analysis function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # Returns a value between -1 (negative) and 1 (positive)

# Apply sentiment analysis to feedback
df['sentiment_score'] = df['feedback'].apply(analyze_sentiment)


# Save dataframe to CSV for Tableau
df.to_csv('customer_feedback_data.csv', index=False)

print("Sentiment data saved to CSV.")
