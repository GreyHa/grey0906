from automation_framework.AOS import AOS
import element.element_test02 as el
import text.text_test02 as text

def googleCalendar_view_select(client:AOS, target:int=0):
    '''
        구글 캘린더 메인에서 사용
        - 캘린더 뷰를 선택
        
        target: int
            0: 일정 보기
            1: 일별
            2: 3일간
            3: 주간
            4: 월간
    '''
    client.func_log(f'target: "{target}"', 1)

    client(el.googleCalendar_bt_menu).Click()

    if target == 0:
        taregt_text = text.scheduleView(client)
    elif target == 1:
        taregt_text = text.dayView(client)
    elif target == 2:
        taregt_text = text.threeDaysView(client)
    elif target == 3:
        taregt_text = text.weekView(client)
    elif target == 4:
        taregt_text = text.monthView(client)
    else:
        client.func_log(f'예상되지 않은 값 target "{target}"',-1)

    if taregt_text not in client(el.googleCalendar_menu_bt_view(text=text.selected(client), contains=True), ValueType='content-desc').FindValues().ElementValue:
        client(el.googleCalendar_menu_bt_view(text=taregt_text, contains=False)).Click(retry_count=1)
    else:
        client.key_back()

    client.func_log(f'구글 캘린더 뷰 선택 완료 "{taregt_text}"', 3)
    
def googleCalendar_event_create(client:AOS, event:dict):
    '''
        구글 캘린더 메인에서 사용
        - 이벤트를 생성

        event = {
            *'title': str,
            'allDay': bool
            'startDate': YYYY-MM-DD
            'endDate': YYYY-MM-DD
            'startTime': 00:00 ~ 23:59
            'endDate': 00:00 ~ 23:59
        }
    '''
    client.func_log(f'event: "{event}"', 1)

    client(el.googleCalendar_bt_addEvent).Click()
    client(el.googleCalendar_addEvent_bt_event).Click()

    if 'title' in event.keys():
        client(el.googleCalendar_eventCreate_input_title, Value=event['title']).Send()
    else:
        client.func_log(f'title은 필수 값입니다. {event}')

    if 'allDay' in event.keys():
        if event['allDay'] == True:
            client(el.googleCalendar_eventCreate_bt_allDay).Click()

    if 'startDate' in event.keys():
        client(el.googleCalendar_eventCreate_bt_startDate).Click()
        datePicker_select(client, stringDate=event['startDate'])

    if 'startTime' in event.keys():
        client(el.googleCalendar_eventCreate_bt_startTime).Click()
        timePicker_select(client, stringTime=event['startTime'])

    if 'endDate' in event.keys():
        client(el.googleCalendar_eventCreate_bt_endDate).Click()
        datePicker_select(client, stringDate=event['endDate'])

    if 'endTime' in event.keys():
        client(el.googleCalendar_eventCreate_bt_endTime).Click()
        timePicker_select(client, stringTime=event['endTime'])

    client(el.googleCalendar_eventCreate_bt_save).Click()

    client.func_log(f'구글 캘린더 이벤트 생성 완료 event: "{event}"', 3)


def datePicker_select(client:AOS, stringDate:str):
    '''
        datePick가 열린 상태에서 사용
        - 날짜를 선택

        stringDate: YYYY-MM-DD
    '''
    client.func_log(f'stringDate: "{stringDate}"', 1)
    
    month_data = {
        '1월': 1, 'january': 1, 'jan': 1, 'ja': 1,
        '2월': 2, 'february': 2, 'feb': 2, 'fe': 2,
        '3월': 3, 'march': 3, 'mar': 3, 'mr': 3,
        '4월': 4, 'april': 4, 'apr': 4, 'al': 4,
        '5월': 5, 'may': 5, 'ma': 5,
        '6월': 6, 'june':6, 'jun':6, 'jn':6,
        '7월': 7, 'july':7, 'jul':7, 'jl':7,
        '8월': 8, 'august':8, 'aug':8, 'au':8,
        '9월': 9, 'september':9, 'sep':9, 'sept':9, 'se':9,
        '10월': 10, 'october':10, 'oct':10, 'oc':10,
        '11월': 11, 'november':11, 'nov':11, 'no':11,
        '12월': 12, 'december':12, 'dec':12, 'de':12
    }
    stringDate_split = stringDate.split('-')
    target_year:int = int(stringDate_split[0])
    target_month:int = int(stringDate_split[1])
    target_day:int = int(stringDate_split[2])

    text_year:str = client(el.datePicker_label_year, ValueType='text').FindValues().ElementValue
    now_year:int = int(text_year.strip().replace('년',''))
    
    if client.driver_locale == 'ko-KR':
        #한글 "9월 7일 (토)"
        date_text:str = client(el.datePicker_label_date, ValueType='text').FindValues().ElementValue
        date_text_split = date_text.replace(',','').split(' ')
        now_month:int = month_data[date_text_split[0].lower()]
        #now_day:int = int(date_text_split[1].lower())
    else:
        #영어 "Sat, Sep 7"
        date_text:str = client(el.datePicker_label_date, ValueType='text').FindValues().ElementValue
        date_text_split = date_text.replace(',','').split(' ')
        now_month:int = month_data[date_text_split[1].lower()]
        #now_day:int = int(date_text_split[2].lower())

    if (target_year - now_year)*12 + (target_month - now_month) > 0:
        el_bt_step = el.datePicker_bt_next
    else:
        el_bt_step = el.datePicker_bt_prev

    for _ in range(abs(target_year - now_year)*12 + (target_month - now_month)):
        client(el_bt_step).Click()

    client(el.datePicker_bts_date, Value=str(target_day)).FindValues(not_find_error=True).Click()
    
    client(el.datePicker_bt_ok).Click()
    
    client.func_log(f'datePicker 선택 완료 stringDate: "{stringDate}"', 3)

def timePicker_select(client:AOS, stringTime:str):
    '''
        stringTime: 00:00 ~ 23:59
        - 시간을 선택

        analog: bool 선택 방식
            일단 아날로그만 구현
    '''
    client.func_log(f'stringTime: "{stringTime}"', 1)

    stringTime_split = stringTime.split(':')
    target_hour = stringTime_split[0]
    target_minute = stringTime_split[1]

    if int(target_hour) >= 0 and int(target_hour) <= 12:
        client(el.timePicker_analog_bt_AM).Click()
        target_hour12 = str(int(target_hour))
    else:
        client(el.timePicker_analog_bt_PM).Click()
        target_hour12 = str(int(target_hour) - 12)

    client(el.timePicker_analog_bt_hour, Value=target_hour12, ValueType='content-desc').FindValues(not_find_error=True).Click()
    client(el.timePicker_analog_bt_minute, Value=str(int(target_minute)), ValueType='content-desc').FindValues(not_find_error=True).Click()

    client(el.timePicker_analog_bt_ok).Click()
    
    client.func_log(f'timePicker 선택 완료 stringTime: "{stringTime}"', 3)


def go_googleCalendar_date(client:AOS, stringDate:str):
    '''
        구글 캘린더 메인에서 사용
        달력 이동

        stringDate: YYYY-MM-DD
    '''
    client.func_log(f'stringDate: "{stringDate}"', 1)

    stringDate_split = stringDate.split('-')
    target_year:int = int(stringDate_split[0])
    target_month:int = int(stringDate_split[1])
    target_day:int = int(stringDate_split[2])

    if not client(el.googleCalendar_expand_layout).WaitElement(none_error=True, retry_count=1).ElementHandle:
        client(el.googleCalendar_bt_calendarExpand).Click()

    now_date = client(el.googleCalendar_expand_bts_date, ValueType='content-desc').FindValues().ElementValue
    now_stringDate = text.googleCalendarText_to_stringDate(client, text=now_date)
    now_stringDate_split = now_stringDate.split('-')
    now_year:int = int(now_stringDate_split[0])
    now_month:int = int(now_stringDate_split[1])
    #now_day:int = int(now_stringDate_split[2])

    width = client.driver_location['width']
    # 기기별 오동작 여부 확인 필요
    if (target_year - now_year)*12 + (target_month - now_month) > 0:
        sourece_x = width/2.1
        target_x = -width/2.2

    else:
        sourece_x = -width/2.1
        target_x = width/2.2
        
    for _ in range(abs(target_year - now_year)*12 + (target_month - now_month)):
        client(el.googleCalendar_expand_layout).Slide(sourece_offset=(sourece_x,0),target_offset=(target_x,0), befoer_duration=1, affter_duration=0)

    client(el.googleCalendar_expand_bts_date, Index=target_day-1).Click()
    client(el.googleCalendar_bt_calendarExpand).Click()
    client.func_log(f'구글 캘린더 이동 완료 stringDate: "{stringDate}"', 3)

def get_googleCalendar_timeLine_event_list(client:AOS) -> list:
    '''
        구글 메인에서 사용
        - 현재 화면의 이벤트를 서치하여 분석 후 event_list를 출력

        event = {
            *'title': str,
            'allDay': bool
            'startDate': YYYY-MM-DD
            'endDate': YYYY-MM-DD
            'startTime': 00:00 ~ 23:59
            'endDate': 00:00 ~ 23:59
        }
    '''

    def number_to_sting(number:int):
        if number > 0 and number < 10:
            return f'0{number}'
        else:
            return str(number)

    def stringTime_change(time_text:str, meridiem:str) -> str:
        '''
            time_text: 01:00 ~ 12:59
            meridiem: AM, PM

            return: 00:00 ~ 23:59
        '''
        time_text_split = time_text.split(':')
        hour = int(time_text_split[0])
        minute = time_text_split[1]

        if meridiem == 'PM':
            hour += 11
        elif meridiem == 'AM':
            pass
        else:
            client.func_log(f'예상되지 않은 값 meridiem "{meridiem}"',-1)

        return f'{number_to_sting(hour)}:{minute}'

    #el.googleCalendar_timeLine_bt_event(search_text=f'{event["title"]}, ')
    result = []
    item_list = client(el.googleCalendar_timeLine_list_event, ValueType='content-desc').FindValues().ElementValueList
    
    date_text = ''
    for event_text in item_list:
        event_text:str
        # event_text 종류는 세가지
        # 날짜,이벤트,빈값으로 세트로 구성되며 반복됨

        if date_text == '':
            # 세트 시작
            # 날짜 "Sunday 29 September 2024, Open Day View"
            date_text = event_text

        elif event_text == '':
            # 세트 초기화
            date_text = ''
        
        else: 
            # 이벤트 분석
            text_split = event_text.replace(' ', ' ').replace(' – ',' ').replace(',', '').split(' ')
            if 'All day' in event_text:
                # all day인 경우 "국군의날, All day: "
                event = {
                    'title': text_split[0],
                    'allDay': True
                }
            else:
                # 시간이 설정된 이벤트 "타이틀, 4:00 PM – 5:00 PM"
                event = {
                    'title': text_split[0],
                    'startTime': stringTime_change(text_split[1], text_split[2]),
                    'endTime': stringTime_change(text_split[3], text_split[4])
                }
            
            result.append(event)

    client.func_log(f'result: {result}')
    return result

def googleCalendar_timeLine_event_select(client:AOS, event:dict):
    '''
        구글 메인 타임라인에서 사용
        - event title을 찾아서 선택
    '''

    client(el.googleCalendar_timeLine_bt_event(search_text=f'{event["title"]}, ')).Click()

    now_title = client(el.googleCalendar_event_label_title).FindValues().ElementValue

    client.compare_log(event['title'], now_title, '==', 0, -1, '이벤트 상세 진입 후 타이틀 비교')

def googleCalendar_event_delete(client:AOS, event:dict):
    '''
        구글 메인 타임라인 또는 이벤트 상세에서 사용
        - event를 삭제
    '''

    target_title = event['title']

    now_title = client(el.googleCalendar_event_label_title).FindValues(retry_count=1).ElementValue

    if now_title != target_title:
        if now_title:
            client.key_back()

        googleCalendar_timeLine_event_select(client, event=event)

    client(el.googleCalendar_event_bt_menu).Click()
    client(el.googleCalendar_event_menu_bt(text=text.eventDelete(client))).Click()
    client(el.googleCalendar_event_delete_bt_ok).Click()

    target_item = client(el.googleCalendar_timeLine_bt_event(search_text=f'{target_title}, ')).WaitElement(none_error=True).ElementHandle
    client.compare_log([], target_item, '==', 0, -1, '이벤트 삭제 후 확인')


def googleCalendar_event_all_delete(client:AOS, search_text:str, count=9999):
    '''
        구글 메인 타임라인에서 사용
        현재 타임 라인의 search_text를 포함하는 제목의 이벤트를 삭제
    '''

    for _ in range(count):
        
        if client(el.googleCalendar_timeLine_bt_event(search_text=search_text)).WaitElement(none_error=True).ElementHandle:
            client.Click()
            client(el.googleCalendar_event_bt_menu).Click()
            client(el.googleCalendar_event_menu_bt(text=text.eventDelete(client))).Click()
            client(el.googleCalendar_event_delete_bt_ok).Click()
        else:
            break

    
        