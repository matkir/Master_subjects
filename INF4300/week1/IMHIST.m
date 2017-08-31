function [ retur ] = IMHIST( img )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
retur=zeros(1,255);
for i = 1:255
    retur(i) = length(find(img==i));
end

