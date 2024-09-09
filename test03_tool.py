from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from support.support_module import json_load, json_dump, path_create, now_time, text_create
from test03_tool_conf import page_template, page_data
import sys, os, base64

base_path = os.path.dirname(os.path.abspath(__file__))
data_path = f'{base_path}/tooldata'
token_data_file_path = f'{data_path}/token.json'
tester_data_file_path = f'{data_path}/testerconf.json'
test_data_file_path = f'{data_path}/testconf.json'
path_create(data_path)

token_data:dict = json_load(token_data_file_path, none_data={})
tester_data:dict = json_load(tester_data_file_path, none_data={})
test_data:dict = json_load(test_data_file_path, none_data={})

tester_keys = ['이메일','이름','핸드폰 번호','생년월일']
test_keys = ['테스트 명']

class table_model():
    def __init__(self, qWindow, col_list:list, data:dict={}):
        self.qWindow = qWindow
        self.col_list = col_list
        self.model = QStandardItemModel(0, len(self.col_list), self.qWindow)
        self.model.setHorizontalHeaderLabels(self.col_list)
        
        self.id = QTableView(self.qWindow)
        self.id.setModel(self.model)
        self.data_set(data=data)
        
    def __dict_to_row_data__(self, row_data:dict):
        result = []

        for col in self.col_list:
            item = QStandardItem(row_data[col])
            item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            result.append(item)

        return result

    def reset(self):
        self.model.removeRows(0,self.model.rowCount())

    def data_set(self, data:dict):
        self.reset()
        for key in data:
            row_data = data[key]
            self.item_add(row_data=row_data)

    def item_add(self, row_data:dict):
        row_index = self.model.rowCount()
        self.model.insertRow(row_index, self.__dict_to_row_data__(row_data))
            
    def item_del(self, row_index:int):
        self.model.removeRow(row_index)


def main():
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.__run_os__ = sys.platform
            self.__main_page__ = '테스트 툴'
            self.__page_history__ = []
            self.setWindowTitle(self.__main_page__)

            page_data['테스트 툴']['items'] = {
                '타이틀 라벨':{'type':QLabel, 'setText':'테스트 툴'},
                '토큰 획득':{'type':QPushButton, 'setText':'토큰 획득', 'clicked.connect': lambda: self.page_change('토큰 획득')},
                '테스터 정보 관리':{'type':QPushButton, 'setText':'테스터 정보 관리', 'clicked.connect': lambda: self.page_change('테스터 정보 관리')},
                '테스트 관리':{'type':QPushButton, 'setText':'테스트 관리', 'clicked.connect': lambda: self.page_change('테스트 관리')},
                '테스트 시작':{'type':QPushButton, 'setText':'테스트 시작', 'clicked.connect': lambda: self.page_change('테스트 시작')},
                '종료':{'type':QPushButton, 'setText':'종료', 'clicked.connect': lambda: self.close()}
            }


            page_data['토큰 획득']['items'] = {
                '타이틀 라벨':{'type':QLabel, 'setText':'토큰 획득'},
                '이메일 입력':{'type':QLineEdit, 'setPlaceholderText':'이메일을 일력하세요.'},
                '뒤로가기':{'type':QPushButton, 'setText':'뒤로가기', 'clicked.connect': lambda: self.page_back()},
                '저장':{'type':QPushButton, 'setText':'저장', 'clicked.connect': lambda: self.token_create('토큰 획득')}
            }

            page_data['테스터 정보 관리']['items'] = {
                '타이틀 라벨':{'type':QLabel, 'setText':'테스터 정보 관리'},
                '저장된 테스터 정보':{'type':QPushButton, 'setText':'저장된 테스터 정보', 'clicked.connect': lambda: (self.table_set('저장된 테스터 정보', '테이블', {}), self.table_set('저장된 테스터 정보', '테이블', tester_data), self.page_change('저장된 테스터 정보'))},
                '테스터 정보 추가':{'type':QPushButton, 'setText':'테스터 정보 추가', 'clicked.connect': lambda: self.page_change('테스터 정보 추가')},
                '테스터 정보 삭제':{'type':QPushButton, 'setText':'테스터 정보 삭제', 'clicked.connect': lambda: self.page_change('테스터 정보 삭제')},
                '뒤로가기':{'type':QPushButton, 'setText':'뒤로가기', 'clicked.connect': lambda: self.page_back()}
            }

            page_data['저장된 테스터 정보']['items'] = {
                '타이틀 라벨':{'type':QLabel, 'setText':'저장된 테스터 정보'},
                '뒤로가기':{'type':QPushButton, 'setText':'뒤로가기', 'clicked.connect': lambda: self.page_back()},
                '테이블':{'type':table_model, 'col_list': tester_keys, 'data':{}},
            }

            page_data['테스터 정보 추가']['items'] = {
                '타이틀 라벨':{'type':QLabel, 'setText':'테스터 정보 추가'},
                '이메일 입력 라벨':{'type':QLabel, 'setText':'이메일'},
                '이메일 입력':{'type':QLineEdit, 'setPlaceholderText':'이메일을 일력하세요.'},
                '이름 입력 라벨':{'type':QLabel, 'setText':'이름'},
                '이름 입력':{'type':QLineEdit, 'setPlaceholderText':'이름을 일력하세요.'},
                '핸드폰 번호 입력 라벨':{'type':QLabel, 'setText':'핸드폰 번호'},
                '핸드폰 번호 입력':{'type':QLineEdit, 'setPlaceholderText':'핸드폰 번호를 일력하세요.'},
                '생년월일 입력 라벨':{'type':QLabel, 'setText':'생년월일'},
                '생년월일 입력':{'type':QDateEdit},
                '뒤로가기':{'type':QPushButton, 'setText':'뒤로가기', 'clicked.connect': lambda: self.page_back()},
                '저장':{'type':QPushButton, 'setText':'저장', 'clicked.connect': lambda: self.tester_create('테스터 정보 추가')}
            }

            page_data['테스터 정보 삭제']['items'] = {
                '타이틀 라벨':{'type':QLabel, 'setText':'테스터 정보 삭제'},
                '이메일 입력':{'type':QLineEdit, 'setPlaceholderText':'이메일을 일력하세요.'},
                '뒤로가기':{'type':QPushButton, 'setText':'뒤로가기', 'clicked.connect': lambda: self.page_back()},
                '삭제':{'type':QPushButton, 'setText':'삭제', 'clicked.connect': lambda: self.tester_delete('테스터 정보 삭제')}
            }

            page_data['테스트 관리']['items'] = {
                '타이틀 라벨':{'type':QLabel, 'setText':'테스트 관리'},
                '저장된 테스트 정보':{'type':QPushButton, 'setText':'저장된 테스트 정보', 'clicked.connect': lambda: (self.table_set('저장된 테스트 정보', '테이블', {}), self.table_set('저장된 테스트 정보', '테이블', test_data), self.page_change('저장된 테스트 정보'))},
                '테스트 추가':{'type':QPushButton, 'setText':'테스트 추가', 'clicked.connect': lambda: self.page_change('테스트 추가')},
                '테스트 삭제':{'type':QPushButton, 'setText':'테스트 삭제', 'clicked.connect': lambda: self.page_change('테스트 삭제')},
                '뒤로가기':{'type':QPushButton, 'setText':'뒤로가기', 'clicked.connect': lambda: self.page_back()}
            }

            page_data['저장된 테스트 정보']['items'] = {
                '타이틀 라벨':{'type':QLabel, 'setText':'저장된 테스트 정보'},
                '뒤로가기':{'type':QPushButton, 'setText':'뒤로가기', 'clicked.connect': lambda: self.page_back()},
                '테이블':{'type':table_model, 'col_list': test_keys, 'data':{}},
            }

            page_data['테스트 추가']['items'] = {
                '타이틀 라벨':{'type':QLabel, 'setText':'테스트 추가'},
                '테스트 명 입력 라벨':{'type':QLabel, 'setText':'테스트 명'},
                '테스트 명 입력':{'type':QLineEdit, 'setPlaceholderText':'테스트 명을 일력하세요.'},
                '뒤로가기':{'type':QPushButton, 'setText':'뒤로가기', 'clicked.connect': lambda: self.page_back()},
                '저장':{'type':QPushButton, 'setText':'저장', 'clicked.connect': lambda: self.test_create('테스트 추가')}
            }

            page_data['테스트 삭제']['items'] = {
                '타이틀 라벨':{'type':QLabel, 'setText':'테스트 삭제'},
                '테스트 명 입력':{'type':QLineEdit, 'setPlaceholderText':'테스트 명을 일력하세요.'},
                '뒤로가기':{'type':QPushButton, 'setText':'뒤로가기', 'clicked.connect': lambda: self.page_back()},
                '삭제':{'type':QPushButton, 'setText':'삭제', 'clicked.connect': lambda: self.test_delete('테스트 삭제')}
            
            }

            page_data['테스트 시작']['items'] = {
                '타이틀 라벨':{'type':QLabel, 'setText':'테스트 시작'},
                '이메일 입력':{'type':QLineEdit, 'setPlaceholderText':'이메일을 일력하세요.'},
                '뒤로가기':{'type':QPushButton, 'setText':'뒤로가기', 'clicked.connect': lambda: self.page_back()},
                '시작':{'type':QPushButton, 'setText':'시작', 'clicked.connect': lambda: self.test_start('테스트 시작')}
            }

            self.page_setting(page_data)
            self.page_reset(self.__main_page__)
                
        def __item__(self, item_data:dict={}) -> dict:

            if item_data['type'] == QPushButton:
                item = QPushButton('', self)

                if 'setText' in item_data.keys():
                    item.setText(item_data['setText'])

                if 'clicked.connect' in item_data.keys():
                    item.clicked.connect(item_data['clicked.connect'])

                item_data['id'] = item

            elif item_data['type'] == QLineEdit:
                item = QLineEdit(self)

                if 'setPlaceholderText' in item_data.keys():
                    item.setPlaceholderText(item_data['setPlaceholderText'])

                item_data['id'] = item

            elif item_data['type'] == QLabel:
                item = QLabel(self)
                
                if 'setText' in item_data.keys():
                    item.setText(item_data['setText'])

                item_data['id'] = item

            elif item_data['type'] == QDateEdit:
                item = QDateEdit(self)
                item.setCalendarPopup(True)
                item.setDate(QDate.currentDate().addYears(-12))
                item.setDisplayFormat("yyyy-MM-dd")
                item_data['id'] = item

            elif item_data['type'] == table_model:
                model = table_model(self, col_list=item_data['col_list'], data=item_data['data'])
                
                item_data['id'] = model.id
                item_data['model'] = model
    
            else:
                raise Exception(f'예상되지 않은 item_type: "{item_data["type"]}"')

            return item_data

        def __page__(self, title:str):
                page:dict = page_data[title]
                template:str = page['template']
                items:dict = page['items']
                window:dict = page['window']

                rect_data = page_template[template]
                column_index = 0
                row_index = 0
                for item_key in items:
                    item_data = items[item_key]
                    item_type = item_data['type']
                    self.__item__(item_data)
                    if template == '메뉴 스타일':
                        if item_type == QLabel:
                            item_data['rect'] = (rect_data['x'], rect_data['y']*1+rect_data['dep']*row_index, rect_data['input_w'], rect_data['input_h'])
                            row_index += 1

                        else:
                            item_data['rect'] = (rect_data['x'], rect_data['y']*1+rect_data['dep']*row_index, rect_data['bt_w'], rect_data['bt_h'])
                            row_index += 1
                            
                    elif template == 'input 스타일':

                        if item_type == QLabel:
                            item_data['rect'] = (rect_data['x'], rect_data['y']*1+rect_data['dep']*column_index, rect_data['input_w'], rect_data['input_h'])
                            column_index += 1

                        elif item_type == QPushButton:
                            item_data['rect'] = (rect_data['x']*(row_index+1)+rect_data['bt_w']*row_index, rect_data['y']*1+rect_data['dep']*column_index, rect_data['bt_w'], rect_data['bt_h'])
                            row_index += 1

                        else:
                            item_data['rect'] = (rect_data['x'], rect_data['y']*1+rect_data['dep']*column_index, rect_data['input_w'], rect_data['input_h'])
                            column_index += 1

                    elif template == 'input 라벨 스타일':
                        
                        if item_type == QPushButton:
                            item_data['rect'] = (rect_data['x']*(1+column_index)+rect_data['bt_w']*column_index, rect_data['y']*2+rect_data['dep']*row_index, rect_data['bt_w'], rect_data['bt_h'])
                            column_index += 1

                        elif item_type == QLineEdit:
                            item_data['rect'] = (rect_data['x'], rect_data['y']*1+rect_data['dep']*row_index-3, rect_data['input_w'], rect_data['input_h'])
                            row_index += 1
                        
                        else:
                            item_data['rect'] = (rect_data['x'], rect_data['y']*1+rect_data['dep']*row_index, rect_data['input_w'], rect_data['input_h'])
                            row_index += 1
                    
                        
                    elif template == '테이블 스타일':
                        if item_type == QPushButton:
                            item_data['rect'] = ( rect_data['x']*(row_index+1)+rect_data['bt_w']*row_index, rect_data['y']*1+rect_data['dep']*column_index, rect_data['bt_w'], rect_data['bt_h'] )
                            row_index += 1

                        elif item_type == table_model:
                            column_index += 1
                            item_data['rect'] = ( rect_data['x']*1+rect_data['bt_w']*0, rect_data['y']*1+rect_data['dep']*column_index, window['window_w']-rect_data['x']*2, window['window_h']-rect_data['y']*2-rect_data['dep']*1 )

                        else:
                            item_data['rect'] = ( rect_data['x']*1, rect_data['y']*1+rect_data['dep']*column_index, rect_data['label_w'], rect_data['label_h'] )
                            column_index += 1

                    rect = item_data['rect']
                    item_data['id'].setGeometry(rect[0],rect[1],rect[2],rect[3])

        def __token__(self, email):
            date_time = now_time()
            token = {
                'email':email,
                'datetime': date_time,
                'token': str(base64.b64encode(f'{email}_{date_time}'.encode('utf-8')))
            }
            return token

        def page_setting(self, page_data:dict):
            for title in page_data:
                self.__page__(title)

        def page_change(self, page_title:int, history=True):
            if page_title == '':
                page_title = self.__main_page__

            if len(self.__page_history__) > 0 :
                last_page = self.__page_history__[-1]
            else:
                last_page = self.__main_page__

            self.display_control(page_data[last_page]['items'], show=False)
            
            page = page_data[page_title]
            self.setWindowTitle(page_title)
            self.setMinimumSize(page['window']['window_w'], page['window']['window_h'])
            
            if page['window']['fixed'] == True:
                self.setFixedSize(page['window']['window_w'],page['window']['window_h'])
            
            self.display_control(page['items'], show=True)

            if history == True:
                self.__page_history__.append(self.windowTitle())

        def page_back(self):
            if len(self.__page_history__) > 1 :
                last_page = self.__page_history__[-2]
            else:
                last_page = self.__main_page__

            self.page_change(last_page, False)
            
            if len(self.__page_history__) > 0:
                self.__page_history__.pop(-1)

        def page_reset(self, page_title):
            
            page = page_data[page_title]
            
            self.setWindowTitle(page_title)
            self.setMinimumSize(page['window']['window_w'], page['window']['window_h'])
            
            if page['window']['fixed'] == True:
                self.setFixedSize(page['window']['window_w'],page['window']['window_h'])
            
            for title in page_data:
                if page_title == title:
                    show = True
                else:
                    show = False

                page = page_data[title]
                items = page['items']
                self.display_control(items=items,show=show)

        def display_control(self, items:dict, show:bool):
            for item_key in items:
                item_data = items[item_key]
                item_id = item_data['id']
                
                if show == True:
                    item_id.show()
                else:
                    item_id.hide()

        def msg_box(self,title:str, text:str, buttons:list=[]):
            '''
                buttons: [button1, button2 ...]

                button: {
                    'text': str,
                    'role': QMessageBox.ButtonRole.role
                }
            '''
            message_box = QMessageBox()
            message_box.setWindowTitle(title)
            message_box.setText(text)

            if buttons != {}:
                for button in buttons:
                    message_box.addButton(button['text'], button['role'])

            message_box.exec()

            return message_box
        
        def table_set(self, page_title:str, item_key:str, data:dict={}):
            model = page_data[page_title]['items'][item_key]['model']
            model.data_set(data)

        def token_create(self, page_title:str):
            items:dict = page_data[page_title]['items']
            email_id:QLineEdit = items['이메일 입력']['id']
            email = email_id.text().strip()
            # email 패턴 검증 필요시 로직 추가 지금은 공백 예외 처리
            if email != '':
                token_data[email] = self.__token__(email)
                json_dump(token_data_file_path, data=token_data)
                self.msg_box('성공', '토큰 획득 완료')
                email_id.setText('')
                self.page_back()
                
            else:
                self.msg_box('실패', '이메일 값이 비어 있습니다.')

        def tester_create(self, page_title:str):
            items:dict = page_data[page_title]['items']
            email_id:QLineEdit = items['이메일 입력']['id']
            name_id:QLineEdit = items['이름 입력']['id']
            tell_id:QLineEdit = items['핸드폰 번호 입력']['id']
            birthday_id:QDateEdit = items['생년월일 입력']['id']
            email = email_id.text().strip()
            name = name_id.text().strip()
            tell = tell_id.text().strip()
            birthday = birthday_id.date().toString('yyyy-MM-dd')
            
            # email tell 패턴 검증 필요시 로직 추가 지금은 공백 예외 처리
            
            if email != '' and name != '' and tell != '' and birthday != '':
                if email not in tester_data.keys():
                    tester_data[email] = {
                        '이메일': email,
                        '이름': name,
                        '핸드폰 번호': tell,
                        '생년월일': birthday
                    }
                    json_dump(tester_data_file_path, tester_data)
                    self.msg_box('성공','테스터 정보 추가 완료')
                    email_id.setText('')
                    name_id.setText('')
                    tell_id.setText('')
                    birthday_id.setDate(QDate.currentDate().addYears(-12))
                else:
                    self.msg_box('실패',f'중복된 이메일 입니다.\n"{email}"')
            else:
                if email == '':
                    self.msg_box('실패','이메일 값이 비어 있습니다.')
                elif name == '':
                    self.msg_box('실패','이름 값이 비어 있습니다.')
                elif tell == '':
                    self.msg_box('실패','핸드폰 번호 값이 비어 있습니다.')
                elif birthday == '':
                    self.msg_box('실패','생년월일 값이 비어 있습니다.')
        
        def tester_delete(self, page_title:str):
            items:dict = page_data[page_title]['items']
            email_id:QLineEdit = items['이메일 입력']['id']
            email = email_id.text().strip()
            if email != '':
                if email in tester_data.keys():
                    msg_box = self.msg_box('확인',f'"{email}"\n테스터 정보를 삭제하시겠습니까?', buttons=[{'text':'삭제', 'role': QMessageBox.ButtonRole.DestructiveRole},{'text':'취소', 'role':QMessageBox.ButtonRole.RejectRole}])
                    if msg_box.buttonRole(msg_box.clickedButton()) == QMessageBox.ButtonRole.DestructiveRole:
                        tester_data.pop(email)
                        json_dump(tester_data_file_path, tester_data)
                        self.msg_box('성공','테스터 정보 삭제 완료')
                        email_id.setText('')
                else:
                    self.msg_box('실패',f'존재하지 않는 이메일 입니다.\n"{email}"')

        def test_create(self, page_title:str):
            items:dict = page_data[page_title]['items']
            test_name_id:QLineEdit = items['테스트 명 입력']['id']
            test_name = test_name_id.text().strip()
            
            if test_name != '':
                if test_name not in test_data.keys():
                    test_data[test_name] = {
                        '테스트 명': test_name,
                    }
                    json_dump(test_data_file_path, test_data)
                    self.msg_box('성공','테스트 정보 추가 완료')
                    test_name_id.setText('')
                else:
                    self.msg_box('실패',f'중복된 테스트 명 입니다.\n"{test_name}"')
            else:
                self.msg_box('실패','테스트 명 값이 비어 있습니다.')

        def test_delete(self, page_title:str):
            items:dict = page_data[page_title]['items']
            test_name_id:QLineEdit = items['테스트 명 입력']['id']
            test_name = test_name_id.text().strip()
            if test_name != '':
                if test_name in test_data.keys():
                    msg_box = self.msg_box('확인',f'"{test_name}"\n테스트 정보를 삭제하시겠습니까?', buttons=[{'text':'삭제', 'role': QMessageBox.ButtonRole.DestructiveRole},{'text':'취소', 'role':QMessageBox.ButtonRole.RejectRole}])
                    if msg_box.buttonRole(msg_box.clickedButton()) == QMessageBox.ButtonRole.DestructiveRole:
                        test_data.pop(test_name)
                        json_dump(test_data_file_path, test_data)
                        self.msg_box('성공','테스트 정보 삭제 완료')
                        test_name_id.setText('')
                else:
                    self.msg_box('실패',f'존재하지 않는 테스트 명 입니다.\n"{test_name}"')

        def test_start(self, page_title:str):
            '''
                실제로 테스트를 시작하는 기능이라면 멀티 프로세스로 개발하여 컨트롤 하는게 좋지만
                단순히 텍스트를 표기하는 용도면 테스트 개수 만큼 반복 하지 않고 한번에 표기하는게 좋아 보이지만 일단 문서대로 개발
            '''
            def dict_to_text(title, data):
                text = f'{title}'

                for key in data:
                    text += f'\n{key}: {data[key]}'

                return text

            items:dict = page_data[page_title]['items']
            email_id:QLineEdit = items['이메일 입력']['id']
            email = email_id.text().strip()
            
            if test_data == {}:
                self.msg_box('실패',f'테스트가 존재하지 않습니다.\n테스트를 추가해주세요.')

            elif email in token_data:
                self.msg_box('정보',dict_to_text('토큰 정보',token_data[email]))

                if email in tester_data:
                    self.msg_box('정보',dict_to_text('테스터 정보',tester_data[email]))

                    for test_name in test_data:
                        self.msg_box('정보',dict_to_text('테스트 정보',test_data[test_name]))

                else:
                    self.msg_box('실패',f'존재하지 않는 테스터 입니다.\n"{email}"')
            else:
                self.msg_box('실패',f'존재하지 않는 토큰 입니다.\n"{email}"')

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

main()