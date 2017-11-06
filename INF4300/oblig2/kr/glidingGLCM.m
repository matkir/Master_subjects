function [IDM, INR, SHD] = glidingGLCM(img, G, dx, dy, window)

[M,N] = size(img);
halfW = floor(window/2);

%expanding the image with a border
imgBorder = zeros(M+window-1, N+window-1);
imgBorder(halfW+1:end-halfW,halfW+1:end-halfW) = img;

%size of the new image
[Mborder, Nborder] = size(imgBorder);

i = repmat((0:(G-1))', 1, G);
j = repmat((0:(G-1)), G, 1);


IDM = zeros(M,N);
INR = zeros(M,N);
SHD = zeros(M,N);

%going through the image
for m = 1+halfW:Mborder-halfW-1
    for n = 1+halfW:Nborder-halfW-1
        
        win = imgBorder(m-halfW:m+halfW, n-halfW:n+halfW);

        p = GLCM(win,G,dx,dy);
        mu = mean(win(:));
        
        
        % Compute GLCM's contrast / inertia
        INR(m-halfW,n-halfW) = sum(sum(p .* ((i - j).^2)));

        
        %Compute GLCM's homogeneity 
        IDM(m-halfW,n-halfW) = sum(sum(1./(1+(i-j).^2).*p));
        
        mux = sum(sum(p.*(i+1)));
        muy = sum(sum(p.*(j+1)));
        
        %Compute GLCM's cluster shade
        SHD(m-halfW,n-halfW) = sum(sum(((i+j-mux - muy).^3).*p));
        
    end
        
        
end
end
