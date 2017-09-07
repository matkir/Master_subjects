function [ glcm ] = GLCM_M( image,Grey,dx,dy,normal,symmetric)
%regner ut stuff

[N,M] = size(image);
glcm = zeros(Grey);
for i=1:N
    for j=1:M
        if i+dy > N || i+dy < 1 || j+dx > M || j+dy < 1 || i + dx < 1 || j + dx < 1
           continue
        end
        from=image(i,j);
        to=image(i+dy,j+dx);
        glcm(from+1,to+1)=glcm(from+1,to+1)+1;
    end
end
%tatt fra en kis det under
    if symmetric
        glcm = glcm+glcm';
    end
    if normal
        glcm = glcm/sum(sum(glcm));
    end
end

