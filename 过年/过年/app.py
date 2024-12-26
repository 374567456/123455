from flask import Flask,render_template,request,redirect
app = Flask(__name__)
people=['刘振坡','孙燕粉','刘铭霖','刘培森','刘振华','郑倩倩','孙浩炯','孙紫钰','孙莹莹','毛文亮','吴一言','李玲玉','李易明']

@app.route('/total',methods=["GET","POST"])
def total():
    if request.method=="POST":
        username=request.form.get("username")
        print("从服务器接收到的数据",username)
        if username==people[0]:
            return redirect("dad")
        elif username==people[1]:
            return redirect("mom")
        elif username==people[2]:
            return redirect("borther_1")
        elif username==people[3]:
            return redirect("borther_2")
        elif username==people[4]:
            return redirect("dabo")
        elif username==people[5]:
            return redirect("jiejie")
        elif username==people[6]:
            return redirect("bother_3")
        elif username==people[7]:
            return redirect("sister_2")
        elif username==people[8]:
            return redirect("sister_1")
        elif username==people[9]:
            return redirect("friend_1")
        elif username==people[10]:
            return redirect("friend_2")
        elif username==people[11]:
            return redirect("bai")
        else:
            return redirect("teacher")
    return render_template("total.html")

@app.route('/dad')
def dad():
    return render_template("dad.html")
@app.route('/mom')
def mom():
    return render_template("mom.html")
@app.route('/borther_1')
def brother_1():
    return render_template("borther_1.html")
@app.route('/borther_2')
def brother_2():
    return render_template("borther_2.html")
@app.route('/dabo')
def dabo():
    return render_template("dabo.html")
@app.route('/jiejie')
def jiejie():
    return render_template("jiejie.html")
@app.route('/sister_1')
def sister_1():
    return render_template("sister_1.html")
@app.route('/sister_2')
def sister_2():
    return render_template("sister_2.html")
@app.route('/friend_1')
def friend_1():
    return render_template("friend_1.html")
@app.route('/friend_2')
def friend_2():
    return render_template("friend_2.html")
@app.route('/teacher')
def reacher():
    return render_template("teacher.html")

if __name__ == '__main__':
    app.run()
