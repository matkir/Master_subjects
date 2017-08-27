clear all 

lib = oblig1lib_oppg2;
img = imread('../houses.png');

%See if image is rgb and ensure
%it is grayscale
if (ndims(img) == 3) 
    img = rgb2gray(img);
end
img = double(img);

N = 11;
sigma = 2;

NN = (N-1)/2;

x = -NN:NN;
y = -NN:NN;
[y,x] = meshgrid(y,x);

H = 1/(2*pi*sigma^2).*exp(-((x.*x + y.*y)./(2*sigma^2)));

img_gauss = lib.convolve2D(img,H);

sobel = [1 2 1;0 0 0;-1 -2 -1];
img_gx = lib.convolve2D(img_gauss,sobel);
img_gy = lib.convolve2D(img_gauss,sobel');


img_grad = sqrt(img_gx.*img_gx + img_gy.*img_gy);

img_direction = atan2(img_gy,img_gx);
img_direction = mod((round(img_direction.*180./(pi*45)).*45),180);

img_thinned = lib.non_max_suppression(img_grad,img_direction);

lib1 = oblig1lib_oppg1;
img_thinned = lib1.from0to255(img_thinned);

img_hyst = lib.hysteresis(img_thinned, 30,60);

figure()
imshow(img_hyst,[]); %colormap(gray(256))
title('Final result')
