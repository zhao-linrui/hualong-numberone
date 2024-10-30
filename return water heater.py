
#热平衡图6 7号加热器（原代码中为2号 1号）纯疏水模型
# A P1*(1-cqys1) B P2*(1-cqys2)待标注暂记 hB L K待标注暂记 hL(h0rh2_sw) DK hK(h1rh1_sw)
# 2号进水流量等于D0 2号疏水流量D1+D2+Drh1+Drh2 1号疏水流量D1+Drh2
# A B进汽温度未标注 记为tA tB

import CoolProp.CoolProp as CP
design_data={'P1*(1-cqys1)':2.673,'P2*(1-cqys2)':1.815}
design_data['D1+Drh2']=581274
design_data['D1+D2+Drh1+Drh2']=1153135

P1=2.729
P2=1.8528
PL=6.242
PK=2.621

DL=309321
D1=256683
Drh2=318560
D0=6124680
Drh1=253904
DK=255853

tA=227.6
tB=207.5
tw2=205.5
td1=210.5
tw3b=180.2

h0rh2_sw=1227.2
hw2=879.8
hd1=900.4
h1rh1_sw=973.7
hw3b=767.7
hd2=777.7
h2=2574.7
h1=2624.9
h0=2771.2
hw1=973.1

Tao1 = hw1 - hw2
Tao2 = hw2 - hw3b

gama2=hd1-hd2

b1 = 0.9756#汽水分离器效率
b2 = 0.9756
c1 = 0.9901
c2 = 0.9885
#b1 b2 c1 c2来自asset_config.py

D2 = (D0 * Tao2 - b1 * Drh1 * (h1rh1_sw - hd2) - (1 - b1) * Drh1 * (h1 - hd2) - (D1 + Drh2) * gama2)\
    / (c2 * (h2 - hd2) + (1 - c2)* (CP.PropsSI('H', 'P', P2 * 1e6, 'Q', 0, 'water') / 1e3 - hd2))
D1 = (D0 * Tao1 - b2 * Drh2 * (h0rh2_sw - hd1) - (1 - b2) * Drh2 * (h0 - hd1)) \
    / (c1 * (h1 - hd1) + (1 - c1) * (CP.PropsSI('H', 'P', P1 * 1e6, 'Q', 0, 'water') / 1e3 - hd1))
DB=(D0*(hw2-hw3b)-(D1+Drh2)*(hd1-hd2)-DK*(h1rh1_sw-hd2))/(hB-hd2)

#DB hB在热平衡图中有两股气流汇入，无直接数据，用道尔顿分压得到数据？还是？
#D1 D2 是仿照原代码与热平衡图有出入 DB是直接根据热平衡图计算，模型参照进展报告2-P11纯疏水模型



#热平衡图 5号除氧器（原代码为3号） 混合式加热器模型
#J 未标记暂记为 DJ h1rh1

Dsepw=654047
D2=313047
DJ=7289

hw3=756.9
hw4=659.6
h3=2489.7
hsepw=760.5
h1rh1=2802.5

Tao3 = hw3 - hw4
x3=0.8569

D3 = ((D0 - D1 - D2 - Drh1 - Drh2 - Dsepw) * Tao3 - (D1 + D2 + Drh1 + Drh2) * (hd2 - hw3) - Dsepw * (hsepw - hw3)) \
     / (h3 - hw4)
D3=(D0*Tao3-Dsepw*(hsepw-hw4)-DJ*(h1rh1-hw4)-(D1+D2+Drh1+Drh2)*(hd2-hw4))/(h3-hw4)*nH
print(D3)

#nH假设为换热器效率，无数值
#前一个D3参考原代码与热平衡图有误差 后一个D3直接根据热平衡图计算，模型参考进展报告2 P13除氧器模型
#后一个D3无除氧器换热效率，不加效率计算结果 D3给值206858 计算值206688
