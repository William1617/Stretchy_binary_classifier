
clc;
clear all
x1=[0,0.2;0.1,0.1;0.2,0;0.1,0.3;0.2,0.2;0.3,0.1;0.1,0.2;0.2,0.1;0.1,0.4;0.2,0.3;0.3,0.2;0.4,0.1;0.2,0.5;0.3,0.4;0.4,0.3;0.5,0.2;0.3,0.6;0.6,0.3];
y1=[-1 -1 -1 -1 -1 -1 1 1 1 1 1 1 1 1 1 1 1 1];
P=1./(1+exp(-x1));
P1=ones(18,10);
for i=1:18
    P1(i,2)=x1(i,1);
    P1(i,3)=x1(i,2);
    P1(i,4)=x1(i,1)*x1(i,1);
    P1(i,5)=x1(i,2)*x1(i,2);
    P1(i,6)=x1(i,1)*x1(i,2);
    P1(i,7)=x1(i,1)*x1(i,1)*x1(i,1);
    P1(i,8)=x1(i,2)*x1(i,2)*x1(i,2);
    P1(i,9)=x1(i,1)*x1(i,2)*x1(i,1);
    P1(i,10)=x1(i,1)*x1(i,2)*x1(i,2);
end
Pt=P1.';
W1=diag([2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1],0); 
W=W1./12;
a0=Pt*W;
k=1.2;
Pow=1/(k-1);
a1=(Pt.^Pow)*P1;
a2=(Pt.^Pow);
a=inv(a1)*a2;
g=P1*a;
ernum=0;
for i=1:6
    if g(i)>0
        ernum=ernum+1;
    end
end
for i=7:18
    if g(i)<0
        ernum=ernum+1;
    end
end
fprintf('the error count is %d',ernum)
bar(a)
title('order=3,k=1.2')



