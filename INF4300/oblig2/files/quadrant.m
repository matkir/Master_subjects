function [ outmat ] = quadrant(num,mat)
%We beleve that the matrix is allways 16x16
%   gives a subquadrant
if num==1
    outmat=mat(1:8,1:8)%./sum(sum(mat));
end
if num==2
    outmat=mat(8:16,1:8)%./sum(sum(mat));
end
if num==3
    outmat=mat(1:8,8:16)%./sum(sum(mat));
end
if num==4
    outmat=mat(8:16,8:16)%./sum(sum(mat));
end    
end

