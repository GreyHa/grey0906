from automation_framework.AOS import AOS
import element.element_test02 as el
import action.action_test02 as action
from support.support_module import json_load
import os, time

#appium --allow-insecure adb_shell


# 설정
start_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
base_path = os.path.dirname(os.path.abspath(__file__))
config_file_path = f'{base_path}/conf/test02.json'
clientinfo = json_load(config_file_path, none_data={})
clientinfo['screenshot_path'] = f'{base_path}/screenshot'
clientinfo['log_file_path'] = f'{base_path}/log/{time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))}.txt'

event1 = {
    'title': f'빼빼로 데이 {start_time}', # 타이틀이 중복 된 경우 비교하기 힘들기 때문에 타임스탬프 추가
    'startDate': '2024-11-11',
    'startTime': '09:00',
    'endDate': '2024-11-11',
    'endTime': '17:00'
}

# 셋팅
client = AOS(clientinfo=clientinfo)
client.adb_get_locale()
client.adb_app_close(app_id=el.app_googleCalendar)
client.adb_app_start(app_id=el.app_googleCalendar)
client.sleep(5)

# 자동화 시작

# 구글 캘린더 주간 일정 보기로 변경
action.googleCalendar_view_select(client, 3)

# 구글 캘린더 이벤트 생성
action.googleCalendar_event_create(client, event=event1)

# 구글 캘린더 타임라인 날짜 이동
action.go_googleCalendar_date(client, stringDate='2024-11-13')

# 구글 캘린더 이벤트 선택
action.googleCalendar_timeLine_event_select(client, event=event1)

# 구글 캘린더 이벤트 삭제
action.googleCalendar_event_delete(client, event=event1)

#화면에 보이는 타이틀에 특정 단어가 들어간 이벤트 전부 삭제
#action.googleCalendar_event_all_delete(client, '빼빼로 데이')