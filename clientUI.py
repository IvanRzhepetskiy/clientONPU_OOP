import socket
import sys
import threading
import time
from kivy.core.text import Label
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
host = 'localhost'
port = 8888
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

# You can create your kv code in the Python file

Builder.load_string("""
#:import Window kivy.core.window.Window
<Lections>:
    orientation: 'horizontal'
    id: bl
    Button:
        size_hint:(1,.1)
        text:'Refresh'
        on_release:root.addButton()
<Tarefas>:

    orientation:'vertical'

    ScrollView:
        BoxLayout:
            id:box
            orientation:'vertical'
            size_hint_y:None
            height:self.minimum_height
    BoxLayout:
        size_hint_y:None
        height:60
        TextInput:
            id:texto
        Button:
            text:'+'
            size_hint_x:None
            width:60
            on_release:root.addWidget()


            
            
<Tarefa>:
    id:child
    size_hint_y:None
    height:200
    Label:
        id:label
        font_size:30
    Button:
        id:button
        text:'X'
        size_hint_x:None
        width:60
        on_release:root.__del__()

       
<TeacherScreenMain>:
    
    BoxLayout:
        orientation: "vertical"
        ScrollView:
            size_hint:(1,None)
            height:48
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
            
            
            GridLayout:
                
                spacing: [20,0]
                size_hint_x: None
                width: self.minimum_width
                
                rows:1
                canvas:
                    Color:
                        rgba: 1, 1, 1, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
                
                
                Button:
                    size_hint: (None, None)
                    width: 230
                    height:48
                    background_normal: 'button_add_lection_normal.png'
                    background_down: 'button_add_lection_press.png'
                    on_press:
                        root.manager.transition.direction = 'up'
                        root.manager.transition.duration = 1.5
                        root.manager.current = 'add_lection_screen'
                Button:
                    size_hint: (None, None)
                    width: 230
                    height:48
                    background_normal: 'button_journal_1.png'
                    background_down: 'button_journal_2.png'
                    on_press:
                        root.manager.transition.direction = 'up'
                        root.manager.transition.duration = 1.5
                        root.manager.current = 'journal_screen'
                Button:
                    size_hint: (None, None)
                    width: 230
                    height:48
                    background_normal: 'button_prognoziruemye-bally_1.png'
                    background_down: 'button_prognoziruemye-bally_2.png'
                    on_press:
                        root.manager.transition.direction = 'up'
                        root.manager.transition.duration = 1.5
                        root.manager.current = 'prediction_points_screen' 
                Button:
                    size_hint: (None, None)
                    width: 230
                    height:48
                    background_normal: 'button_lichnyj-kabinet_1.png'
                    background_down: 'button_lichnyj-kabinet_2.png'
                    on_press:
                        root.manager.transition.direction = 'up'
                        root.manager.transition.duration = 1.5
                        root.manager.current = 'user_settings_screen'
                Button:
                    size_hint: (None, None)
                    width: 48
                    height: 48
                    background_normal: 'exit.png'
                    
                    on_press: app.stop()
                
                
        BoxLayout:
            orientation: "vertical"
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size


<AddLection>:
    BoxLayout:
        
        orientation:'vertical'
        BoxLayout:
            size_hint:(1,0.15)
            AnchorLayout:
                anchor_x:'left'
                anchor_y:'top'
                Button:
                    background_normal: 'back_1.png'
                    background_down: 'back_2.png'
                    size_hint: (None, None)
                    width: 64
                    height: 64
                    on_press:
                        root.manager.transition.direction = 'down'
                        root.manager.transition.duration = 1.5
                        root.manager.current = 'teacher_screen'
            AnchorLayout:
                anchor_x:'right'
                anchor_y:'top'    
                Button:
                    size_hint: (None, None)
                    width: 64
                    height: 64
                    background_normal: 'exit.png'
                    
                    on_press: app.stop()
        
        BoxLayout:
            orientation: 'horizontal'
            BoxLayout:
                orientation:'horizontal'
                BoxLayout:
                    orientation:'vertical'
                    TextInput:  
                        id: name_of_lection
                        text: 'Введите название лекции'
                        size_hint:1, .1
                    TextInput:
                        id : lection_main
                        text: 'Введите текст лекции'
                ScrollView:    
                    BoxLayout:
                        size_hint_y:None
                        height:900
                        orientation:'vertical'    
                        TextInput
                            id: question_1
                            text: 'Вопрос 1'
                        TextInput
                            id: input_1_answer
                            text: 'Ответ'
                        TextInput
                            id: question_2
                            text: 'Вопрос 2'
                        TextInput
                            id: input_2_answer
                            text: 'Ответ'
                        TextInput
                            id: question_3
                            text: 'Вопрос 3'
                        TextInput
                            id: input_3_answer 
                            text: 'Ответ'   
                        TextInput
                            id: question_4
                            text: 'Вопрос 4'
                        TextInput
                            id: input_4_answer
                            text: 'Ответ'
                        Button:
                            text: 'Сохранить'
                            on_press:
                                root.addNewLection(name_of_lection.text, lection_main.text, question_1.text,  question_2.text, question_3.text, question_4.text, input_1_answer.text, input_2_answer.text, input_3_answer.text, input_4_answer.text)
                            


<Journal>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        orientation:'vertical'
        BoxLayout:
            size_hint:(1,0.3)
            AnchorLayout:
                anchor_x:'left'
                anchor_y:'top'
                Button:
                    background_normal: 'back_1.png'
                    background_down: 'back_2.png'
                    size_hint: (None, None)
                    width: 64
                    height: 64
                    on_press:
                        root.manager.transition.direction = 'down'
                        root.manager.transition.duration = 1.5
                        root.manager.current = 'teacher_screen'
            AnchorLayout:
                anchor_x:'right'
                anchor_y:'top'    
                Button:
                    size_hint: (None, None)
                    width: 64
                    height: 64
                    background_normal: 'exit.png'
                    
                    on_press: app.stop()
        
        BoxLayout:
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
    
        
<PredictionPoints>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        orientation:'vertical'
        BoxLayout:
            size_hint:(1,0.3)
            AnchorLayout:
                anchor_x:'left'
                anchor_y:'top'
                Button:
                    background_normal: 'back_1.png'
                    background_down: 'back_2.png'
                    size_hint: (None, None)
                    width: 64
                    height: 64
                    on_press:
                        root.manager.transition.direction = 'down'
                        root.manager.transition.duration = 1.5
                        root.manager.current = 'teacher_screen'
            AnchorLayout:
                anchor_x:'right'
                anchor_y:'top'    
                Button:
                    size_hint: (None, None)
                    width: 64
                    height: 64
                    background_normal: 'exit.png'
                    
                    on_press: app.stop()
        
        BoxLayout:
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size    


<UserSettings>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        orientation:'vertical'
        BoxLayout:
            size_hint:(1,0.3)
            AnchorLayout:
                anchor_x:'left'
                anchor_y:'top'
                Button:
                    background_normal: 'back_1.png'
                    background_down: 'back_2.png'
                    size_hint: (None, None)
                    width: 64
                    height: 64
                    on_press:
                        root.manager.transition.direction = 'down'
                        root.manager.transition.duration = 1.5
                        root.manager.current = 'teacher_screen'
            AnchorLayout:
                anchor_x:'right'
                anchor_y:'top'    
                Button:
                    size_hint: (None, None)
                    width: 64
                    height: 64
                    background_normal: 'exit.png'
                    
                    on_press: app.stop()
        
        BoxLayout:
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size        
                
                
                
                
                
                
<LoginBoxLayout@BoxLayout>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'lights.png'
    orientation: "vertical"
    padding: 30
    
    
    
<MyBigButt@Button>:
    text_size: self.size
    font_size: '25sp'
    markup: True
    
    
<ScreenOne>:
    BoxLayout:
        orientation: "horizontal"
    
        LoginBoxLayout:
            TextInput:
                size_hint: (1, .2)
                height: self.minimum_height
                font_size: 25
                margin_bottom: dp(30)
                id:username
            TextInput:
                hint_text: "Пароль"
                id: password
                password:"True"
                size_hint: (1,.2)
                height: self.minimum_height
                font_size: dp(30)
           
                
            Button:
                size_hint: (1,.2)
                radius: [50,]
                text: "Sign in"
                
              
                
                on_press:
                    root.getLoginAndPassword(username.text, password.text)
                    # You can define the duration of the change
                    # and the direction of the slide
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                text: "Sign in"
                    
            Widget:
                size_hint: (1,.2)
                
            LoginBoxLayout:
                Label:
                    text: "Don't have an account?"
                Button:
                    text: "I am new here"
                    on_press:
                        # You can define the duration of the change
                        # and the direction of the slide
                        root.manager.transition.direction = 'up'
                        root.manager.transition.duration = 1
                        root.manager.current = 'register_screen'
    
            
<RegisterScreen>:
    BoxLayout:
        orientation: "vertical"
        TextInput:
            hint_text: "Имя Фамилия"
            size_hint: (.5, .2)
            height: self.minimum_height
            font_size: 25
            margin_bottom: dp(30)
            id:register_name
        TextInput:
            hint_text: "Логин"
            id: register_login
            password:"True"
            size_hint: (.5,.2)
            height: self.minimum_height
            font_size: dp(30)
        TextInput:
            hint_text: "Пароль"
            id: register_password
            password:"True"
            size_hint: (.5,.2)
            height: self.minimum_height
            font_size: dp(30)
        CheckBox:
            id: check_teacher
        Button:
            text:'register'
            on_press:
                root.registerNewUser(register_name.text, register_login.text, register_password.text,check_teacher.active )
        
                
        BoxLayout:
            
            orientation: "horizontal"
            Label:
                text: root.register_status
                id: register_status
            Button:
                text: "Go to Screen 1"
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'screen_one'
                
<MainScreen>:
    BoxLayout:
        orientation: "vertical"
        ScrollView:
            size_hint:(1,None)
            height:48
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
            
            
            GridLayout:
                
                spacing: [20,0]
                size_hint_x: None
                width: self.minimum_width
                
                rows:1
                canvas:
                    Color:
                        rgba: 1, 1, 1, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
                
                
                Button:
                    size_hint: (None, None)
                    width: 230
                    height:48
                    background_normal: 'button_lekcii.png'
                    background_down: 'button_lekcii_2.png'
                    on_press:
                        root.manager.transition.direction = 'up'
                        root.manager.transition.duration = 1.5
                        root.getListOfLections()
                Button:
                    size_hint: (None, None)
                    width: 230
                    height:48
                    background_normal: 'button_ocenki.png'
                    background_down: 'button_ocenki_2.png'
                    on_press:
                        root.manager.transition.direction = 'up'
                        root.manager.transition.duration = 1.5
                        root.manager.current = 'marks_screen'
               
                Button:
                    size_hint: (None, None)
                    width: 48
                    height: 48
                    background_normal: 'exit.png'
                    
                    on_press: app.stop()
      
        BoxLayout:
            Button:
                text: "Logout"
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.logout()

<LectionScreen>:
    BoxLayout:   
        orientation:'vertical'
        height:64
        width:64
        BoxLayout:
            height:64
            width:64
            AnchorLayout:
                anchor_x:'left'
                anchor_y:'top'
                Button:
                    background_normal: 'back_1.png'
                    background_down: 'back_2.png'
                    size_hint: (None, None)
                    width: 64
                    height: 64
                    on_press:
                        root.manager.transition.direction = 'down'
                        root.manager.transition.duration = 1.5
                        root.manager.current = 'main_screen'
            AnchorLayout:
                anchor_x:'right'
                anchor_y:'top'    
                Button:
                    size_hint: (None, None)
                    width: 64
                    height: 64
                    background_normal: 'exit.png'
                    on_press: app.stop()
    BoxLayout:
        orientation:'vertical' 
        Lections:
           
        ScrollView:
            bar_width: 10
            bar_color: 0, 0, 1, 1   # blue
            bar_inactive_color: 1, 0, 0, 1   # red
            effect_cls: "ScrollEffect"
            scroll_type: ['bars']
            size_hint: (1, None)
            size: (Window.width ,  Window.height - Window.height/100*30)    
            GridLayout:
                cols: 1
                spacing: 10
                size_hint_y: None
                height: self.minimum_height   
                Label:
                    text:root.text_of_lection
                    id:text_of_lection
                    size_hint_y: None
                    text_size: self.width, None
                    height: self.texture_size[1]
                Label:
                    text: root.question_1
                    id:question_1
                    size_hint_y: None
                    text_size: self.width, None
                    height: self.texture_size[1]
                    
                TextInput:
                    text:'Ответ 1'
                    id: answer_1
                    size_hint_y: None
                    text_size: self.width, None
                    
                Label:
                    text: root.question_2
                    id:question_2
                    size_hint_y: None
                    text_size: self.width, None
                    height: self.texture_size[1]
                TextInput:
                    text:'Ответ 2'
                    id: answer_2
                    size_hint_y: None
                    text_size: self.width, None
                    
                Label:
                    text: root.question_3
                    id:question_3
                    size_hint_y: None
                    text_size: self.width, None
                    height: self.texture_size[1]
                TextInput:
                    text:'Ответ 3'
                    id: answer_3
                    size_hint_y: None
                    text_size: self.width, None
                    
                Label:
                    text: root.question_4
                    id:question_4
                    size_hint_y: None
                    text_size: self.width, None
                    height: self.texture_size[1]
                TextInput:
                    text:'Ответ 4'
                    id: answer_4
                    size_hint_y: None
                    text_size: self.width, None
                    
                Button:
                    size_hint_y: None
                    text_size: self.width, None
                    height: self.texture_size[1]    
                    text:'Submit'
                    on_press:
                        root.submitLection(answer_1.text,answer_2.text,answer_3.text,answer_4.text)

<StudentMarksScreen>:
    BoxLayout:   
        orientation:'vertical'
        height:64
        width:64
        BoxLayout:
            height:64
            width:64
            AnchorLayout:
                anchor_x:'left'
                anchor_y:'top'
                Button:
                    background_normal: 'back_1.png'
                    background_down: 'back_2.png'
                    size_hint: (None, None)
                    width: 64
                    height: 64
                    on_press:
                        root.manager.transition.direction = 'down'
                        root.manager.transition.duration = 1.5
                        root.manager.current = 'main_screen'
            AnchorLayout:
                anchor_x:'center'
                anchor_y:'top'    
                Button:
                    size_hint: (None, None)
                    width: 64
                    height: 64
                    background_normal: 'refresh-page-option.png'
                    on_press:root.fill_marks()
            AnchorLayout:
                anchor_x:'right'
                anchor_y:'top'    
                Button:
                    size_hint: (None, None)
                    width: 64
                    height: 64
                    background_normal: 'exit.png'
                    on_press: app.stop()
            
                        
    BoxLayout:
        orientation:'vertical'
        id:students_marks
        
    
    
""")
from kivy.core.window import Window
Window.clearcolor = (.9, .9, .9, 1)

login_of_user = ''
current_lection = ''
right_answers = []
lection_names = []
student_marks = []
user_id = -1
flag = False
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Creating socket FAILED")
    sys.exit()

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("HOSTNAME COULD NOT BE RESOLVED")
    sys.exit()
s.connect((remote_ip, port))


def getMes():
    # В єтом методе я принимаю сообщения и в зависимости от ключа запускаю нужные методы
    global s
    global current_lection
    global RegisterScreen
    global student_marks
    while True:
        data = s.recv(50024)
        # accepted для ученика и учителя разный
        if data.decode() == '--accepted_student--':
            print('accepted')
            screen_manager.current = 'main_screen'
        elif data.decode() == '--accepted_teacher--':
            screen_manager.current = 'teacher_screen'
            #TODO Добавить страницу учителя и научить сервер распозновать ученик это или учитель
        elif data.decode() == '--pass_incorrect--':
            print("Неправильный пароль")
        elif data.decode() == '--log_incorrect--':
            print("Неправильный логин")
        elif data.decode() == '--login_exists--':
            print('Логин уже существует')
            screen_manager.screens[1].register_status = 'Логин существует'
        elif (data.decode()).find('--lections--') == 0:
            global lection_names
            lection_names = data.decode()[12:].split('!=,/ds')
            del lection_names[-1]
            print(lection_names)
            #Now we should add them to button names
        elif (data.decode()).find('--lection_ready--') == 0:
            print(data.decode()[18:])
            data = data.decode()[17:].split('!=,/ds')
            print(data)
            current_lection = data[0]
            screen_manager.screens[3].text_of_lection = data[1]
            screen_manager.screens[3].question_1 = data[2]
            screen_manager.screens[3].question_2 = data[4]
            screen_manager.screens[3].question_3 = data[6]
            screen_manager.screens[3].question_4 = data[8]

            right_answers.append(data[3].upper())
            right_answers.append(data[5].upper())
            right_answers.append(data[7].upper())
            right_answers.append(data[9].upper())

        elif (data.decode()).find('--marks_ready--') == 0:
            student_marks = data.decode()[15:].split('!=,/ds')
            del student_marks[-1]
            print(student_marks)
    pass

# Create a class for all screens in which you can include
# helpful methods specific to that screen
class ScreenOne(Screen):
    def getLoginAndPassword(self, username, password):
        global login_of_user
        login_of_user = username
        s.send(('--connect--'+ str(username)+ str(' ')+str(password)).encode())
        pass


class Lections(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def addButton(self):
        global lection_names
        if lection_names:
            for lection in lection_names:
                self.btn = Button(text=lection, on_press=self.showLection, size_hint = (1,.1),halign='center')
                self.add_widget(self.btn)
            lection_names = []
    def showLection(self,  instance):
        print('Wait please, your request is getting ready')
        s.send(('--get_exact_lection--'+ str(instance.text)).encode())
        print(instance.text)

        pass



class LectionScreen(Screen):

    text_of_lection = StringProperty()
    question_1 = StringProperty()
    question_2 = StringProperty()
    question_3 = StringProperty()
    question_4 = StringProperty()

    def changeLabel(self,text):
        self.text_of_lection = text
        pass



    def submitLection(self,answer_1,answer_2,answer_3,answer_4):
        global current_lection
        global login_of_user
        result = 0
        counter = 0
        print(right_answers)
        if answer_1.upper() == right_answers[0]:
            result+=1

        if answer_2.upper() == right_answers[1]:
            result+=1

        if answer_3.upper() == right_answers[2]:
            result+=1

        if answer_4.upper() == right_answers[3]:
            result+=1

        result = result/4

        print(current_lection)
        lection_names.clear()
            # Now we will send results in Format (LECTION_NAME, POINTS_GOT/MAX_POINTS)

        s.send(('--add_mark--'+current_lection+'!=,/ds'+str(result)+'!=,/ds'+login_of_user).encode())
        print(login_of_user)
        pass

    pass


class StudentMarksScreen(Screen):

    def fill_marks(self):
        s.send(('--get_marks--' + login_of_user).encode())
        time.sleep(1)
        self.ids.students_marks.clear_widgets()
        global student_marks
        a = 0
        mark_str =''
        if student_marks:
            for text in student_marks:
                a= a + 1
                mark_str = mark_str + text + ' '
                if a == 2:
                    self.lab = Label(text=mark_str)
                    self.ids.students_marks.add_widget(self.lab)
                    mark_str = ''
                    a = 0
        print("callback")
        print(student_marks)

        pass

    pass

class RegisterScreen(Screen):
    register_status = StringProperty()
    def registerNewUser(self, name,login,password,isTeacher):
        global login_of_user
        login_of_user = login
        if len(name)==0 or len(login)==0 or len(password) == 0:
            print(isTeacher)
            self.register_status = 'Пожалуйста, введите всю информацию'
        else:
            if isTeacher:
                isTeacher = str('1')
            else:
                isTeacher = str('0')
            s.send(('--register--' + str(name) + str('!=,/ds')+ str(login)+ str('!=,/ds') + str(password)+str('!=,/ds')+ str(isTeacher)).encode())
        pass

    def changeLabel(self,text):
        self.register_status = text
        pass



    pass


class MainScreen(Screen):
    global s
    def getListOfLections(self):
        s.send('--get_lections--'.encode())
        screen_manager.current = 'lection_screen'
        pass

    #toDo add logout button in kv
    def logout(self):
        #s.send('--quit--'.encode())
        screen_manager.current = 'screen_one'
        pass






class Tarefas(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ''

class Tarefa(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text
    def __del__(self):
        self.parent.remove_widget(self)
        #self.remove_widget(self.ids.label)
        #self.remove_widget(self.ids.button)




class TeacherScreenMain(Screen):
    pass



class AddLection(Screen):
    #bl = BoxLayout(orientation='horizontal', spacing=100)
    def addNewLection(self,nameOfLection, lection_text,question_1,question_2,question_3,question_4,answer_1,answer_2,answer_3,answer_4):
        stringToSend = '--add_lection--'+ nameOfLection + str('!=,/ds') + lection_text + str('!=,/ds')
        if question_1:
            stringToSend += question_1 + str('!=,/ds')
            stringToSend += answer_1 + str('!=,/ds')
        if question_2:
            stringToSend += question_2 + str('!=,/ds')
            stringToSend += answer_2 + str('!=,/ds')
        if question_3:
            stringToSend += question_3 + str('!=,/ds')
            stringToSend += answer_3 + str('!=,/ds')
        if question_4:
            stringToSend += question_4 + str('!=,/ds')
            stringToSend += answer_4 + str('!=,/ds')

        #s.send(('--add_lection--' +str(nameOfLection) + str('!=,/ds') + str(lection_text) + str('!=,/ds') + str(question_1) + str('!=,/ds') + str(question_2) + str('!=,/ds') + str(question_3)+ str('!=,/ds') + str(question_4) ).encode())
        print(stringToSend)
        s.send(stringToSend.encode())

        self.ids.name_of_lection .text = ''
        self.ids.lection_main.text = ''
        self.ids.question_1.text = ''
        self.ids.question_2.text = ''
        self.ids.question_3.text = ''
        self.ids.question_4.text = ''
        self.ids.input_1_answer.text = ''
        self.ids.input_2_answer.text = ''
        self.ids.input_3_answer.text = ''
        self.ids.input_4_answer.text = ''

    pass

class Journal(Screen):
    pass


class PredictionPoints(Screen):
    pass


class UserSettings(Screen):
    pass

# The ScreenManager controls moving between screens
screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(RegisterScreen(name="register_screen"))
screen_manager.add_widget(MainScreen(name="main_screen"))
screen_manager.add_widget(LectionScreen(name="lection_screen"))
screen_manager.add_widget(StudentMarksScreen(name="marks_screen"))
screen_manager.add_widget(TeacherScreenMain(name="teacher_screen"))
screen_manager.add_widget(AddLection(name="add_lection_screen"))
screen_manager.add_widget(Journal(name="journal_screen"))
screen_manager.add_widget(PredictionPoints(name="prediction_points_screen"))
screen_manager.add_widget(UserSettings(name="user_settings_screen"))


class KivyTut2App(App):

    def build(self):
        flag = True
        return screen_manager


if __name__ == '__main__':
    t = threading.Thread(target=getMes)
    t.start()
    KivyTut2App().run()
    print("Creating socket")




"""
code words for server

to quit and logout type  --quit--

to connect --connect--

to register --register--


"""

