%I = imread('img_cells.jpg');
%figure(19); imshow(I), title('Cell image')

%bw = im2bw(I, graythresh(I));
%figure(20); imshow(bw), title('BWed using Otsu''s threshold')

%bw_filled = bwareaopen(bw, 200);
%figure(21); imshow(bw_filled), title('After filling gaps')

%D = bwdist(bw_filled);
%figure(22); imshow(D, []), title('Distance image')




clear all;
close all;
rgb = imread('pears.png');
I = rgb2gray(rgb);

figure(4)
imshow(I)
text(732, 501, 'Image courtesy of Corel', ...
     'FontSize', 7, 'HorizontalAlignment', 'right')
title('Grayscale image of pears');



hy = fspecial('sobel')
hx = hy';
Iy = imfilter(double(I), hy, 'replicate');
Ix = imfilter(double(I), hx, 'replicate');
gradmag = sqrt(Ix.^2 + Iy.^2);
%figure(5); imshow(Iy,[]);
%figure(6); imshow(Ix,[]);
figure(7); imshow(gradmag,[]);
title('Gradient magnitude (gradmag)');

L = watershed(gradmag);
Lrgb = label2rgb(L);
%h6 = figure(8); imshow(Lrgb);
%title('Watershed transform of gradient magnitude, does this work?');

