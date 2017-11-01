clear all
close all



fullMatFileName = fullfile('mosaic1_train.mat')
if ~exist(fullMatFileName, 'file')
  message = sprintf('%s does not exist', fullMatFileName);
  uiwait(warndlg(message));
else
  s = load(fullMatFileName);
end

s.mosaic1_train;

figure(1);clf
imagesc(s.mosaic1_train)
colormap gray
title('Texture 1');

