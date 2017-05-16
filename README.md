# ABD-Market-Intelligence-Analysis-Bitcoin-price-Analysis
EECS 6895 course project<br />
Here's the introduction of the files in the code folder based on their functions.<br />
1. Data Preparation<br />
Using API to gather data:<br />
blockchain_api.py: using API of blockchain.info<br />
coindesk_api.py: using API of coindesk.com<br />
Using web crawling to gather data:<br />
bitcointalk_crawling.py: crawling titles from bitcointalk forum<br />
forumbitcoin_crawling.py: crawling titles from forumbitcoin<br />
abd_dataprocessing.m: process data to generate X set and Y set<br />
normalization.m: normalize every column in X set<br />

2. Sentiment Analysis<br />
sentiment_bitcoin.py: analyze single sentence (for demo)<br />
readsentiment.py: analyze all the titles we got<br />

3. Data Training<br />
lstm16.py: LSTM not considering technical indicator data<br />
lstm.py: LSTM considering technical indicator data<br />
lstm_s.py: LSTM considering social media data<br />
gru16.py: GRU not considering technical indicator data<br />
gru.py: GRU considering technical indicator data<br />
gru_s.py: GRU considering social media data<br />

4. Data Testing<br />
lstm_test16.py: testing using model trained by LSTM not considering technical indicator data<br />
lstm_test.py: testing using model trained by LSTM considering technical indicator data<br />
lstm_test_s.py: testing using model trained by LSTM considering social media data<br />
gru_test16.py: testing using model trained by GRU not considering technical indicator data<br />
gru_test.py: testing using model trained by GRU considering technical indicator data<br />
gru_test_s.py: testing using model trained by GRU considering social media data<br />

5. Model Optimization and Plotting Figures<br />
prediction_formula.m<br />

6. Others<br />
readnpy.py<br />
read_mat_file.py<br />
