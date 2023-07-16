from flask import Flask,render_template,request
from flask_socketio import SocketIO,send
import json
import random
import pyjokes


app=Flask(__name__)
app.config['SECKRET_KEY']='ndsiogj89343'
socket=SocketIO(app,cors_allowed_origins="*")

with open("chat.json") as file:
    data=json.load(file)

more_than_one_word=[]
more_than_one_word1=[]
more_than_one_word2=[]
for da in data['greeting']:
    if len(da.split())>1:
        more_than_one_word.append(da)
        #print(more_than_one_word)
for da1 in data['questions']:
    if len(da1.split())>1:
        more_than_one_word1.append(da1)
for da2 in data['todo']:
    if len(da2.split())>1:
        more_than_one_word2.append(da2)
@app.route("/")
def rend():
    return render_template("index.html")
@socket.on('message')
def handel_message(msg):
    marks=["!","@","#","$","%","^","&","*"]
    x=msg
    li=[]
    li1=[]
    li2=[]
    list_set=set(li)
    list_set1=set(li1)
    list_set2=set(li2)
    def find(name):
        name=name.lower()
        for mark in marks:
            if mark in name:
                name=str.replace(name,mark,"")
                #print(name)
        for i in name.split():
            if i in data['greeting']:    
                #print(i)
                list_set.add(i)
                #print(li)
            elif i in data['questions']:
                list_set1.add(i)
            elif i in data['questions']:
                list_set2.add(i)
            for f in more_than_one_word:
                if i in f.split():
                    list_set.add(i)
            for f1 in more_than_one_word1:
                if i in f1.split():
                    list_set1.add(i)
            for f2 in more_than_one_word2:
                if i in f2.split():
                    list_set2.add(i)
        #print(str(more_than_one_word)+" 1")
        print(list_set)
        print(list_set1)
        print(list_set2)
        if len(list_set)>=2:
            data['greeting'].append(name)
            more_than_one_word.append(name)
            li.clear()
            list_set.clear()
            #print(data['greeting'])
            #print(str(more_than_one_word)+"2")
            metaresponde=("meta_AI: "+random.choice(data['responde']))
            send(f"you: {msg}")
            send(metaresponde)
            #print(metaresponde)
        if len(list_set1)>=3:
            data['questions'].append(name)
            more_than_one_word1.append(name)
            li1.clear()
            list_set1.clear()
            #print(data['greeting'])
            #print(str(more_than_one_word)+"2")
            metaresponde1=("meta_AI: "+random.choice(data['respondequest']))
            send(f"you: {msg}",)
            send(metaresponde1)
            print(metaresponde1)
        if len(list_set2)>=3:
            data['todo'].append(name)
            more_than_one_word2.append(name)
            li2.clear()
            list_set2.clear()
            #print(data['greeting'])
            #print(str(more_than_one_word)+"2")
            res_todo=random.choice(data['respondetodo'])
            if res_todo =="watch movie":
                res_todo=f'watch "" movie'
            elif res_todo =="ok, hear is a joke":
                res_todo=f'ok, hear is a joke, "{pyjokes.get_joke()}"'
            metaresponde2=("meta_AI: "+res_todo)
            send(f"you: {msg}")
            send(metaresponde2)
            print(metaresponde2)
        elif name in data['greeting']:
            #print(more_than_one_word)
            metaresponde3=("meta_AI: "+random.choice(data['responde']))
            send(f"you: {msg}")
            send(metaresponde3)
            #print(metaresponde)
            pass
        else:
            metaresponde=("meta_AI: sorry didn't get that")
            send(f"you: {msg}")
            send(metaresponde)
            print(metaresponde)
        #print(li)
#____________________________________________________________________________________________________________________
    find(x)
    #print(data['greeting'])
    #print(more_than_one_word)
    #send(f"you: {msg}",broadcast=True)
    #send(metaresponde,broadcast=True) or send(metaresponde1,broadcast=True)
socket.run(app)