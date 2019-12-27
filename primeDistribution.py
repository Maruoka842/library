import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import math

plt.rcParams["xtick.labelsize"] = 25                       # デフォルトは12。tickのラベルのサイズ。
plt.rcParams["ytick.labelsize"] = 25                       # デフォルトは12
plt.rcParams["xtick.major.size"] = 15 # 主メモリのサイズ                       
plt.rcParams["ytick.major.size"] = 15 # 主メモリのサイズ
plt.rcParams["xtick.major.width"] = 1.5 # 主メモリのサイズ                       
plt.rcParams["ytick.major.width"] = 1.5 # 主メモリのサイズ
plt.rcParams['axes.linewidth'] = 1.5 # 枠の太さ
plt.rcParams["ytick.minor.size"] = 7 # 副メモリのサイズ
plt.rcParams["xtick.minor.size"] = 7 # 副メモリのサイズ
plt.rcParams["ytick.minor.size"] = 7 # 副メモリのサイズ
plt.rcParams['xtick.major.pad'] = 8  
plt.rcParams['ytick.major.pad'] = 8  

plt.rcParams["axes.labelsize"]  = 28                       # デフォルトは12。軸のラベルのサイズ。
plt.rcParams['legend.fontsize'] = 20
plt.rcParams["figure.autolayout"] = True                   # ラベルが切れないように自動調整
plt.rcParams["axes.titlesize"] = 25                        # 時刻を表示する以外には使用していない
plt.rcParams['http://font.family'] = 'Liberation Sans' 
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['xtick.direction'] = 'in'                     # x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in'                     # y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams["legend.fancybox"] = False                    # fancyboxは角の丸み
plt.rcParams["legend.edgecolor"] = 'black'                 # 枠線は黒色

def run():
    fig=plt.figure()
    ax=fig.add_subplot()
    n=30
    isPrime=np.empty((n,n),bool)
    for i in range(n):
        for j in range(n):
            isPrime[i][j]=True
    isPrime[0][0]=False
    D=3
    sz=0
    # (2i + j) + j √D
    for i in range(n):
        for j in range(n):
            if not isPrime[i][j]:
                continue
            sz = sz+1
            for k in range(n):
                for l in range(n):
                    if ((2*i+j)*(2*i+j)+j*j*D >= (2*k+l)*(2*k+l)+l*l*D):
                        continue
                    #(u,v) // (x,y)
                    #u/v=x/y
                    #u*y=x*v
                    if (2*i + j) * l != (2*k + l) * j :
                        continue
                    isPrime[k][l]=False
    x=np.empty((6*sz),float)
    y=np.empty((6*sz),float)
    p=0
    for i in range(n):
        for j in range(n):
            if isPrime[i][j]:
                for k in range(6):
                    u=(2*i+j)*0.5
                    v=j*math.sqrt(3)*0.5
                    c=math.cos(2*math.pi/6*k)
                    s=math.sin(2*math.pi/6*k)
                    x[p+k*sz]=u*c-v*s
                    y[p+k*sz]=u*s+v*c
                p=p+1
    ax.scatter(x,y,marker=".")
    ax.set_xlim(left=-20,right=20)
    ax.set_ylim(bottom=-20,top=20)
    ax.set_aspect("equal")
    ax.set_xticks([-20,-10,0,10,20])
    http://plt.show()
run()
