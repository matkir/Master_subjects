clear all 

lib = oblig1lib_oppg1;
img = double(imread('../portrett.png'));

figure()
image(img); colormap(gray(256))
title('Original image')

sigma = 64;
mean = 127;
img_standarized = lib.from0to255(lib.standarize_contrast(img,mean,sigma));

figure()
image(round(img_standarized)); colormap(gray(256))
title('After standarized mean and standarddeviation')
exit

mask = double(rgb2gray(imread('geometrimaske.png')));
% figure()
% image(mask);colormap(gray(256))
% title('Mask')

% Manually chosen points by looking at the image of the mask
% Left eye:              (173, 258)
% Right eye:             (343, 259)
% Midpoint at the mouth: (254, 439)
points_mask = [[173 258];[343 259];[254 439]];

% Manually chosen points by looking at the portrait of SYLVESTER STALLONE
% Left eye:              (84,88)
% Right eye:             (119,68)
% Midpoint at the mouth: (128,109)
points_img = [[84 88];[119 68];[128 109]];

coordinate_matrix = cat(2,points_img,ones(3,1));

% Along x-axis (horizontal axis)
a = coordinate_matrix\points_mask(:,1);

% One could also use the method of minimizing the mean square error as
% described in slide 28 about geometric operations

% Along y-axis (vertical axis)
b = coordinate_matrix\points_mask(:,2);

A = zeros(3,3);
A(1,:) = a';
A(2,:) = b';
A(3,:) = [0 0 1];

size_new = size(mask);
size_old = size(img);
img_forward_mapped = lib.forward_map(size_old,size_new,img_standarized,A);

figure()
image(img_forward_mapped); colormap(gray(256))
title('Result after forwardmapping')

img_backward_mapped_nearest = lib.backward_map(size_old,size_new,img_standarized,A);

figure()
image(img_backward_mapped_nearest); colormap(gray(256));
title('Result after backwardmapping using nearest neighbour interpolation')

img_backward_mapped_bilin = lib.backward_map(size_old,size_new,img_standarized,A,'bilinear');

figure()
image(img_backward_mapped_bilin); colormap(gray(256));
title('Result after backwardmapping using bilinear interpolation')

