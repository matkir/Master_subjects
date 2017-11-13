function glcm = GLCM(img, G, dx, dy)
% at this pont in the process this function was not self-made.
% Heavy inspiration for Kristoffer Høisæter, since he did the first
% obligatory assignment in MATLAB, and I made my gliding window in python.


%size of image
[M,N] = size(img);


W = 1./((M-dx)*(N-dy));
glcm = zeros(G);

%going through and counting
for i=1:M
    for j=1:N
        %making sure the indexes does not exceed matrix dimensions
        if j + dy < 1 || j + dy > N || i + dx < 1 || i + dx > M
            continue
        else
            a = img(i,j);
            b = img(i+dx,j+dy);
            glcm(a+1,b+1) = glcm(a+1,b+1) + 1; 
        end
    end
end

%symmetric and normalized
glcm = glcm + glcm';
glcm = glcm./sum(sum(glcm));
%glcm = W*glcm;