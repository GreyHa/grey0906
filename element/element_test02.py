app_googleCalendar = 'com.google.android.calendar'

## 구글 캘린더 메인 페이지 
googleCalendar_bt_addEvent = {'Target':'com.google.android.calendar:id/floating_action_button'}
googleCalendar_addEvent_bt_reminder = {'Target':'com.google.android.calendar:id/speed_dial_reminder_container'}
googleCalendar_addEvent_bt_tasks = {'Target':'com.google.android.calendar:id/tasks_speed_dial_container'}
googleCalendar_addEvent_bt_event = {'Target':'com.google.android.calendar:id/speed_dial_event_container'}

googleCalendar_bt_calendarExpand = {'Target':'com.google.android.calendar:id/date_picker_button'}
googleCalendar_bt_search = {'Target':'com.google.android.calendar:id/action_search'}
googleCalendar_bt_today = {'Target':'com.google.android.calendar:id/action_today'}
googleCalendar_bt_acount = {'Target':'com.google.android.calendar:id/og_apd_internal_image_view'}

googleCalendar_bt_menu = {'Type':'xpath','Target':'//android.widget.FrameLayout[@resource-id="com.google.android.calendar:id/header"]/android.view.ViewGroup[@resource-id="com.google.android.calendar:id/toolbar"]/android.widget.ImageButton'}

def googleCalendar_menu_bt_view(text:str, contains=False) -> dict:
    '''
        text: 
            en: Schedule view, Day view, 3-days view, Week view, Month view, Selected
            kr: 일정 보기, 일별 일정 보기, 3일간 일정 보기, 주간 일정 보기, 월간 일정 보기, 선택함

        contains: 비교를 문구 포함으로 변경, 디폴트 False
    '''
    if contains == False:
        return {'Type':'xpath','Target':f'//android.widget.ListView[@resource-id="com.google.android.calendar:id/drawer_list"]//android.widget.TextView[@content-desc="{text}"]'}
    else:
        return {'Type':'xpath','Target':f'//android.widget.ListView[@resource-id="com.google.android.calendar:id/drawer_list"]//android.widget.TextView[contains(@content-desc,"{text}")]'}
    
#googleCalendar_menu_bt_schedule = {'Type':'xpath','Target':'//android.widget.ListView[@resource-id="com.google.android.calendar:id/drawer_list"]//android.widget.TextView[contains(@content-desc,"Schedule view")]'}
#googleCalendar_menu_bt_day = {'Type':'xpath','Target':'//android.widget.ListView[@resource-id="com.google.android.calendar:id/drawer_list"]//android.widget.TextView[contains(@content-desc,"Day view")]'}
#googleCalendar_menu_bt_3day = {'Type':'xpath','Target':'//android.widget.ListView[@resource-id="com.google.android.calendar:id/drawer_list"]//android.widget.TextView[contains(@content-desc,"3-days view")]'}
#googleCalendar_menu_bt_week = {'Type':'xpath','Target':'//android.widget.ListView[@resource-id="com.google.android.calendar:id/drawer_list"]//android.widget.TextView[contains(@content-desc,"Week view")]'}
#googleCalendar_menu_bt_month = {'Type':'xpath','Target':'//android.widget.ListView[@resource-id="com.google.android.calendar:id/drawer_list"]//android.widget.TextView[contains(@content-desc,"Month view")]'}
#googleCalendar_menu_bt_selected = {'Type':'xpath','Target':'//android.widget.ListView[@resource-id="com.google.android.calendar:id/drawer_list"]//android.widget.TextView[contains(@content-desc,"Selected")]'}

googleCalendar_expand_layout = {'Type':'xpath','Target':'//android.widget.FrameLayout[@resource-id="com.google.android.calendar:id/alternate_timeline_holder"]/android.widget.FrameLayout//android.widget.FrameLayout[@resource-id="com.google.android.calendar:id/timely_date_picker_container"]'}
googleCalendar_expand_bts_date = {'Type':'xpath','Target':'//android.widget.FrameLayout[@resource-id="com.google.android.calendar:id/alternate_timeline_holder"]/android.widget.FrameLayout//android.widget.FrameLayout[@resource-id="com.google.android.calendar:id/timely_date_picker_container"]//androidx.viewpager.widget.ViewPager/android.view.View/android.view.View'}

googleCalendar_timeLine_list_event = {'Type':'xpath','Target':'//android.widget.FrameLayout[@resource-id="com.google.android.calendar:id/alternate_timeline_fragment_container"]//android.view.View'}

def googleCalendar_timeLine_bt_event(search_text:str) -> dict:
    return {'Type':'xpath','Target':f'//android.widget.FrameLayout[@resource-id="com.google.android.calendar:id/alternate_timeline_fragment_container"]//android.view.View[contains(@content-desc,"{search_text}")]'}
    

# 구글 캘린더 이벤트 상세
googleCalendar_event_label_title = {'Target':'com.google.android.calendar:id/title'}
googleCalendar_event_bt_menu = {'Target':'com.google.android.calendar:id/info_action_overflow'}
def googleCalendar_event_menu_bt(text):
    return {'Type':'xpath','Target':f'//android.widget.TextView[@resource-id="com.google.android.calendar:id/title" and @text="{text}"]'}

googleCalendar_event_delete_bt_cancel = {'Target':'android:id/button2'}
googleCalendar_event_delete_bt_ok = {'Target':'android:id/button1'}


## 구글 캘린더 이벤트 생성 페이지
googleCalendar_eventCreate_bt_save = {'Target':'com.google.android.calendar:id/save'}
googleCalendar_eventCreate_input_title = {'Target':'com.google.android.calendar:id/title'}

__googleCalendar_eventCreate_datetime__ = '//android.view.ViewGroup[@resource-id="com.google.android.calendar:id/coordinator_layout"]//*[@resource-id="com.google.android.calendar:id/expanded_recycler"]//android.widget.LinearLayout[1]'
googleCalendar_eventCreate_bt_allDay = {'Type':'xpath','Target':f'{__googleCalendar_eventCreate_datetime__}/android.view.ViewGroup[@resource-id="com.google.android.calendar:id/all_day_tile"]/android.widget.Switch'}
googleCalendar_eventCreate_bt_startDate = {'Type':'xpath','Target':f'{__googleCalendar_eventCreate_datetime__}/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]'}
googleCalendar_eventCreate_bt_startTime = {'Type':'xpath','Target':f'{__googleCalendar_eventCreate_datetime__}/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[2]'}
googleCalendar_eventCreate_bt_endDate = {'Type':'xpath','Target':f'{__googleCalendar_eventCreate_datetime__}/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]'}
googleCalendar_eventCreate_bt_endTime = {'Type':'xpath','Target':f'{__googleCalendar_eventCreate_datetime__}/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[2]'}

## 데이트피커
datePicker_label_year = {'Target':'android:id/date_picker_header_year'}
datePicker_label_date = {'Target':'android:id/date_picker_header_date'}

datePicker_bt_prev = {'Target':'android:id/prev'}
datePicker_bt_next = {'Target':'android:id/next'}
datePicker_bts_date = {'Type':'xpath','Target':'//android.view.View[@resource-id="android:id/month_view"]/android.view.View'}
datePicker_bt_cancel = {'Target':'android:id/button2'}
datePicker_bt_ok = {'Target':'android:id/button1'}

# 타임피커 아날로그 시계 타입
timePicker_analog_bt_AM = {'Target':'android:id/am_label'}
timePicker_analog_bt_PM = {'Target':'android:id/pm_label'}
timePicker_analog_bt_hour = {'Type':'xpath','Target':'//android.view.View[@resource-id="android:id/radial_picker"]/android.widget.RadialTimePickerView.RadialPickerTouchHelper'}
timePicker_analog_bt_minute = {'Type':'xpath','Target':'//android.view.View[@resource-id="android:id/radial_picker"]/android.widget.RadialTimePickerView.RadialPickerTouchHelper'}
timePicker_analog_bt_cancel = {'Target':'android:id/button2'}
timePicker_analog_bt_ok = {'Target':'android:id/button1'}