%define resistors in potential divider
res1 = 1e6;
res2 = 7.5e5;
res3 = 7.2e5;
res4 = 7.2e5;

S = readtable('original_data_from_serialPort.csv');
S = table2cell(S);

Adata = zeros(size(S,1),1);
Edata = zeros(size(S,1),1);

for i = 1:size(S,1)
    results = str2num(cell2mat(S(i,2)));
    Adata(i) = results(1);
    Edata(i) = results(2);
end

T = readtable('captured_data_from_serialPort.csv');
T = table2cell(T);

Adata = [Adata; zeros(size(T,1),1)];
Edata = [Edata; zeros(size(T,1),1)];
Fdata = zeros(size(T,1),1);
FCAdata = zeros(size(T,1),1);

for i = 1:size(T,1)
    results = str2num(cell2mat(T(i,2)));
    Adata(i+size(S,1)) = results(1);
    Edata(i+size(S,1)) = results(2);
    Fdata(i) = results(3);
    FCAdata(i) = results(4);
end

Ares = converttores(Adata, res1);
Eres = converttores(Edata, res2);
Fres = converttores(Fdata, res3);
FCAres = converttores(FCAdata, res4);

figure();
plotresults(Ares);
hold on
plotresults(Eres);
plotresults(Fres);
plotresults(FCAres);
ylabel('Resistance (Ohms)');
xlabel('Time (h)');

function dataout = converttores(data, kres)
    dataout = zeros(size(data));
    for i = 1:length(data)
        dataout(i) = (data(i)*kres)/(1023-data(i));
    end
end

function plotresults(results)
    plot(0:1/6:((length(results)-1)/6), results);
end
