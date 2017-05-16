price_no_ti = xlsread('abd_final_proj/price_no_ti.xls');
price_ti = xlsread('abd_final_proj/price_ti.xls');
price_sa = xlsread('abd_final_proj/price_sa.xls');
price_gru_ti = xlsread('abd_final_proj/price_gru.xls');
price_gru_noti = xlsread('abd_final_proj/price_gru16.xls');
groundtruth = zeros(length(price_no_ti),1);
for i = 1:length(pricetiS1)
    groundtruth(i,1) = str2num(pricetiS1{i});
end

y_predict = 0.07.*(price_gru_noti-100).^1.4 + 14.*(price_sa).^0.5 + 0.1.*(price_gru_ti-20) -60;

% LSTM
figure,
subplot(1,3,1);
plot(groundtruth,'r');
hold on,
plot(price_no_ti,'k');
title('Bitcoin/USD price');
xlabel('day');
ylabel('Bitcoin price');
legend('ground truth','prediction not considering technical indicators');

subplot(1,3,2);
plot(groundtruth,'r');
hold on,
plot(price_ti,'k');
title('Bitcoin/USD price');
xlabel('day');
ylabel('Bitcoin price');
legend('ground truth','prediction considering technical indicators');

subplot(1,3,3);
plot(groundtruth,'r');
hold on,
plot(price_sa,'k');
title('Bitcoin/USD price');
xlabel('day');
ylabel('Bitcoin price');
legend('ground truth','prediction considering sentiment analysis');

% LSTM VS GRU with technical indicators
figure,
subplot(1,2,1);
plot(groundtruth,'r');
hold on,
plot(price_ti,'k');
title('Bitcoin/USD price');
xlabel('day');
ylabel('Bitcoin price');
legend('ground truth','LSTM');

subplot(1,2,2);
plot(groundtruth,'r');
hold on,
plot(price_gru,'k');
title('Bitcoin/USD price');
xlabel('day');
ylabel('Bitcoin price');
legend('ground truth','GRU');

% LSTM VS GRU without technical indicators
figure,
subplot(1,2,1);
plot(groundtruth,'r');
hold on,
plot(price_no_ti,'k');
title('Bitcoin/USD price');
xlabel('day');
ylabel('Bitcoin price');
legend('ground truth','LSTM');
subplot(1,2,2);
plot(groundtruth,'r');
hold on,
plot(price_gru_noti,'k');
title('Bitcoin/USD price');
xlabel('day');
ylabel('Bitcoin price');
legend('ground truth','GRU');

% GRU
figure,
subplot(1,2,1);
plot(groundtruth,'r');
hold on,
plot(price_gru_noti,'k');
title('Bitcoin/USD price');
xlabel('day');
ylabel('Bitcoin price');
legend('ground truth','no technical indicator');
subplot(1,2,2);
plot(groundtruth,'r');
hold on,
plot(price_gru_ti,'k');
title('Bitcoin/USD price');
xlabel('day');
ylabel('Bitcoin price');
legend('ground truth','with technical indicator');

% combined_prediction
figure,
plot(groundtruth,'r');
hold on,
plot(y_predict,'b');
title('Bitcoin/USD price');
xlabel('day');
ylabel('Bitcoin price');
legend('ground truth','prediction');