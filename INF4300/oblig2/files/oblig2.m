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
[Q1,Q2,Q3,Q4,Q11,Q12,Q13,Q14] = gGLCM(t,G,1,0,31);
[tQ1,tQ2,tQ3,tQ4,tQ11,tQ12,tQ13,tQ14] = glidingGLCM(t2,G,1,0,31);
%%
figure(1);clf
imagesc(Q1)
colormap jet
title('Q1');

figure(2);clf
imagesc(Q2)
colormap jet
title('Q2');

figure(3);clf
imagesc(Q3)
colormap jet
title('Q3');

figure(4);clf
imagesc(Q4)
colormap hot
title('Q4');



% o2_1=quadrant(1,s1);
% o2_2=quadrant(3,s3);
% stats = graycoprops(o2_1);
% stats = graycoprops(o2_2);
% 
% o2_3=quadrant(3,s7);
% o2_4=quadrant(2,s5);
% stats = graycoprops(o2_3);
% stats = graycoprops(o2_4);
% 
% o2_5=quadrant(2,s9);
% o2_6=quadrant(4,s11);
% stats = graycoprops(o2_5);
% stats = graycoprops(o2_6);
% 
% o2_7=quadrant(2,s15);
% o2_8=quadrant(4,s16);
% stats = graycoprops(o2_7);
% stats = graycoprops(o2_8);





%% Oppgave 3



%Plot dat data
figure(1)
imagesc(training_mask);
colorbar
title('Training Mask');

figure(2);clf
imagesc(Q1)
colormap hot
title('Q1 feature');

figure(3);clf
imagesc(Q2)
colormap hot
title('Q2 feature');

figure(4);clf
imagesc(Q12)
colormap hot
title('Q12 feature');




%% Oppgave 4
a=Gclas();

%% Oppgave 5





