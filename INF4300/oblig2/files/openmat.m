function [ ret ] = openmat( name )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

fullMatFileName = fullfile(name);
if ~exist(fullMatFileName, 'file')
  message = sprintf('%s does not exist', fullMatFileName);
  uiwait(warndlg(message));
else
  s = load(fullMatFileName);
  ret=s;
end
end

