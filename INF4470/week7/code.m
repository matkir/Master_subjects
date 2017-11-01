%% Oppgave 1
F = 700; 
Fs = 2800; %2800, 1190, 490 Hz
t = 0: 1/Fs :0.1;
y = sin(2*pi*F*t);
plot(t,y)
%sound(y,Fs)

%freqz(y,Fs)
%ck = fftshift(fft(y,2*length(y)));
%plot(y,ck)




%% 6.03 ?
Fs = 20;
t = linspace(-Fs,Fs, 200);
n = linspace(-Fs,Fs, 200/0.5);


xn = 2*cos(0.5*pi*n - pi/3) - 3*sin(0.8*pi*n);
xc = 2*cos(10*pi*t-pi/3) - 3*sin(16*pi*t);


plot(t,xc)
hold('on')
plot(n,xn)


%% Oppgave 6.17

FL = 105;
FH = 145;
dF = 0.01;
GB = 10;
FL2 = FL - GB/2;
FH2 = FH + GB/2;
Fs = 100;
F = -150:dF:150;
X = zeros(size(F));
XP = zeros(size(F));
XN = zeros(size(F));
for j = -10:10
    ind  = F > FL + j*Fs & F < FH + j*Fs;
    X(ind) = X(ind) + 1;
    XP(ind) = XP(ind) + 1;
end
ind = X == 0;
X(ind) = nan;
plot(F,XP, F, XN)
xlim([-150 150])
ylim([0 1.5])
