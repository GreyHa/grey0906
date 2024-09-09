from automation_framework.AOS import AOS
import element.element_test02 as el
import action.action_test02 as action
from support.support_module import json_load
import os, time

#appium --allow-insecure adb_shell

start_time = time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
base_path = os.path.dirname(os.path.abspath(__file__))
config_file_path = f'{base_path}/conf/test02.json'
clientinfo = json_load(config_file_path, none_data={})

clientinfo['screenshot_path'] = f'{base_path}/screenshot'
clientinfo['log_file_path'] = f'{base_path}/log/{time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))}.txt'

event1 = {
    'title': f'빼빼로 데이 {start_time}',
    'startDate': '2024-11-11',
    'startTime': '09:00',
    'endDate': '2024-11-11',
    'endTime': '17:00'
}

client = AOS(clientinfo=clientinfo)

client.adb_get_locale()
client.adb_app_close(app_id=el.app_googleCalendar)
client.adb_app_start(app_id=el.app_googleCalendar)
client.sleep(5)

action.googleCalendar_view_select(client, 3)
action.googleCalendar_event_create(client, event=event1)
action.go_googleCalendar_date(client, stringDate='2024-11-13')
action.googleCalendar_timeLine_event_select(client, event=event1)
action.googleCalendar_event_delete(client, event=event1)

#action.googleCalendar_event_all_delete(client, '빼빼로 데이')