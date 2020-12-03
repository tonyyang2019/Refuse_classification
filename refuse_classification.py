# encoding:utf-8
import requests
import base64

def ljfl(x): #垃圾分类函数
    if x==0:
        y='可回收垃圾'
    elif x==1:
        y = '有害垃圾'
    elif x==2:
        y = '厨余(湿)垃圾'
    elif x==3:
        y = '其他(干)垃圾'
    return y

def classification(Img):
    data={}
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={you id}&client_secret={you key}'
    response = requests.get(host)
    if response:
        key_list = response.json()

    # 通用物体识别 https://ai.baidu.com/tech/imagerecognition/general
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
    # 二进制方式打开图片文件
    f = open(Img, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = key_list['access_token']
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        result = response.json()['result']
        # 获取api结果，提取准确率最高的结果
    max_result = result[1]
    #print(max_result)
    data['物品名称'] = max_result['keyword']
    data['准确率'] = max_result['score']
    print('物品名称：', max_result['keyword'])
    print('准确率：', max_result['score'])

    # 垃圾分类 https://www.tianapi.com/apiview/97#viewerrorcode
    Result = max_result['keyword']
    host = 'http://api.tianapi.com/txapi/lajifenlei/index?key={you key}'
    part = requests.get(host + Result)
    if response:
        a = part.json()['newslist'][0]
    #print(a)
    data['垃圾类别'] = ljfl(a['type'])
    data['分类解释'] = a['explain']
    data['投放提示'] = a['tip']
    #print('垃圾类别：', ljfl(a['type']))
    #print('分类解释:', a['explain'])
    #print('投放提示:', a['tip'])
    return data


