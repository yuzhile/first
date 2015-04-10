[?1049h[?1h=[1;41r[?12;25h[?12l[?25h[27m[m[H[2J[?25l[41;1H"train.py" 171L, 3909C[1;1H[35mimport[m MySQLdb [33mas[m db
[35mimport[m csv
[35mimport[m numpy [33mas[m np
[33mdef[m [36misBuy[m(itemType):[5;9H[33mif[m [31m4[m==itemType:[6;17H[33mreturn[m [36mTrue[m
[33mdef[m [36mgettimeItem[m(userinfo,timeItems):[8;9H[33mfor[m user [33min[m userinfo:[9;17Htemp = [][10;17H[33mif[m timeItems.has_key(user[-[31m1[m]):[11;25HtimeItems[user[-[31m1[m]].append(user[[31m3[m])[12;17H[33melse[m:[13;25Htemp.append(user[[31m3[m])[14;25HtimeItems[user[-[31m1[m]] = temp
[33mdef[m [36mgetValue[m(weight,action,timeItem,user):[16;9Hpre = timeItem.count(user[[31m3[m])/([31m1.0[m*[36mlen[m(timeItem))[17;9Hlw = [31m31[m - [36mint[m(user[-[31m1[m])


[34m#       print time[m[21;9H[33mreturn[m weight[lw]*action[user[[31m2[m]]*pre
[33mdef[m [36minsertScore[m(scores,item_id,value):[23;9H[33mif[m scores.has_key(item_id):[24;17Hscores[item_id] = scores[item_id] + value[25;9H[33melse[m:[26;17Hscores[item_id] = value

[33mdef[m [36mrateScore[m(user_id,scores,writer):
[34m#       values = scores.values()
#       npvalues = np.array(values)
#       argvalues = np.argsort(-npvalues)
#       print argvalues
#       print scores.keys()[m[34;9Hkeys = scores.keys()[35;9H[33mif[m [31m0[m == [36mlen[m(keys):[36;17H[33mreturn[m[37;9Hi = [31m0[m[38;9Hline = [][39;9H[33mfor[m  key [33min[m keys:[40;17H[33mif[m scores[key] >= [31m10[m:[41;127H1,1[11CTop[1;1H[?12l[?25h[?25l[41;1HType  :quit<Enter>  to exit Vim[41;127H[K[41;127H1,1[11CTop[1;1H[?12l[?25h[?25l[1;40r[1;1H[20M[1;41r[21;25H[36mprint[m user_id,key
[34m#               else:
#                       print values[arg][24;25H#print scores[key][25;9H#       line = [][26;9H#       writer.writerow(scores[key])[27;9H#for i in range(5):[28;9H#       if i >= len(keys):[29;9H#               break[30;9H#       line = [][31;9H#       line.append(user_id)[32;9H#       line.append(keys[argvalues[i]])[33;17H#line.append(values[argvalues[i]])[34;9H#       writer.writerow(line)[35;17H#print line[37;9H#print user_id,keys[argvalues[0]],values[argvalues[0]]  [m
[33mdef[m [36mmax_time[m(x,y):[39;9H[33mif[m x < y:[40;17H[33mreturn[m y[41;1H[K[41;127H21,2-9[8C15%[1;9H[?12l[?25h[?25l[41;1HType  :quit<Enter>  to exit Vim[41;127H[K[41;127H21,2-9[8C15%[1;9H[?12l[?25h[?25l[41;127H[K[41;127H21,2-9[8C15%[1;9H[?12l[?25h[?25l[41;127H[K[41;127H21,2-9[8C15%[1;9H[?12l[?25h[?25l[41;127H[K[41;127H21,2-9[8C15%[1;9H[?12l[?25h[?25l[41;127H[K[41;127H21,2-9[8C15%[1;9H[?12l[?25h[?25l[41;127H[K[41;127H21,2-9[8C15%[1;9H[?12l[?25h[?25l[41;1H[K[41;1H:[?12l[?25h[?25l[41;1H[K[41;127H21,2-9[8C15%[1;9H[?12l[?25h[?25l[41;1HType  :quit<Enter>  to exit Vim[41;127H[K[41;127H21,2-9[8C15%[1;9H[?12l[?25h[?25l[41;127H[K[41;127H21,2-9[8C15%[1;9H[?12l[?25h[?25l[41;127H[K[41;127H21,2-9[8C15%[1;9H[?12l[?25h[?25l[1;40r[1;1H[20M[1;41r[21;9H[33melse[m:[22;17H[33mreturn[m x


[33mdef[m [36mconnectDb[m(command):[26;9H[31m'''
                input:command is the command executed by sql    
                output :the rusult executed by sql,it is curor of the db
        '''[m[30;9Hcxn = db.connect(host=[31m'localhost'[m,db=[31m'albb'[m,user=[31m'root'[m,passwd=[31m'root'[m)[31;9Hcuror = cxn.cursor()[32;9H[34m#result = curor.execute('select * from test_user order by user_id limit 10000')[m[33;9Hresult = curor.execute(command)[34;9H[33mreturn[m curor

[33mdef[m [36mgetScore[m(weight,action,userinfo,buyitem,writer):
[34m#       scores = [i*0 for i in range(10)][m[39;9HtimeItems = {}[41;1H[K[41;127H41,4-25[7C30%[1;25H[?12l[?25h[?25l[1;40r[1;1H[20M[1;41r[21;9Hscores = {}[22;9HgettimeItem(userinfo,timeItems)[23;9Huser_id = [31m0[m[24;9Hitem_keys = buyitem.keys()[25;9H[33mfor[m user [33min[m userinfo:[26;17H[33mif[m user[[31m1[m] [33min[m item_keys:[27;25H[33mcontinue[28;17Helse[m:[29;25HtimeItem = timeItems[user[-[31m1[m]][30;25Hvalue = getValue(weight,action,timeItem,user)[31;25HinsertScore(scores,user[[31m1[m],value)[32;25Huser_id = user[[31m0[m][33;25H[34m#print scores.keys()
#       print scores.keys()[m[35;9HrateScore(user_id,scores,writer)[39;1H[33mdef[m [36mloadParamter[m(paramterfile):[40;9Hparafile = [36mfile[m(paramterfile)[41;127H[K[41;127H61,2-9[8C45%[1;9H[?12l[?25h[?25l[1;40r[1;1H[20M[1;41r[21;9Hreader = csv.reader(parafile)[22;9Hparamter = reader.[36mnext[m()[23;9Hlparamter = [i*[31m0[m [33mfor[m i [33min[m [36mrange[m([36mlen[m(paramter)+[31m1[m)][24;9Hi = [31m0[m[25;9H[33mfor[m l [33min[m paramter:[26;17Hlparamter[i] = [36mint[m(l)[27;17Hi = i+[31m1[m[28;9Hpsum = [36msum[m(lparamter)[29;9Hi = [31m0[m[30;9H[33mfor[m p [33min[m lparamter:[31;17Hlparamter[i] = [31m100[m*(p/(psum*[31m1.0[m))[32;17Hi = i+[31m1[m[33;9Haction = reader.[36mnext[m()[34;9Hlaction = [i*[31m0[m [33mfor[m i [33min[m [36mrange[m([36mlen[m(action)+[31m1[m)][36;9Hi = [31m0[m[37;9H[33mfor[m l [33min[m action:[38;17Hlaction[i] = [36mfloat[m(l)* [31m10.0[m[39;17Hi = i+[31m1[m[41;127H[K[41;127H81,2-9[8C61%[1;9H[?12l[?25h[?25l[41;127H[K[41;1H:[?12l[?25hq[?25l[?12l[?25h[?25l
qall     quit     quitall
:q[?12l[?25h[?1l>[?1049lVim: Caught deadly signal HUP
Vim: Finished.
[41;1H