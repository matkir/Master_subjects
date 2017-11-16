function [Q1,Q2,Q3,Q4,Q11,Q12,Q13,Q14] = gGLCM(img, G, dx, dy, window)
% at this pont in the process this function was not 100% self-made.
% Inspiration for Kristoffer Hoiseter, since he did the first
% obligatory assignment in MATLAB, and I made my gliding window in python.


[M,N] = size(img);
halfWindow = floor(window/2);

%expanding the image with a border
imgBorder = zeros(M+window-1, N+window-1);
imgBorder(halfWindow+1:end-halfWindow,halfWindow+1:end-halfWindow) = img;

%size of the new image
[Mborder, Nborder] = size(imgBorder);

i = repmat((0:(G-1))', 1, G);
j = repmat((0:(G-1)), G, 1);


Q1 = zeros(M,N);
Q2 = zeros(M,N);
Q3 = zeros(M,N);
Q4 = zeros(M,N);

%spitting the top left quadrant in 4, because the action is happening here
Q11 = zeros(M,N);
Q12 = zeros(M,N);
Q13 = zeros(M,N);
Q14 = zeros(M,N);


%going through the image
for m = 1+halfWindow:Mborder-halfWindow-1;
    for n = 1+halfWindow:Nborder-halfWindow-1;
        
        win = imgBorder(m-halfWindow:m+halfWindow, n-halfWindow:n+halfWindow);

        p = GLCM(win,G,dx,dy);
        
        Q1(m-halfWindow,n-halfWindow)=sum(sum(p(1:G/2,1:G/2)))/sum(sum(p));
        Q2(m-halfWindow,n-halfWindow)=sum(sum(p(1:G/2,G/2:G)))/sum(sum(p));
        Q3(m-halfWindow,n-halfWindow)=sum(sum(p(G/2:G,1:G/2)))/sum(sum(p));
        Q4(m-halfWindow,n-halfWindow)=sum(sum(p(G/2:G,G/2:G)))/sum(sum(p));
        
        Q11(m-halfWindow,n-halfWindow)=sum(sum(p(1:G/4,1:G/4)))/sum(sum(p));
        Q12(m-halfWindow,n-halfWindow)=sum(sum(p(1:G/4,1+G/4:G/2)))/sum(sum(p));
        Q13(m-halfWindow,n-halfWindow)=sum(sum(p(1+G/4:G/2,1:G/4)))/sum(sum(p));
        Q14(m-halfWindow,n-halfWindow)=sum(sum(p(1+G/4:G/2,1+G/4:G/2)))/sum(sum(p));
        
        
    end
        
        
end
end
