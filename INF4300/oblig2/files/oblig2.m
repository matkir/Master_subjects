clear all
close all


s=openmat('mosaic1_train.mat');
s=s.mosaic1_train;

s2=openmat('training_mask.mat');
s2=s2.training_mask;

%figure(1);clf
%imagesc(s.mosaic1_train)
%imagesc(s2)
%colormap gray
%title('Texture 1');


names=[...
    "texture1_glcmdx0dymin1.mat","texture1_glcmdxplus1dy0.mat",...
    "texture1_glcmdxplus1dymin1.mat","texture1_glcmdxmin1dymin1.mat",...
    "texture2_glcmdx0dymin1.mat","texture2_glcmdxplus1dy0.mat",...
    "texture2_glcmdxplus1dymin1.mat","texture2_glcmdxmin1dymin1.mat",...
    "texture3_glcmdx0dymin1.mat","texture3_glcmdxplus1dy0.mat",...
    "texture3_glcmdxplus1dymin1.mat","texture3_glcmdxmin1dymin1.mat",...
    "texture4_glcmdx0dymin1.mat","texture4_glcmdxplus1dy0.mat",...
    "texture4_glcmdxplus1dymin1.mat","texture4_glcmdxmin1dymin1.mat",...
    ];



figure(1);clf
a=openmat('texture1_glcmdx0dymin1.mat');
imagesc(a.texture1_glcmdx0dymin1)
colormap gray
title('Texture 1');
