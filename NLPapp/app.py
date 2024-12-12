from http.client import responses
from tkinter import ttk
from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API
import requests
from PIL import Image, ImageTk
from io import BytesIO




class NLPApp:

    def __init__(self):
        # datbase obj create
        self.dbo = Database()

        # api onj
        self.apio = API( )


        #login gui load
        self.root = Tk()
        self.root.geometry('2560x1664')
        self.root.title('NLP APP')
        self.root.config(bg='black')
        self.root.iconbitmap('/Users/ddhanushnaik/Documents/career/ML/python 2/project/NLPapp/resourse/favicon.ico')
        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()
        app_title = Label(self.root,text='NLP APP',bg='black' ,fg='#25F6D8')
        app_title.pack(pady = (60,20))
        app_title.configure(font=('Georgia',60,'bold'))


        page_title = Label(self.root,text='LOGIN' , bg='black',fg='#839192')
        page_title.pack(pady=(60,5))
        page_title.configure(font=('Times New Roman',54,'bold'))


        lable1 = Label(self.root , text='Enter Email' , bg='black' , font=('Times New Roman',24))
        lable1.pack(pady=(20,20))

        self.email_input = ttk.Entry(self.root , width=30 )
        self.email_input.pack(pady=(10,20) , ipady=3)

        lable2 = Label(self.root, text='Enter Password', bg='black', font=('Times New Roman', 24))
        lable2.pack(pady=(20,10))

        self.password_input = ttk.Entry(self.root, width=30 , show='*')
        self.password_input.pack(pady=(40, 20), ipady=3)

        login_btn = Button(self.root,text='Login',bg='black' ,fg='grey', font=('Times New Roman', 20) , command=self.perform_login)
        login_btn.pack(pady=(10,10))

        lable3 = Label(self.root,text='Not a Member?',bg='black', font=('Times New Roman', 15))
        lable3.pack(pady=10)

        redirect_btn = Button(self.root, text='Register',background='blue',activeforeground='black', fg='grey', font=('Times New Roman', 15),command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))


    def register_gui(self):
        self.clear()

        app_title = Label(self.root, text='NLP APP', bg='black', fg='#25F6D8')
        app_title.pack(pady=(60, 20))
        app_title.configure(font=('Georgia', 60, 'bold'))

        page_title = Label(self.root, text='REGISTER', bg='black', fg='#839192')
        page_title.pack(pady=(60, 5))
        page_title.configure(font=('Times New Roman', 54, 'bold'))

        lable0 = Label(self.root, text='Enter Name', bg='black', font=('Times New Roman', 24))
        lable0.pack(pady=(20, 20))

        self.name_input = ttk.Entry(self.root, width=30)
        self.name_input.pack(pady=(10, 20), ipady=3)

        lable1 = Label(self.root, text='Enter Email', bg='black', font=('Times New Roman', 24))
        lable1.pack(pady=(20, 20))

        self.email_input = ttk.Entry(self.root, width=30)
        self.email_input.pack(pady=(10, 20), ipady=3)

        lable2 = Label(self.root, text='Enter Password', bg='black', font=('Times New Roman', 24))
        lable2.pack(pady=(20, 10))

        self.password_input = ttk.Entry(self.root, width=30, show='*')
        self.password_input.pack(pady=(40, 20), ipady=3)

        register_btn = Button(self.root, text='Register', bg='black', fg='grey', font=('Times New Roman', 20) , command=self.perform_regestration)
        register_btn.pack(pady=(10, 10))

        lable3 = Label(self.root, text='Already a Member?', bg='black', font=('Times New Roman', 15))
        lable3.pack(pady=10)

        redirect_btn = Button(self.root, text='Login', background='blue', fg='grey', font=('Times New Roman', 15),
                              command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_regestration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name , email, password)

        if response:
            messagebox.showinfo('Success','Regestration Sucessfull you can Login now')
        else:
            messagebox.showerror('Error','Email Exists')


    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            # messagebox.showinfo('Success','Login Sucessfull ')
            self.Home_gui()
        else:
            messagebox.showerror('Error','incorrect email/password')

    def Home_gui(self):
        self.clear()

        app_title = Label(self.root, text='NLP APP', bg='black', fg='#25F6D8')
        app_title.pack(pady=(60, 20))
        app_title.configure(font=('Georgia', 60, 'bold'))

        sentiment_btn = Button(self.root, text='SENTIMENTAL ANALYSIS', font=('Times New Roman', 20),width=40,height=4,
                             command=self.sentimental_analysis)
        sentiment_btn.pack(pady=(80, 10))


        ner_btn = Button(self.root, text='NAME ENTITY DETECTION',  font=('Times New Roman', 20),width=40,height=4,
                             command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='EMOTION DETECTION', font=('Times New Roman', 20),width=40,height=4,
                             command=self.emotion_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Login Out', background='blue', fg='grey', font=('Times New Roman', 15),
                              command=self.login_gui)
        logout_btn.pack(pady=(10, 10))



    def sentimental_analysis(self):
        self.clear()

        app_title = Label(self.root, text='NLP APP', bg='black', fg='#25F6D8')
        app_title.pack(pady=(60, 20))
        app_title.configure(font=('Georgia', 60, 'bold'))

        app_title = Label(self.root, text='SENTIMENTAL ANALYSIS', bg='black', fg='#25F6D8')
        app_title.pack(pady=(60, 20))
        app_title.configure(font=('Georgia', 30))

        lable1 = Label(self.root, text='Enter the text', bg='black', font=('Times New Roman', 24))
        lable1.pack(pady=(20, 20))

        self.sentimental_analysis_input = ttk.Entry(self.root, width=50 )
        self.sentimental_analysis_input.pack(pady=(20, 20), ipady=10)

        sentimental_analysis_btn = Button(self.root, text='Submit', background='blue', fg='grey', font=('Times New Roman', 15),command=self.do_sentimental_analysis)
        sentimental_analysis_btn.pack(pady=(10, 10))

        self.sentimental_analysis_result = Label(self.root, text='', bg='black',fg='white' ,font=('Times New Roman', 24))
        self.sentimental_analysis_result.pack(pady=(20, 20))
        self.sentimental_analysis_result.configure(font=('Georgia',16))

        back_btn = Button(self.root, text='Back', background='blue', fg='grey', font=('Times New Roman', 15),command=self.Home_gui)
        back_btn.pack(pady=(10, 10))

    def do_sentimental_analysis(self):
        text = self.sentimental_analysis_input.get()
        result = self.apio.sentiment_analysis(text)
        #
        # for i in result['scored_labels']:
        #     print(i,result['scored_labels']['label'])
        self.sentimental_analysis_result['text'] = result









    def ner_gui(self):
        self.clear()

        app_title = Label(self.root, text='NLP APP', bg='black', fg='#25F6D8')
        app_title.pack(pady=(60, 20))
        app_title.configure(font=('Georgia', 60, 'bold'))

        app_title = Label(self.root, text='NAME ENTITY DETECTION', bg='black', fg='#25F6D8')
        app_title.pack(pady=(60, 20))
        app_title.configure(font=('Georgia', 30))

        lable1 = Label(self.root, text='Enter the text', bg='black', font=('Times New Roman', 24))
        lable1.pack(pady=(20, 20))

        self.ner_input = ttk.Entry(self.root, width=50)
        self.ner_input.pack(pady=(20, 20), ipady=10)

        ner_btn = Button(self.root, text='Submit', background='blue', fg='grey',
                                          font=('Times New Roman', 15), command=self.do_ner)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg='black', fg='white', font=('Times New Roman', 24))
        self.ner_result.pack(pady=(20, 20))
        self.ner_result.configure(font=('Georgia', 16))

        back_btn = Button(self.root, text='Back', background='blue', fg='grey', font=('Times New Roman', 15),
                          command=self.Home_gui)
        back_btn.pack(pady=(10, 10))


    def do_ner(self):
        text = self.ner_input.get()
        result = self.apio.ner(text)
        #
        # for i in result['scored_labels']:
        #     print(i,result['scored_labels']['label'])
        self.ner_result['text'] = result





    def emotion_gui(self):
        self.clear()

        app_title = Label(self.root, text='NLP APP', bg='black', fg='#25F6D8')
        app_title.pack(pady=(60, 20))
        app_title.configure(font=('Georgia', 60, 'bold'))

        app_title = Label(self.root, text='EMOTION DETECTION', bg='black', fg='#25F6D8')
        app_title.pack(pady=(60, 20))
        app_title.configure(font=('Georgia', 30))

        lable1 = Label(self.root, text='Enter the text', bg='black', font=('Times New Roman', 24))
        lable1.pack(pady=(20, 20))

        self.emotion_input = ttk.Entry(self.root, width=50)
        self.emotion_input.pack(pady=(20, 20), ipady=10)

        emotion_btn = Button(self.root, text='Submit', background='blue', fg='grey',
                         font=('Times New Roman', 15), command=self.do_emotion)
        emotion_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text='', bg='black', fg='white', font=('Times New Roman', 24))
        self.emotion_result.pack(pady=(20, 20))
        self.emotion_result.configure(font=('Georgia', 16))

        back_btn = Button(self.root, text='Back', background='blue', fg='grey', font=('Times New Roman', 15),
                          command=self.Home_gui)
        back_btn.pack(pady=(10, 10))

    def do_emotion(self):
        text = self.emotion_input.get()
        result = self.apio.emotion(text)
        #
        # for i in result['scored_labels']:
        #     print(i,result['scored_labels']['label'])
        self.emotion_result['text'] = result








obj = NLPApp()
