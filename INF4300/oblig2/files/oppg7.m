function [ acc,outimg,confusion ] = oppg7( f_all, my, sigma, cl, actual_matrix)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
likelihood = zeros(cl, 512, 512);
for c = 1:cl
    d = sqrt((2 * pi)^3 * det(sigma(:,:,c)));
    for m = 1:512
        for n = 1:512
            likelihood(c, m, n) = (1/d)* exp(-0.5 * (rot90(f_all(:,m,n)) - my(c,:)) / sigma(:,:,c) * transpose(rot90(f_all(:,m,n)) - my(c,:)));
        end
    end
end



normfactor = sum(likelihood);
normfactor_reshape = zeros(cl,512,512);
normfactor1 = squeeze(normfactor(1,:,:));
for c = 1:cl
    normfactor_reshape(c, :, :) = normfactor1;
end


posterior = likelihood ./ normfactor_reshape ./ cl;


filler = zeros(512,512);
outimg = zeros(512,512);
for m = 1:512
    for n = 1:512
        for c = 1:cl
            if posterior(c, m, n) > filler(m, n)
                filler(m,n) = posterior(c, m, n);
                outimg(m,n) = c;
            end
        end
    end
end


confusion = confusionmat(outimg(:), actual_matrix(:)); 
acc = sum(sum(diag(confusion)))/ sum(sum(confusion)) *100 ; %calc percent


end

