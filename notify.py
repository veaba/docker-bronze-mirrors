"""
@desc 推送消息的类型
@todo 将推送的日志都异步写到notify.log 日志文件里面去

"""

import requests
import json
from config import post_url
# 动作
ACTIONS={

}
NOTIFY={
    "SOME_ONE_LOGIN":1,     # 有人在登录
    "DOCER_IS_CLOSE":2,     # docker 在关闭
}

# 警告类型1
NOTIFY_TYPE={
    "SOME_ONE_CLOSE_DOCKER":1,              # 有人关闭docler
    "DOCKER_IS_DOWN_FOR_THREE_MINUTES":2,    # docker 宕机 x 分钟
}

""""
@desc d->sss  low->high
"""
LEVEL={
    "SSS":"恭喜您，获得举世震惊（SSSensational）成就！！！",
    "SS":"恭喜您，获得超级虐待狂（SSadistic）", 
    "S":"恭喜您，获得灭绝人性（Savage）记录",
    "A":"恭喜您，获得无法无天（Anarchic）记录",
    "B":"恭喜您，获得残暴（Burtal）记录",
    "C":"恭喜您，烦死了心情！",
    "D":"恭喜您，获得日常搞事记录",
}
"""
@desc 谁关闭了docker 触发
@who  {ip:xxx,name:xxx,time:xxx}
@docker {name:xx,ip:xx,level:xxx}

"""
def notify_who_shut_down_the_docker(who,docker):
    pass


"""
@desc 僵死推送 docker

【A级】：检测到从节点181.2.6.1服务器，容器：3df85570271c (user-server 服务)已退出，状态：dead，影响用户登录业务，威胁级别较高，请负责人@张三 负责处理，建议：kill容器、重启容器、或从network从一处该id，教程：http://url.cn/RAasddfc
【B级】：检测到从节点181.2.6.1服务器，容器：3df85570271c (label-server 服务)已退出，状态：dead，影响会员标签相关业务，威胁级别一般，请负责人@李四 负责处理，建议：kill容器、重启容器、或从network从一处该id，教程：http://url.cn/RAasddfc

"""

def notify_docker_is_dead(id):
    body={
        'msgtype':'text',
        'text':{
            'content':'容器ID：'+id+'僵死',
        }
    }
    res=requests.post(post_url,data=json.dumps(body),headers={'content-type':'application/json'})
    print(res.text)

"""
@desc 退出推送 docker
【A级】：检测到从节点181.2.6.1服务器，容器：3df85570271c (user-server 服务)已退出，状态：dead，影响用户登录业务，威胁级别较高，请负责人@张三 负责处理，建议：kill容器、重启容器、或从network从一处该id，教程：http://url.cn/RAasddfc
【B级】：检测到从节点181.2.6.1服务器，容器：3df85570271c (label-server 服务)已退出，状态：dead，影响会员标签相关业务，威胁级别一般，请负责人@李四 负责处理，建议：kill容器、重启容器、或从network从一处该id，教程：http://url.cn/RAasddfc


"""

def notify_docker_is_exit(id):
    body={
        'msgtype':'text',
        'text':{
            'content':'容器ID：'+id+'退出',
        }
    }
    res=requests.post(post_url,data=json.dumps(body),headers={'content-type':'application/json'})
    print(res.text)

    
    


#  todo

if __name__ == "__main__":
    notify_docker_is_dead('111')