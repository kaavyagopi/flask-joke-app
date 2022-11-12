from webbrowser import get
from flask import Flask, render_template
import random

app = Flask(__name__)

#add new jokes at last
jks=("You're not completely useless,you can always serve as a bad example.",
     "You don't need a parachute to go skydiving.You need a parachute to go skydiving twice.",
     "Parallel lines have so much in common. It's a shame they'll never meet.",
     "Someone stole my mood ring,don't know how feel about that.",
     "Why do cows wear bell? Because their horns don't work.",
     "What do you call a dog with No legs? It doesn't matter, it's Not Going to come anyway",
     )
a=random.choice(jks)

#add new assigning in nested form
if a == jks[0]:
    c=0
elif a == jks[1]:
    c=1
elif a == jks[2]:
    c=2
elif a == jks[3]:
    c=3
elif a == jks[4]:
    c=4
else:
    c=10

@app.route("/")
def home():
    
    return render_template("index.html",a=a,c=c)
