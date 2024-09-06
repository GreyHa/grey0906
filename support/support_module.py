import os, json

def json_load(json_path:str, encoding='utf-8', none_data={}):
    if os.path.isfile(json_path):
        with open(json_path, mode='r', encoding=encoding) as json_file:
            json_data = json.load(json_file)
            return json_data
    else:
        return none_data
    
def json_dump(json_path:str, data, encoding='utf-8'):
    '''
        data: list 또는 dict
    '''
    json_dump = json.dump(data, indent='\t', ensure_ascii=False)
    file = open(json_path, mode='w', encoding=encoding)
    file.write(json_dump)
    file.close()

def text_create(file_path, text, mode='a', encoding='utf-8', newline=False):
    '''
        mode: a 라인 추가, w 새로 쓰기
    '''
    log_file = open(file_path, mode=mode, encoding=encoding)
    if newline == False:
        log_file.write(text)
    else:
        log_file.write(f'{text}\n')
    log_file.close()

def dict_list_to_csv(file_path:str, data_list:list, col=[], separator=',', encoding='utf-8'):
    '''
        data_list = [item1, item2, item3...]
        item:dict

        col: 칼럼 키값 리스트, 순서대로 정렬 및 사용

        separator: 구분 기호 디폴트 ","  "\t" 사용시 tsv
    '''
    
    def line_create(text, value):
        result = text
        if result == '':
            result = f'"{value}"'
        else:
            result += f'{separator}"{value}"'
        return result

    if col != []:
        text = ''
        for key in col:
            text = line_create(text=text, value=key)

        text_create(file_path=file_path, text=f'{text}', mode='w', encoding=encoding, newline=True)

    for item_index in range(len(data_list)):
        item = data_list[item_index]
        text = ''
        if col != []:
            for key in col:
                value = item[key]
                text = line_create(text=text, value=value)
        else:
            for key in item:
                value = item[key]
                text = line_create(text=text, value=value)
        
        if item_index > 1 or col != []:
            text_create(file_path=file_path, text=f'{text}', mode='a', encoding=encoding, newline=True)
        else:
            text_create(file_path=file_path, text=f'{text}', mode='w', encoding=encoding, newline=True)

            