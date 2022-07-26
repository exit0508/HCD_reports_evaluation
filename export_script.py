import csv
import pprint
import pandas as pd
import glob

list = []
student_num = []
student_list = []
evl = []
early = []
late = []
early_sum = []
late_sum = []
result = []

# パスで指定したファイルの一覧をリスト形式で取得
csv_files = glob.glob('CSV/*.csv')


df = pd.DataFrame(columns = [])

# CSVを1つのファイルに縦方向に結合
for file in csv_files:
    print(file)
    tmp = pd.read_csv(file)
    df = pd.concat([df, tmp], axis=0)

print(df)

#CSVに出力
df.to_csv("CSV/total.csv",index=False)

with open('CSV/total.csv', encoding="utf-8") as f:
    reader = csv.reader(f)  # csvリーダを作成
    list = [row for row in reader]  # 二次元配列を作成

    for i in range(len(list)):
        if i < len(list)-1:
            i += 1
            student_num.append(list[i][0])
            evl.append(int(list[i][1]))
            early.append(int(list[i][2]))
            late.append(int(list[i][3]))
        
    # print('student_num', student_num)
    # print('evl', evl)
    # print('early', early)
    # print('late',late)

f.close()

# -------ここは授業によって変えてください---------
n = 2 # 授業回数
member = 5 #履修者数
# -------ここは授業によって変えてください---------

for m in range(len(list)):
    if m < member:
        temp_early_sum = 0
        temp_late_sum = 0
        temp_evl = 0
        temp_list = []
        sums = []
        print(student_num[m])
        temp_list.append(student_num[m])
        for l in range(n):
            temp_early_sum += early[m+member*l]
            temp_late_sum += late[m+member*l]
            temp_evl = evl[m+member*l]
            print(l+1,'回目評価', temp_evl)
            temp_list.append(temp_evl)

        print('早期提出回数',temp_early_sum, '遅刻提出回数', temp_late_sum)
        sums.append(temp_early_sum)
        sums.append(temp_late_sum)
        student_list = temp_list + sums
        result.append(student_list)

print(result)

with open('result.csv','w', newline='') as f:
    dataWriter = csv.writer(f)
    dataWriter.writerows(result)


