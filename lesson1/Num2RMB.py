

# 9999 9999 9999 . 99
# 玖仟玖佰玖拾玖 亿 玖仟玖佰玖拾玖 万 玖仟玖佰玖拾玖 圆 玖角玖分

level = {
    2:'亿',
    1:'万',
    0:''
}

desc = {
    3:'仟',
    2:'佰',
    1:'拾',
    0:''
}

desc2 = {
    0:'角',
    1:'分',
    2:' 我擦能不能别算这么小的单位,老子不知道单位了!',
    3:' 我擦能不能别算这么小的单位,老子不知道单位了!',
    4:' 我擦能不能别算这么小的单位,老子不知道单位了!',
    5:' 我擦能不能别算这么小的单位,老子不知道单位了!',
    6:' 我擦能不能别算这么小的单位,老子不知道单位了!',
    7:' 我擦能不能别算这么小的单位,老子不知道单位了!'
}

num_names = {
    '0':'零',
    '1':'壹',
    '2':'贰',
    '3':'叁',
    '4':'肆',
    '5':'伍',
    '6':'陆',
    '7':'柒',
    '8':'捌',
    '9':'玖',
}

def getWei(len):
    lev = len/4
    lev_name = level[lev]
    dec = len%4
    dec_name = desc[dec]
    pass

def getDec(index):

    pass

def parse(num):
    name = num_names[int(num) % 10]
    print(name)
    pass

def removeHeadEmpty(num):
    if (num.startswith('0')):
        num = num[1:]
        print(num)
        return removeHeadEmpty(num)
    else:
        return num

if __name__ == '__main__':
    stringnum = input('请输入价格:')
    try:
        num = float(stringnum)
        nums = stringnum.split('.')
        zhengs = nums[0]
        zhengs = str(removeHeadEmpty(zhengs))

        # 逆顺序加字
        reVal = reversed(zhengs)
        it = iter(reVal)
        result = '圆'
        lastItem = ''
        lastIndex = 0
        for index, item in enumerate(it):
            # item = reVal[index]
            if index/4 != 0 and index % 4 == 0:
                result = level[index / 4] + result

            if lastItem == '0' and lastIndex != 0:
                result = num_names[lastItem] + result

            lastItem = item
            lastIndex = index
            if item == '0':
                continue


            result = desc[index % 4] + result
            result = num_names[item] + result

        print(result)
        lastItem = ''
        lastIndex = 0
        if len(nums) > 1:
            xiao = nums[1]
            it2 = iter(xiao)
            print(xiao)
            for index, item in enumerate(it2):
                if lastItem == '0' and lastIndex != 0:
                    result = num_names[lastItem] + result
                lastItem = item
                lastIndex = index
                if item == '0':
                    continue
                result += num_names[item]
                print(index)
                result += desc2[index]

        print(result)
    except ValueError:
        print('你逗我呢?')

