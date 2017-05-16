# ABD-Market-Intelligence-Analysis-Bitcoin-price-Analysis
EECS 6895 course project
Here's the introduction of the files in the code folder based on their functions.
1. Data Preparation
Using API to gather data:\n
blockchain_api.py: using API of blockchain.info
coindesk_api.py: using API of coindesk.com
Using web crawling to gather data:
bitcointalk_crawling.py: crawling titles from bitcointalk forum
forumbitcoin_crawling.py: crawling titles from forumbitcoin
abd_dataprocessing.m: process data to generate X set and Y set
normalization.m: normalize every column in X set

2. Sentiment Analysis
sentiment_bitcoin.py: analyze single sentence (for demo)
readsentiment.py: analyze all the titles we got

3. Data Training
lstm16.py: LSTM not considering technical indicator data
lstm.py: LSTM considering technical indicator data
lstm_s.py: LSTM considering social media data
gru16.py: GRU not considering technical indicator data
gru.py: GRU considering technical indicator data
gru_s.py: GRU considering social media data

4. Data Testing
lstm_test16.py: testing using model trained by LSTM not considering technical indicator data
lstm_test.py: testing using model trained by LSTM considering technical indicator data
lstm_test_s.py: testing using model trained by LSTM considering social media data
gru_test16.py: testing using model trained by GRU not considering technical indicator data
gru_test.py: testing using model trained by GRU considering technical indicator data
gru_test_s.py: testing using model trained by GRU considering social media data

5. Model Optimization and Plotting Figures
prediction_formula.m

6. Others
readnpy.py
read_mat_file.py
