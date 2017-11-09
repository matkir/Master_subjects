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



s1=openmat('texture1dx0dymin1.mat');
s1=s1.texture1dx0dymin1;
s2=openmat('texture1dx1dymin1.mat');
s2=s2.texture1dx1dymin1;
s3=openmat('texture1dxmin1dymin1.mat');
s3=s3.texture1dxmin1dymin1;
s4=openmat('texture1dxplus1dy0.mat');
s4=s4.texture1dx1dy0;
s5=openmat('texture2dx0dymin1.mat');
s5=s5.texture2dx0dymin1;
s6=openmat('texture2dxplus1dy0.mat');
s6=s6.texture2dx1dy0;
s7=openmat('texture2dxplus1dymin1.mat');
s7=s7.texture2dx1dymin1;
s8=openmat('texture2dxmin1dymin1.mat');
s8=s8.texture2dxmin1dymin1;
s9=openmat('texture3dx0dymin1.mat');
s9=s9.texture3dx0dymin1;
s10=openmat('texture3dxplus1dy0.mat');
s10=s10.texture3dx1dy0;
s11=openmat('texture3dxplus1dymin1.mat');
s11=s11.texture3dx1dymin1;
s12=openmat('texture3dxmin1dymin1.mat');
s12=s12.texture3dxmin1dymin1;
s13=openmat('texture4dx0dymin1.mat');
s13=s13.texture4dx0dymin1;
s14=openmat('texture4dxplus1dy0.mat');
s14=s14.texture4dx1dy0;
s15=openmat('texture4dxplus1dymin1.mat');
s15=s15.texture4dx1dymin1;
s16=openmat('texture4dxmin1dymin1.mat');
s16=s16.texture4dxmin1dymin1;


figure(1);clf
title('Texture 1');
colormap gray
subplot(2,2,1) 
imagesc(s1)
subplot(2,2,2) 
imagesc(s2)
subplot(2,2,3) 
imagesc(s3)
subplot(2,2,4) 
imagesc(s4)

figure(2);clf
title('Texture 1');
colormap gray
subplot(2,2,1) 
imagesc(s5)
subplot(2,2,2) 
imagesc(s6)
subplot(2,2,3) 
imagesc(s7)
subplot(2,2,4) 
imagesc(s8)

figure(3);clf
title('Texture 1');
colormap gray
subplot(2,2,1) 
imagesc(s9)
subplot(2,2,2) 
imagesc(s10)
subplot(2,2,3) 
imagesc(s11)
subplot(2,2,4) 
imagesc(s12)

figure(4);clf
title('Texture 1');
colormap gray
subplot(2,2,1) 
imagesc(s13)
subplot(2,2,2) 
imagesc(s14)
subplot(2,2,3) 
imagesc(s15)
subplot(2,2,4) 
imagesc(s16)


%as described in the report. we kept 
%
%from texture 1
%
%from texture 2
%
%from texture 3
%
%from texture 4
%

a=quadrant(1,s1);



