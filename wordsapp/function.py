"""            
import random
import tkinter
from tkinter import messagebox
import numpy as np

from wordsapp.models import Post

class Question(Post):

    def __init__(self,master):
        self.master = master
        self.question_list = []
        self.now_question = None

        self.choice_value = tkinter.IntVar
        self.getQuestion()
        self.createWidgets()
        self.showQuestion()

    
    def getQuestion(self):
        
        fields = ['category','question','answer','memory']
        object_list = Post.objects.filter(user = self.request.user).order_by('-posted_at')
        object_list = Post.objects.filter(memory = False)
        object_list.remove('category')
        listOfValues = object_list.values
        listOfValues = list(listOfValues)
        
        
        for i in range(len(listOfValues)):
            self.question_list.append(i)


    def createWidgets(self):

        self.frame = tkinter.Frame(
            self.master,
            width=400,
            height=200
        )
        self.frame.pack()

        self.botton = tkinter.Button(
            self.master,
            text = '次の問題へ',
            command = self.check.Answer
        )

    def showQuestion(self):
        
        num_question = random.randrange(len(self.quiz_list))
        question = self.question_list[num_question]

        self.problem = tkinter.Label(
            self.frame,
            text = question[0]
        )

        self.problem.grid(
        column=0,
        row=0,
        columnspan=4,
        pady=10
        )

        self.choices = []

        for i in range(4):
            choice = tkinter.Radiobutton(
                self.frame,
                text = question[i+1],
                variable =self.choice_value,
                value = i
            )

            choice.grid(
            row=1,
            column=i,
            padx=10,
            pady=10,
            )

            self.choices.append(choice)

        self.question_list.remove(question)

        self.now_question = question


    def deleteQuestion(self):
        self.problem.destory()
        for choice in self.choices:
            choice.destroy()

    def checkAnswer(self):


        if self.choice_value.get() == int(self.now_quiz[5]):
            messagebox.showinfo('正解です')
        else:
            messagebox.showerror('不正解です')

        self.deleteQuestion()

        if self.question_list:

            self.showQuestion()
        else:
            
            self.endAppli()

        def endAppli(self):
            
            self.problem = tkinter.Label(
                self.frame,
                text="クイズは全て出題ずみです"
            )
            self.problem.grid(
                column=0,
                row=0,
                padx=10,
                pady=10
            )

            
            self.button.config(
                command=self.master.destroy
            )
"""