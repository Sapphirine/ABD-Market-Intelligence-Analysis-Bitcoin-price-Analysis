%financial data processing
%need to manually import: price, high, low, change
%data needed manually update: TODAY, BCHAIN-XXXXX.csv, high-low-price.csv

%% import BCHAIN-XXXXX.csv and normalization
ATRCT = readtable('abd_final_proj/BCHAIN-ATRCT.csv');
AVBLS = readtable('abd_final_proj/BCHAIN-AVBLS.csv');
BLCHS = readtable('abd_final_proj/BCHAIN-BLCHS.csv');
CPTRA = readtable('abd_final_proj/BCHAIN-CPTRA.csv');
CPTRV = readtable('abd_final_proj/BCHAIN-CPTRV.csv');
ETRAV = readtable('abd_final_proj/BCHAIN-ETRAV.csv');
ETRVU = readtable('abd_final_proj/BCHAIN-ETRVU.csv');
HRATE = readtable('abd_final_proj/BCHAIN-HRATE.csv');
MIREV = readtable('abd_final_proj/BCHAIN-MIREV.csv');
MKTCP = readtable('abd_final_proj/BCHAIN-MKTCP.csv');
NADDU = readtable('abd_final_proj/BCHAIN-NADDU.csv');
NTRAN = readtable('abd_final_proj/BCHAIN-NTRAN.csv');
NTRAT = readtable('abd_final_proj/BCHAIN-NTRAT.csv');
NTRBL = readtable('abd_final_proj/BCHAIN-NTRBL.csv');
NTREP = readtable('abd_final_proj/BCHAIN-NTREP.csv');
TOTBC = readtable('abd_final_proj/BCHAIN-TOTBC.csv');
TOUTV = readtable('abd_final_proj/BCHAIN-TOUTV.csv');
TRFEE = readtable('abd_final_proj/BCHAIN-TRFEE.csv');
TRFUS = readtable('abd_final_proj/BCHAIN-TRFUS.csv');
TRVOU = readtable('abd_final_proj/BCHAIN-TRVOU.csv');
%manually add price,open,high,low,change
change = (change+100)./200;

% unormalized data
C1 = table2array(ATRCT(:,2));
C2 = table2array(AVBLS(:,2));
C3 = table2array(BLCHS(:,2));
C4 = table2array(CPTRA(:,2));
C5 = table2array(CPTRV(:,2));
C6 = table2array(ETRAV(:,2));
C7 = table2array(ETRVU(:,2));
C8 = table2array(HRATE(:,2));
C9 = table2array(MIREV(:,2));
C10 = table2array(MKTCP(:,2));
C11 = table2array(NADDU(:,2));
C12 = table2array(NTRAN(:,2));
C13 = table2array(NTRAT(:,2));
C14 = table2array(NTRBL(:,2));
C15 = table2array(NTREP(:,2));
C16 = table2array(TOTBC(:,2));
C17 = table2array(TOUTV(:,2));
C18 = table2array(TRFEE(:,2));
C19 = table2array(TRFUS(:,2));
C20 = table2array(TRVOU(:,2));
%L = length(price);
L = 35;

% normalized data
N1 = normalization( C1(1:L) );
N2 = normalization( C2(1:L) );
N3 = normalization( C3(1:L) );
N4 = normalization( C4(1:L) );
N5 = normalization( C5(1:L) );
N6 = normalization( C6(1:L) );
N7 = normalization( C7(1:L) );
N8 = normalization( C8(1:L) );
N9 = normalization( C9(1:L) );
N10 = normalization( C10(1:L) );
N11 = normalization( C11(1:L) );
N12 = normalization( C12(1:L) );
N13 = normalization( C13(1:L) );
N14 = normalization( C14(1:L) );
N15 = normalization( C15(1:L) );
N16 = normalization( C16(1:L) );
N17 = normalization( C17(1:L) );
N18 = normalization( C18(1:L) );
N19 = normalization( C19(1:L) );
N20 = normalization( C20(1:L) );

%% technical indicator
adx = indicators([high,low,price],'adx');
adx = adx(:,3);
cci= indicators([high,low,price],'cci');
macd  = indicators(price,'macd');
macd = macd(:,3);
roc = indicators(price,'roc');
rsi = indicators(price,'rsi');
adx(isnan(adx)) = 0;
cci(isnan(cci)) = 0;
macd(isnan(macd)) = 0;
roc(isnan(roc)) = 0;
rsi(isnan(rsi)) = 0;
N21 = normalization(adx(1:L));
N22 = normalization(cci(1:L));
N23 = normalization(macd(1:L));
N24 = normalization(roc(1:L));
N25 = normalization(rsi(1:L));
change = change(1:L);
%% generate input
%input X_set
X_set = [N1 N2 N3 N4 N5 N6 N7 N8 N9 N10 N11 N12 N13 N14 N15 N16 N17 N18 N19 N20 N21 N22 N23 N24 N25 change];

%input Y_set
TODAY = 1771.65;
Y_set = [TODAY;price(1:end-1)];