# d.txtからbill.csvを生成するプログラム
menu = {
    'asari':620,
    'niku':590,
    'kamaage':290,
    'bukkake':300,
    'curry':490,
    'kitune':440,
    'kakiage':140,
    'ebiten':160,
    'pumpkin':110,
    'satumaimo':110
}

name = {
'asari':'あさりうどん',
'niku':'肉うどん',
'kamaage':'釜揚げうどん',
'bukkake':'ぶっかけうどん',
'curry':'カレーうどん',
'kitune':'きつねうどん',
'kakiage':'野菜かき揚げ',
'ebiten':'海老天',
'pumpkin':'かぼちゃ天',
'satumaimo':'さつまいも天'
}

dnDir = '/Users/hidenori/Desktop/darknet/'; #darknetディレクトリへのパス(pythonの場合, ホームディレクトリを"~"とするとうまくいかないようです, txt_nameと繋げるため, 必ず最後に"/"をつけてください)
txt_name = 'd.txt'
txt_path = dnDir+txt_name

# 注文商品を表す辞書を作成
with open(txt_path,'r') as f:
    items = f.read()               
items = items.splitlines()  
items_num = {'asari': 0, 'niku': 0 ,'kamaage': 0, 'bukkake': 0, 'curry': 0, 'kitune': 0, 'kakiage': 0, 'ebiten': 0, 'pumpkin': 0, 'satumaimo': 0 }
for item in items:
    items_num[item] += 1

ls = []
for k,v in items_num.items():
    if v == 0:
        ls.append(k)

for x in ls:
    items_num.pop(x)

# 各項目に対し金額計算する関数
def calc_subtotal(k):
        subtotal = menu[k]*items_num[k]
        return subtotal

with open("new.txt","w") as f:
    for k in items_num.keys():
        f.write('{} {}点 ¥{}\n'.format(name[k], items_num[k], calc_subtotal(k))) #改行を入れる(次のブロックでfor文を回すとき, 1行ずつ読み込まれるため)
        
    subtotal_list = []
    for k in items_num.keys():
        subtotal_list.append(calc_subtotal(k))
        total = sum(subtotal_list)
        
    f.write('計  ¥{}'.format(total)) #半角の空白2つ入ってることに注意


import csv
with open("new.txt","r") as f:
    with open("bill.csv", "w") as g:
        writer = csv.writer(g)
        
        for line in f:
            ls = line.split(" ") #各行を空白で分割し, リストに変換
            ls = [s.strip() for s in ls] #\nが邪魔なので取り除く
            writer.writerow(ls)
