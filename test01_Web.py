from automation_framework.Web import Web
import element.element_test01 as el
import action.action_test01 as action
from support.support_module import dict_list_to_csv
from __chromedriver_autoinstall__ import chrome_driver_install_path
from support.support_module import json_load
import os, time

#/Applications//Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9223 --user-data-dir="~/Chrome/Chrome-user01"

# 설정 
base_path = os.path.dirname(os.path.abspath(__file__))
chrome_driver_path = chrome_driver_install_path()
config_file_path = f'{base_path}/conf/test01.json'
clientinfo = json_load(config_file_path, none_data={})
clientinfo['executable_path'] = chrome_driver_path
clientinfo['screenshot_path'] = f'{base_path}/screenshot'
clientinfo['log_file_path'] = f'{base_path}/log/{time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))}.txt'

# 셋팅
client = Web(clientinfo=clientinfo)


# 자동화 시작

# 페이지 이동
search_url = el.google_search_url({'q':'삼쩜삼','tbm':'nws','tbs':'qdr:w'})
client.driver.get(search_url)

# 검색 내용 조회
#item = action.get_google_search_item(client, item_index=0)
items = action.get_google_search_items(client)
for item_index in range(len(items)):
    print(f'{item_index}: {items[item_index]}')

# 검색 내용 출력
dict_list_to_csv('./test01_result.csv', data_list=items, col=['title','url'], separator=',')
