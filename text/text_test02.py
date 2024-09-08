from automation_framework.AOS import AOS

def __auto_locale__(text_data, locale):
    if locale not in text_data.keys():
        return text_data['en-US']
    else:
        return text_data[locale]

def scheduleView(client:AOS) -> str:
    text_data = {
        'en-US': 'Schedule view',
        'ko-KR': '일정 보기',
    }

    return __auto_locale__(text_data=text_data, locale=client.driver_locale)


def dayView(client:AOS) -> str:
    text_data = {
        'en-US': 'Day view',
        'ko-KR': '일별 일정 보기',
    }

    return __auto_locale__(text_data=text_data, locale=client.driver_locale)

def threeDaysView(client:AOS) -> str:
    text_data = {
        'en-US': '3-days view',
        'ko-KR': '3일간 일정 보기',
    }

    return __auto_locale__(text_data=text_data, locale=client.driver_locale)

def weekView(client:AOS) -> str:
    text_data = {
        'en-US': 'Week view',
        'ko-KR': '주간 일정 보기',
    }

    return __auto_locale__(text_data=text_data, locale=client.driver_locale)

def monthView(client:AOS) -> str:
    text_data = {
        'en-US': 'Month view',
        'ko-KR': '주간 일정 보기',
    }

    return __auto_locale__(text_data=text_data, locale=client.driver_locale)

def selected(client:AOS) -> str:
    text_data = {
        'en-US': 'Selected',
        'ko-KR': '선택함',
    }

    return __auto_locale__(text_data=text_data, locale=client.driver_locale)

def eventDelete(client:AOS) -> str:
    text_data = {
        'en-US': 'Delete',
        'ko-KR': '삭제',
    }

    return __auto_locale__(text_data=text_data, locale=client.driver_locale)


def datePikerText(client:AOS, year:int, month:int, day:int) -> str:

    month_data = {
        'en-US': {
            '1': 'January',
            '2': 'February',
            '3': 'March',
            '4': 'April',
            '5': 'May',
            '6': 'June',
            '7': 'July',
            '8': 'August',
            '9': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December'
        },
        'ko-KR': {
            '1': '1월',
            '2': '2월',
            '3': '3월',
            '4': '4월',
            '5': '5월',
            '6': '6월',
            '7': '7월',
            '8': '8월',
            '9': '9월',
            '10': '10월',
            '11': '11월',
            '12': '12월'
        },
    }

    def number_to_sting(number:int):
        if number > 0 and number < 10:
            return f'0{number}'
        else:
            return str(number)

    if client.driver_locale == 'ko-KR':
        return f'{year} {month_data[client.driver_locale][str(month)]} {number_to_sting(day)}'
    else:
        return f'{number_to_sting(day)} {month_data["en-US"][str(month)]} {year}'
    
def googleCalendarText_to_stringDate(client:AOS, text:str) -> str:
    '''
        en-US: "Sunday 01 September 2024"
        ko-KR: ""
    '''
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


    if client.driver_locale == 'ko-KR':
        # 한글 "일요일 01 9월 2024"
        text_split = text.split(' ')
        #요일 = text_split[0]
        day = text_split[1]
        month = text_split[2]
        year = text_split[3]
        return f'{year}-{month_data[month.lower()]}-{day}'
    
    else:
        # 영어 "Sunday 01 September 2024"
        text_split = text.split(' ')
        #요일 = text_split[0]
        day = text_split[1]
        month = text_split[2]
        year = text_split[3]
        return f'{year}-{month_data[month.lower()]}-{day}'

    