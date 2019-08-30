from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import WindowBase
from kivy.uix.spinner import Spinner
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.graphics import Canvas
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import os

from kivy.config import Config

import sqlite3

path = r'C:/Users/capit/Documents/Bot'
conn = sqlite3.connect(path + '/bot.db')
cursor = conn.cursor()
cursor.execute("""
create table if not exists cadastro(
    id integer primary key autoincrement not null,
    login unique not null,
    senha not null,
    config integer default 0,
    rei_dos_imortais integer default 0,
    vale_dos_imortais integer default 0,
    altar_dos_deuses integer default 0,
    torneio_de_clas integer default 0,
    coliseu_de_clas integer default 0,
    anunciar_eventos integer default 0,
    doar_prata integer default 0,
    doar_gold integer default 0,
    masmorra integer default 0,
    arena integer default 0,
    cofre_pessoal integer default 0,
    campanha integer default 0,
    coletar_gold integer default 0
);
""")
cursor.execute("""
create table if not exists id_select(
    ident integer primary key autoincrement not null,
    name text unique default 0
);
""")
conn.commit()
x = cursor.execute("""
select * from id_select
;
""")
rows = x.fetchall()
print(rows)
if(rows==[]):
    path = r'C:/Users/capit/Documents/Bot'
    conn = sqlite3.connect(path + '/bot.db')
    cursor = conn.cursor()
    cursor.execute("""
     insert into id_select(name) Values(0)
    ;
    """)
    conn.commit()
    print("criada")
else:
    print("já existe")
    print(rows)



def select(oq, deq, x=None, y=None):
    cursor = conn.cursor()
    '''oq1= str(oq)
    deq1=str(deq)'''
    all = cursor.execute("""
    Select """ + str(oq) + """ from """ + str(deq) + """;
    """)
    rows = all.fetchall()
    if (x == None and y == None):
        return rows
    elif (x != None and y != None):
        return rows[int(x)][int(y)]
    elif (x != None and y == None):
        return rows[int(x)]


def select_where(oq, deq, b="", c="", f=None):
    cursor = conn.cursor()
    print("selecr_where")
    a = " "
    d = ""
    if (b != "" and c != ""):
        a = " Where "
        d = "=="
    all = cursor.execute("""
    Select """ + str(oq) + """ from """ + str(deq) + str(a) + str(b) + str(d) + str(c) + """
    ;""")
    rows = all.fetchall()
    z = 0
    y = []
    if (b == "" and c == ""):
        for v in rows:
            for x in v:
                y += [x]
        return y
    elif (b != "" and c == ""):
        print("falta argumentos")
    elif (b != "" and c != "" and f == None):
        for v in rows:
            y +=[v]
            return y[0]
    elif (b != "" and c != "" and f != None):
        for v in rows:
            for x in v:
                if (x == f):
                    return x


def update_cadastro(login, oq, deq):
    b = select_where('*','cadastro','login','"'+login+'"')
    print(b)
    path = r'C:/Users/capit/Documents/Bot'
    conn = sqlite3.connect(path + '/bot.db')
    cursor = conn.cursor()
    cursor.execute('update cadastro set "' + str(oq) + '"= "' + str(deq) + '" where login= "'+str(login)+'";')
    conn.commit()
    conn.close()
b=select_where('*','cadastro','login','"sss"')
print(b)
def insert_cadastro(tabela, a):
    if (tabela == "digite o login" or a == "digite a senha"):
        pass
    else:
        x = select_where('id', 'cadastro')
        if (1 not in x):
            id = 1
        elif (2 not in x):
            id = 2
        elif (3 not in x):
            id = 3
        elif (4 not in x):
            id = 4
        elif (5 not in x):
            id = 5
        elif (6 not in x):
            id = 6
        elif (7 not in x):
            id = 7
        elif (8 not in x):
            id = 8
        elif (9 not in x):
            id = 9
        print(x)
        path = r'C:/Users/capit/Documents/Bot'
        conn = sqlite3.connect(path + '/bot.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO cadastro("id","login", "senha") VALUES(?, ?, ?)', (str(id), str(tabela), str(a)))
        print(f'insert ok, inseridos {tabela} e {a}')
        conn.commit()
        conn.close()


def alter_cadastro(tabela, a, b):
    path = r'C:/Users/capit/Documents/Bot'
    conn = sqlite3.connect(path + '/bot.db')
    cursor = conn.cursor()
    cursor.execute('update cadastro set "senha" = "' + str(tabela) + '" WHERE ' + str(a) + ' = "' + str(b) + '"')
    conn.commit()
    conn.close()


def remove_cadastro(tabela, a):
    path = r'C:/Users/capit/Documents/Bot'
    conn = sqlite3.connect(path + '/bot.db')
    cursor = conn.cursor()
    cursor.execute("""Delete from cadastro
        where """ + tabela + '=="' + str(a) + '"'";")
    print(f'delet ok, removidos {tabela} e {a}')
    conn.commit()
    conn.close()


x = select_where('id', 'cadastro')
'''for e in x:
    print(e)
print(x)'''

Config.set("graphics", "fullscreen", 0)


# os.startfile('chrome')
class CustomDropDown(DropDown):
    pass


class Main(Screen, object):
    pass


class Alerta_limit(FloatLayout):
    cancel = ObjectProperty(None)


class Alerta_nchange(FloatLayout):
    cancel = ObjectProperty(None)


class Alerta_existe(FloatLayout):
    cancel = ObjectProperty(None)


class Alerta_criated(FloatLayout):
    cancel = ObjectProperty(None)


class Alerta_start(FloatLayout):
    cancel = ObjectProperty(None)


class Alerta_config(FloatLayout):
    cancel = ObjectProperty(None)


class ScrollAdd(BoxLayout):
    pass


mudar = False


class Bot(Screen):
    def att_bd(self):
        print("bd apagado")
        if (True):
            self.ids.bd_login.clear_widgets()
            self.ids.bd_senha.clear_widgets()
            self.ids.bd_remove.clear_widgets()
        if (True):
            t = select('*', 'cadastro')
            print(t)
            for x in t:
                if (x == []):
                    print("bd vazio")
                elif (x[0] == 1):
                    ident = 'btn1'
                    func = self.remove_bd
                    self.login1 = Button(id=x[1], text=x[1], size=(2, 40), size_hint=(1, None),
                                         on_press=self.alter_senha1)
                    self.ids.bd_login.add_widget(self.login1)
                    self.senha1 = Button(id=x[2], text=x[2], size=(2, 40), size_hint=(1, None))
                    self.ids.bd_senha.add_widget(self.senha1)
                    self.btn1 = Button(id=ident, text=str(x[0]), size=(2, 40), size_hint=(1, None), on_press=func)
                    self.ids.bd_remove.add_widget(self.btn1)
                elif (x[0] == 2):
                    ident = 'btn2'
                    func = self.remove_bd2
                    self.login2 = Button(id=x[1], text=x[1], size=(2, 40), size_hint=(1, None),
                                         on_press=self.alter_senha2)
                    self.ids.bd_login.add_widget(self.login2)
                    self.senha2 = Button(id=x[2], text=x[2], size=(2, 40), size_hint=(1, None))
                    self.ids.bd_senha.add_widget(self.senha2)
                    self.btn2 = Button(id=ident, text=str(x[0]), size=(2, 40), size_hint=(1, None), on_press=func)
                    self.ids.bd_remove.add_widget(self.btn2)
                elif (x[0] == 3):
                    ident = 'btn3'
                    func = self.remove_bd3
                    self.login3 = Button(id=x[1], text=x[1], size=(2, 40), size_hint=(1, None),
                                         on_press=self.alter_senha3)
                    self.ids.bd_login.add_widget(self.login3)
                    self.senha3 = Button(id=x[2], text=x[2], size=(2, 40), size_hint=(1, None))
                    self.ids.bd_senha.add_widget(self.senha3)
                    self.btn3 = Button(id=ident, text=str(x[0]), size=(2, 40), size_hint=(1, None), on_press=func)
                    self.ids.bd_remove.add_widget(self.btn3)
                elif (x[0] == 4):
                    ident = 'btn4'
                    func = self.remove_bd4
                    self.login4 = Button(id=x[1], text=x[1], size=(2, 40), size_hint=(1, None),
                                         on_press=self.alter_senha4)
                    self.ids.bd_login.add_widget(self.login4)
                    self.senha4 = Button(id=x[2], text=x[2], size=(2, 40), size_hint=(1, None))
                    self.ids.bd_senha.add_widget(self.senha4)
                    self.btn4 = Button(id=ident, text=str(x[0]), size=(2, 40), size_hint=(1, None), on_press=func)
                    self.ids.bd_remove.add_widget(self.btn4)
                elif (x[0] == 5):
                    ident = 'btn5'
                    func = self.remove_bd5
                    self.login5 = Button(id=x[1], text=x[1], size=(2, 40), size_hint=(1, None),
                                         on_press=self.alter_senha5)
                    self.ids.bd_login.add_widget(self.login5)
                    self.senha5 = Button(id=x[2], text=x[2], size=(2, 40), size_hint=(1, None))
                    self.ids.bd_senha.add_widget(self.senha5)
                    self.btn5 = Button(id=ident, text=str(x[0]), size=(2, 40), size_hint=(1, None), on_press=func)
                    self.ids.bd_remove.add_widget(self.btn5)
                elif (x[0] == 6):
                    ident = 'btn6'
                    func = self.remove_bd6
                    self.login6 = Button(id=x[1], text=x[1], size=(2, 40), size_hint=(1, None),
                                         on_press=self.alter_senha6)
                    self.ids.bd_login.add_widget(self.login6)
                    self.senha6 = Button(id=x[2], text=x[2], size=(2, 40), size_hint=(1, None))
                    self.ids.bd_senha.add_widget(self.senha6)
                    self.btn6 = Button(id=ident, text=str(x[0]), size=(2, 40), size_hint=(1, None), on_press=func)
                    self.ids.bd_remove.add_widget(self.btn6)
                elif (x[0] == 7):
                    ident = 'btn7'
                    func = self.remove_bd7
                    self.login7 = Button(id=x[1], text=x[1], size=(2, 40), size_hint=(1, None),
                                         on_press=self.alter_senha7)
                    self.ids.bd_login.add_widget(self.login7)
                    self.senha7 = Button(id=x[2], text=x[2], size=(2, 40), size_hint=(1, None))
                    self.ids.bd_senha.add_widget(self.senha7)
                    self.btn7 = Button(id=ident, text=str(x[0]), size=(2, 40), size_hint=(1, None), on_press=func)
                    self.ids.bd_remove.add_widget(self.btn7)
                elif (x[0] == 8):
                    ident = 'btn8'
                    func = self.remove_bd8
                    self.login8 = Button(id=x[1], text=x[1], size=(2, 40), size_hint=(1, None),
                                         on_press=self.alter_senha8)
                    self.ids.bd_login.add_widget(self.login8)
                    self.senha8 = Button(id=x[2], text=x[2], size=(2, 40), size_hint=(1, None))
                    self.ids.bd_senha.add_widget(self.senha8)
                    self.btn8 = Button(id=ident, text=str(x[0]), size=(2, 40), size_hint=(1, None), on_press=func)
                    self.ids.bd_remove.add_widget(self.btn8)
                elif (x[0] == 9):
                    ident = 'btn9'
                    func = self.remove_bd9
                    self.login9 = Button(id=x[1], text=x[1], size=(2, 40), size_hint=(1, None),
                                         on_press=self.alter_senha9)
                    self.ids.bd_login.add_widget(self.login9)
                    self.senha9 = Button(id=x[2], text=x[2], size=(2, 40), size_hint=(1, None))
                    self.ids.bd_senha.add_widget(self.senha9)
                    self.btn9 = Button(id=ident, text=str(x[0]), size=(2, 40), size_hint=(1, None), on_press=func)
                    self.ids.bd_remove.add_widget(self.btn9)
                    print(x[0])
                print("terminado")

    def alter_senha(self):
        print(self.ids.login.text)
        print(self.ids.senha.text)
        alter_cadastro(self.ids.senha.text, 'login', self.ids.login.text)

    def alter_senha1(self, var):
        global config_setup
        self.ids.login.text = self.login1.text
        self.ids.start.text = "iniciar bot: " + self.login1.text
        self.ids.start.name = self.login1.text
        config_setup = self.login1.text


    def alter_senha2(self, var):
        global config_setup
        self.ids.login.text = self.login2.text
        self.ids.start.text = "iniciar bot: " + self.login2.text
        self.ids.start.name = self.login2.text
        config_setup = self.login2.text

    def alter_senha3(self, var):
        global config_setup
        self.ids.login.text = self.login3.text
        self.ids.start.text = "iniciar bot: " + self.login3.text
        self.ids.start.name = self.login3.text
        config_setup = self.login3.text

    def alter_senha4(self, var):
        global config_setup
        self.ids.login.text = self.login4.text
        self.ids.start.text = "iniciar bot: " + self.login4.text
        self.ids.start.name = self.login4.text
        config_setup = self.login4.text

    def alter_senha5(self, var):
        global config_setup
        self.ids.login.text = self.login5.text
        self.ids.start.text = "iniciar bot: " + self.login5.text
        self.ids.start.name = self.login5.text
        config_setup = self.login5.text

    def alter_senha6(self, var):
        global config_setup
        self.ids.login.text = self.login6.text
        self.ids.start.text = "iniciar bot: " + self.login6.text
        self.ids.start.name = self.login6.text
        config_setup = self.login6.text

    def alter_senha7(self, var):
        global config_setup
        self.ids.login.text = self.login7.text
        self.ids.start.text = "iniciar bot: " + self.login7.text
        self.ids.start.name = self.login7.text
        config_setup = self.login7.text

    def alter_senha8(self, var):
        global config_setup
        self.ids.login.text = self.login8.text
        self.ids.start.text = "iniciar bot: " + self.login8.text
        self.ids.start.name = self.login8.text
        config_setup = self.login8.text

    def alter_senha9(self, var):
        global config_setup
        self.ids.login.text = self.login9.text
        self.ids.start.text = "iniciar bot: " + self.login9.text
        self.ids.start.name = self.login9.text
        config_setup = self.login9.text

    def remove_bd(self, var):
        print(var)
        print('remove')
        t = select('*', 'cadastro')
        for x in t:
            if (x[0] == 1):
                remove_cadastro('id', '1')
                self.ids.bd_login.remove_widget(self.login1)
                self.ids.bd_senha.remove_widget(self.senha1)
                self.ids.bd_remove.remove_widget(self.btn1)
            print(x)

    def remove_bd2(self, var):
        print(var)
        print('remove 2')
        t = select('*', 'cadastro')
        for x in t:
            if (x[0] == 2):
                remove_cadastro('id', '2')
                self.ids.bd_login.remove_widget(self.login2)
                self.ids.bd_senha.remove_widget(self.senha2)
                self.ids.bd_remove.remove_widget(self.btn2)
            print(x)

    def remove_bd3(self, var):
        print(var)
        print('remove 3')
        t = select('*', 'cadastro')
        for x in t:
            if (x[0] == 3):
                remove_cadastro('id', '3')
                self.ids.bd_login.remove_widget(self.login3)
                self.ids.bd_senha.remove_widget(self.senha3)
                self.ids.bd_remove.remove_widget(self.btn3)
                print(x[0])
            print(x)

    def remove_bd4(self, var):
        print(var)
        print('remove 4')
        t = select('*', 'cadastro')
        for x in t:
            if (x[0] == 4):
                remove_cadastro('id', '4')
                self.ids.bd_login.remove_widget(self.login4)
                self.ids.bd_senha.remove_widget(self.senha4)
                self.ids.bd_remove.remove_widget(self.btn4)
                print(x[0])
            print(x)

    def remove_bd5(self, var):
        print(var)
        print('remove 5')
        t = select('*', 'cadastro')
        for x in t:
            if (x[0] == 5):
                remove_cadastro('id', '5')
                self.ids.bd_login.remove_widget(self.login5)
                self.ids.bd_senha.remove_widget(self.senha5)
                self.ids.bd_remove.remove_widget(self.btn5)
                print(x[0])
            print(x)

    def remove_bd6(self, var):
        print(var)
        print('remove 6')
        t = select('*', 'cadastro')
        for x in t:
            if (x[0] == 6):
                remove_cadastro('id', '6')
                self.ids.bd_login.remove_widget(self.login6)
                self.ids.bd_senha.remove_widget(self.senha6)
                self.ids.bd_remove.remove_widget(self.btn6)
                print(x[0])
            print(x)

    def remove_bd7(self, var):
        print(var)
        print('remove 7')
        t = select('*', 'cadastro')
        for x in t:
            if (x[0] == 7):
                remove_cadastro('id', '7')
                self.ids.bd_login.remove_widget(self.login7)
                self.ids.bd_senha.remove_widget(self.senha7)
                self.ids.bd_remove.remove_widget(self.btn7)
                print(x[0])
            print(x)

    def remove_bd8(self, var):
        print(var)
        print('remove 8')
        t = select('*', 'cadastro')
        for x in t:
            if (x[0] == 8):
                remove_cadastro('id', '8')
                self.ids.bd_login.remove_widget(self.login8)
                self.ids.bd_senha.remove_widget(self.senha8)
                self.ids.bd_remove.remove_widget(self.btn8)
                print(x[0])
            print(x)

    def remove_bd9(self, var):
        print(var)
        print('remove 9')
        t = select('*', 'cadastro')
        for x in t:
            if (x[0] == 9):
                remove_cadastro('id', '9')
                self.ids.bd_login.remove_widget(self.login9)
                self.ids.bd_senha.remove_widget(self.senha9)
                self.ids.bd_remove.remove_widget(self.btn9)
                print(x[0])
            print(x)

    def add(self):
        print("dentro")
        f = select_where('*', 'cadastro', 'login', '"' + self.ids.login.text + '"')
        print("saiu do where")
        r = select_where('id', 'cadastro')
        print(r)
        limit = False
        if (r != []):
            if (len(r) >= 9):
                limit = True
        if (limit == True):
            content = Alerta_limit(cancel=self.dismiss_popup)
            self._popup = Popup(title="Setup", content=content,
                                size_hint=(0.5, 0.5))
            self._popup.open()
            print("alerta_limite")
        elif (self.ids.login.text == "digite o login" or self.ids.senha.text == "digite a senha"):
            content = Alerta_nchange(cancel=self.dismiss_popup)
            self._popup = Popup(title="Setup", content=content,
                                size_hint=(0.5, 0.5))
            self._popup.open()
        elif (f == None):
            insert_cadastro(self.ids.login.text, self.ids.senha.text)
            content = Alerta_criated(cancel=self.dismiss_popup)
            self._popup = Popup(title="Setup", content=content,
                                size_hint=(0.5, 0.5))
            self._popup.open()
        elif (f != None):
            content = Alerta_existe(cancel=self.dismiss_popup)
            self._popup = Popup(title="Alert", content=content,
                                size_hint=(0.5, 0.5))
            self._popup.open()

    def dismiss_popup(self):
        self._popup.dismiss()

    cancel = ObjectProperty(None)

    def open_config(self):
        global config_setup
        if(config_setup == False):
            content = Alerta_start(cancel=self.dismiss_popup)
            self._popup = Popup(title="Alert", content=content,
                                size_hint=(0.5, 0.5))
            self._popup.open()
        else:
            self.manager.current = "bot_config"

    def iniciar_bot(self):

        if(self.ids.start.name == "nome do start"):

            content = Alerta_start(cancel=self.dismiss_popup)
            self._popup = Popup(title="Alert", content=content,
                                size_hint=(0.5, 0.5))
            self._popup.open()
        elif(select_where('*', 'cadastro', 'login', '"' + self.ids.start.name + '"')[3] == 0):
            print("alerta_config")
            content = Alerta_config(cancel=self.dismiss_popup)
            self._popup = Popup(title="Alert", content=content,
                                size_hint=(0.5, 0.5))
            self._popup.open()
        elif(select_where('*', 'cadastro', 'login', '"' + self.ids.start.name + '"')[3] == 1):
            global config_setup, login_bot, senha_bot
            s = select_where('*', 'cadastro', 'login', '"' + self.ids.start.name + '"')
            print(s)
            path = r'C:/Users/capit/Documents/Bot'
            conn = sqlite3.connect(path + '/bot.db')
            cursor = conn.cursor()
            cursor.execute('''update id_select set 
            "name"= "''' + self.ids.start.name + '" where ident= 1;')
            x = cursor.execute("""select * from id_select
            ;""")
            rows = x.fetchall()
            print(rows)
            print("alterado")
            conn.commit()
            conn.close()
            os.startfile('bot.py')



class Bot_Config(Screen):
    def active_atr(self):
        global rei_dos_imortais, vale_dos_imortais, altar_dos_deuses, torneio_de_clas, coliseu_de_clas, anunciar_eventos, doar_prata,\
            doar_gold, masmorra, config_setup, is_att_config
        if(is_att_config==False):
            y="Config a mudar: "
            self.ids.config_login.text = y + config_setup
            is_att_config=True

    def save_config(self):
        global config_setup
        update_cadastro(config_setup, 'config', 1)
        if (self.ids.rei_dos_imortais.active == True):
            update_cadastro(config_setup, 'rei_dos_imortais', 1)
        else:
            update_cadastro(config_setup, 'rei_dos_imortais', 0)
        if (self.ids.vale_dos_imortais.active == True):
            update_cadastro(config_setup, 'vale_dos_imortais', 1)
        else:
            update_cadastro(config_setup, 'vale_dos_imortais', 0)
        if (self.ids.altar_dos_deuses.active == True):
            update_cadastro(config_setup, 'altar_dos_deuses', 1)
        else:
            update_cadastro(config_setup, 'altar_dos_deuses', 0)
        if (self.ids.torneio_de_clas.active == True):
            update_cadastro(config_setup, 'torneio_de_clas', 1)
        else:
            update_cadastro(config_setup, 'torneio_de_clas', 0)
        if(self.ids.coliseu_de_clas.active== True):
            update_cadastro(config_setup, 'coliseu_de_clas', 1)
        else:
            update_cadastro(config_setup, 'coliseu_de_clas', 0)
        if (self.ids.anunciar_eventos.active == True):
            update_cadastro(config_setup, 'anunciar_eventos', 1)
        else:
            update_cadastro(config_setup, 'anunciar_eventos', 0)
        if (self.ids.doar_prata.active == True):
            update_cadastro(config_setup, 'doar_prata', 1)
        else:
            update_cadastro(config_setup, 'doar_prata', 0)
        if (self.ids.doar_gold.active == True):
            update_cadastro(config_setup, 'doar_gold', 1)
        else:
            update_cadastro(config_setup, 'doar_gold', 0)
        if (self.ids.masmorra.active == True):
            update_cadastro(config_setup, 'masmorra', 1)
        else:
            update_cadastro(config_setup, 'masmorra', 0)
        if (self.ids.arena.active == True):
            update_cadastro(config_setup, 'arena', 1)
        else:
            update_cadastro(config_setup, 'arena', 0)
        if (self.ids.cofre_pessoal.active == True):
            update_cadastro(config_setup, 'cofre_pessoal', 1)
        else:
            update_cadastro(config_setup, 'cofre_pessoal', 0)
        if (self.ids.campanha.active == True):
            update_cadastro(config_setup, 'campanha', 1)
        else:
            update_cadastro(config_setup, 'campanha', 0)
        if (self.ids.coletar_gold.active == True):
            update_cadastro(config_setup, 'coletar_gold', 1)
        else:
            update_cadastro(config_setup, 'coletar_gold', 0)

    def reset(self):
        global config_setup, is_att_config
        config_setup = False
        is_att_config = False
        self.manager.current = "bot"

config_setup=False
is_att_config= False

class Att_hack(Screen):
    pass


class Alerta(Screen):
    pass


class WindowManager(ScreenManager, object):
    pass


screen_manager = ScreenManager()
screen_manager.add_widget(Main())
kv_file = Builder.load_file("manager.kv")


class Editor(App):
    def build(self):
        return kv_file


if __name__ == '__main__':
    Editor().run()

conn.close()
