relativeweights(PrintedSamplesA)
figure();
relativeweights(PrintedSamplesB)
figure();
relativeweights(PrintedSamplesC)
figure();
relativeweights(PrintedSamplesD)
figure();
relativeweights(PrintedSamplesE)
figure();
relativeweights(PrintedSamplesF)

%%

relativeresistance(PrintedSamplesA)
figure();
relativeresistance(PrintedSamplesB)
figure();
relativeresistance(PrintedSamplesC)
figure();
relativeresistance(PrintedSamplesD)
figure();
relativeresistance(PrintedSamplesE)
figure();
relativeresistance(PrintedSamplesF)

%%
figure();
resistance(PrintedSamplesA)
hold on
resistance(PrintedSamplesB)
resistance(PrintedSamplesC)
resistance(PrintedSamplesD)
resistance(PrintedSamplesE)
resistance(PrintedSamplesF)

%%

function relativeweights(samples)
    samples =  str2double(table2array(samples));
    for i = 1:(size(samples,2)-3)
        plot(samples(:,1), samples(:,i+1)/samples(1,i+1));
        hold on
    end
    ylim([0 1]);
end

function relativeresistance(samples)
    samples =  str2double(table2array(samples));
    scatter(samples(:,1), samples(:,end)/samples(1,end));
end

function resistance(samples)
    samples =  str2double(table2array(samples));
    scatter(samples(:,1), samples(:,end));
    lsline
end