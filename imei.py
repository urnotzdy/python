# 校验imei

# 读取excel中的imei数据
import pandas as pd
import json


def validateImei(imei):
    if len(imei) != 15:
        return 0
    
    sum1 = 0
    # try:
    last = int(imei[14])
    print(last)
    for i in range(14):
        curr = int(imei[i])
        if i % 2 != 0:
            curr = 2 * curr
            if curr > 9:
                curr = (curr / 10) + (curr - 10)
            sum1 = int(sum1 + curr)
        else:
            sum1 = int(sum1 + curr)
    print(sum1)
    # round = sum1 if sum1 % 10 == 0 else ((sum1 / 10 + 1) * 10)
    return int(sum1 + last) % 10 == 0
    # round = sum1 if sum1 % 10 == 0 else 10-sum1 % 10
    # print(int(round))
    # except  Exception:
    #     print(imei)
    # else:
    # return 1 if (round - sum1 == last) else 0


# 读取工作簿和工作簿中的工作表
data_frame = pd.read_excel('/Users/zhangdanyang/Desktop/imei.out.xlsx', usecols=[4])

# 获取imei的列表
imeis = []
for imei_reaons in data_frame.values:
    imei_reson = json.loads(imei_reaons[0])
    imeis.append(imei_reson['evidences']['imei'])

print(validateImei('490154203237518'))
