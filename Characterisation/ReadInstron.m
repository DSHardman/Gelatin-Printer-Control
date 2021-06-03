%plotfile('1');
%hold on;
plotfile('2');
hold on
%plotfile('3');
%plotfile('4');
plotfile('5');
%plotfile('6');
plotfile('7');
plotfile('8');
plotfile('9');
plotfile('10');
plotfile('11');
plotfile('12');
legend();

ylabel('Load')
xlabel('Extension')


function plotfile(stub)
    S = cell2mat(table2cell(readtable(strcat('Instron/',stub,'.csv'))));
    S = addstrain(S, str2double(stub));
    plot(S(:,4), S(:,3), 'LineWidth', 2, 'DisplayName', maplabel(stub));
end

function label = maplabel(stub)
    samples = ["An"; "En"; "Bn"; "Fn"; "Cn";...
        "Dn"; "Ao"; "Eo"; "Bo"; "Fo"; "Co";...
        "Do"];
    label = samples(str2double(stub));
end

function newarray = addstrain(results, samplenumber)
    initiallengths = [8.5; 10.8; 8.5; 9.5; 10.5;...
        10.3; 9.5; 11.4; 12.6; 11.6; 12.1; 11.9];
    newarray = [results zeros(size(results,1), 1)];
    for i = 1:size(results,1)
        newarray(i,4) = 100*((results(i,2) -...
            results(1,2))/initiallengths(samplenumber));
    end
end

