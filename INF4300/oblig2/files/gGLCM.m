function [Q1,Q2,Q3,Q4,Q11,Q12,Q13,Q14] = gGLCM(img, G, dx, dy, window)
% at this pont in the process this function was not self-made.
% Heavy inspiration for Kristoffer Hoiseter, since he did the first
% obligatory assignment in MATLAB, and I made my gliding window in python.


[M,N] = size(img);
halfW = floor(window/2);

%expanding the image with a border
imgBorder = zeros(M+window-1, N+window-1);
imgBorder(halfW+1:end-halfW,halfW+1:end-halfW) = img;

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
for m = 1+halfW:Mborder-halfW-1
    for n = 1+halfW:Nborder-halfW-1
        
        win = imgBorder(m-halfW:m+halfW, n-halfW:n+halfW);

        p = GLCM(win,G,dx,dy);
        
        Q1(m-halfW,n-halfW)=sum(sum(p(1:G/2,1:G/2)))/sum(sum(p));
        Q2(m-halfW,n-halfW)=sum(sum(p(1:G/2,G/2:G)))/sum(sum(p));
        Q3(m-halfW,n-halfW)=sum(sum(p(G/2:G,1:G/2)))/sum(sum(p));
        Q4(m-halfW,n-halfW)=sum(sum(p(G/2:G,G/2:G)))/sum(sum(p));
        
        Q11(m-halfW,n-halfW)=sum(sum(p(1:G/4,1:G/4)))/sum(sum(p));
        Q12(m-halfW,n-halfW)=sum(sum(p(1:G/4,1+G/4:G/2)))/sum(sum(p));
        Q13(m-halfW,n-halfW)=sum(sum(p(1+G/4:G/2,1:G/4)))/sum(sum(p));
        Q14(m-halfW,n-halfW)=sum(sum(p(1+G/4:G/2,1+G/4:G/2)))/sum(sum(p));
        
        
    end
        
        
end
end
