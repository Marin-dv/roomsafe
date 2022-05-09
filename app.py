from email.mime import application
import sqlite3
#from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from cmath import pi, sqrt

from functools import wraps
import urllib.parse
import random
import math
from calculator import calc
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np
from Hcalculator import Hcalc

#rg

# Configure application
app = Flask(__name__)

def rg():
    a = 0
    return a

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/front-page")
        return f(*args, **kwargs)
    return decorated_function

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def apology1(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("Apology1.html", top=code, bottom=escape(message)), code


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
def Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq, RiskTolerance, outvalue):
    img = BytesIO()
    ymax = int(surfarea)
    if outvalue==1:
        def f(x):
            with np.errstate(divide='ignore', invalid='ignore'):
                return ((1+pow((1+((4*3600*Lc*float(surfarea)*float(ceiling)*RiskTolerance)/(0.3*(float(Qbh)*float(Qbh)*float(MaskReq)*float(MaskReq)*float(Cqh)*float(Pih)*(1-float(Pih))*x)))), 1/2))/2)
    else:
        if math.floor(float(MaskReq)) == 1:
            def f(x):
                with np.errstate(divide='ignore', invalid='ignore'):
                    return ((2*RiskTolerance*(sqrt(float(pi)*float(surfarea))))/(float(Pih)*(1-float(Pih))*3*float(Qbh)*float(MaskReq)*float(Cqh)*x*sqrt(0.0006)))
        else:
            def f(x):
                with np.errstate(divide='ignore', invalid='ignore'):
                    return ymax

            
    x=np.linspace(0,12,101)
    y=f(x)
    ymax = int(int(surfarea))
    fig = plt.figure()
    ax1 = fig.subplots()
    ax1.set_ylabel('Number of guests')
    ax1.set_xlabel('Event duration')
    ax1.fill_between(x, 0, y, color='#72FF89')#green
    ax1.fill_between(x, y, ymax, color='#FF7878')#red
    plt.ylim(0, ymax)
    plt.grid(color = 'blue', linestyle = '--', linewidth = 0.5)
    plt.axvline(x=0, c="blue")
    plt.axhline(y=0, c="blue")
    plt.legend(loc='upper left')
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url

conn = sqlite3.connect('Mcode.db', check_same_thread=False)
db = conn.cursor()
#FOR NICE PAGE USE THIS WHEN IMPORTING: {{ url_for('static', filename='nicepage.css') }}
@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "GET":
        userid = session['user_id']
        db.execute("SELECT username FROM users WHERE id=?", (userid,))
        usernamee = db.fetchall()
        User_ID = usernamee[0][0]
        username = User_ID
        db.execute("SELECT name FROM Files WHERE User_ID=?", (User_ID,))
        names = db.fetchall()
        db.execute("SELECT Event_ID FROM Files WHERE User_ID=?", (User_ID,))
        numbers = db.fetchall()
        db.execute("SELECT event_date FROM Files WHERE User_ID=?", (User_ID,))
        dates = db.fetchall()
        db.execute("SELECT LastUpdate FROM Files WHERE User_ID=?", (User_ID,))
        nos = db.fetchall()
        db.execute("SELECT NEGuest FROM Files WHERE User_ID=?", (User_ID,))
        NEGuests = db.fetchall()
        db.execute("SELECT GuestsReg FROM Files WHERE User_ID=?", (User_ID,))
        GuestsRegs = db.fetchall()
        db.execute("SELECT RScore FROM Files WHERE User_ID=?", (User_ID,))
        RScores = db.fetchall()
        name = []
        number = []
        date = []
        LastUpdate = []
        j = len(names)
        k = len(numbers)
        l = len(dates)
        r = len(nos)
        for i in range(k):
            g=numbers[i][0]
            number.append(g)
        for i in range(j):
            g=names[i][0]
            name.append(g)
        for i in range(l):
            g=dates[i][0]
            date.append(g)
        for i in range(r):
            g=nos[i][0]
            LastUpdate.append(g)
        db.execute("SELECT Event_Name FROM GuestLogs WHERE username=?", (username,))
        namesg = db.fetchall()
        db.execute("SELECT Event_ID FROM GuestLogs WHERE username=?", (username,))
        numbersg = db.fetchall()
        db.execute("SELECT event_date FROM GuestLogs WHERE username=?", (username,))
        datesg = db.fetchall()
        db.execute("SELECT GuestLastUpdate FROM GuestLogs WHERE username=?", (username,))
        GuestLastUpdates = db.fetchall()
        db.execute("SELECT RScoreGuest FROM GuestLogs WHERE username=?", (User_ID,))
        SafeGuests = db.fetchall()

        GuestsReg = []
        RScore = []
        SafeGuest = []
        NEGuest = []
        GuestLastUpdate = []
        nameg = []
        numberg = []
        dateg = []
        print(GuestsRegs)
        jkj = len(SafeGuests)
        jkh = len(NEGuests)
        tdr = len(GuestsRegs)
        erg = len(RScores)
        jg = len(namesg)
        kg = len(numbersg)
        lg = len(datesg)
        rg = len(GuestLastUpdates)
        for i in range(kg):
            g=numbersg[i][0]
            numberg.append(g)
        for i in range(jg):
            g=namesg[i][0]
            nameg.append(g)
        for i in range(lg):
            g=datesg[i][0]
            dateg.append(g)
        for i in range(rg):
            g=GuestLastUpdates[i][0]
            GuestLastUpdate.append(g)
        for i in range(jkj):
            g=SafeGuests[i][0]
            SafeGuest.append(g)
        for i in range(erg):
            g = RScores[i][0]
            RScore.append(g)
        for i in range(jkh):
            g = NEGuests[i][0]
            NEGuest.append(g)
        for i in range(tdr):
            g = GuestsRegs[i][0]
            GuestsReg.append(g)
            #GuestsReg.append(GuestsRegs[i][0])
            #RScore.append(RScores[i][0])
            #NEGuest.append(NEGuests[i][0])
            #SafeGuest.append(SafeGuests[i][0])
        print(NEGuest)
        print(NEGuests)
        print("okok", list(zip(NEGuest)))
        return render_template("Home.html", results=zip(name, number, date, LastUpdate, RScore, NEGuest, GuestsReg), otherresults=zip(nameg, numberg, dateg, GuestLastUpdate, SafeGuest, NEGuest, GuestsReg))
    if request.method == "POST":
        return redirect("/opened")

@app.route("/profile")
@login_required
def profile():
    user_id = session["user_id"]
    db.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    info = db.fetchall()
    name = info[0][0]
    email = info[0][3]
    return render_template("profile.html", name=name, email=email)

@app.route("/guestlog", methods=["GET", "POST"])
@login_required
def guestlog():
    if request.method == "GET":
        return render_template("guestlog.html")
    if request.method == "POST":
        user_id = session["user_id"]
        db.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        info = db.fetchall()
        name = info[0][0]
        Event_ID = request.form.get("event_id")
        db.execute("SELECT Event_ID FROM files WHERE Event_ID=?", (Event_ID,))
        exist = db.fetchall()
        db.execute("SELECT pm FROM GuestLogs WHERE username=? AND Event_ID=?", (name, Event_ID))
        okay = db.fetchall()
        try:
            if not okay[0] == None:
                return apology("Already registered!", 400)
        except:
            try:
                if not exist[0] == None:
                    session["event_id"] = Event_ID
                    return redirect("/guest")
            except:
                return apology("ID does not exist!", 400)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.errorhandler(500)
def page_not_found(error):
    return render_template('page_error.html'), 500

@app.route("/info", methods=["GET"])
def info():
    infofs = request.args["info"]
    session["info"] = infofs
    return jsonify(True)

@app.route("/files", methods=["GET", "POST"])
@login_required
def files():
    if request.method == "GET":
        userid = session['user_id']
        username = db.execute("SELECT username FROM users WHERE id=:userid", userid=userid)
        User_ID = username[0]["username"]
        name = db.execute("SELECT name FROM Files WHERE User_ID=:User_ID", User_ID=User_ID)
        flash(name)
        return render_template("files.html", name=name)
    else:
        return redirect("/opened")

@app.route("/opened", methods=["GET", "POST"])
@login_required
def opened():
    if request.method == "GET":
        Event_ID = session["info"]
        db.execute("SELECT RScore, User_ID, name, location, localinci, event_date, stime, recirculation, filtration, humidity, ceiling, surfarea, Qbh, Cqh, outdoor, ageAvg, LastUpdate, RiskTolerance, NEGuest, Description, MaskReq, minutes, hours, GuestsReg, RScore FROM Files WHERE Event_ID=?", (Event_ID,))
        info = db.fetchall()
        User_ID = info[0][1]
        name = info[0][2]
        location = info[0][3]
        localinci = info[0][4]
        event_date = info[0][5]
        stime = info[0][6]
        recirculation = info[0][7]
        filtration = info[0][8]
        humidity = info[0][9]
        surfarea = info[0][11]
        ceiling = info[0][10]
        Pih = int(localinci)/100000
        Qbh = info[0][12]
        Cqh = info[0][13]
        outdoor = info[0][14]
        ageAvg = info[0][15]
        LastUpdate = info[0][16]
        outvalue = info[0][17]
        NEGuest = info[0][18]
        Description = info[0][19]
        MaskReq = info[0][20]
        minutes = info[0][21]
        hours = info[0][22]
        GuestsReg = info[0][23]
        RScore = info[0][24]
        if not Description:
            Description = "No Description"

        HRj = Hcalc(surfarea, ceiling, hours, minutes, recirculation, filtration, humidity, Pih, Qbh, MaskReq, Cqh, NEGuest, outdoor, ageAvg, outvalue)

        

        img = BytesIO()
        Rc = ((0.00007/60)*pow(float(recirculation)*float(ceiling), 1/2))
        Lc = (float(recirculation)/3600)*(1+(pow(10, -12)/(Rc*Rc)))+((0.6*float(humidity)/3600))+((float(outdoor)*float(filtration))/3600)
        #equation here at return function
        ymax = int(surfarea)
        if outvalue==1:
            def f(x):
                with np.errstate(divide='ignore', invalid='ignore'):
                    return ((1+pow((1+((4*3600*Lc*float(surfarea)*float(ceiling)*0.1)/(0.3*(float(Qbh)*float(Qbh)*float(MaskReq)*float(MaskReq)*float(Cqh)*float(Pih)*(1-float(Pih))*x)))), 1/2))/2)
        else:
            if math.floor(float(MaskReq)) == 1:
                def f(x):
                    with np.errstate(divide='ignore', invalid='ignore'):
                        return ((2*0.1*(sqrt(float(pi)*float(surfarea))))/(float(Pih)*(1-float(Pih))*3*float(Qbh)*float(MaskReq)*float(Cqh)*x*sqrt(0.0006)))
            else:
                def f(x):
                    with np.errstate(divide='ignore', invalid='ignore'):
                        return ymax

        
        
        print((int(np.sign(float(MaskReq)-1))+1))
        
        NEGuests = int(NEGuest)
        dd = int(hours)+(int(minutes)/60)
        x=np.linspace(0,12,101)
        y=f(x)
        print(f(x))
        fig = plt.figure()
        ax1 = fig.subplots()
        ax1.plot(dd, NEGuests, "ro", color="#053b91")
        ax1.set_ylabel('Number of guests')
        ax1.set_xlabel('Event duration (h)')
        ax1.fill_between(x, 0, y, color='#72FF89')#green
        ax1.fill_between(x, y, ymax, color='#FF7878')#red
        plt.grid(color = 'blue', linestyle = '--', linewidth = 0.5)
        plt.ylim(0, ymax)
        plt.axvline(x=0, c="blue")
        plt.axhline(y=0, c="blue")
        plt.legend(loc='upper left')
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
            
        Qbhs=""
        if float(Qbh) == 0.5:
            Qbhs = "stationary - standing, sitting, laying down"
        elif float(Qbh) == 1.38:
            Qbhs = "low exertion - walking around, light movement"
        elif float(Qbh) == 2.35:
            Qbhs = "moderate exertion - formal dancing, moderate exercise"
        elif float(Qbh) == 3.3:
            Qbhs = "high exertion - fast/energetic dancing, intense exercise"


        Cqhs=""
        if float(Cqh) == 9:
            Cqhs="silence"
        elif float(Cqh) == 29:
            Cqhs="whispering"
        elif float(Cqh) == 72:
            Cqhs ="talking"
        elif float(Cqh) == 142:
            Cqhs = "loud talking"
        elif float(Cqh) == 970:
            Cqhs = "singing"

        MaskReqs=""
        if float(MaskReq) == 1:
            MaskReqs = "no mask"
        elif float(MaskReq) == 0.5:
            MaskReqs = "single-layer textile (50% filtration efficiency)"
        elif float(MaskReq) == 0.3:
            MaskReqs = "multi-layer textile (70%)"
        elif float(MaskReq) == 0.1:
            MaskReqs = "disposable surgical (90%)"
        elif float(MaskReq) == 0.05:
            MaskReqs = "FFP2/N95 (95%)"
            
        ageAvgs=""
        if float(ageAvg)==0.23:
            ageAvgs="children (0-14)"
        if float(ageAvg)==0.68:
            ageAvgs="adults (15-64)"
        if float(ageAvg) == 1:
            ageAvgs="elderly (65+)"

        humidity=100*float(humidity)
        return render_template("opened.html", GuestsReg=GuestsReg, Qbhs=Qbhs, Cqhs=Cqhs, humidity=humidity, MaskReqs=MaskReqs, plot_url=plot_url, Event_ID=Event_ID, User_ID=User_ID, name=name, location=location, event_date=event_date, stime=stime, surfarea=surfarea, ceiling=ceiling, recirculation=recirculation, filtration=filtration, hours=hours, minutes=minutes, NEGuest=NEGuest, localinci=localinci, Description=Description, ageAvgs=ageAvgs, LastUpdate=LastUpdate, HRj=HRj)
    else:
        name = session["info"]
        event = db.execute("SELECT * FROM Files WHERE name=:name", name=name)
        Event_ID = event[0]["Event_ID"]
        recirculation = request.form.get("recirculation")
        hours = request.form.get("hours")
        minutes = request.form.get("minutes")
        filtration = request.form.get("filtration")
        humidity = request.form.get("humidity")
        outdoor = request.form.get("outdoor")
        ceiling = request.form.get("ceiling")
        name = request.form.get("name")
        if not name or not ceiling or not outdoor or not humidity or not filtration or not minutes or not hours or not recirculation:
            return apology("Oops! one of the fields is empty!")
        db.execute("UPDATE Files SET recirculation=:recirculation, hours=:hours, minutes=:minutes, filtration=:filtration, humidity=:humidity, outdoor=:outdoor, ceiling=:ceiling, name=:name WHERE Event_ID=:Event_ID", recirculation=recirculation, hours=hours, minutes=minutes, filtration=filtration, humidity=humidity, outdoor=outdoor, ceiling=ceiling, name=name, Event_ID=Event_ID)
        conn.commit()
        flash("Updated successfully!")
        return redirect("/")

@app.route("/host", methods=["GET", "POST"])
@login_required
def host():
    if request.method == "GET":
        return render_template("HostedEvent_Edit_1.html")
    if request.method == "POST":
        #add each request.form to its if value except for name and neguest, in if function, add variables to database. Create on elif name, update on neguest

        room = request.form.get("surfarea")
        humidity = request.form.get("humidity")
        NEGuest = request.form.get("NEGuest")
        if room:
            Event_ID = str(random.randint(1000,9999))
            session["ID_EVENT"] = Event_ID
            name=request.form.get("name")
            location = request.form.get("location")
            localinci = request.form.get("localinci")
            event_date = request.form.get("date")
            stime = request.form.get("stime")
            recirculation = request.form.get("recirculation")
            filtration = request.form.get("filtration")
            outdoor = request.form.get("outdoor")
            humidity = request.form.get("humidity")
            ceiling = request.form.get("ceiling")
            surfarea = request.form.get("surfarea")
            Cqh = request.form.get("Cqh")
            Qbh = request.form.get("Qbh")
            ageAvg = request.form.get("ageAvg")
            airfiltercheck = request.form.get("checkbox-1")
            checkoutdoor = request.form.get("checkoutdoor")
            if checkoutdoor != "on":
                if not ceiling:
                    return apology("Make sure all fields are filled.", 400)
                else:
                    ceiling = int(float(ceiling))
                    ceiling = str(ceiling)
            if not humidity or not surfarea or not localinci:
                return apology("Make sure all fields are filled.", 400)

            humidity = int(float(humidity))
            humidity = str(humidity)
            surfarea = int(float(surfarea))
            surfarea = str(surfarea)
            localinci = int(float(localinci))
            localinci = str(localinci)
            if name.isnumeric() or len(name) > 50 or len(name) < 2:
                return apology("Event name must be maximum 50 characters.", 400)
            if len(location) > 100 or location.isnumeric():
                return apology("Location must be maximum 100 characters.", 400)    
            #make sure date is not before current
            if len(stime) > 20:
                return apology("Starting time must be maximum 20 characters.", 400)    
            if surfarea.isnumeric() == False or int(surfarea)<10 or int(surfarea) > 5000:
                return apology("400", "Floor surface area must be a number between 10 and 5000.") 
            if checkoutdoor != "on":
                k=1
                if ceiling.isnumeric() == False or int(ceiling) < 2 or int(ceiling) > 15:
                    return apology("Ceiling height must be a number between 2 and 15.", 400)  
                if not recirculation:
                    return apology("Please select a ventilation type.", 400)
                if airfiltercheck == "On":
                    if not filtration:
                        return apology("Please select recirculation rate.", 400)
                    if not outdoor:
                        return apology("Please select air filter quality.", 400)
                elif airfiltercheck =="Off":
                    filtration = 1
                    outdoor=1
            else:
                k=0
                ceiling = 1
                recirculation = 1
                filtration = 1
                outdoor = 1
                
            if not filtration:
                filtration = 0.001
            if not outdoor:
                outdoor = 0.001

            #fix air filter used checkbox
            #use air filter used checkbox to make sure field has to be checked
            #if filtration == 0.111 and airfiltercheckbox=true:
                #return apology("Please select the air filter quality that most closely matches your unit.", 400)
            #if outdoor == 0.1 and airfiltercheckbox=true:
                #return apology("Please select the air filter quality that most closely matches your unit.", 400)
            if Qbh == "0.1":
                return apology("Please select an expected level of activity.", 400)
            if Cqh == "0.1":
                return apology("Please select an expected level of speaking.", 400)
            #fix food/beverage served checkbox
            
            #do equivalent for hours, service mode+timing 
            #if filtration == 0.111 and airfiltercheckbox=true:
                #return apology("Please select the air filter quality that most closely matches your unit.", 400)
            #if outdoor == 0.1 and airfiltercheckbox=true:
                #return apology("Please select the air filter quality that most closely matches your unit.", 400)
            if humidity.isnumeric() == False or int(humidity)>100 or int(humidity)<0:
                return apology("Expected % humidity must be a number between 0 and 100.", 400)
            if localinci.isnumeric() == False or int(localinci)>100000 or int(localinci)<0:
                return apology("Expected local incidence must be between 0 and 100 000.", 400)
            
            if not ageAvg:
                return apology("Make sure to select an age average", 400)

            Pih = int(localinci)/100000

            humidity = int(humidity)/100
            Rc = ((0.00007/60)*pow(float(recirculation)*float(ceiling), 1/2))
            Lc = (float(recirculation)/3600)*(1+(pow(10, -12)/(Rc*Rc)))+((0.6*float(humidity)/3600))+((float(outdoor)*float(filtration))/3600)
            #equation here at return function
            MaskReq1 = 0.05
            MaskReq2 = 0.1
            MaskReq3 = 0.3
            MaskReq4 = 0.5
            MaskReq5 = 1
            RiskTolerance1 = 1
            #2 * the actual value of risk tolerance, so 0.1*2
            RiskTolerance2 = 0.2
            RiskTolerance3 = 0.02
            plot_url1 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq1, RiskTolerance1, k)
            plot_url2 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq2, RiskTolerance1, k)
            plot_url3 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq3, RiskTolerance1, k)
            plot_url4 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq4, RiskTolerance1, k)
            plot_url5 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq5, RiskTolerance1, k)
            plot_url6 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq1, RiskTolerance2, k)
            plot_url7 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq2, RiskTolerance2, k)
            plot_url8 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq3, RiskTolerance2, k)
            plot_url9 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq4, RiskTolerance2, k)
            plot_url10 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq5, RiskTolerance2, k)
            plot_url11 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq1, RiskTolerance3, k)
            plot_url12 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq2, RiskTolerance3, k)
            plot_url13 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq3, RiskTolerance3, k)
            plot_url14 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq4, RiskTolerance3, k)
            plot_url15 = Mgraph(Lc, surfarea, ceiling, Qbh, Cqh, Pih, MaskReq5, RiskTolerance3, k)
            LastUpdate = datetime.now().strftime("%Y-%m-%d, %H:%M") 
            db.execute("INSERT INTO Files(LastUpdate, outdoor, Qbh, Cqh, Event_ID, name, location, localinci, event_date, stime, recirculation, filtration, humidity, ceiling, surfarea, ageAvg, RiskTolerance) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" , (LastUpdate, outdoor, Qbh, Cqh, Event_ID, name, location, localinci, event_date, stime, recirculation, filtration, humidity, ceiling, surfarea, ageAvg, k))
            conn.commit()
            return render_template("HostedEvent_Edit_25.html", plot_url1=plot_url1, plot_url2=plot_url2, plot_url3=plot_url3, plot_url4=plot_url4, plot_url5=plot_url5, plot_url6=plot_url6, plot_url7=plot_url7, plot_url8=plot_url8, plot_url9=plot_url9, plot_url10=plot_url10, plot_url11=plot_url11, plot_url12=plot_url12, plot_url13=plot_url13, plot_url14=plot_url14, plot_url15=plot_url15)
            
        elif NEGuest:
            ServTiming = request.form.get("ServTiming")
            ServHours = request.form.get("ServHours")
            ServMinutes = request.form.get("ServMinutes")
            PassReq = request.form.get("PassReq")
            MaskReq = request.form.get("MaskReq")

            ServMode = request.form.get("ServMode")
            Description = request.form.get("Description")
            foodcheck = request.form.get("checkbox-3")
            if not Description:
                Description = "No Description"
            if not PassReq:
                PassReq = "Off"
            hours = request.form.get("hour")
            minutes = request.form.get("minute")

            Event_ID = session["ID_EVENT"]
            
            #check for a time larger than 0, doesnt work
            if int(float(hours))+int(float(minutes))==0:
                return apology1("Please select duration of event.", 400)
            if not NEGuest or NEGuest.isnumeric() == False or int(NEGuest)>500 or int(NEGuest)<2:
                return apology1("Enter expected number of guests between 2 and 500.", 400)
            
            aok="l"
            if foodcheck == "On":
                aok="served"
                if not ServTiming or not ServMode or not ServHours or not ServMinutes:
                    return apology1("Please select all service informations.", 400)
            
            if foodcheck != "On":
                ServMode = 0
                ServTiming = 0
                ServHours = 0
                ServMinutes = 0
                aok="not served"
            
            #current user? Change to event user instead

            userid = session['user_id']
            db.execute("SELECT username FROM users WHERE id=?", (userid,))
            username = db.fetchall()
            User_ID = username[0][0]
            db.execute("UPDATE Files SET User_ID=?, NEGuest=?, minutes=?, hours=?, PassReq=?, MaskReq=?, Description=?, ServMode=?, ServTiming=?, ServHours=?, ServMinutes=? WHERE Event_ID=?", (User_ID, NEGuest, minutes, hours, PassReq, MaskReq, Description, ServMode, ServTiming, ServHours, ServMinutes, Event_ID))
            conn.commit()
            flash("created successfully!")
            db.execute("SELECT Event_ID, User_ID, name, location, localinci, event_date, stime, recirculation, filtration, humidity, ceiling, surfarea, Qbh, Cqh, outdoor, ageAvg, LastUpdate, RiskTolerance FROM Files WHERE Event_ID=?", (Event_ID,))
            info = db.fetchall()
            Event_ID = info[0][0]
            User_ID = info[0][1]
            name = info[0][2]
            location = info[0][3]
            localinci = info[0][4]
            event_date = info[0][5]
            stime = info[0][6]
            recirculation = info[0][7]
            filtration = info[0][8]
            humidity = info[0][9]
            surfarea = info[0][11]
            ceiling = info[0][10]
            Pih = int(localinci)/100000
            Qbh = info[0][12]
            Cqh = info[0][13]
            outdoor = info[0][14]
            ageAvg = info[0][15]
            LastUpdate = info[0][16]
            outvalue = info[0][17]

            
            HRj = Hcalc(surfarea, ceiling, hours, minutes, recirculation, filtration, humidity, Pih, Qbh, MaskReq, Cqh, NEGuest, outdoor, ageAvg, outvalue)
            db.execute("UPDATE Files SET RScore=? WHERE Event_ID=?", (HRj, Event_ID))
            conn.commit()
            ps=0
            if float(str(MaskReq))<1:
                ps=0
            else:
                ps=1
            
            if float(outvalue)==1:
                invalue=0
            else:
                invalue=1


            img = BytesIO()
            Rc = ((0.00007/60)*pow(float(recirculation)*float(ceiling), 1/2))
            Lc = (float(recirculation)/3600)*(1+(pow(10, -12)/(Rc*Rc)))+((0.6*float(humidity)/3600))+((float(outdoor)*float(filtration))/3600)
            #equation here at return function
            ymax = int(surfarea)
            if outvalue==1:
                def f(x):
                    with np.errstate(divide='ignore', invalid='ignore'):
                        return ((1+pow((1+((4*3600*Lc*float(surfarea)*float(ceiling)*0.1)/(0.3*(float(Qbh)*float(Qbh)*float(MaskReq)*float(MaskReq)*float(Cqh)*float(Pih)*(1-float(Pih))*x)))), 1/2))/2)
            else:
                if math.floor(float(MaskReq)) == 1:
                    def f(x):
                        with np.errstate(divide='ignore', invalid='ignore'):
                            print("ROOMSAFEW")
                            return ((2*0.1*(pi+0.15*0.15)*(sqrt(float(surfarea))))/(float(Pih)*(1-float(Pih))*3*float(Qbh)*float(MaskReq)*float(Cqh)*x*sqrt(pi*0.0006)))
                else:
                    def f(x):
                        with np.errstate(divide='ignore', invalid='ignore'):
                            return ymax

            x=np.linspace(0,12,101)
            y=f(x)
            ymax = int(surfarea)
            NEGuests = int(NEGuest)
            dd = int(hours)+int(minutes)/60
            fig = plt.figure()
            ax1 = fig.subplots()
            ax1.plot(dd, NEGuests, "ro", color="#053b91")
            ax1.set_ylabel('Number of guests')
            ax1.set_xlabel('Event duration')
            ax1.fill_between(x, 0, y, color='#72FF89')#green
            ax1.fill_between(x, y, ymax, color='#FF7878')#red
            plt.grid(color = 'blue', linestyle = '--', linewidth = 0.5)
            plt.ylim(0, ymax)
            plt.axvline(x=0, c="blue")
            plt.axhline(y=0, c="blue")
            plt.legend(loc='upper left')
            plt.savefig(img, format='png')
            plt.close()
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode('utf8')
            
            Qbhs=""
            if float(Qbh) == 0.5:
                Qbhs = "stationary - standing, sitting, laying down"
            elif float(Qbh) == 1.38:
                Qbhs = "low exertion - walking around, light movement"
            elif float(Qbh) == 2.35:
                Qbhs = "moderate exertion - formal dancing, moderate exercise"
            elif float(Qbh) == 3.3:
                Qbhs = "high exertion - fast/energetic dancing, intense exercise"


            Cqhs=""
            if float(Cqh) == 9:
                Cqhs="silence"
            elif float(Cqh) == 29:
                Cqhs="whispering"
            elif float(Cqh) == 72:
                Cqhs ="talking"
            elif float(Cqh) == 142:
                Cqhs = "loud talking"
            elif float(Cqh) == 970:
                Cqhs = "singing"

            MaskReqs=""
            if MaskReq == "1":
                MaskReqs = "no mask"
            elif MaskReq == "0.5":
                MaskReqs = "single-layer textile (50% filtration efficiency)"
            elif MaskReq == "0.3":
                MaskReqs = "multi-layer textile (70%)"
            elif MaskReq == "0.1":
                MaskReqs = "disposable surgical (90%)"
            elif MaskReq == "0.05":
                MaskReqs = "FFP2/N95 (95%)"
            
            ageAvgs=""
            if float(ageAvg)==0.23:
                ageAvgs="children (0-14)"
            if float(ageAvg)==0.68:
                ageAvgs="adults (15-64)"
            if float(ageAvg) == 1:
                ageAvgs="elderly (65+)"

            humidity=100*float(humidity)


            return render_template("HostedEvent_Record4.html", Qbhs=Qbhs, Cqhs=Cqhs, humidity=humidity, aok=aok, MaskReqs=MaskReqs, plot_url=plot_url, Event_ID=Event_ID, User_ID=User_ID, name=name, location=location, event_date=event_date, stime=stime, surfarea=surfarea, ceiling=ceiling, recirculation=recirculation, filtration=filtration, hours=hours, minutes=minutes, NEGuest=NEGuest, localinci=localinci, Description=Description, ageAvgs=ageAvgs, LastUpdate=LastUpdate, HRj=HRj)
        else:
            return render_template("HostedEvent_Edit_1.html")

@app.route("/guest", methods=["GET", "POST"])
@login_required
def guest():
    if request.method == "GET":
        Event_ID = session["event_id"]
        db.execute("SELECT name, surfarea, ceiling, hours, minutes, outdoor, recirculation, filtration, humidity, NEGuest, Description, event_date, stime, location, User_ID, LastUpdate FROM Files WHERE Event_ID=?", (Event_ID,))
        event = db.fetchall()
        NEGuest = event[0][9]
        name = event[0][0]
        surfarea = event[0][1]
        ceiling = event[0][2]
        hours = event[0][3]
        minutes = event[0][4]
        outdoor = event[0][5]
        recirculation = event[0][6]
        filtration = event[0][7]
        humidity = event[0][8]
        Description = event[0][10]
        event_date = event[0][11]
        stime = event[0][12]
        location = event[0][13]
        User_ID = event[0][14]
        LastUpdated = event[0][15]
        humidity = humidity *100
        return render_template("Guest_Edit.html", LastUpdated=LastUpdated, Event_ID=Event_ID, User_ID=User_ID, location=location, event_date=event_date, stime=stime, Description=Description, NEGuest=NEGuest, name=name, surfarea=surfarea, ceiling=ceiling, hours=hours, minutes=minutes, outdoor=outdoor, recirculation=recirculation, filtration=filtration, humidity=humidity)
    if request.method == "POST":
        Event_ID = session["event_id"]
        userid = session['user_id']
        db.execute("SELECT username FROM users WHERE id=?", (userid,))
        usernamess = db.fetchall()
        username = usernamess[0][0]
        db.execute("SELECT surfarea, NEGuest, ceiling, humidity, hours, minutes, recirculation, outdoor, filtration, localinci, ServMode, ServTiming, ServHours, event_date, Qbh, Cqh, ServMinutes, MaskReq, User_ID, location, Description, LastUpdate, ageAvg, stime, RiskTolerance, GuestsReg FROM Files WHERE Event_ID=?", (Event_ID,))
        event = db.fetchall()
        surfarea = event[0][0]
        NEGuest = event[0][1]
        ceiling = event[0][2]
        humidity = event[0][3]
        humidity1 = humidity*100
        hours = event[0][4]
        minutes = event[0][5]
        recirculation = event[0][6]   
        outdoor = event[0][7]
        filtration = event[0][8]
        localinci = event[0][9]
        ServMode = event[0][10]
        ServTiming = event[0][11]
        ServHours = event[0][12]
        event_date = event[0][13]
        Qbh = event[0][14]
        Cqh = event[0][15]
        ServMinutes = event[0][16]
        Pmh = event[0][17]
        User_ID = event[0][18]
        location = event[0][19]
        Description = event[0][20]
        LastUpdate = event[0][21]
        ageAvg = event[0][22]
        stime = event[0][23]
        outvalue = event[0][24]
        GuestsReg = event[0][25]
        GuestsReg = GuestsReg+1
        
        Qb = request.form.get("Qb")
        Cq = request.form.get("Cq")
        Th = request.form.get("Th")
        Tm = request.form.get("Tm")
        Tstay = request.form.get("Tstay")
        pm = request.form.get("pm")
        Vs = request.form.get("Vs")
        Vt = request.form.get("Vt")
        age = request.form.get("age")



        if not Qb or not Cq or not Th or not Tm or not Tstay or not pm or not pm or not age or not Vs:
            return apology("Make sure all fields are filled!", 400)


        db.execute("SELECT name FROM files WHERE Event_ID=?", (Event_ID,))
        EventName = db.fetchall()
        Event_Name = EventName[0][0]
        names = db.execute("SELECT Qb FROM GuestLogs WHERE Event_ID=?", (Event_ID,))                
        names = db.fetchall()

        numbers = db.execute("SELECT Cq FROM GuestLogs WHERE Event_ID=?", (Event_ID,))
        numbers = db.fetchall()

        dates = db.execute("SELECT Th FROM GuestLogs WHERE Event_ID=?", (Event_ID,))
        dates = db.fetchall()

        datess = db.execute("SELECT Tm FROM GuestLogs WHERE Event_ID=?", (Event_ID,))
        datess = db.fetchall()

        datesss = db.execute("SELECT pm FROM GuestLogs WHERE Event_ID=?", (Event_ID,))
        datesss = db.fetchall()

        ages = db.execute("SELECT age FROM GuestLogs WHERE Event_ID=?", (Event_ID,))
        ages = db.fetchall()

        age = []
        Cql = []
        Qbl = []
        Thl = []
        Tml = []
        pml = []
        p = len(ages)
        j = len(names)
        k = len(numbers)
        l = len(dates)
        ls = len(datess)
        lss = len(datesss)
        for i in range(p):
            g=ages[i][0]
            age.append(g)
        for i in range(k):
            g=names[i][0]
            Qbl.append(g)
        for i in range(j):
            g=numbers[i][0]
            Cql.append(g)
        for i in range(l):
            g=dates[i][0]
            Thl.append(g)
        for i in range(ls):
            g=datess[i][0]
            Tml.append(g)
        for i in range(lss):
            g=datesss[i][0]
            pml.append(g)
        for i in range(NEGuest-j):
            Cql.append(Cqh)
            Qbl.append(Qbh)
            Thl.append(hours)
            Tml.append(minutes)
            pml.append(Pmh)
            age.append(ageAvg)
        #values1 = [0.65, 0.24, 0.32, 0.43, 0.52, 0.59, 0.57]
        #Values2 = [0.65, 0.2, 0.26, 0.29, 0.29, 0.29, 0.29]
        #Values3 = [0.65, 0.08, 0.1, 0.17, 0.22, 0.22, 0.22]
        #if infec1 == 0:
            #infec = 0.65
        #elif infec1 == 1:
            #infec = Values1[int(infec2)]
        #elif infec1 == 2:
            #infec = Values2[int(infec2)]
        #else:
            #infec = Values3[int(infec2)]
        #find infectivity rate using table of values
        age = request.form.get("age")
        S=0

        if Tstay == ServTiming:
            S=1
        elif Tstay == "z" or ServTiming == "z":
            S=1

        if pm=="0.3":
            pm=0.3
            pr = "Multilayer textile"
        elif pm == "0.5":
            pm=0.5
            pr = "Single layer textile"
        elif pm == "1":
            pm=1
            pr = "No mask"
        elif pm == "0.1":
            pm = 0.1
            pr = "Disposable surgical"
        elif pm == "0.05":
            pm = 0.05
            pr = "N95"

        if float(Pmh)==0.3:
            Pmhs = "Multilayer textile"
        elif float(Pmh) == 0.5:
            Pmhs = "Single layer textile"
        elif float(Pmh) == 1:
            Pmhs = "No mask"
        elif float(Pmh) == 0.1:
            Pmhs = "Disposable surgical"
        elif float(Pmh) == 0.05:
            Pmhs = "N95" 
        Tnet = 3600*hours+60*minutes
        ServNet = int(ServHours)*3600+int(ServMinutes)*60

        pid = pm
        pm=(((S*ServNet)/float(Tnet))*(1.000-pm))
        if pm==0:
            pm=pid

        Pih = int(localinci)/100000
        
        Grj = calc(surfarea, ceiling, hours, minutes, recirculation, filtration, humidity, Pih, Qb, pm, Cq, Vs, Vt, NEGuest, pml, Cql, Qbl, Thl, Tml, outdoor, S, ServHours, ServMinutes, age, outvalue)


        HRj = Hcalc(surfarea, ceiling, hours, minutes, recirculation, filtration, humidity, Pih, Qbh, Pmh, Cqh, NEGuest, outdoor, ageAvg, outvalue)
        db.execute("UPDATE Files SET RScore=?, GuestsReg=? WHERE Event_ID=?", (HRj, GuestsReg, Event_ID))
        conn.commit()

        GuestLastUpdate = datetime.now().strftime("%Y-%m-%d, %H:%M")
        Qbb = ""
        if (Qb) == "0.5":
            Qbb = "stationary - standing, sitting, laying down"
        elif (Qb) == "1.38":
            Qbb = "low exertion - walking around, light movement"
        elif (Qb) == "2.35":
            Qbb = "moderate exertion - formal dancing, moderate exercise"
        elif (Qb) == "3.3":
            Qbb = "high exertion - fast/energetic dancing, intense exercise"
        if (age)=="0.23":
            age="children (0-14)"
        if (age)=="0.68":
            age="adults (15-64)"
        if (age) == "1":
            age="elderly (65+)"
        Qbhs=""
        if float(Qbh) == 0.5:
            Qbhs = "stationary - standing, sitting, laying down"
        elif float(Qbh) == 1.38:
            Qbhs = "low exertion - walking around, light movement"
        elif float(Qbh) == 2.35:
            Qbhs = "moderate exertion - formal dancing, moderate exercise"
        elif float(Qbh) == 3.3:
            Qbhs = "high exertion - fast/energetic dancing, intense exercise"
        Cqhs=""
        ages = ""
        if float(Cqh) == 9:
            Cqhs="silence"
        elif float(Cqh) == 29:
            Cqhs="whispering"
        elif float(Cqh) == 72:
            Cqhs ="talking"
        elif float(Cqh) == 142:
            Cqhs = "loud talking"
        elif float(Cqh) == 970:
            Cqhs = "singing"
        db.execute("INSERT INTO GuestLogs (GuestLastUpdate, Qb, pm, Cq, Vs, Vt, Tm, Th, Event_ID, Event_Name, username, event_date, age, RScoreGuest) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (GuestLastUpdate, Qb, pm, Cq, Vs, Vt, Tm, Th, Event_ID, Event_Name, username, event_date, age, Grj))
        conn.commit()
        return render_template("Guest_Record3.html", Vs=Vs, stime=stime, Qbhs=Qbhs, Cqhs=Cqhs, Pmhs=Pmhs, LastUpdate=LastUpdate, Description=Description, recirculation=recirculation, location=location, User_ID=User_ID, NEGuest=NEGuest, pr=pr, hours=hours, minutes=minutes, GuestLastUpdate=GuestLastUpdate, Event_ID=Event_ID, HRj=HRj, Grj=Grj, username=username, Qbb=Qbb, event_date=event_date, humidity1=humidity1, Event_Name=Event_Name, surfarea=surfarea, ceiling=ceiling, age=age)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        username = request.form.get("username")
        db.execute("SELECT * FROM users WHERE username = ?", (username,))
        rows = db.fetchall()
        # Ensure username exists and password is correct
        password = request.form.get("password")
        if len(rows) != 1 or not check_password_hash(rows[0][1], password):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0][2]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/front-page")
def fron_page():
    return render_template("Front-Page.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    username = request.args["username"]

    if len(username) == 0:
        return jsonify(False)

    db.execute("SELECT * FROM users WHERE username = ?", (username,))
    rows = db.fetchall()
    if rows:
        return jsonify(False)

    return jsonify(True)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        current_email = request.form.get("Email")
        db.execute("SELECT * FROM users WHERE username = ?", (username,))
        check_username = db.fetchall()
        if check_username:
            return apology("Username already exists", 400)
        elif not username:
            return apology("Missing username", 400)
        elif not password:
            return apology("Missing password", 400)
        elif not confirmation:
            return apology("Missing confirmation password", 400)
        elif password != confirmation:
            return apology("Passwords don't match!", 400)

        hash = generate_password_hash(password)
        username=request.form.get("username")
        db.execute("INSERT INTO users (username, hash, Email) VALUES (?, ?, ?)", (username, hash, current_email))
        conn.commit()
        db.execute("SELECT id FROM users WHERE username = :username AND hash = ?", (username, hash))
        user_id = db.fetchall()
        session["user_id"] = user_id[0][0]

       #sender.send(receiver=current_email, subject='Welcome to RoomSafe!', message="""<h2>Welcome to <strong>RoomSafe</strong>!</h2> 
       #<body>
       #    <p></p>
       #    Try our new Hosting features.
       #    <p>Find how COVID Safe your events really are!</p>
       #    <small>If you have not registered for RoomSafe.org, simply ignore this message.</small>
       #</body>
       #""")
       
        return redirect("/")



@app.route("/confirmation", methods=["GET", "POST"])
def send_confirmation_email(user_email):
    confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

    confirm_url = url_for(
        'users.confirm_email',
        token=confirm_serializer.dumps(user_email, salt='email-confirmation-salt'),
        _external=True)

    html = render_template(
        'email_confirmation.html',
        confirm_url=confirm_url)

    send_email('Confirm Your Email Address', [user_email], html) 

