# 执行python docker.py 在windows 下无法打印出来
import os

# 检查docker 僵死
def docker_check_is_dead(containerId):
    docker_dead_status=os.popen('docker inspect --format="{{.State.Dead}}" '+containerId)
    if docker_dead_status=='true':
        return True
    else:
        return False

# 检查docker exit
def docker_check_is_exit(containerId):
    docker_exit_status=os.open('docker inspect --format="{{.State.Status}}" '+containerId)
    if docker_exit_status=='exited':
        return True
    else:
        return False

# 所有列表-所有容器
def docker_get_all_containers_list():
    containers_list= os.popen('docker ps -a -q')
    std_lines= containers_list.readlines()
    return [id.replace('\n','') for id in std_lines]  


# 活着列表-列出活着容器
def docker_get_live_containers_list():
    container_live_list = os.popen('docker ps -q')
    std_lines= container_live_list.readlines()
    return [id.replace('\n','') for id in std_lines]  

# 退出列表-列出退出容器的列表
def docker_get_exit_containers_list():
    container_exit_list=os.popen('docker ps -f STATUS=exited -q')
    std_lines=container_exit_list.readlines()
    return [id.replace('\n','') for id in std_lines]  

# 列出镜像列表
def docker_image_list():
    container_live_list = os.popen('docker images -q')
    std_lines= container_live_list.readlines()
    return [id.replace('\n','') for id in std_lines]  

# todo 获取通过id 获取name
def docker_get_name_by_container_id():
    pass

# todo 判断容器列表中，谁被关闭了


# if __name__ == "__main__":
#     docker_get_all_containers_list()