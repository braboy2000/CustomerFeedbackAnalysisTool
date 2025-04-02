# Sentiment Analysis Dashboard

## Project Overview
This project performs sentiment analysis on customer feedback data collected via Google Sheets. The goal is to analyze the sentiment of customer responses and visualize the results in a Tableau dashboard. The project utilizes Python for data processing and sentiment analysis, while Tableau is used to create insightful visualizations.

## Features
- 📊 **Data Collection:** Uses the Google Sheets API to fetch customer feedback data.
- 📈 **Sentiment Analysis:** Uses TextBlob to calculate sentiment polarity scores for each feedback entry.
- 💾 **Data Export:** Saves the processed sentiment data as a CSV file for easy import into Tableau.
- 🖥️ **Dashboard Visualization:** Uses Tableau to display sentiment scores in an interactive and user-friendly format.

## Technologies Used
- **Python** for data processing and sentiment analysis.
- **Google Sheets API** to fetch data from spreadsheets.
- **TextBlob** for sentiment analysis.
- **Pandas** for data manipulation.
- **Tableau** for creating visual dashboards.

## Project Setup
### Prerequisites
- Python 3.x
- Google Cloud Platform account with API credentials
- Tableau Desktop

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/sentiment-analysis-dashboard.git
   ```

2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Google API Setup
1. Create a service account in the [Google Cloud Platform](https://console.cloud.google.com/).
2. Enable the **Google Sheets API** and **Google Drive API**.
3. Download the credentials JSON file and save it as `credentials.json` in the project root.
4. Share the Google Sheet with the service account email (Editor access).

### Running the Script
Execute the script to generate sentiment analysis data:
```bash
python script.py
```
The script will fetch data from the Google Sheet, perform sentiment analysis, and save the results to a CSV file.

### Dashboard Creation
1. Open Tableau and connect to the generated CSV file.
2. Create visualizations to analyze sentiment scores.

## Example Usage
```bash
python script.py
```

## Contributing
Contributions are welcome! Please feel free to submit issues or pull requests to improve the project.

## License
This project is licensed under the MIT License.

