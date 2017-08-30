k=3;
N=10;

dirac_delta=zeros(1,2*N+1);
dirac_delta(N+1+k)=1;

figure(1)
stem(-N:N,dirac_delta,'LineWitdth',2);
axis([-N,N,-1,1]); grid on;
title(['Plott av $\delta[n-k]$ med k=' num2str(k)],'interpreter','latex')
xlabel('Sample Number');
ylabel('$\delta[n]$','interpreter','latex');

