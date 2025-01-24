# Twitter Data Analysis and Word Cloud Generator

This Python script retrieves tweets from a specific Twitter user, processes them to extract useful information, and generates word clouds based on the frequency of nouns, verbs, and adjectives found in the tweets. It utilizes the Twitter API and natural language processing (NLP) techniques.

## Features
1. **Retrieve Tweets**:
   - Fetches up to 500 tweets from a specific Twitter user.
   - Excludes replies and retweets for cleaner analysis.
2. **Text Cleaning**:
   - Removes URLs from tweet text for better readability.
3. **Natural Language Processing**:
   - Tokenizes the tweets and identifies parts of speech (nouns, verbs, adjectives).
   - Organizes the identified words into separate lists.
4. **Word Cloud Generation**:
   - Creates word clouds for nouns, verbs, and adjectives based on their frequency of appearance in the tweets.

## Requirements
- Python 3.6 or later
- Required Python libraries:
  - `tweepy` (install via `pip install tweepy`)
  - `nltk` (install via `pip install nltk`)
  - `wordcloud` (install via `pip install wordcloud`)
  - `matplotlib` (install via `pip install matplotlib`)

## Setup and Usage
1. **Twitter API Access**:
   - Create a developer account on [Twitter Developer Portal](https://developer.twitter.com/).
   - Generate a Bearer Token from your Twitter developer account and replace `YOUR_BEARER_TOKEN` in the script with your token.
2. **User ID**:
   - Find the Twitter User ID of the user you want to analyze. You can use tools like [Code of a Ninja's Twitter ID Finder](https://codeofaninja.com/tools/find-twitter-id/) to obtain the ID.
   - Replace `ΧΧΧΧΧΧ` in the `user_id` variable with the User ID.
3. **Run the Script**:
   - Save the script to a file (e.g., `twitter_analysis.py`).
   - Install required libraries:
     ```bash
     pip install tweepy nltk wordcloud matplotlib
     ```
   - Download and initialize NLTK data for tokenization and POS tagging:
     ```python
     import nltk
     nltk.download('punkt')
     nltk.download('averaged_perceptron_tagger')
     ```
   - Execute the script:
     ```bash
     python twitter_analysis.py
     ```
4. **Output**:
   - The script generates three word clouds:
     - **Nouns**: Visualizes the most frequent nouns.
     - **Verbs**: Visualizes the most frequent verbs.
     - **Adjectives**: Visualizes the most frequent adjectives.
   - These word clouds provide insight into the content and tone of the user's tweets.

## Notes
- The script fetches a maximum of 500 tweets due to API limitations.
- The `tweepy.Paginator` is used to handle pagination for large tweet datasets.
- Ensure your Bearer Token is valid and properly set in the script.

## License
This project is open source and available under the [MIT License](LICENSE).
