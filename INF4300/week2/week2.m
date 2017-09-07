

img = imread('zebra_2.tif');



figure(1);
imshow(img, []);
title('Original image');

G = 8; % We just want to use G gray levels

% Make the histogram (approx.) uniform with G grey levels.
% See the curriculum for INF2310 if you do not know histogram equalization
img_std = histeq(img,G);
img_std = uint8(round(double(img_std) * (G-1) / double(max(img_std(:)))));

figure(2);
imshow(img_std, [0 G-1]);

GLCM2=GLCM_M(img_std,G,10,0,0,1);
stats = graycoprops(GLCM2)

figure(3);
subplot(211)
h = imhist(img);
plot([0:255],h/sum(h),'linewidth',2);
xlim([0 15])
title('Normalized histogram of original image');
subplot(212)
h = imhist(img_std);
plot([0:255],h/sum(h),'linewidth',2);
xlim([0 15])
title('Normalized histogram of image after histeq');

% Define GLCM-parameters.
windowSize = 31;
dx = 0;
dy = 2;
calculateGLCM=1;

% Call the function to calculate the feature images with gliding GLCM
if calculateGLCM == 1
    [glcmVar,glcmCtr,glcmEnt] = glidingGLCM_M(img_std,G,dx,dy,windowSize);
    save('Data.mat','glcmVar','glcmCtr','glcmEnt','windowSize','G');
else
    load Data.mat;
end


% Display the results
figure(4);clf
subplot(211)
imshow(glcmVar, []); title('GLCM Variance');
subplot(212)
imshow(img.*uint8(glcmVar > (max(glcmVar(:)) * 0.5)),[]);
title('Image thresholded with GLCM Variance');

figure(5);clf
subplot(211)
imshow(glcmCtr, []); title('GLCM Contrast');
subplot(212)
imshow(img.*uint8(glcmCtr > (max(glcmCtr(:)) * 0.2)),[]);
title('GLCM Contrast thresholded');

figure(6);clf
subplot(211)
imshow(glcmEnt, []); title('GLCM Entropy' );
subplot(212)
imshow(img.*uint8(abs(glcmEnt) < (max(abs(glcmEnt(:))) * 0.7)),[]);
title('GLCM Entropy tresholded');