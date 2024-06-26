import subprocess
import os
from tkinter import *
import tkinter as tk
from tkinter import ttk, Tk
from tkinter import messagebox
from PIL import Image, ImageTk
import psutil

root=tk.Tk()

img=PhotoImage(file='alisa.png')
root.iconphoto(False,img)
root.resizable(width=False, height=False)

root.title('Ассистент Alisa')
root.geometry('600x400')
root['bg'] = 'black'


#vosk model

def rep_model_vosk_small():
    f = open('vosk.txt', 'w', encoding='utf-8')
    f.write('small')
    
def rep_model_vosk_big():
    f = open('vosk.txt', 'w', encoding='utf-8')
    f.write('big')
    

#speech
def rep_speech_model_aidar():
    f = open('speech.txt', 'w', encoding='utf-8')
    f.write('aidar')
    
def rep_speech_model_baya():
    f = open('speech.txt', 'w', encoding='utf-8')
    f.write('baya')

def rep_speech_model_kseniya():
    f = open('speech.txt', 'w', encoding='utf-8')
    f.write('kseniya')
    
def rep_speech_model_xenia():
    f = open('speech.txt', 'w', encoding='utf-8')
    f.write('xenia')





def Addrun():
    return os.system("start cmd")

    
    # return subprocess.call('python run.py', shell = True) # работае даже без консоли
    # return os.system('python run.py') # работает с консолью
    # return os.system('python run.py')
    # return subprocess('')

def Addexit():
    for proc in psutil.process_iter():
        if proc.name() == 'python.exe':
            proc.terminate()

# speech
def open_window_Modelvois_replacement():
    window_Modelvois_replacement = Toplevel(root)
    img=PhotoImage(file='alisa.png')
    window_Modelvois_replacement.iconphoto(False,img)
    window_Modelvois_replacement.resizable(width=False, height=False)
    window_Modelvois_replacement.title('vois')
    window_Modelvois_replacement.resizable(0, 0)
    Modelvois_replacement= Canvas(window_Modelvois_replacement, width=300, height=10, bg='#65da88', highlightthickness=0) #bg='#65da88'
        
    btn_aidar = tk.Button(window_Modelvois_replacement, text='Aidar', font = ('Comic Sans MS', 12), width = '10', 
                    height = '1', fg = 'black', bg  = 'darkgoldenrod', activebackground='gray', border=0, 
                    cursor='hand1', command=rep_speech_model_aidar) 
    
    btn_baya =tk.Button(window_Modelvois_replacement, text='Baya', font = ('Comic Sans MS', 12), width = '10', 
                    height = '1', fg = 'black', bg  = 'darkgoldenrod', activebackground='gray', border=0, 
                    cursor='hand1', command=rep_speech_model_baya) #command
    btn_kseniya = tk.Button(window_Modelvois_replacement, text='Kseniya', font = ('Comic Sans MS', 12), command= rep_speech_model_kseniya, width = '10', 
                    height = '1', fg = 'black', bg  = 'darkgoldenrod', activebackground='gray', border=0, 
                    cursor='hand1')
    btn_xenia =tk.Button(window_Modelvois_replacement, text='xenia', font = ('Comic Sans MS', 12), command= rep_speech_model_xenia, width = '10', 
                    height = '1', fg = 'black', bg  = 'darkgoldenrod', activebackground='gray', border=0, 
                    cursor='hand1')

    
    
    
    # aidar, baya, kseniya, xenia, random
    Modelvois_replacement.pack(pady=0)
    btn_aidar.pack(pady=5)
    btn_baya.pack(pady=5)
    btn_kseniya.pack(pady=5)
    btn_xenia.pack(pady=5)
    Modelvois_replacement.pack(pady=5)


# def open_window_Modelspeech_replacement():
#     window_Modelspeech_replacement = Toplevel(root)
#     img=PhotoImage(file='J:\\Stella\\stellaPR\\python_web_pr\\alisa.png')
#     window_Modelspeech_replacement.iconphoto(False,img)
#     window_Modelspeech_replacement.resizable(width=False, height=False)
#     window_Modelspeech_replacement.title('Modelspeek')
#     window_Modelspeech_replacement.resizable(0, 0)
#     window_Modelspeech= Canvas(window_Modelspeech_replacement, width=300, height=10, bg='#65da88', highlightthickness=0)
    
#     btn_vosk = tk.Button(window_Modelspeech_replacement, text ='Vosk model', font=('Comic Sans MS', 12), width = '10', 
#                     height = '1', fg = 'black', bg  = 'darkgoldenrod', activebackground='gray', border=0, 
#                     cursor='hand1')
#     btn_alt = tk.Button(window_Modelspeech_replacement, text ='Alt model', font=('Comic Sans MS', 12), width = '10', 
#                     height = '1', fg = 'black', bg  = 'darkgoldenrod', activebackground='gray', border=0, 
#                     cursor='hand1')
    
#     window_Modelspeech.pack(pady=3)
#     btn_vosk.pack(pady=5)
#     btn_alt.pack(pady=5)

def open_window_Modelvolume_replacemen():
    window_Modelvolume_replacemen = Toplevel(root)
    img=PhotoImage(file='alisa.png')
    window_Modelvolume_replacemen.iconphoto(False,img)
    window_Modelvolume_replacemen.resizable(width=False, height=False)
    window_Modelvolume_replacemen.title('volume')
    window_Modelvolume_replacemen.resizable(0, 0)
    window_Modelvolume= Canvas(window_Modelvolume_replacemen, width=300, height=10, bg='#65da88', highlightthickness=0)
    
    btn_big = tk.Button(window_Modelvolume_replacemen, text ='Big model', font=('Comic Sans MS', 12), command= rep_model_vosk_big, width = '10', 
                    height = '1', fg = 'black', bg  = 'darkgoldenrod', activebackground='gray', border=0, 
                    cursor='hand1')
    btn_small = tk.Button(window_Modelvolume_replacemen, text ='Small model', font=('Comic Sans MS', 12), command= rep_model_vosk_small, width = '10', 
                    height = '1', fg = 'black', bg  = 'darkgoldenrod', activebackground='gray', border=0, 
                    cursor='hand1')
    
    window_Modelvolume.pack(pady=3)
    btn_big.pack(pady=5)
    btn_small.pack(pady=5)


def home_page():
    home_frame = tk.Frame(main_frame)
    
    home_page = tk.Label(home_frame, text = ('_______________HOME_______________\n'), font = ('Arial', 16), fg = 'black')
    
    com = tk.Label(home_frame, text = '{alt_name} \n ассистент, робот, алиса \n\n {short_programs} \n ответь, переведи, скажи, говори, сколько вермя',
                   font = ('Bold', 14))
    cop = tk.Label(home_frame, text = 'python run.py',
                   font = ('Bold', 14))
    btn = tk.Button(home_frame, text='START', font = ('Comic Sans MS', 12), command= Addrun, width = '18', 
                    height = '1', fg = 'black', bg  = 'darkgoldenrod', activebackground='gray', border=0, 
                    cursor='hand1')
    
    # mic = tk.Button(home_frame, text='ON', font = ('Comic Sans MS', 12),
    #                 width = '180', height = '40', fg = 'black', bg  = 'darkgoldenrod', activebackground='gray', 
    #                 image=img_mic_on, compound=RIGHT, border=0, cursor='hand1') #command= Addrun,
    
    #root/window
    btn2 = tk.Button(home_frame, text='OUTPUT', font = ('Comic Sans MS', 12), command= Addexit,
                     width = '18', height = '1', fg = 'black', bg  = 'darkgoldenrod', activebackground='gray', border=0, cursor='hand1')

    
    # home.pack()
    home_page.pack()
    com.pack(pady=5)
    cop.pack(pady=5)
    btn.pack(pady=5)
    # mic.pack(pady=5)
    btn2.pack(pady=5)
    
    home_frame.pack(pady=(10))
    
     
def cmd_page():
    
    home_frame = tk.Frame(main_frame)
    
    cmd_page = tk.Label(home_frame, text = ('_______________CMD_______________'), font = ('Arial', 16), fg = 'black')
    
    cmd1_text = tk.Label(home_frame, text = '[__listen_list_commands__]', 
                   font = ('Comic Sans MS', 12), fg='darkgoldenrod')
    
    cmd1 = tk.Label(home_frame, text = 'список команд, команды, что ты умеешья', 
                   font = ('Comic Sans MS', 12))
    
    # cmd2_text = tk.Label(home_frame, text = '[__time__]', 
    #                font = ('Comic Sans MS', 12), fg ='darkgoldenrod')
    # cmd2 = tk.Label(home_frame, text = 'время, текущее время, сейчас времени, который час', 
    #                font = ('Comic Sans MS', 12))
    
    
    # cmd3_text = tk.Label(home_frame, text = '[__open_sharex__]', 
    #                font = ('Comic Sans MS', 12), fg = 'darkgoldenrod')
    # cmd3 = tk.Label(home_frame, text = 'снимок экрана, запусти снимок', 
    #                font = ('Comic Sans MS', 12))
    

    cmd2_text = tk.Label(home_frame, text = '[__open_discord__]', 
                   font = ('Comic Sans MS', 12), fg = 'darkgoldenrod')
    cmd2 = tk.Label(home_frame, text = 'общение, друзья', 
                   font = ('Comic Sans MS', 12))
    
    
    cmd3_text = tk.Label(home_frame, text = '[__open_vs_code__]', 
                   font = ('Comic Sans MS', 12), fg = 'darkgoldenrod')
    cmd3 = tk.Label(home_frame, text = 'код, программирование', 
                   font = ('Comic Sans MS', 12))
    
    cmd4_text = tk.Label(home_frame, text = '[__history__]', 
                   font = ('Comic Sans MS', 12), fg = 'darkgoldenrod')
    cmd4 = tk.Label(home_frame, text = 'навык', 
                   font = ('Comic Sans MS', 12))
    
    cmd5_text = tk.Label(home_frame, text = '[__chat_llama__]', 
                   font = ('Comic Sans MS', 12), fg = 'darkgoldenrod')
    cmd5 = tk.Label(home_frame, text = 'вопрос', 
                   font = ('Comic Sans MS', 12))
    
    cmd6_text = tk.Label(home_frame, text = '[__exit__]', 
                   font = ('Comic Sans MS', 12), fg = 'darkgoldenrod')
    cmd6 = tk.Label(home_frame, text = 'закрыть, заврешение работы, конец работы', 
                   font = ('Comic Sans MS', 12))
    

    
    cmd_page.pack()
    
    cmd1_text.pack(pady=(5, 5))
    cmd1.pack()
    
    cmd2_text.pack()
    cmd2.pack()
    
    cmd3_text.pack()
    cmd3.pack()
    
    cmd4_text.pack()
    cmd4.pack()
    
    cmd5_text.pack()
    cmd5.pack()
    
    cmd6_text.pack()
    cmd6.pack()
    
    
    home_frame.pack()
    

def setting_page():
    
    home_frame = tk.Frame(main_frame)
    
    setting = tk.Label(home_frame, text = 'Setting\n', font = ('Bold', 24))
    
    # inst = tk.Label(home_frame, text = 'Model speech: vosk', font=('Comic Sans MS', 16))
    # btn1_setting = Button(home_frame, text = 'replacement spech model', font=('Comic Sans MS', 12), # font=('Comic Sans MS', 12, 'overstrike')/'overstrike'
    #                       width=20, height=1, fg='black', bg='darkgoldenrod', activebackground='gray', 
    #                       command=open_window_Modelspeech_replacement, border=0, cursor='hand1')
    
    inst2 = tk.Label(home_frame, text = ' Model volume', font=('Comic Sans MS', 16))
    btn2_setting = Button(home_frame, text = 'replacement volume', font=('Comic Sans MS', 12),
                          width=20, height=1, fg='black', bg='darkgoldenrod', activebackground='gray', 
                          command=open_window_Modelvolume_replacemen, border=0, cursor='hand1')
    
    inst3 = tk.Label(home_frame, text = ' Model vois', font=('Comic Sans MS', 16))
    btn3_setting = Button(home_frame, text = 'replacement vois', font=('Comic Sans MS', 12),
                          width=20, height=1, fg='black', bg='darkgoldenrod', activebackground='gray', 
                          command=open_window_Modelvois_replacement, border=0, cursor='hand1')
    
    setting.pack()
    # inst.pack()
    # btn1_setting.pack()
    inst2.pack()
    btn2_setting.pack()
    inst3.pack()
    btn3_setting.pack()
    
    home_frame.pack(pady=20)
    
def log_page():
    
    home_frame = tk.Frame(main_frame)
    log = tk.Label(home_frame, text = 'Log\n', font = ('Bold', 16))
    log_text = tk.Label(home_frame, text = '--Список команд:-- \n- list: список команд, команды, что ты умеешь\n- time: время, текущее время, сейчас времени, который чаc\n- open_browser: гугл хром, браузер\n- open_steam: стим, запусти стим \n- open_browser_server: сервер, запусти сервер  \n- open_sharex: снимок, снимок экрана \n- open_OBS: запись, запись экрана \n- open_vs: код, программирование \n- open_vtube: аватар, виртуальная студия \n- open_discord: общение, друзья \n- joke: расскажи анекдот, рассмеши, шутка, расскажи \nшутку, пошути, развесели\n- exit: заврешение работы, конец работы, закрыть', 
                        font=('Comic Sans MS',12 ))
    
    log.pack()
    log_text.pack()
    
    home_frame.pack(pady=10)




# BETA

def chat_page():
    
    home_frame = tk.Frame(main_frame)
    
    enter = Entry(home_frame)
    
    text = open('chat_save.txt', encoding='utf-8').readlines()
    text = ''.join(text)
    textline = Text(home_frame)
    #add text
    textline.insert(1.0, text)
    textline.pack()

    enter.pack()
    
    home_frame.pack(pady=10)





#lines on/off, page arg

def hide_indicators():
    home_indicate.config(bg='black')
    cmd_indicate.config(bg='black')
    setting_indicate.config(bg='black')
    log_indicate.config(bg='black')
    CHAT_indicate.config(bg='black')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()
        
def indicate(lb, page):
    
    hide_indicators()
    lb.config(bg='darkgoldenrod')
    delete_pages()
    page()

    
#window
options_frame = tk.Frame(root, bg='black')


#home
home_btn =tk.Button(options_frame, text='Главная', font=('Bold', 12), 
                    fg='white', bd=0, bg='black',
                    command=lambda: indicate(home_indicate,home_page))
home_btn.place(x = 10, y = 50)


home_indicate = tk.Label(options_frame, text='', bg='black')
home_indicate.place(x=3, y=50, width=3, height=30)


#cmd
cmd_btn =tk.Button(options_frame, text='Команды', font=('Bold', 12), 
                    fg='white', bd=0, bg='black',
                    command=lambda: indicate(cmd_indicate, cmd_page))
cmd_btn.place(x = 10, y = 100)

cmd_indicate = tk.Label(options_frame, text='', bg='black')
cmd_indicate.place(x=3, y=100, width=3, height=30)

# setting
setting_btn =tk.Button(options_frame, text='Настройки', font=('Bold', 12), 
                    fg='white', bd=0, bg='black',
                    command=lambda: indicate(setting_indicate, setting_page))
setting_btn.place(x = 10, y = 150)

setting_indicate = tk.Label(options_frame, text='', bg='black')
setting_indicate.place(x=3, y=150, width=3, height=30)

#log
log_btn =tk.Button(options_frame, text='Логи', font=('Bold', 12), 
                    fg='white', bd=0, bg='black',
                    command=lambda: indicate(log_indicate, log_page))
log_btn.place(x = 10, y = 200)

log_indicate = tk.Label(options_frame, text='', bg='black')
log_indicate.place(x=3, y=200, width=3, height=30)

# chat_page

CHAT_btn =tk.Button(options_frame, text='CHAT', font=('Bold', 12), 
                    fg='white', bd=0, bg='black',
                    command=lambda: indicate(CHAT_indicate, chat_page))
CHAT_btn.place(x = 10, y = 250)

CHAT_indicate = tk.Label(options_frame, text='', bg='black')
CHAT_indicate.place(x=3, y=250, width=3, height=30)


options_frame.pack(side=tk.LEFT) 
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=400)


main_frame = tk.Frame(root,highlightbackground='white', 
                      highlightthickness=1)


main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400, width=500)


root.mainloop()
