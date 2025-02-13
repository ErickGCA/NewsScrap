# News Scraper with OpenAI Summarization

This Python script scrapes news articles from the G1 website, extracts their content, and generates short summaries using OpenAI's GPT model. The script fetches the latest news headlines, retrieves the full article text, and then summarizes it in a concise format.

## Features
- Scrapes news headlines and links from [G1](https://g1.globo.com/)
- Extracts article content from the given links
- Summarizes the extracted content using OpenAI's GPT model
- Handles API rate limits with automatic retries

## Requirements
Before running the script, ensure you have the required dependencies installed:

```bash
pip install requests beautifulsoup4 openai python-dotenv
```

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/news-scraper.git
   cd news-scraper
   ```
2. Create a `.env` file and add your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY=your_api_key_here
   ```
3. Run the script:
   ```bash
   python script.py
   ```

## Usage
The script will:
1. Fetch the latest news headlines from G1
2. Display the first 5 headlines along with their links
3. Extract the content of each article
4. Summarize the content using OpenAI's GPT model
5. Print the summarized news on the console

## Example Output
```plaintext
1. Example News Title
   🔗 https://g1.globo.com/example-news-link
   📝 Resumo: This is a short summary of the news article...
```

## Limitations
⚠️ **This script is not fully functional yet due to limitations of the free OpenAI API.** If you are using the free API tier, you may encounter rate limits or restrictions that prevent successful summarization.

## License
This project is open-source and available under the MIT License.

