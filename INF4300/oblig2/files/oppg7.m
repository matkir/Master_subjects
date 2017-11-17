function [ acc,outimg,confusion ] = oppg7( f_all, my, sigma, cl, actual_matrix)

%first we make the array that will hold the values for all the calculated
%values fir the Multivariate Normal Distribution
MultivariateNormalDistribution = zeros(cl, 512, 512);
for c = 1:cl %for each class
    d = 1/sqrt((2 * pi)^3 * det(sigma(:,:,c))); %denominator
    for m = 1:512 %for each x pixel
        for n = 1:512 %for each y pixel
            MultivariateNormalDistribution(c, m, n) = d*exp(-0.5 * (rot90(f_all(:,m,n)) - my(c,:)) / sigma(:,:,c) * transpose(rot90(f_all(:,m,n)) - my(c,:)));
        end
    end
end

chance = MultivariateNormalDistribution  ./ cl; 

filler = zeros(512,512); %filler gets the val for the chanse it have at the current run of c
outimg = zeros(512,512);
for c = 1:cl
    for m = 1:512
        for n = 1:512
            if chance(c, m, n) > filler(m, n)
                filler(m,n) = chance(c, m, n);
                outimg(m,n) = c;
            end
        end
    end
end


confusion = confusionmat(outimg(:), actual_matrix(:));  %make the confusionmatrix
acc = sum(sum(diag(confusion)))/ sum(sum(confusion)) *100 ; %calc percent


% used For PLOTTING DURING REPORT. INGNORE
% figure();clf
% imagesc(squeeze(chance(1,:,:)))
% colormap hot
% title(' probability of class 1');
% figure();clf
% imagesc(squeeze(chance(2,:,:)))
% colormap hot
% title(' probability of class 2');
% figure();clf
% imagesc(squeeze(chance(3,:,:)))
% colormap hot
% title(' probability of class 3');
% figure();clf
% imagesc(squeeze(chance(4,:,:)))
% colormap hot
% title(' probability of class 4');

end

