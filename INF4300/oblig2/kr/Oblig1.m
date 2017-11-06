
%% Part B

%reading the images
img1 = imread('mosaic1.png');
img2 = imread('mosaic2.png');



[x1,y1] = size(img1);
[x2,y2] = size(img2);
%number of graylevels
G = 16;
dx = 1;
dy = 0;

%histogram equalizing 
img1 = histeq(img1,G);
img2 = histeq(img2,G);
%normalizing
img1 = uint8(round(double(img1) * (G-1) / double(max(img1(:)))));
img2 = uint8(round(double(img2) * (G-1) / double(max(img2(:)))));

%dividing into subimages
texture1 = img1(1:floor(x1./2), 1:floor(y1./2));
texture2 = img1(1:floor(x1./2), floor(y1./2):y1);
texture3 = img1(floor(x1./2):x1, 1:floor(y1./2));
texture4 = img1(floor(x1./2):x1, floor(y1./2):y1);

texture5 = img2(1:floor(x1./2), 1:floor(y1./2));
texture6 = img2(1:floor(x1./2), floor(y1./2):y1);
texture7 = img2(floor(x1./2):x1, 1:floor(y1./2));
texture8 = img2(floor(x1./2):x1, floor(y1./2):y1);


P1 = GLCM(texture1, G, dx, dy);
P2 = GLCM(texture2, G, dx, dy);
P3 = GLCM(texture3, G, dx, dy);
P4 = GLCM(texture4, G, dx, dy);

P5 = GLCM(texture5, G, dx, dy);
P6 = GLCM(texture6, G, dx, dy);
P7 = GLCM(texture7, G, dx, dy);
P8 = GLCM(texture8, G, dx, dy);

%I do not know why this would not work...
% for i = 1:8
%     figure(i)
%     texture = strcat('P', num2str(i))
%     imagesc(texture)
%     colorbar
%     colormap jet
% end
    

figure(1)
imagesc(P1);
title('Texture 1');
colormap jet
figure(2)
imagesc(P2);
title('Texture 2');
colormap jet
colorbar
% 
figure(3)
imagesc(P3);
title('Texture 3');
colormap jet
figure(4)
imagesc(P4);
title('Texture 4');
colormap jet
colorbar
% 
figure(5)
imagesc(P5);
title('Texture 5');
colormap jet
figure(6)
imagesc(P6);
title('Texture 6');
colormap jet
colorbar

figure(7)
imagesc(P7);
title('Texture 7');
colormap jet
figure(8)
imagesc(P8)
title('Texture 8');
colormap jet
colorbar
%% Part C

%the different features for testing and experimenting. 
i = repmat((0:(G-1))', 1, G);
j = repmat((0:(G-1)), G, 1);

%inertia 
INR_weight = (i-j).^2;

%homogeneity 
IDM_weight = 1./(1+(i-j).^2);

%cluster shade of P1 (texture1) 
mu_x_1 = sum(sum(P1 .* (i+1)));
mu_y_1 = sum(sum(P1 .* (j+1)));
SHD_weight1 = (i+j - mu_x_1 - mu_y_1).^3;

% figure(3)
% imagesc(INR_weight)

% figure(4)
% imagesc(IDM_weight)
% 
% figure(5)
% imagesc(SHD_weight)

%my chosen window size
window = 31;

%compute the features
[glcmINR,glcmIDM, glcmSHD] = glidingGLCM(img1, G, dx,dy, window);
%%
figure(6)
imagesc(glcmSHD)
title('GLCM - Cluster Shade')
colormap jet
colorbar

figure(7)
imagesc(glcmINR)
title('GLCM - Inertia')
colorbar
colormap jet

figure(8)
imagesc(glcmIDM)
title('GLCM - Inverse Difference Moment')
colormap jet
colorbar

figure(9)
imagesc(img1)
colormap gray


figure(10)
treshold10 = -750;
imagesc(img1.*uint8(glcmSHD < treshold10))
colormap gray
title('SHD: dx = 1, dy = 0. Treshold < -750')


% thresholds found while experimenting
% Texture 6
% dx = 1, dy = 0
% treshold < 0.34
% IDM
% figure(11)
% treshold10 = 0.34;
% imagesc(img2.*uint8(glcmIDM < treshold10))
% colormap gray
% title('IDM: dx = 1, dy = 0. Treshold < 0.34')

% Texture 5
% dx = 1, dy = 0
% treshold > 0.53
% IDM
% figure(12)
% treshold10 = 0.53;
% imagesc(img2.*uint8(glcmIDM > treshold10))
% colormap gray
% title('INR: dx = 1, dy = 0. Treshold > 0.53')

% Texture 3
% dx = 0, dy = 1
% treshold > 0.53
% IDM
% figure(13)
% treshold10 = 0.53;
% imagesc(img1.*uint8(glcmIDM > treshold10))
% colormap gray
% title('INR: dx = 0, dy = 1. Treshold > 0.53')

% Texture 4 
% dx = 1, dy = 1
% treshold > 9
% INR
% figure(14)
% treshold10 = 14;
% imagesc(img1.*uint8(glcmINR > treshold10))
% colormap gray
% title('INR: dx = 1, dy = 1. Treshold > 14')

% Texture 2
% dx = 1, dy = 0
% treshold < 4 ikke hist
% INR
% figure(15)
% treshold11 = 4;
% imagesc(img1.*uint8(glcmINR < treshold11))
% colormap gray
% title('INR: dx = 1, dy = 0. Treshold < 4')








