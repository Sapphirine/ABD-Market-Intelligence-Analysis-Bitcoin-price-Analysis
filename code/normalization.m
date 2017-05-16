function [ output ] = normalization( C )
% Normalization for each column C
maxC = max(C);
minC = min(C);
mm = maxC - minC;
for i = 1:length(C)
    C(i) = (C(i)-minC)/mm;
end
output = C;
end

