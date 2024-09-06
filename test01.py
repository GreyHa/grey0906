from __chromedriver_autoinstall__ import chrome_driver_install_path
from automation_framework.Web import Web
import element.element_test01 as el
import action.action_test01 as action
from support.support_module import dict_list_to_csv
#/Applications//Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9223 --user-data-dir="~/Chrome/Chrome-user01"

chrome_driver_path = chrome_driver_install_path()

clientinfo = {
    'executable_path':chrome_driver_path
}

clientinfo2 = {
    'executable_path':chrome_driver_path,
    'ip':'127.0.0.1',
    'port':'9223',
}

client = Web(clientinfo=clientinfo)
search_url = el.google_search({'q':'삼쩜삼','tbm':'nws','tbs':'qdr:w'})
client.driver.get(search_url)
item = action.get_google_search_item(client, item_index=0)

#items = action.get_google_search_items(client)
#for item_index in range(len(items)):
#    print(f'{item_index}: {items[item_index]}')

dict_list_to_csv('./test01_result.csv', data_list=[item], col=['title','url'], separator=',')