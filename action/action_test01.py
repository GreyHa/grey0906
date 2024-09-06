from automation_framework.Web import Web
import element.element_test01 as el

def get_google_search_items(client:Web) -> list:
    '''
        result = [item1, item2, ...]
        item = {
            'title: title,
            'url': url
        }
    '''
    result = []

    item_titles = client(el.google_search_news_list_title).FindValues().ElementValueList

    for item_index in range(len(item_titles)):
        item = {}
        item['title'] = item_titles[item_index]
        item['url'] = client(el.google_search_new_index_url(item_index=item_index)).FindValues().ElementValue

        result.append(item)

    return result

def get_google_search_item(client:Web, item_index:int=0) -> dict:
    '''
        result = {
            'title': title,
            'url': url
        }
    '''

    result = {}
    result['title'] = client(el.google_search_news_list_title, Index=item_index).FindValues().ElementValue
    result['url'] = client(el.google_search_new_index_url(item_index=item_index)).FindValues().ElementValue
    return result