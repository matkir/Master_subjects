function [ class_img,error_train,confusion_train,u,c ] = Gclas( tm tm_train )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
[M,N] = size(tm_train);
res_train = zeros(M,N); 
res_test = zeros(M,N);

% I have one implementation where I train the classifier, but also run the
% classifier on the trining data. Giving me the accuarcy for the classifier
% on the traning data
[class_img,error_train,confusion_train,u,c] = trainMultiGaussClassifier(tm,tm_train);
% The second implementation takes the mean values (u) and the covariance
% matrices (c) from the traning part and classifies the image. From this I
% calculate the accuracy on the test part of the image
[class_img2,error_test,confusion_test] = multiGaussClassifierNoTraining(tm,tm_test,u,c);
% Note that the two classified images will be the sam (class_img and
% class_img2) the difference is which mask I use.

% Lets make the resulting image within the training masks
res_train(tm_train==1) = class_img(tm_train==1);
res_train(tm_train==2) = class_img(tm_train==2);
res_train(tm_train==3) = class_img(tm_train==3);
res_train(tm_train==4) = class_img(tm_train==4);

% And within the test masks
res_test(tm_test==1) = class_img(tm_test==1);
res_test(tm_test==2) = class_img(tm_test==2);
res_test(tm_test==3) = class_img(tm_test==3);
res_test(tm_test==4) = class_img(tm_test==4);

% And display them
figure(5);
imagesc(class_img);
title('Classified image');
colormap jet
drawnow

figure(6);
imagesc(res_train);
title('Classified pixels in training masks');
colormap jet
drawnow

figure(7)
imagesc(res_test);
title('Classified pixels in test masks');
colormap jet
drawnow

% Lets load  the tm_classres
load tm_classres

figure(8)
imagesc(klassim)
title('Given classification (from tm classres)');
colormap jet
drawnow

p = sum(sum(class_img == klassim))*100/(N*M);
fprintf('Comparing my result with tm_classres: %f \n',p);

error_train

confusion_train

error_test

confusion_test

end

