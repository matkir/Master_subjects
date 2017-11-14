clear all
close all

%% Oppgave 1
G=16;
t=openmat('mosaic1_train.mat');
t=t.mosaic1_train;
t2=openmat('mosaic2_test.mat');
t2=t2.mosaic2_test;
t3=openmat('mosaic3_test.mat');
t3=t3.mosaic3_test;

tm=openmat('training_mask.mat');
tm=tm.training_mask;

%making the images easyer to work with
t = uint8(round(double(t) * (G-1) / double(max(t(:)))));
t2 = uint8(round(double(t2) * (G-1) / double(max(t2(:)))));
t3 = uint8(round(double(t3) * (G-1) / double(max(t3(:)))));

figure(1);clf
imagesc(t)
colormap gray
title('Texture 1');


%% print tm

figure(1);clf
imagesc(t)
colormap gray
title('Texture 1');


%% oppgave 1-2
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


figure(2);clf
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

figure(3);clf
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

figure(4);clf
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

figure(5);clf
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



%% Oppgave 2
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

[tmpQ1,tmpQ2,tmpQ3,tmpQ4,tmpQ11,tmpQ12,tmpQ13,tmpQ14] = gGLCM(t,G,1,0,31);
Q1=tmpQ1;
[tmpQ1,tmpQ2,tmpQ3,tmpQ4,tmpQ11,tmpQ12,tmpQ13,tmpQ14] = gGLCM(t,G,0,-1,31);
Q4=tmpQ4;
Q12=tmpQ12;


%test sets
[TMPt2Q1,TMPt2Q2,TMPt2Q3,TMPt2Q4,TMPt2Q11,TMPt2Q12,TMPt2Q13,TMPt2Q14] = gGLCM(t2,G,1,0,31);
t2Q1=TMPt2Q1;
[TMPt2Q1,TMPt2Q2,TMPt2Q3,TMPt2Q4,TMPt2Q11,TMPt2Q12,TMPt2Q13,TMPt2Q14] = gGLCM(t2,G,0,-1,31);
t2Q4=TMPt2Q4;
t2Q12=TMPt2Q12;
 
[TMPt3Q1,TMPt3Q2,TMPt3Q3,TMPt3Q4,TMPt3Q11,TMPt3Q12,TMPt3Q13,TMPt3Q14] = gGLCM(t3,G,1,0,31);
t3Q1=TMPt3Q1;
[TMPt3Q1,TMPt3Q2,TMPt3Q3,TMPt3Q4,TMPt3Q11,TMPt3Q12,TMPt3Q13,TMPt3Q14] = gGLCM(t3,G,0,-1,31);
t3Q4=TMPt3Q4;
t3Q12=TMPt3Q12;


%% oppgave 3
figure(6);clf
imagesc(Q1)
colormap jet
title('Q1 with dx=1 dy=0');

figure(7);clf
imagesc(Q4)
colormap jet
title('Q4 with dx=0 dy=-1');

figure(8);clf
imagesc(Q12)
colormap jet
title('Q12 with dx=0 dy=-1');





%% Oppgave 4
%we got 4 classes and 3 features we use
cl=4;
feature=3;
% actual classes needs to be made.
%Here we make a new ACtualCLass as a mask. 
accl = zeros(512,512);
accl(1:512/2, 1:512/2) = 1;
accl(1:512/2, 512/2:512) = 2;
accl(512/2:512, 1:512/2) = 3;
accl(512/2:512, 512/2:512) = 4;




%calculating mu and sigma for each feature*class
my = zeros(cl,feature);
sigma = zeros(feature,feature,cl);


%flatten the training mask
[tmp1 , tmp2] = size(tm);
mask = reshape(tm, tmp1 * tmp2, 1);

%get the 3 feture images
mysigma(1,:)=Q1(:);
mysigma(2,:)=Q4(:);
mysigma(3,:)=Q12(:);
for c = 1:cl
    for i = 1:feature
        tmp(:, 1) = mysigma(i, :);
        my(c,i) = mean(rot90(tmp(mask == c)));
    end
    sigma(:, :, c) = cov(rot90(mysigma(:,mask == c)));
end





%% Oppgave 5
f_all(1,:,:) = Q1;
f_all(2,:,:) = Q4;
f_all(3,:,:) = Q12;
[acc,outimg,confusion] = oppg7(f_all, my, sigma, cl, accl);

figure(15);clf
imagesc(outimg)
title('Classefied img');

confusion
acc

%% oppg6.2


f_all(1,:,:) = t2Q1;
f_all(2,:,:) = t2Q4;
f_all(3,:,:) = t2Q12;
[acc,outimg,confusion] = oppg7(f_all, my, sigma, cl, accl);


figure(16);clf
imagesc(outimg)
title('test2 img');

confusion
acc


%% oppg6.1
f_all(1,:,:) = t3Q1;
f_all(2,:,:) = t3Q4;
f_all(3,:,:) = t3Q12;
[acc,outimg,confusion] = oppg7(f_all, my, sigma, cl, accl);


figure(76);clf
imagesc(outimg)
title('test3 img');

confusion
acc

