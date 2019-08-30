import sqlite3
import time
import datetime
from datetime import datetime
from datetime import date
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = r'C:/Users/capit/Documents/Bot'
conn = sqlite3.connect(path + '/bot.db')
cursor = conn.cursor()
x = cursor.execute("""select * from id_select
            ;""")
for i in x:
    login_bot = i[1]
    print(login_bot)

def select_where(oq, deq, b="", c="", f=None):
    path = r'C:/Users/capit/Documents/Bot'
    conn = sqlite3.connect(path + '/bot.db')
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
            y += [v]
            return y[0]
    elif (b != "" and c != "" and f != None):
        for v in rows:
            for x in v:
                if (x == f):
                    return x


y = select_where('*', 'cadastro', 'login', '"' + login_bot + '"')
print(y)
senha_bot = y[2]
config_setup = y[3]
rei_dos_imortais = y[4]
vale_dos_imortais = y[5]
altar_dos_deuses = y[6]
torneio_de_clas = y[7]
coliseu_de_clas = y[8]
anunciar_eventos = y[9]
doar_prata = y[10]
doar_gold = y[11]
masmorra = y[12]
arena = y[13]
cofre_pessoal= y[14]
campanha = y[15]
coletar_gold = y[16]
anunciar_rei = 0
anunciar_tc = 0
anunciar_coliseu = 0
anunciar_altar = 0
anunciar_vale = 0
energia= 0

running = True
print(senha_bot, config_setup, rei_dos_imortais, vale_dos_imortais, altar_dos_deuses, torneio_de_clas,
      anunciar_eventos, doar_prata, doar_gold, masmorra)

def horaminsec():
    day = date.today()
    hora = datetime.now().hour
    min = datetime.now().minute
    sec = datetime.now().second
    return [hora] + [min] + [sec] + [day]

def att_arena():
    driver.get('http://furiadetitas.net/arena')
    try:
        vid_mana = driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[1]/span[2]").text
    except:
        vid_mana = driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[1]/span/span").text
    vida = ""
    mana = ""
    count = 0
    if (vid_mana[0] == "|" and vid_mana[2] == "|"):
        for i in vid_mana[4:]:
            if (i != "|" and count == 0):
                if (i == " "):
                    pass
                else:
                    vida += i
            if (i == "|"):
                count = 1
            if (i != "|" and count == 1):
                if (i == " "):
                    pass
                else:
                    mana += i
    elif (vid_mana[0] == "|"):
        for i in vid_mana[2:]:
            if (i != "|" and count == 0):
                if (i == " "):
                    pass
                else:
                    vida += i
            if (i == "|"):
                count = 1
            if (i != "|" and count == 1):
                if (i == " "):
                    pass
                else:
                    mana += i
    else:
        for i in vid_mana:
            if (i != "|" and count == 0):
                if (i == " "):
                    pass
                else:
                    vida += i
            if (i == "|"):
                count = 1
            if (i != "|" and count == 1):
                if (i == " "):
                    pass
                else:
                    mana += i
    try:
        vida=int(vida)
        mana=int(mana)
    except:
        pass
    return int(vida), int(mana)

def att_poder():
    driver.get('http://furiadetitas.net/user/?show=might')
    try:
        driver.find_element_by_link_text("Esconder").click()
    except Exception as ee:
        print(ee)
    driver.get('http://furiadetitas.net/user/?show=might')
    time.sleep(1)
    z = driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[5]").text
    print(z.find(":"))
    count = 0
    forca = ""
    saude = ""
    agilidade = ""
    protecao = ""
    energia = ""
    x = False
    for i in z:
        if (True):
            if (i == " "):
                print("primeiro espaco")
            elif (i == ":" or i == " :" or i == ": "):
                count += 1
                print(count, "count")
            else:
                if (i == "S"):
                    count += 1
                    forca = forca
                    print(forca, type(forca))
                if (i == "A"):
                    count += 1
                    print(saude)
                if (i == "P"):
                    count += 1
                    print(agilidade)
                if (i == "E"):
                    count += 1
                    print(protecao)
                if (count == 1 and i != "\n"):
                    forca += i
                if (count == 3 and i != "\n"):
                    saude += i
                if (count == 5 and i != "\n"):
                    agilidade += i
                if (count == 7 and i != "\n"):
                    protecao += i
                if (count == 9 and i != "\n"):
                    energia += i
    return [int(forca)] + [int(saude)] + [int(agilidade)] + [int(protecao)] + [int(energia)]

def masmorra_start():
    z = 1
    while (z == 1):
        try:
            driver.get('https://furiadetitas.net/clandungeon')
            try:
                driver.find_element_by_link_text("Esconder").click()
            except:
                try:
                    driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div/a/span/span").click()
                except:
                    try:
                        x = driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[8]").text
                        if (x[0] == "N"):
                            z = 0
                        else:
                            c = driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[8]/a/span/span").click()
                            time.sleep(2)
                    except:
                        pass
        except Exception as ee:
            print(ee)

'''
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("--disable-gpu")
#options.binary_location = 'C:\\Program Files (x86)\\Google\\Chrome\\Application'
'''
driver = webdriver.Chrome('C:\\Users\\capit\Documents\\Bot\\chromedriver.exe')#, chrome_options=options)
driver.get("http://furiadetitas.net/?sign_in=1")
# driver.maximize_window()
driver.find_element_by_name("login").send_keys(login_bot)  # login
driver.find_element_by_name("pass").send_keys(senha_bot)  # senha
driver.find_element_by_xpath("//span//input").click()  # subimit_login
time.sleep(2)
try:
    x = driver.find_element_by_xpath("//span//input").text
except:
    print("login efetuado")
    #driver.minimize_window()
else:
    print("login não efetuado!! Motivo:  dados incorretos")
    exit()
atributos = att_poder()
print(type(atributos[1] / 5))
print(type(att_arena()[0]))

def att_masmorra():
    driver.get('https://furiadetitas.net/clandungeon')
    z=1
    while(z==1):
        try:
            driver.find_element_by_link_text("Esconder").click()
        except:
            try:
                time.sleep(0.5)
                driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[3]/div/a[1]").click()
            except:
                try:
                    driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[3]/div/a[1]/span").click()
                except:
                    try:
                        driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div/a/span/span").click()
                    except:
                        x = driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[8]").text
                        print(x)
                        if (x[0] == "N"):
                            c = driver.find_element_by_xpath("//div[8]/span/span").text
                            try:
                                time_masmorra = [c[0] + c[1]] + [c[3] + c[4]] + [c[6] + c[7]]
                            except:
                                time_masmorra = [0] + [c[0] + c[1]] + [c[3] + c[4]]
                            t_masmorra = [int(time_masmorra[0]) + horaminsec()[0]] + [int(time_masmorra[1]) + horaminsec()[1]] + [
                                int(time_masmorra[2]) + horaminsec()[2]] + [horaminsec()[3].day]
                            if (t_masmorra[2] >= 60):
                                t_masmorra[2] = t_masmorra[2] - 60
                                t_masmorra[1] += 1
                            if (t_masmorra[1] >= 60):
                                t_masmorra[1] = t_masmorra[1] - 60
                                t_masmorra[0] += 1
                            if (t_masmorra[0] > 23):
                                t_masmorra[0] = t_masmorra[0] - 24
                                r = horaminsec()[3] + timedelta(days=1)
                                print(r, "dia de amanhã")
                                print(horaminsec()[3].day, "dia de hoje")
                                t_masmorra[3] = r.day
                            print(t_masmorra)
                            z=0
                        else:
                            print("hora da masmorra")
                            t_masmorra = [0, 0, 0, horaminsec()[3].day]
                            z=0
    return t_masmorra

def campanha_start():
    while (True):
        try:
            try:
                driver.get('http://furiadetitas.net/campaign/')
                driver.find_element_by_xpath("//a/span/span").click()  # iniciar campanha
                time.sleep(1)
                driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div[3]/a[2]/span/span").click()  # lutar
                time.sleep(1)
            except:
                try:
                    driver.find_element_by_xpath(
                        "//div[@id='topdiv']/div/div[3]/div[3]/div/a/span/span").click()  # atacar
                    time.sleep(3)
                except:
                    try:
                        driver.find_element_by_xpath(
                            "//div[@id='topdiv']/div/div[3]/div[3]/div/a/span/span/span").click()  # receber recompensa
                        time.sleep(3)
                        driver.find_element_by_xpath(
                            "//div[@id='topdiv']/div/div[3]/div/a/span/span").click()  # voltar para campanha
                        print("campanha realizada")
                    except:
                        print("campanhas realizadas")
                        break
        except Exception as ee:
            print(ee)
            break

print(masmorra, "masmorra_is")
if (masmorra == 1):
    time_masmorra = att_masmorra()
    print("masmorra atualizada")

def att_campanha():  # //*[@id="topdiv"]/div[1]/div[3]/div/a[1] vá para masmorra(quando termina o tempo)
    try:
        try:
            day = horaminsec()[3].day
            time_campanha = [0, 0, 0, day]
            driver.get('http://furiadetitas.net/campaign/')
            try:
                y = driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[3]/div[5]").text
                print(y)
            except:
                y=""
            if (y[-1] == "1"):
                time_campanha = [0, 0, 0, day]
            elif (y[-1] == "2"):
                time_campanha = [0, 0, 0, day]
            elif (y[-1] == "3"):
                time_campanha = [0, 0, 0, day]
            else:
                x = driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div[5]/span").text
                print(x)
                print("passou dos try")
                if (x[-1] == "n" and x[-8:-7]=="h"):  # 0987654321
                    print(x[-1])                      # 7 h 35 min
                    time_campanha[2] = 0
                    time_campanha[1] = int(x[-6:-4])
                    time_campanha[0] = int(x[-10:-9])
                    timee = horaminsec()
                    print(timee)
                    time_campanha = [timee[0] + time_campanha[0]] + [timee[1] + time_campanha[1]] + [
                        timee[2] + time_campanha[2]] + [day]
                    print(time_campanha)
                    print(time_campanha)
                    print("7h 35 min exemplo ")       # 987654321
                elif(x[-1] == "n" and x[-7:-6]=="h"):  # 3 h 3 min
                    print(x[-1])
                    time_campanha[2] = 0
                    time_campanha[1] = int(x[-5:-4])
                    time_campanha[0] = int(x[-9:-8])
                    timee = horaminsec()
                    print(timee)
                    time_campanha = [timee[0] + time_campanha[0]] + [timee[1] + time_campanha[1]] + [
                        timee[2] + time_campanha[2]] + [day]
                    print(time_campanha)
                    print(time_campanha)
                    print("3 h 3 min exemplo")
                elif(x[-1] == "h"):  # 3 h
                    print(x[-1])
                    time_campanha[2] = 0
                    time_campanha[1] = 1
                    time_campanha[0] = int(x[-3:-2])
                    timee = horaminsec()
                    print(timee)
                    time_campanha = [timee[0] + time_campanha[0]] + [timee[1] + time_campanha[1]] + [
                        timee[2] + time_campanha[2]] + [day]
                    print(time_campanha)
                    print(time_campanha)
                    print("3 h exemplo")
                elif(x[-1] == "g" and x[-8:-7]=="m" and x[-11:-10]!=" "):  # 10987654321
                    print(x[-1])                                              # 43 m 22 seg
                    time_campanha[2] = int(x[-6:-4])
                    time_campanha[1] = int(x[-11:-9])
                    time_campanha[0] = 0
                    timee = horaminsec()
                    print(timee)
                    time_campanha = [timee[0] + time_campanha[0]] + [timee[1] + time_campanha[1]] + [
                        timee[2] + time_campanha[2]] + [day]
                    print(time_campanha)
                    print("43 m 22 seg exemplo")
                                # 10987654321
                                 # 3 m 22 seg
                elif(x[-1] == "g" and x[-8:-7]=="m" and x[-11:-10]==" "):
                    time_campanha[2] = int(x[-6:-4])
                    time_campanha[1] = int(x[-10:-9])
                    time_campanha[0] = 0
                    timee = horaminsec()
                    print(timee)
                    time_campanha = [timee[0] + time_campanha[0]] + [timee[1] + time_campanha[1]] + [
                        timee[2] + time_campanha[2]] + [day]
                    print(time_campanha)
                    print("3 m 22 seg exemplo")
                elif (x[-1] == "g" and x[-7:-6]=="m"):
                    time_campanha[2] = int(x[-5:-4])
                    time_campanha[1] = int(x[-9:-8])
                    time_campanha[0] = 0
                    timee = horaminsec()
                    print(timee)
                    time_campanha = [timee[0] + time_campanha[0]] + [
                        timee[1] + time_campanha[1]] + [
                                        timee[2] + time_campanha[2]] + [day]
                    print(time_campanha)
                    print("4 m 2 seg exemplo")
                elif(x[-1] == "g" and x[-7:-6!="m"]):  # 2 seg
                    time_campanha[2] = int(x[-5:-4])
                    time_campanha[1] = 1
                    time_campanha[0] = 0
                    timee = horaminsec()
                    print(timee)
                    time_campanha = [timee[0] + time_campanha[0]] + [
                        timee[1] + time_campanha[1]] + [
                                        timee[2] + time_campanha[2]] + [day]
                    print(time_campanha)
                    print("2 seg exemplo")
        except Exception as ee:
            print(ee, "dentro do segundo try")
    except Exception as fe:
        print(fe)
    if (time_campanha[2] >= 60):
        time_campanha[2] -= 60
        time_campanha[1] += 1
    if (time_campanha[2] >= 30):
        time_campanha[2] = 0
        time_campanha[1] += 1
    if (time_campanha[1] >= 60):
        time_campanha[1] -= 60
        time_campanha[0] += 1
    if (time_campanha[1] >= 40):
        time_campanha[1] = 0
        time_campanha[0] += 1
    if (time_campanha[0] > 24):
        time_campanha[0] -= 24
        r = date.today() + timedelta(days=1)
        time_campanha[3] = r.day
    print(time_campanha, "time campanha antes do retorno")
    return time_campanha

if (campanha == 1):
    time_campanha = att_campanha()
    print("time campanha", time_campanha)

driver.get("https://furiadetitas.net/clan/e/money/")
s = driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[5]").text
print(s)
prata = ""
gold = ""
count = 0
try:
    if (s[0] == "C"):
        z = driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[11]/span").text
    else:
        z = driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[9]/span").text
except:
    print("sem clã")
for i in z:
    if (i == " "):
        print("primeiro espaco")
    elif (i == ":" or i == " :" or i == ": "):
        count += 1
        print(count, "count")
    else:
        if (i == "P"):
            count += 1
        if (count == 1 and i != "\n"):
            gold += i
        if (count == 3 and i != "\n"):
            prata += i

if (doar_prata == 1):
    print(type(driver.find_element_by_name("silver").clear()))
    driver.find_element_by_name("silver").clear()
    driver.find_element_by_name("silver").send_keys(prata)
if (doar_gold == 1):
    driver.find_element_by_name("gold").clear()
    driver.find_element_by_name("gold").send_keys(gold)
driver.find_element_by_xpath("//input[@value='Financiar a tesouraria']").click()
if (doar_gold == 1 and int(gold) != 0):
    x = driver.find_element_by_link_text("Sim, com certeza").click()

print(prata, "prata")
time.sleep(1)
dia_ouro = day_event =horaminsec()[3].day

def ouro_diario():
    driver.get('http://furiadetitas.net/trade/exchange')
    try:
        driver.find_element_by_xpath("//div[@id='topdiv']/div/div[7]/li/a").click()
    except Exception as ee:
        print(ee)
    r = date.today() + timedelta(days=1)
    dia = r.day
    return dia

def anunciar(texto):
    driver.get('http://furiadetitas.net/clan/')
    while (True):
        try:
            try:
                driver.find_element_by_link_text("Ocultar clã gestão").click()
            except:
                driver.find_element_by_link_text("Gerenciar o clã").click()
                time.sleep(1)
                driver.find_element_by_name("text").clear()
                driver.find_element_by_name("text").send_keys(texto)
                driver.find_element_by_xpath("//input[@value='Enviar']").click()
                driver.find_element_by_link_text("Esconder").click()
                print("texto anunciado")
                break
        except Exception as ee:
            print(ee, "não tem permissão para anunciar(cargo inferior)")
            break


def att_cofre():
    count = 0
    energia = ""
    try:
        driver.get("http://furiadetitas.net/quest/")
        try:
            x = driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[3]").text
            print(x)
            for i in x:
                if (i == " "):
                    pass
                else:
                    if ((count == 2 or count == 3) and (i == "d" or i == "e")):
                        count += 1
                    if (i == "P"):
                        count += 1
                    if (count == 2 and i != "'"):
                        energia += i
                    if (i == ":"):
                        count += 1
            try:
                x = driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/span/span").text
            except:
                x = driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[3]").text
            bau_bronze = 0
            bau_prata = 0
            print(x[0:4])
            if (x == "Cofre de bronze"):
                print("cofre de bronze")
                pass
            elif (x == "Cofre de prata"):
                print("cofre de prata")
                bau_bronze = 1
                bau_prata = 0
            elif(x[0:4] =="Abra"):
                print("abra")
                bau_bronze = 0
                bau_prata = 0
            else:
                bau_bronze = 1
                bau_prata = 1
            try:
                energia = int(energia)
            except:
                energia = 99999
            print(energia)
            return bau_bronze, bau_prata, energia
        except Exception as ee:
            print(ee)
            print("error cofre pessoal")
    except Exception as ee:
        print(ee)
while (running == True):
    try:
        time.sleep(1)
        driver.find_element_by_link_text("Esconder").click()
    except:
        try:
            timee = horaminsec()
            if(day_event==timee[3].day):
                if (cofre_pessoal == 1):
                    bau= att_cofre()
                    bau_bronze=bau[0]
                    bau_prata=bau[1]
                    energia=bau[2]
                    print(bau_bronze, bau_prata, energia, "att cofre")
                driver.get("http://furiadetitas.net/settings/")
                try:
                    driver.find_element_by_xpath("//a[contains(@href, '/settings/graphics/0')]").click()
                except:
                    print("graphics já ativado")
                else:
                    print("graphics ativado")
                r = date.today() + timedelta(days=1)
                day_event = r.day

            if(anunciar_eventos==1):  #(anunciar_eventos == 1): anunciar_evento (0) testa todos
                if (timee[0] == 12 and (timee[1] >= 23 and timee[1] < 29)) or (timee[0] == 16 and
                                                                               (timee[1] >= 23 and timee[1] < 29)) or (
                        timee[0] == 16 and (timee[1] >= 23 and timee[1] < 29)):
                    if(timee[0] == 12 and (timee[1] >= 23 and timee[1] < 29) and (anunciar_rei==1 or anunciar_rei==0)):
                        texto = """Rei dos imortais em breve!!! participem!!!"""
                        anunciar(texto)
                        anunciar_rei=2
                    if(timee[0] == 16 and (timee[1] >= 23 and timee[1] < 29) and (anunciar_rei==2 or anunciar_rei==0)):
                        texto = """Rei dos imortais em breve!!! participem!!!"""
                        anunciar(texto)
                        anunciar_rei = 3
                    if(timee[0] == 16 and (timee[1] >= 23 and timee[1] < 29) and (anunciar_rei==3 or anunciar_rei==0)):
                        texto = """Rei dos imortais em breve!!! participem!!!"""
                        anunciar(texto)
                        anunciar_rei = 1
                if ((timee[0] == 10 and (timee[1] >= 45 and timee[1] < 59)) or (
                        timee[0] == 18 and (timee[1] >= 45 and timee[1] < 59))):
                    if(timee[0] == 10 and (timee[1] >= 45 and timee[1] < 59) and (anunciar_tc==1 or anunciar_tc==0)):
                        texto = """Torneio de Clãs em breve!!! participem!!!"""
                        anunciar(texto)
                        anunciar_tc = 2
                    if (timee[0] == 18 and (timee[1] >= 45 and timee[1] < 59) and (anunciar_tc == 2 or anunciar_tc == 0)):
                        texto = """Torneio de Clãs em breve!!! participem!!!"""
                        anunciar(texto)
                        anunciar_tc = 1
                if ((timee[0] == 10 and (timee[1] >= 20 and timee[1] < 29)) or (
                        timee[0] == 14 and (timee[1] >= 50 and timee[1] < 59)) or (
                        timee[0] == 22 and (timee[1] >= 50 and timee[1] < 59))):
                    if(timee[0] == 10 and (timee[1] >= 20 and timee[1] < 29) and (anunciar_coliseu == 1 or anunciar_coliseu == 0)):
                        texto = """Coliseu do Clã em breve!!! participem!!!"""
                        anunciar(texto)
                        anunciar_coliseu = 2
                    if(timee[0] == 14 and (timee[1] >= 50 and timee[1] < 59) and (anunciar_coliseu == 2 or anunciar_coliseu == 0)):
                        texto = """Coliseu do Clã em breve!!! participem!!!"""
                        anunciar(texto)
                        anunciar_coliseu = 3
                    if (timee[0] == 22 and (timee[1] >= 50 and timee[1] < 59) and (anunciar_coliseu == 3 or anunciar_coliseu == 0)):
                        texto = """Coliseu do Clã em breve!!! participem!!!"""
                        anunciar(texto)
                        anunciar_coliseu = 1
                if ((timee[0] == 13 and (timee[1] >= 50 and timee[1] < 59)) or (
                        timee[0] == 20 and (timee[1] >= 50 and timee[1] < 59))):
                    if (timee[0] == 13 and (timee[1] >= 50 and timee[1] < 59) and (anunciar_altar == 1 or anunciar_altar == 0)):
                        texto = """Altar dos Deuses em breve!!! participem!!!"""
                        anunciar(texto)
                        anunciar_altar = 2
                    if (timee[0] == 20 and (timee[1] >= 50 and timee[1] < 59) and (anunciar_altar == 2 or anunciar_altar == 0)):
                        texto = """Altar dos Deuses em breve!!! participem!!!"""
                        anunciar(texto)
                        anunciar_altar = 1
            if (rei_dos_imortais == 1):
                while((timee[0] == 12 and (timee[1] >= 27 and timee[1] < 38)) or (
                        timee[0] == 16 and (timee[1] >= 27 and timee[1] < 38)) or
                       (timee[0] == 16 and (timee[1] >= 27 and timee[1] < 38))):
                    driver.get("http://furiadetitas.net/king/figths")
                    timee = horaminsec()
                    try:
                        driver.find_element_by_link_text("Esconder").click()
                    except:
                        try:                             #//div[@id='topdiv']/div/div[6]/div[9]/a/span/span
                            driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[6]/div[9]/a/span").click()
                        except:
                            try:
                                driver.find_element_by_xpath("//div[@id='topdiv']/div/div[6]/div[9]/a/span/span").click()
                                driver.find_element_by_xpath("//div[@id='topdiv']/div/div[7]/div[7]/a/span/span").click()
                            except:
                                try:
                                    s = driver.find_element_by_xpath(
                                        "//div[@id='topdiv']/div/div[6]/div[7]/a/span/span").text  # rei_dos_imortais_atualizar
                                    if (s[1] == "t"):
                                        c = driver.find_element_by_xpath("//div[@id='topdiv']/div/div[6]/div[5]/span").text
                                    elif (s[1] == "p"):
                                        driver.find_element_by_xpath("//div[@id='topdiv']/div/div[6]/div[7]/a/span/span").click()
                                except:
                                    print("dentro do rei dos imortais")
                                    try:
                                        driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div[3]/a/span/span").click()
                                    except:
                                        print("atacar rei não achado")
                                        try:
                                            print("rei morreu")
                                            timee = horaminsec()
                                            driver.find_element_by_xpath(
                                            "//div[@id='topdiv']/div/div[3]/div[3]/a/span/span").click()  # esquivar
                                            try:
                                                w=driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[3]/div[1]/div[1]/span").click()
                                                if(atributos[1]/4.6):
                                                    try:
                                                        s=driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[3]/div[3]/a[7]/span/span").text
                                                        driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[3]/div[3]/a[5]/span").click()
                                                    except:
                                                        driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[3]/div[3]/a[4]/span").click()
                                            except Exception as ee:
                                                print(ee)

                                            #try:
                                            #    if():
                                            # driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div[3]/a[2]/span/span").click()#atacar
                                        except:
                                            print("botao atacar não achado")
                                    else:
                                        time.sleep(3)
            if(altar_dos_deuses==1):
                while((timee[0] == 13 and (timee[1] >= 57)) or (timee[0]==14 and (timee[1] <= 7)) or (
                        timee[0] == 20 and (timee[1] >= 50 and timee[1] < 59)) or (timee[0]==21 and time[1] < 8)):
                    try:
                        timee = horaminsec()
                        driver.get("http://furiadetitas.net/altars/")
                        try:
                            driver.find_element_by_xpath("//div[@id='topdiv']/div/div[6]/div[5]/a/span/span").click()#aplicar / atualizar
                        except:
                            try:
                                try:
                                    x = driver.find_element_by_xpath("//div[@id='topdiv']/div/div/span/span").text
                                except:
                                    try:
                                        x = driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div/a/span/span").text
                                    except:
                                        pass
                                '''if(int(x) <= atributos[1]/4.6):
                                    driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div[3]/a[2]/span/span").click()
                                    print(x)
                                    print("exilir usado")
                                    time.sleep(2)
                                '''
                                driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div/div/a/span/span").click()
                                time.sleep(2)
                            except:
                                try:
                                    driver.find_element_by_link_text("De volta à batalha").click()
                                except:
                                    driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div/a/span/span").click()
                    except Exception as ee:
                        print(ee)
            if(torneio_de_clas==1):
                while(((timee[0] == 10 and timee[1] >= 57) or (timee[0]==11 and(timee[1] < 8)))or(((
                        timee[0] == 18 and timee[1] >= 57) or(timee[0] == 19 and timee[1] < 8)))):
                    try:
                        driver.get("http://furiadetitas.net/clanfight/")
                        timee = horaminsec()
                        try:
                            driver.find_element_by_xpath("//div[@id='topdiv']/div/div[5]/div[7]/a/span/span").click()
                        except:
                            try:
                                driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div/div/a/span/span").click()
                                time.sleep(3)
                            except:
                                try:
                                    driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div[3]/a/span/span/span").click()
                                except:
                                    try:
                                        driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div[3]/a/span/span").click()
                                    except:
                                        try:
                                            driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div[3]/div[2]").click()
                                        except:
                                            try:
                                                driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div[3]/div/a/span/span").click()
                                            except:
                                                try:
                                                    driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div[3]/a[6]/span/span").click()
                                                except:
                                                    try:
                                                        driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div/a/span/span").click()#atualizar após morto
                                                    except:
                                                        ("error falta de botoes tc")
                                            else:
                                                time.sleep(3)
                                        else:
                                            time.sleep(3)
                                    else:
                                        time.sleep(3)
                                else:
                                    time.sleep(3)
                            else:
                                time.sleep(3)
                    except Exception as ee:
                        print(ee)
            if(coliseu_de_clas==1):
                while((timee[0] == 10 and (27 <= timee[1] <= 37)) or (timee[0] == 14 and timee[1] > 57) or
                      (timee[0] == 15 and timee[1] < 7) and ((timee[0] == 22 and timee[1] >= 57) or
                      (timee[0] == 23 and timee[1] < 7))):
                    try:
                        driver.get("http://furiadetitas.net/clancoliseum/")
                        timee = horaminsec()
                        try:
                            driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[8]/a/span/span").click()
                        except:
                            try:
                                driver.find_element_by_xpath("//div[@id='topdiv']/div/div[8]/a/span/span").click()
                            except:
                                try:
                                    driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div[3]/a[2]/span/span").click()
                                except:
                                    try:
                                        driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div[3]/a/span/span").click()
                                    except:
                                        print("coliseu incompleto")
                                    else:
                                        time.sleep(3)
                                else:
                                    time.sleep(3)
                    except Exception as ee:
                        print(ee)

            if(vale_dos_imortais==1):
                while((timee[0] == 9 and (timee[1] >= 57)) or (timee[0]==10 and timee[1]<8) or (
                        timee[0] == 18 and timee[1] >= 57) or (timee[0]==19 and timee[1]<8)):
                    try:
                        driver.get("http://furiadetitas.net/undying/")
                        timee = horaminsec()
                        try:
                            driver.find_element_by_link_text("Esconder").click()
                        except:
                            try:
                                driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[5]/div[9]/a/span/span").click()
                            except:
                                try:
                                    driver.find_element_by_xpath("//div[@id='topdiv']/div/div[6]/div[7]/a/span/span").click()
                                except:
                                    try:
                                        driver.find_element_by_xpath("//div[@id='topdiv']/div/div[5]/div[9]/a/span/span")\
                                            .click()#aplicar depois de ganhar//*[@id="topdiv"]/div[1]/div[5]/div[9]/a/span/span
                                    except:
                                        try:
                                            driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[5]/div[9]/a/span/span")\
                                                .click()
                                        except:
                                            try:
                                                driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[5]/div[9]/a/span/span").click()#//*[@id='topdiv']/div[1]/div[8]/a/span/span
                                            except:
                                                try:
                                                    driver.find_element_by_xpath("//div[@id='topdiv']/div/div[5]/div[7]/a/span/span").click()# aplicar/ atualizar
                                                except:
                                                    try:
                                                        driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div[3]/a/span/span").click()
                                                        time.sleep(1)
                                                    except:
                                                        try:
                                                            driver.find_element_by_xpath("//div[@id='topdiv']/div/div[3]/div[5]/a/span/span").click()
                                                            time.sleep(5)
                                                        except:
                                                            print("vale dos imortais incompleto")
                    except Exception as ee:
                        print(ee)
                        break
            if(masmorra == 1 and (
                    time_masmorra[0] <= timee[0] and time_masmorra[1] < timee[1] and time_masmorra[3] ==
                    horaminsec()[3].day)):
                masmorra_start()
                time_masmorra = att_masmorra()
                timee = horaminsec()
                print(time_masmorra)
                print("masmorra realizada, proxima de:", time_masmorra)
            if(campanha == 1):
                if (time_campanha[0] <= timee[0] and time_campanha[1] <= timee[1] and
                        time_campanha[3] == horaminsec()[3].day):
                    campanha_start()
                    timee = horaminsec()
                    time_campanha = att_campanha()
                    print(time_campanha)
            if(arena == 1):
                t = att_arena()
                if(int(t[1]) >= (atributos[4] - (atributos[4] / 8)) and t[0] >= (atributos[1] / 5)):
                    driver.find_element_by_css_selector(".label").click()
                    while (True):
                        time.sleep(1)
                        t = att_arena()
                        if (int(t[0]) >= (atributos[1] / 5)):
                            try:
                                driver.find_element_by_xpath("//div[@id='topdiv']/div/div[5]/div/a[2]/span/span").click()
                            except:
                                print("//div[@id='topdiv']/div/div[5]/div/a[2]/span/span error")
                            print("mana balanciada")
                            #try:
                            #    driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[3]/div/a[1]").click()#vender itens
                            driver.get("http://furiadetitas.net/")
                            t=att_arena()
                            break
                elif(int(t[1]) >= 50 and t[0] >= (atributos[1] / 5)):
                    print("Lutando arena")
                    energia+=50
                    driver.find_element_by_css_selector(".label").click()  # atacar_arena
                    time.sleep(3)
            if(cofre_pessoal==1):
                if(bau_bronze==0 and energia>=(atributos[4]*3)):
                    driver.get("http://furiadetitas.net/quest/")
                    try:
                        driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[4]/div[1]/a/span").click()
                        print("bau bronze coletado")
                        bau=att_cofre()
                        bau_bronze=bau[0]
                        bau_prata=bau_prata[1]
                        energia=bau[2]
                    except:
                        print("bau bronze não coletado")
                        print(energia)
                if (bau_prata==0 and energia>=(atributos[4]*10)):
                    driver.get("http://furiadetitas.net/quest/")
                    try:
                        try:
                            driver.find_element_by_xpath("//div[@id='topdiv']/div/div[4]/div[2]/a/span").click()
                        except:
                            driver.find_element_by_xpath("//*[@id='topdiv']/div[1]/div[4]/div[2]/a/span").click()
                        print("bau prata aberto")
                        bau=att_cofre()
                        bau_prata=bau[1]
                        energia=0
                    except:
                        print("error ao abrir bau prata")
                        print(energia)
            if(coletar_gold == 1):
                if (dia_ouro == timee[3].day):
                    dia_ouro = ouro_diario()
                    print("ouro coletado")
        except Exception as ee:
            print(ee, "no while principal")

time.sleep(1)
conn.close()
driver.quit()
