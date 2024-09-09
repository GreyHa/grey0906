import urllib.parse

def google_search_url(query:dict) -> str:
    '''
        query: dict key와 value로 구성

        q: 검색어
        tbm: nws, shop, vid, 전체 검색인 경우 선언하지 않음
        tbs: 0 기본값
             qdr:h 지난 1시간
             qdr:d 일
             qdr:w 주
             qdr:h 월
             qdr:y 년
             ar:1 자료실?
             cdr:1,cd_min:9/2/2024,cd_max:9/6/2024 날짜 설정
    '''
    query_encode = urllib.parse.urlencode(query=query)
    result = f'https://www.google.com/search?{query_encode}'
    print(result)
    return result

__google_search_news_item_index__ = 'div#search div#rso > div > div > div:nth-child({item_index})'
__google_search_news_item_index_reverse__ = 'div#search div#rso > div > div > div:nth-last-child({item_index})'


google_search_news_list_title = {'Target':'div#search div#rso > div > div > div div[role="heading"]'}

def google_search_new_index_url(item_index:int=0) -> dict:
    if item_index >= 0:
        return {'Target':f'{__google_search_news_item_index__} a'.replace('{item_index}',str(item_index+1)),'ValueType':'href'}
    else:
        return {'Target':f'{__google_search_news_item_index_reverse__} a'.replace('{item_index}',str(abs(item_index))),'ValueType':'href'}