%% oppgave
1wp=0.3*pi;
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

wvtool(h)

%% kaiser
L=ceil(6.6*pi/DeltaW);
M=L;
n=0:M;
hd=ideallp(omegac,M);
tmp= kaiser(L)';
h=(hd.*tmp);

%wvtool(h)
%fvtool(h);


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





