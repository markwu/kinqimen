# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 17:01:10 2020

@author: hooki
"""


ordernum = list(range(1,10))
eight_door = list("休死傷杜中開驚生景")
eight_star = list("蓬芮沖輔禽心柱任英")
eight_gua = list("坎坤震巽中乾兌艮離")

eight_door_orderlist = list("休生傷杜景死驚開")
eight_star_orderlist = list("蓬任沖輔英芮柱心")
eight_gods_yinyang = {"陽遁":list("符蛇陰合勾朱地天"), "陰遁":list("符天地玄白合陰蛇")}


Gan = list("甲乙丙丁戊己庚辛壬癸")
Zhi = list("子丑寅卯辰巳午未申酉戌亥")

hourgang_dict = dict(zip(Gan, list(range(1,11))))
gong_dict = dict(zip(list(range(1,10)), eight_gua))
door_dict = dict(zip(list(range(1,10)), eight_door))
star_dict = dict(zip(list(range(1,10)), eight_star))

jia_hidden_dict = { "甲子":"戊", "甲戌":"己", "甲申":"庚", "甲午":"辛", "甲辰":"壬","甲壬":"癸"}

def new_list_r(olist, o):
    zhihead_code = olist.index(o)
    res1 = []
    for i in range(len(olist)):
        res1.append( olist[zhihead_code % len(olist)])
        zhihead_code = zhihead_code + 1
    return res1

def new_list(olist, o):
    zhihead_code = olist.index(o)
    res1 = []
    for i in range(len(olist)):
        res1.append( olist[zhihead_code % len(olist)])
        zhihead_code = zhihead_code + 1
    return res1


def multi_key_dict_get(d, k):
    for keys, v in d.items():
        if k in keys:
            return v
    return None

def jiazi():
    tiangan = '甲乙丙丁戊己庚辛壬癸'
    dizhi = '子丑寅卯辰巳午未申酉戌亥'
    jiazi = [tiangan[x % len(tiangan)] + dizhi[x % len(dizhi)] for x in range(60)]
    return jiazi

def daykong_shikong(daygangzhi,hourgangzhi):
    liujiashun_dict = {tuple(jiazi()[0:10]):'甲子', tuple(jiazi()[10:20]):"甲戌", tuple(jiazi()[20:30]):"甲申", tuple(jiazi()[30:40]):"甲午", tuple(jiazi()[40:50]):"甲辰",  tuple(jiazi()[50:60]):"甲寅"  }
    guxu = {'甲子':{'孤':'戌亥', '虛':'辰巳'}, '甲戌':{'孤':'申酉', '虛':'寅卯'},'甲申':{'孤':'午未', '虛':'子丑'},'甲午':{'孤':'辰巳', '虛':'戌亥'},'甲辰':{'孤':'寅卯', '虛':'申酉'},'甲寅':{'孤':'子丑', '虛':'午未'} }
    return {"日空":multi_key_dict_get(guxu, multi_key_dict_get(liujiashun_dict, daygangzhi)).get("孤"), "時空":multi_key_dict_get(guxu, multi_key_dict_get(liujiashun_dict, hourgangzhi)).get("孤")}

def qimen_ju_day(daygangzhi):
    ju_day_dict = {"甲":"甲己日", "己":"甲己日", "乙":"乙庚日", "庚":"乙庚日", "丙":"丙辛日", "辛":"丙辛日","丁":"丁壬日", "壬":"丁壬日", "戊":"戊癸日", "癸":"戊癸日"}
    ju_day = ju_day_dict.get(daygangzhi[0])
    return ju_day

def ganzhiyear(year):
    year_gan_code = year%10 -3 +10
    if year_gan_code > 10:
        year_gan_code = year_gan_code -10
    year_zhi_code = year%12 -3 +12
    if year_zhi_code > 12:
        year_zhi_code = year_zhi_code -12
    year_ganzhi = Gan[year_gan_code-1] + Zhi[year_zhi_code-1]
    result = year_ganzhi[0]
    if result == "甲":
        result = jia_hidden_dict.get(year_ganzhi)
    return result, year_ganzhi

def qimen_ju_name(jieqi, daygangzhi):
    find_yuen_dict = {("甲子","乙丑","丙寅","丁卯","戊辰","己卯","庚辰","辛巳","壬午","癸未", "甲午","乙未","丙申","丁酉","戊戌","己酉","庚戌","辛亥","壬子","癸丑"): "上元", ("己巳","庚午","辛未","壬申","癸酉", "甲申","乙酉","丙戌","丁亥","戊子","己亥","庚子","辛丑","壬寅","癸卯", "甲寅","乙卯","丙辰","丁巳","戊午"): "中元", ("甲戌","乙亥","丙子","丁丑","戊寅","己丑","庚寅","辛卯","壬辰","癸巳","甲辰","乙巳","丙午","丁未","戊申","己未","庚申","辛酉","壬戌","癸亥"):  "下元"}
    jieqi_panju = {
    "立春":{"上元":"陰遁八局",  "中元":"陰遁五局", "下元":"陰遁二局"},
    "立冬":{"上元":"陰遁六局",  "中元":"陰遁九局", "下元":"陰遁三局"},
    "立秋":{"上元":"陰遁二局",  "中元":"陰遁五局", "下元":"陰遁八局"},
    "芒種":{"上元":"陽遁六局",  "中元":"陽遁三局", "下元":"陽遁九局"},
    "小寒":{"上元":"陽遁二局",  "中元":"陽遁八局", "下元":"陽遁五局"},
    "大暑":{"上元":"陰遁七局",  "中元":"陰遁一局", "下元":"陰遁四局"},
    "大寒":{"上元":"陽遁三局",  "中元":"陽遁九局", "下元":"陽遁六局"},
    "處暑":{"上元":"陰遁一局",  "中元":"陰遁四局", "下元":"陰遁七局"},
    "秋分":{"上元":"陰遁七局",  "中元":"陰遁一局", "下元":"陰遁四局"},
    "小滿":{"上元":"陽遁五局",  "中元":"陽遁二局", "下元":"陽遁八局"},
    "大雪":{"上元":"陰遁四局",  "中元":"陰遁七局", "下元":"陰遁一局"},
    "驚蟄":{"上元":"陽遁一局",  "中元":"陽遁七局", "下元":"陽遁四局"},
    "春分":{"上元":"陽遁三局",  "中元":"陽遁九局", "下元":"陽遁六局"},
    "穀雨":{"上元":"陽遁五局",  "中元":"陽遁二局", "下元":"陽遁八局"},
    "寒露":{"上元":"陰遁六局",  "中元":"陰遁九局", "下元":"陰遁三局"},
    "冬至":{"上元":"陽遁一局",  "中元":"陽遁七局", "下元":"陽遁四局"},
    "立夏":{"上元":"陽遁四局",  "中元":"陽遁一局", "下元":"陽遁七局"},
    "夏至":{"上元":"陰遁九局",  "中元":"陰遁三局", "下元":"陰遁六局"},
    "白露":{"上元":"陰遁九局",  "中元":"陰遁三局", "下元":"陰遁六局"},
    "霜降":{"上元":"陰遁五局",  "中元":"陰遁八局", "下元":"陰遁二局"},
    "雨水":{"上元":"陽遁九局",  "中元":"陽遁六局", "下元":"陽遁三局"},
    "小暑":{"上元":"陰遁八局",  "中元":"陰遁二局", "下元":"陰遁五局"},
    "清明":{"上元":"陽遁四局",  "中元":"陽遁一局", "下元":"陽遁七局"},
    "小雪":{"上元":"陰遁五局",  "中元":"陰遁八局", "下元":"陰遁二局"}}
    find_yuen = multi_key_dict_get(find_yuen_dict, daygangzhi)
    findju = jieqi_panju.get(jieqi).get(find_yuen)
    return findju

def shun(gangzhi):
    shunlist = {0:"戊", 10:"己", 8:"庚", 6:"辛", 4:"壬", 2:"癸"}
    gangzhi_gang = dict(zip(Gan, list(range(1,11))))
    gangzhi_zhi = dict(zip(Zhi, list(range(1,13))))
    gang = gangzhi_gang.get(gangzhi[0])
    zhi = gangzhi_zhi.get(gangzhi[1])
    shun_value =  zhi - gang
    if shun_value < 0:
        shun_value = shun_value+12
    return shunlist.get(shun_value)


def zhifu_zhishi(jieqi, daygangzhi, hourgangzhi):
    qimen_ju = qimen_ju_name(jieqi, daygangzhi)
    shun1 = shun(hourgangzhi)
    kok_num_dict = dict(zip(list("一二三四五六七八九"), list(range(1,10))))
    shun_num_dict = dict(zip(list("戊己庚辛壬癸"), list(range(1,7))))
    sanqiliuyi_dict = {"乙":9, "戊":1, "己":2, "庚":3, "辛":4, "壬":5, "癸":6, "丙":8, "丁":7}
    hidden_jia = {'甲子':'戊', '甲戌':'己','甲申':'庚','甲午':'辛','甲辰':'壬','甲寅':'癸' }
    shun_num = shun_num_dict.get(shun1)
    kok_num = kok_num_dict.get(qimen_ju[2])
    if hourgangzhi[0] == "甲":
        hourgang_num = 1
        new_hour_code = hidden_jia.get(hourgangzhi)
        hourgangzhi_code =  multi_key_dict_get(sanqiliuyi_dict, new_hour_code)
    elif hourgangzhi[0] != "甲":
        hourgang_num = hourgang_dict.get(hourgangzhi[0])
        hourgangzhi_code =  multi_key_dict_get(sanqiliuyi_dict, hourgangzhi[0])
    
    if qimen_ju[0] == "陽":
        zhifu_zhishi_num = kok_num + shun_num -1
        if zhifu_zhishi_num > 9 :
            zhifu_zhishi_num = zhifu_zhishi_num - 9
           
        if hourgangzhi[0] == "甲":
            zhifu_lokgong = zhifu_zhishi_num + hourgang_num  - 1
        elif hourgangzhi[0] != "甲":
            zhifu_lokgong = hourgangzhi_code  + kok_num - 1
            if zhifu_lokgong > 9:
                zhifu_lokgong = zhifu_lokgong -9
            elif zhifu_lokgong < 0:
                zhifu_lokgong = zhifu_lokgong +9
        
        zhishi_lokgong = zhifu_zhishi_num + hourgang_num - 1
        if zhishi_lokgong > 9:
            zhishi_lokgong = zhishi_lokgong-9
        elif zhishi_lokgong > 9:
            zhishi_lokgong = zhishi_lokgong-9

    elif qimen_ju[0] == "陰":
        zhifu_zhishi_num = 1 + kok_num - shun_num
        if zhifu_zhishi_num > 9 :
            zhifu_zhishi_num = zhifu_zhishi_num - 9
        
        if hourgangzhi[0] == "甲":
            zhifu_lokgong = zhifu_zhishi_num + hourgang_num - 1
            zhishi_lokgong = zhifu_zhishi_num + hourgang_num - 1
        elif hourgangzhi[0] != "甲":
            zhifu_lokgong = 1 + kok_num - hourgangzhi_code
            zhishi_lokgong = zhifu_zhishi_num + hourgangzhi_code - 1
            if zhifu_lokgong > 9:
                zhifu_lokgong = zhifu_lokgong -9
            elif zhifu_lokgong < 0:
                zhifu_lokgong = zhifu_lokgong +9
        
        if zhishi_lokgong > 9:
            zhishi_lokgong = zhishi_lokgong-9
        elif zhishi_lokgong > 9:
            zhishi_lokgong = zhishi_lokgong-9
    zhifugong = gong_dict.get(zhifu_lokgong)
    zhishigong = gong_dict.get(zhishi_lokgong)
    if gong_dict.get(zhifu_lokgong) == "中":
        zhifugong = zhishigong
    result = [{"值符":[star_dict.get(zhifu_zhishi_num), zhifugong ], "直使":[door_dict.get(zhifu_zhishi_num), zhishigong ]}]
    return result

def qimen(jieqi, daygangzhi, hourgangzhi):
    qimen_ju = qimen_ju_name(jieqi, daygangzhi)
    zhifu_zhishi1 = zhifu_zhishi(jieqi, daygangzhi, hourgangzhi)
    zhifu_lokgong_o = zhifu_zhishi(jieqi, daygangzhi, hourgangzhi)[0].get("值符")[0]
    zhifu_lokgong_g = zhifu_zhishi(jieqi, daygangzhi, hourgangzhi)[0].get("值符")[1]
    zhishi_lokgong_o = zhifu_zhishi(jieqi, daygangzhi, hourgangzhi)[0].get("直使")[0]
    zhishi_lokgong_g = zhifu_zhishi(jieqi, daygangzhi, hourgangzhi)[0].get("直使")[1]
    star_new_dict = dict(zip(new_list(eight_gua,zhifu_lokgong_g), new_list(eight_star, zhifu_lokgong_o)))
    door_new_dict = dict(zip(new_list(eight_gua,zhishi_lokgong_g), new_list(eight_door, zhishi_lokgong_o)))
    if qimen_ju[0] == "陽":
        god_new_dict = dict(zip(new_list(list("兌乾坎艮震巽離坤"), zhifu_lokgong_g),eight_gods_yinyang.get("陽遁")))
        yang_dun_lei = dict(zip(list("一二三四五六七八九"), list("乙丙丁癸壬辛庚己戊")))
        lei_gong = yang_dun_lei.get(qimen_ju[2])
        earth_pan = dict(zip(new_list_r(eight_gua, "離"), new_list(list("戊己庚辛壬癸丁丙乙"), lei_gong)))
    elif qimen_ju[0] == "陰":
        god_new_dict = dict(zip(new_list(list("兌乾坎艮震巽離坤"), zhifu_lokgong_g) ,eight_gods_yinyang.get("陰遁")))
        yin_dun_lei = dict(zip(list("一二三四五六七八九"), list("己庚辛壬癸丁丙乙戊")))
        lei_gong = yin_dun_lei.get(qimen_ju[2])
        earth_pan = dict(zip(new_list_r(eight_gua, "離"), new_list(list("戊乙丙丁癸壬辛庚己"), lei_gong)))
    earth_pan_list = list(earth_pan.values())
    del earth_pan_list[5]
    sky_pan = dict(zip(new_list(list("坎艮震巽離坤兌乾"), zhifu_lokgong_g),  new_list([earth_pan.get(i) for i in list("坎艮震巽離坤兌乾")], shun(hourgangzhi))))
    return  {"排局": [qimen_ju, jieqi, daygangzhi+"日", hourgangzhi+"時"], "孤虛":daykong_shikong(daygangzhi,hourgangzhi) , "值符":zhifu_zhishi1[0]["值符"], "直使":zhifu_zhishi1[0]["直使"], "天地盤":{ "地盤":earth_pan, "天盤":sky_pan}, "八星":star_new_dict, "八門":door_new_dict, "八神":god_new_dict}

#print(qimen("小雪", "乙未", "甲申"))
#print(qimen("小寒", "甲寅", "壬申"))
#print(shun( "辛未"))