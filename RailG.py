
import matplotlib.pyplot as plt



print("Введите серию локомотива")
seria=input()
print("Введите тип пути")
railtype=input()
nagruzkaos=int(input("Введите среднюю нагрузку на ось"))
Ph=2677.21
Vspeed = list(range(0, 101, 5))

ВЛ10=[613000,534000,514000,502000,492000,483000,475000,467000,460000,451000,446000,441000,396000,318000,265000,226000,196000,172000,148000,130000,112000]
ВЛ80К=[649000,607000,565000,536000,527000,518000,502000,496000,490000,485000,480000,470000,466000,456000,375000,294000,256000,219000,195000,171000,153000,136000]
Э5К=[339000,300000,292000,280000,274000,268000,263000,258000,254000,249000,246000,242000,239000,235000,159000,125000,117000,100000,92000,80000,76000]
П2ЭС5К=[678000,630000,584000,560000,549000,530000,526000,515000,508000,500000,492000,480000,477000,400000,319000,270000,234000,200000,185000,160000,152000]
П3ЭС5К=[1017000,900000,877000,840000,823000,800000,789000,770000,762000,755000,738000,725000,716000,600000,478000,400000,350000,300000,277000,240000,228000]
ВЛ82=[640000,581000,552000,533000,518000,507000,497000,488000,479000,472000,463000,455000,452000,347000,272000,220000,183000,150000,133000,100000,95000]
П2ТЭ10Л=[744000,661000,603000,561000,529000,520000,447000,350000,321000,283000,245000,223000,196000,188000,175000,165000,156000,147000,137000,127000,119000]
П3ТЭ10М=[1194000,1083000,1001000,939000,865000,732000,670000,525000,482000,426000,368000,335000,294000,283000,263000,248000,234000,220000,205000,191000,179000]
П4ТЭ10С=[1594000,1445000,1336000,1253000,1154000,992000,895000,700000,643000,568000,491000,447000,392000,377000,351000,331000,312000,294000,274000,255000,239000]
П2ТЭ116У=[803000,730000,670000,630000,600000,570000,503000,435000,379000,335000,301000,273000,265000,235000,214000,200000,187000,179000,167000,162000,151000]
П2ТЭ25К=[797000,723000,668000,626000,594000,567000,484000,414000,360000,319000,287000,259000,242000,226000,211000,200000,186000,174000,164000,155000,147000]
П2М62=[697000,620000,566000,525000,382000,320000,278000,248000,209000,193000,170000,150000,143000,130000,122000,115000,104000,95000,89000,80000,76000]



if seria== "ВЛ10":
    sseria=ВЛ10
elif seria =="ВЛ80К":
    sseria=ВЛ80К
elif seria=="Э5К":
    sseria=Э5К
elif seria=="П2ЭС5К":
    sseria =П2ЭС5К
elif seria=="П3ЭС5К":
    sseria =П3ЭС5К
elif seria=="ВЛ82":
    sseria =ВЛ82
elif seria=="П2ТЭ10Л":
    sseria =П2ТЭ10Л
elif seria=="П3ТЭ10М":
    sseria =П3ТЭ10М
elif seria=="П4ТЭ10С":
    sseria =П4ТЭ10С
elif seria=="П2ТЭ116У":
    sseria =П2ТЭ116У
elif seria=="П2ТЭ25К":
    sseria =П2ТЭ25К
elif seria=="П2М62":
    sseria =П2М62
if railtype=="1":
    W01list = []
    W011list=[]
    Wo1list=[]
    W0111list=[]
    Wobsh1list=[]
    Ftyag1list=[]
    Ftyag11list=[]
    Wox1list=[]
    Wox11list=[]
    Woxobsh1list=[]
    sopr1list=[]
    Fi1list=[]
    Bt21list=[]
    auskorlist1=[]
    vtplusdtlist1=[]
    timelist1=[]
    xtplusdtlist1=[]
    avibeg1list=[]
    vvibeg1list=[]
    svibeglist1=[]
    atyaglist1=[]
    vtyaglist1=[]
    styagalist1=[]
    atormozlist1=[]
    vtormozlist1=[]
    stormozlist1=[]
    o5btpluswxlist1=[]
    for i in Vspeed:
        W01=1.9+0.01*i+0.0003*i*i
        W01list.append(W01)
    for i in Vspeed:
        W011=0.53+(3.6+0.08*i+0.0028*i**2)/nagruzkaos
        W011list.append(W011)
    for i in W01list:
        Wo1=i*Ph
        Wo1list.append(Wo1)
    for i in W011list:
        W0111=i*37422.18
        W0111list.append(W0111)
    for x,y in zip(W01list,W0111list):
        Wobsh1=x+y
        Wobsh1list.append(Wobsh1)
    for x,y in zip(sseria,Wobsh1list):
        Ftyag1=x-y
        Ftyag1list.append(Ftyag1)
    for x,y in zip(sseria,Wobsh1list):
        Ftyag11=(x+y)/(37670)
        Ftyag11list.append(Ftyag11)
    for i in Vspeed:
        Wox1=2.4+0.011*i+0.0003*i**2
        Wox1list.append(Wox1)
    for i in Wox1list:
        Wox11=i*Ph
        Wox11list.append(Wox11)
    for x,y in zip(Wox11list,W0111list):
        Woxobsh1 = x + y
        Woxobsh1list.append(Woxobsh1)
    for i in Wox11list:
        sopr1=i/(2677+37422)
        sopr1list.append(sopr1)
    for i in Vspeed:
        Fi1=0.27*(i+100)/(5*i+100)
        Fi1list.append(Fi1)
    for i in Fi1list:
        Bt21=(i*330)/2
        Bt21list.append(Bt21)
    for x,y in zip (Bt21list,sopr1list):
        o5btpluswx=x+y
        o5btpluswxlist1.append(o5btpluswx)
    for i in Ftyag11list:
        auskor1=i*12.2
        auskorlist1.append(auskor1)
    for x,y in zip(auskorlist1,Vspeed):
        vtplusdt1=y+x*0.002778
        vtplusdtlist1.append(vtplusdt1)
    vtplusdtlist1.insert(0,0)
    for i in range(0,51):
        time=i*0.002778
        timelist1.append(time)
    for i in range(len(vtplusdtlist1)):
        if i==0:
            xtplusdtlist1.append(0)
        else:
            auskorlist1.append(0)
            xtplusdt1=xtplusdtlist1[i-1]+vtplusdtlist1[i]*0.002778+(0.002778**2/2)*auskorlist1[i]
            xtplusdtlist1.append(xtplusdt1)
     # VIBEGGGGG
    schetlist1=[]
    vchetlist1=[]
    avibeg1=(sopr1list[18]+3.00043)*12.2
    avibeg2=(sopr1list[17]+3-1.00043)*12.2
    avibeg3=(sopr1list[16]+3-1.00043)*12.2
    avibeg4 = (sopr1list[15] +3- 1.00043) * 12.2
    avibeg5 = (sopr1list[14] + 3 - 1.00043) * 12.2
    avibeg6 = (sopr1list[13] + 3 - 1.00043) * 12.2
    avibeg1list+=[avibeg1,avibeg2,avibeg3,avibeg4,avibeg5,avibeg6,]
    vchet1=Vspeed[19]+avibeg1*0.00278
    vchet2=Vspeed[13]+avibeg2*0.00278



    vvs1=Vspeed[18]+avibeg1list[0]*0.002778
    vvs2=Vspeed[17]+avibeg1list[1]*0.002778
    vvs3=Vspeed[16]+avibeg1list[2]*0.002778
    vvs4=Vspeed[15]+avibeg1list[3]*0.002778
    vvs5 = Vspeed[14] + avibeg1list[4] * 0.002778
    vvs6 = Vspeed[13] + avibeg1list[5] * 0.002778
    vvibeg1list+=[vvs1,vvs2,vvs3,vvs4,vvs5,vvs6,]

    svibeg1=xtplusdtlist1[17]+vtplusdtlist1[17]*0.002778+(0.002778*0.002778/2)*avibeg1
    svibeg2=svibeg1+vvs1*0.002778+(0.002778*0.002778/2)*avibeg2
    svibeg3=svibeg2+vvs2*0.002778+(0.002778*0.002778/2)*avibeg3
    svibeg4=svibeg3+vvs3*0.002778+(0.002778*0.002778/2)*avibeg4
    svibeg5 = svibeg4 + vvs4 * 0.002778 + (0.002778 * 0.002778 / 2) * avibeg5
    svibeg6 = svibeg5 + vvs5 * 0.002778 + (0.002778 * 0.002778 / 2) * avibeg6
    svibeglist1+=[svibeg1,svibeg2,svibeg3,svibeg4,svibeg5,svibeg6,]
        #VIBEGGGGGGGGGGG

        #TYAGAAAAA№
    for i in Ftyag11list[13:19]:
        atyag=(i+3)*12.2
        atyaglist1.append(atyag)
    for x,y in zip(Vspeed[13:19],atyaglist1):
        vtyag=x+y*0.002778
        vtyaglist1.append(vtyag)
    styaga1 = svibeglist1[4] + vvibeg1list[4] * 0.002778 + (0.002778 * 0.002778 / 2) * atyaglist1[0]
    styaga2 = styaga1 + vtyaglist1[0] * 0.002778 + (0.002778 * 0.002778 / 2) * atyaglist1[1]
    styaga3 = styaga2 + vtyaglist1[1] * 0.002778 + (0.002778 * 0.002778 / 2) * atyaglist1[2]
    styaga4 = styaga3 + vtyaglist1[2] * 0.002778 + (0.002778 * 0.002778 / 2) * atyaglist1[3]
    styaga5 = styaga4 + vtyaglist1[3] * 0.002778 + (0.002778 * 0.002778 / 2) * atyaglist1[4]
    styaga6 = styaga5 + vtyaglist1[4] * 0.002778 + (0.002778 * 0.002778 / 2) * atyaglist1[5]
    styagalist1 += [styaga1,styaga2,styaga3,styaga4,styaga5,styaga6 ]
    vchetlist1 += [vtyaglist1[-1], vchet2]
        #TYAGAAAAA

        #TORMOZ
    stormozlist11=[]
    for i in o5btpluswxlist1:
        atormoz=i*12.2
        atormozlist1.append(atormoz)
    for x,y in zip(Vspeed,atormozlist1):
        vtormoz=x+y*0.002778
        vtormozlist1.append(vtormoz)
    srsr = styaga6+vtormozlist1[18]*0.002778+(0.002778**2/2)*atormozlist1[18]
    srsr2 = srsr + vvs1 * 0.002778 + (0.002778 ** 2 / 2) * avibeg1
    atormozlist1.insert(0,0)
    stormozlist1.append(srsr2)
    auskorlist1.append(0)
    vtormozlist1.insert(0,0)
    for i in range(len(vtormozlist1)):
        stormoz = stormozlist1[i] + vtormozlist1[i] * 0.002778 + (0.002778 ** 2 / 2) * atormozlist1[i]
        stormozlist1.append(stormoz)
    stormozlist11 += [styaga6, srsr2]
        #TORMOZ


    stormozgraph1=stormozlist1[::-1]
    vtormozlist1graph=vtormozlist1[::-1]
    vtplusdtlist1.pop(0)
    Ftyaggraph1=[-x for x in Ftyag11list]
    xlist=list(range (len(sopr1list)))
    fig, axs=plt.subplots(3)
    axs[1].set_title("Кривая скорости")
    axs[1].plot(xtplusdtlist1[0:19],vtplusdtlist1[0:19],label="tyaga")
    axs[1].plot(svibeglist1,vvibeg1list,label="vibeg")
    axs[1].grid()
    axs[1].plot(styagalist1,vtyaglist1)
    axs[1].plot(stormozlist11,vchetlist1)
    axs[1].plot(stormozlist1[1:16],vtormozlist1graph[7:22])


    axs[0].set_title("Диаграмма равнодействующих сил")
    axs[0].plot(Ftyaggraph1,xlist,label="fk - wо, Н/кН (тяга)")
    axs[0].plot(sopr1list,xlist,label="wох, Н/кН (выбег)")
    axs[0].plot(Bt21list,xlist, label="0,5bТ + wох, Н/кН (торм.)")
    axs[0].grid()
    axs[0].legend()

    axs[2].set_title("Кривая времени")
    axs[2].plot(xtplusdtlist1[0:4],timelist1[0:4],label="0")
    axs[2].plot(xtplusdtlist1[3:8],timelist1[3:8],label="1")
    axs[2].plot(xtplusdtlist1[7:12], timelist1[7:12],label="2")
    axs[2].plot(xtplusdtlist1[11:16], timelist1[11:16],label="3")
    axs[2].plot(xtplusdtlist1[15:21], timelist1[15:21],label="4")
    axs[2].grid()



    plt.show()
else:
    W01list = []
    W011list = []
    Wo1list = []
    W0111list = []
    Wobsh1list = []
    Ftyag1list = []
    Ftyag11list = []
    Wox1list = []
    Wox11list = []
    Woxobsh1list = []
    sopr1list = []
    Fi1list = []
    Bt21list = []
    auskorlist1 = []
    vtplusdtlist1 = []
    timelist1 = []
    xtplusdtlist1 = []
    avibeg1list = []
    vvibeg1list = []
    svibeglist1 = []
    atyaglist1 = []
    vtyaglist1 = []
    styagalist1 = []
    atormozlist1 = []
    vtormozlist1 = []
    stormozlist1 = []
    o5btpluswxlist1 = []
    for i in Vspeed:
        W01 = 1.9 + 0.008 * i + 0.00024 * i * i
        W01list.append(W01)
    for i in Vspeed:
        W011 = 0.53 + (3.5 + 0.074 * i + 0.0022 * i ** 2) / nagruzkaos
        W011list.append(W011)
    for i in W01list:
        Wo1 = i * Ph
        Wo1list.append(Wo1)
    for i in W011list:
        W0111 = i * 37422.18
        W0111list.append(W0111)
    for x, y in zip(W01list, W0111list):
        Wobsh1 = x + y
        Wobsh1list.append(Wobsh1)
    for x, y in zip(sseria, Wobsh1list):
        Ftyag1 = x - y
        Ftyag1list.append(Ftyag1)
    for x, y in zip(sseria, Wobsh1list):
        Ftyag11 = (x + y) / (37670)
        Ftyag11list.append(Ftyag11)
    for i in Vspeed:
        Wox1 = 2.4 + 0.009 * i + 0.0003 * i ** 2
        Wox1list.append(Wox1)
    for i in Wox1list:
        Wox11 = i * Ph
        Wox11list.append(Wox11)
    for x, y in zip(Wox11list, W0111list):
        Woxobsh1 = x + y
        Woxobsh1list.append(Woxobsh1)
    for i in Wox11list:
        sopr1 = i / (2677 + 37422)
        sopr1list.append(sopr1)
    for i in Vspeed:
        Fi1 = 0.27 * (i + 100) / (5 * i + 100)
        Fi1list.append(Fi1)
    for i in Fi1list:
        Bt21 = (i * 330) / 2
        Bt21list.append(Bt21)
    for x, y in zip(Bt21list, sopr1list):
        o5btpluswx = x + y
        o5btpluswxlist1.append(o5btpluswx)
    for i in Ftyag11list:
        auskor1 = i * 12.2
        auskorlist1.append(auskor1)
    for x, y in zip(auskorlist1, Vspeed):
        vtplusdt1 = y + x * 0.002778
        vtplusdtlist1.append(vtplusdt1)
    vtplusdtlist1.insert(0, 0)
    for i in range(0, 51):
        time = i * 0.002778
        timelist1.append(time)
    for i in range(len(vtplusdtlist1)):
        if i == 0:
            xtplusdtlist1.append(0)
        else:
            auskorlist1.append(0)
            xtplusdt1 = xtplusdtlist1[i - 1] + vtplusdtlist1[i] * 0.002778 + (0.002778 ** 2 / 2) * auskorlist1[i]
            xtplusdtlist1.append(xtplusdt1)
    # VIBEGGGGG
    schetlist1 = []
    vchetlist1 = []
    avibeg1 = (sopr1list[18] + 3.00043) * 12.2
    avibeg2 = (sopr1list[17] + 3 - 1.00043) * 12.2
    avibeg3 = (sopr1list[16] + 3 - 1.00043) * 12.2
    avibeg4 = (sopr1list[15] + 3 - 1.00043) * 12.2
    avibeg5 = (sopr1list[14] + 3 - 1.00043) * 12.2
    avibeg6 = (sopr1list[13] + 3 - 1.00043) * 12.2
    avibeg1list += [avibeg1, avibeg2, avibeg3, avibeg4, avibeg5, avibeg6, ]
    vchet1 = Vspeed[19] + avibeg1 * 0.00278
    vchet2 = Vspeed[13] + avibeg2 * 0.00278

    vvs1 = Vspeed[18] + avibeg1list[0] * 0.002778
    vvs2 = Vspeed[17] + avibeg1list[1] * 0.002778
    vvs3 = Vspeed[16] + avibeg1list[2] * 0.002778
    vvs4 = Vspeed[15] + avibeg1list[3] * 0.002778
    vvs5 = Vspeed[14] + avibeg1list[4] * 0.002778
    vvs6 = Vspeed[13] + avibeg1list[5] * 0.002778
    vvibeg1list += [vvs1, vvs2, vvs3, vvs4, vvs5, vvs6, ]

    svibeg1 = xtplusdtlist1[17] + vtplusdtlist1[17] * 0.002778 + (0.002778 * 0.002778 / 2) * avibeg1
    svibeg2 = svibeg1 + vvs1 * 0.002778 + (0.002778 * 0.002778 / 2) * avibeg2
    svibeg3 = svibeg2 + vvs2 * 0.002778 + (0.002778 * 0.002778 / 2) * avibeg3
    svibeg4 = svibeg3 + vvs3 * 0.002778 + (0.002778 * 0.002778 / 2) * avibeg4
    svibeg5 = svibeg4 + vvs4 * 0.002778 + (0.002778 * 0.002778 / 2) * avibeg5
    svibeg6 = svibeg5 + vvs5 * 0.002778 + (0.002778 * 0.002778 / 2) * avibeg6
    svibeglist1 += [svibeg1, svibeg2, svibeg3, svibeg4, svibeg5, svibeg6, ]
    # VIBEGGGGGGGGGGG

    # TYAGAAAAA№
    for i in Ftyag11list[13:19]:
        atyag = (i + 3) * 12.2
        atyaglist1.append(atyag)
    for x, y in zip(Vspeed[13:19], atyaglist1):
        vtyag = x + y * 0.002778
        vtyaglist1.append(vtyag)
    styaga1 = svibeglist1[4] + vvibeg1list[4] * 0.002778 + (0.002778 * 0.002778 / 2) * atyaglist1[0]
    styaga2 = styaga1 + vtyaglist1[0] * 0.002778 + (0.002778 * 0.002778 / 2) * atyaglist1[1]
    styaga3 = styaga2 + vtyaglist1[1] * 0.002778 + (0.002778 * 0.002778 / 2) * atyaglist1[2]
    styaga4 = styaga3 + vtyaglist1[2] * 0.002778 + (0.002778 * 0.002778 / 2) * atyaglist1[3]
    styaga5 = styaga4 + vtyaglist1[3] * 0.002778 + (0.002778 * 0.002778 / 2) * atyaglist1[4]
    styaga6 = styaga5 + vtyaglist1[4] * 0.002778 + (0.002778 * 0.002778 / 2) * atyaglist1[5]
    styagalist1 += [styaga1, styaga2, styaga3, styaga4, styaga5, styaga6]
    vchetlist1 += [vtyaglist1[-1], vchet2]
    # TYAGAAAAA


    # TORMOZ
    stormozlist11 = []
    for i in o5btpluswxlist1:
        atormoz = i * 12.2
        atormozlist1.append(atormoz)
    for x, y in zip(Vspeed, atormozlist1):
        vtormoz = x + y * 0.002778
        vtormozlist1.append(vtormoz)
    srsr = styaga6 + vtormozlist1[18] * 0.002778 + (0.002778 ** 2 / 2) * atormozlist1[18]
    srsr2 = srsr + vvs1 * 0.002778 + (0.002778 ** 2 / 2) * avibeg1
    atormozlist1.insert(0, 0)
    stormozlist1.append(srsr2)
    auskorlist1.append(0)
    vtormozlist1.insert(0, 0)
    for i in range(len(vtormozlist1)):
        stormoz = stormozlist1[i] + vtormozlist1[i] * 0.002778 + (0.002778 ** 2 / 2) * atormozlist1[i]
        stormozlist1.append(stormoz)
    stormozlist11 += [styaga6, srsr2]


    # TORMOZ
    stormozgraph1 = stormozlist1[::-1]
    vtormozlist1graph = vtormozlist1[::-1]
    vtplusdtlist1.pop(0)
    Ftyaggraph1 = [-x for x in Ftyag11list]
    xlist = list(range(len(sopr1list)))
    fig, axs = plt.subplots(3)
    axs[1].set_title("Кривая скорости")
    axs[1].plot(xtplusdtlist1[0:19], vtplusdtlist1[0:19], label="tyaga")
    axs[1].plot(svibeglist1, vvibeg1list, label="vibeg")
    axs[1].grid()
    axs[1].plot(styagalist1, vtyaglist1)
    axs[1].plot(stormozlist11, vchetlist1)
    axs[1].plot(stormozlist1[1:16], vtormozlist1graph[7:22])

    axs[0].set_title("Диаграмма равнодействующих сил")
    axs[0].plot(Ftyaggraph1, xlist, label="fk - wо, Н/кН (тяга)")
    axs[0].plot(sopr1list, xlist, label="wох, Н/кН (выбег)")
    axs[0].plot(Bt21list, xlist, label="0,5bТ + wох, Н/кН (торм.)")
    axs[0].grid()
    axs[0].legend()

    axs[2].set_title("Кривая времени")
    axs[2].plot(xtplusdtlist1[0:4], timelist1[0:4], label="0")
    axs[2].plot(xtplusdtlist1[3:8], timelist1[3:8], label="1")
    axs[2].plot(xtplusdtlist1[7:12], timelist1[7:12], label="2")
    axs[2].plot(xtplusdtlist1[11:16], timelist1[11:16], label="3")
    axs[2].plot(xtplusdtlist1[15:21], timelist1[15:21], label="4")
    axs[2].grid()

    plt.show()