import json
import requests
 
def dingding_409robot(data):
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=80e4251b904f3088f7959d1de12191d9cb7c9a83d8061fa936d3e42e03188106"
    headers = {'content-type': 'application/json'} # 请求头
    r = requests.post(webhook, headers=headers, data=json.dumps(data))
    r.encoding = 'utf-8'
    return (r.text)
 
 
if __name__ == "__main__":
    data = {
        "msgtype": "text",
        "text": { "content":"我是机器人2号，提醒你测试成功" }
        }
    res = dingding_409robot(data)
    print(res) 

