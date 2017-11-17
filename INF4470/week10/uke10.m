%% oppgave
wp=0.3*pi;
ws=0.5*pi;
Ap=0.5;
As=50;
deltap=(10^(Ap/20)-1)/(10^(Ap/20)+1);
deltas=(1+deltap)/(10^(As/20));
delta=min(deltap,deltas);
A=-20*log10(delta);
DeltaW=ws-wp;
omegac=(wp+ws)/2;

%% hamming
L=ceil(6.6*pi/DeltaW);
M=L;
n=0:M;
hd=ideallp(omegac,M);
tmp=hamming(L)';
h=hd.*tmp;


%% kaiser
L=ceil(6.6*pi/DeltaW);
M=L;
n=0:M;
hd=ideallp(omegac,M);
tmp= kaiser(L)';
h=(hd.*tmp);

%wvtool(h)
%fvtool(h);



%% plots 

wvtool(h)

figure();
stem(h)

figure()
tmp=linspace(-pi,pi,10000);
pl=fftshift(fft(h,length(tmp)));
plp=abs(pl(tmp>=wp));
pls=abs(pl(tmp<=wp & tmp>=0));
plot(tmp/pi,20*log10(abs(pl)));
hold on;
plot(tmp(tmp>=wp)/pi,20*log10(plp));
plot(tmp(tmp<=ws & tmp>=0)/pi,20*log10(pls));

hold off;

figure()
%[Ax,H1,H2]=plotyy( tmp(tmp>=wp)/pi, 20*log10(plp) , tmp(tmp<=ws & tmp>=0)/pi , 20*log10(pls) );






%% oppgave 2
wp=0.5*pi;
ws=0.3*pi;
Ap=0.001;
As=50;
deltap=(10^(Ap/20)-1)/(10^(Ap/20)+1);
deltas=(1+deltap)/(10^(As/20));
delta=min(deltap,deltas);
A=-20*log10(delta);
DeltaW=ws-wp;
omegac=(wp+ws)/2;

%manuel
f0=[ws wp]/pi;
a=[0 1];
dev=[deltas deltap];
[M wN beta type]=kaiserord(f0,a,dev);
n=(0:M);

hd=ideallp(omegac,M+1);
tmp=kaiser(M+1,beta);
h=hd .* tmp';

%fir funksjon
% M=M+1;
% L=L+1;
% f0=[ws wp]/pi;
% a=[0 1];
% h=fir1(M,f0,a,kaiser(L));
% k=(0:M);


























%% oppgave 3
clear all
M=61;
L=M+1;

alpha=M/2;
n=(0:M);
hd=cos(pi*(n-alpha))./(n-alpha)-sin(pi*(n-alpha))/pi./(n-alpha).^2;
h=hd.*blackman(M+1).';

figure()
subplot(1,2,1)
stem(n,h)
tmp=linspace(-pi,pi,1000);
pl=fftshift(fft(h,length(tmp)));
subplot(1,2,2);
plot(tmp,abs(pl))
xlim([0 pi]);
hold on;
plot(tmp,abs(1i*tmp.*exp(-1i*tmp*alpha)))
hold off;


s1=cos(2*pi*2*n/L);
s2=n.^2;
s3=cos(2*pi*2.*n/L*2.*n/L);
s1c=conv(s1,h);
s2c=conv(s2,h);
s3c=conv(s3,h);

figure()
subplot(1,2,1)
plot(s1)
subplot(1,2,2)
plot(s1c)

figure()
subplot(1,2,1)
plot(s2)
subplot(1,2,2)
plot(s2c)

figure()
subplot(1,2,1)
plot(s3)
subplot(1,2,2)
plot(s3c)


%% oppgave 4
clear all
wp=0.8*pi;
ws=0.6*pi;
Ap=1;
As=50;
deltap=(10^(Ap/20)-1)/(10^(Ap/20)+1);
deltas=(1+deltap)/(10^(As/20));
delta=min(deltap,deltas);

M=33;
L=34;

a=2*pi/M;
tmp=(0:L/2-1)*a;
pls=tmp(tmp<=ws);
plp=tmp(tmp>=wp);
plPS=tmp(tmp>ws & tmp<wp);
b=0*tmp;
b(tmp<=ws)=0;
b(tmp>=wp)=1;
b(tmp>ws & tmp<wp)=(plPS-ws)*(1/(wp-ws));


%fir funksjon
% M=34;
% L=35;
% h=fir2(M,[tmp/pi 1],[b 1],hamming(L));
% k=(0:M);

%manuelt
k=(0:M);
phase=pi/2-2*pi*k*M/(2*L);
magnitude=[b fliplr(b)];
h=magnitude.*exp(1i*phase);
h=real(ifft(h));




wvtool(h)
figure()
stem(h)
