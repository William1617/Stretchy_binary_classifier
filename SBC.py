import numpy as np

def SBC(x,y,k,type):

    data_num=len(x)
    P1=np.ones((data_num,10))
    m1=(data_num+np.sum(y))//2
    m2=data_num-m1
    W=np.eye(data_num)
    for idx in range(data_num):
        P1[idx][1]=x[idx][0]
        P1[idx][2]=x[idx][1]
        P1[idx][3]=x[idx][0]*x[idx][0]
        P1[idx][4]=x[idx][1]*x[idx][1]
        P1[idx][5]=x[idx][1]*x[idx][0]
        P1[idx][6]=x[idx][0]*x[idx][0]*x[idx][0]
        P1[idx][7]=x[idx][1]*x[idx][1]*x[idx][1]
        P1[idx][8]=x[idx][1]*x[idx][0]*x[idx][0]
        P1[idx][9]=x[idx][1]*x[idx][1]*x[idx][0]
        W[idx][idx]=(1+y[idx])/(2*m1)+(1-y[idx])/(2*m2)
    
    if(type==2):
        a0=np.matmul(P1.T,W)
    else:
        a0=P1.T
   
    Pow=1/(k-1)
    a1=np.matmul(np.power(a0,Pow),P1)
    a2=np.power(a0,Pow)
    a=np.matmul(np.linalg.inv(a1),a2)
    a=np.matmul(a,y)

    result=np.matmul(P1,a)

    result=np.where(result>0,1,-1)
    print(a)
    return result


if __name__=='__main__':
    x1=[[0,0.2],[0.1,0.1],[0.2,0],[0.1,0.3],[0.2,0.2],[0.3,0.1],[0.1,0.2],[0.2,0.1],[0.1,0.4],[0.2,0.3],[0.3,0.2],[0.4,0.1],\
        [0.2,0.5],[0.3,0.4],[0.4,0.3],[0.5,0.2],[0.3,0.6],[0.6,0.3]]
    y1=[-1,-1,-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    result=SBC(x1,y1,1.15,2)
    print(result)

