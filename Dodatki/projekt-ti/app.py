from flask import Flask, escape, request, render_template, session
from werkzeug.utils import secure_filename
import os
import tempfile
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import csv
import numbers
import math


app = Flask(__name__)
app.secret_key = b'_5#y2L"Fff8z\n\xec]/'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/footer.html")
def footer():
    return render_template("footer.html")

@app.route("/header.html")
def header():
    return render_template("header.html")

@app.route("/analysis.html")
def analysis_html():
    if "file_name" in session:
        file_name = session["file_name"]
    else:
        file_name = None
    if "choose_data" in session:
        choose_data = session["choose_data"] 
    else:
        choose_data=None
    if "first_line" in session:
        first_line = session["first_line"] 
    else:
        first_line=[]
    if "list_categorical_data" in session:
        list_categorical_data = session["list_categorical_data"]
    else:
        list_categorical_data=[]
    if "list_categorical_data_header" in session:
        list_categorical_data_header = session["list_categorical_data_header"]
    else:
        list_categorical_data_header = []
    if "select_1" in session:
        select_1 = session["select_1"]
    else:
        session["select_1"] = None
        select_1 = None
    if "select_2" in session:
        select_2 = session["select_2"]
    else:
        session["select_2"] = None
        select_2 = None
    if "select_categorical" in session:
        select_categorical = session["select_categorical"]
    else:
        session["select_categorical"] = None
        select_categorical = None
    if "categorical_index" in session:
        categorical_index = session["categorical_index"]
    else:
        categorical_index = None
    if "X" in session:
        X = session["X"]
    else:
        X = []
    if "Y" in session:
        Y = session["Y"]
    else:
        Y = []
    if "average_X" in session:
        average_X = session["average_X"]
    else:
        average_X = None
    if "average_Y" in session:
        average_Y = session["average_Y"]
    else:
        average_Y = None
    if "zip_table" in session:
        zip_table = session["zip_table"]
    else:
        zip_table = None
    if "color" in session:
        color = session["color"]
    else:
        color = "#FFFFFF"
    if "graph" in session:
        graph = session["graph"]
    else:
        graph = None
    return render_template("analysis.html", graph=graph, file_name=file_name, choose_data=choose_data, first_line=first_line, list_categorical_data_header=list_categorical_data_header, list_categorical_data=list_categorical_data, select_1=select_1, select_2=select_2, select_categorical=select_categorical,categorical_index=categorical_index, X=X, Y=Y, average_X=average_X, average_Y=average_Y,zip_table=zip_table, color=color)

@app.route("/analysis", methods=['POST', 'GET'])
def analysis():
    if request.method == 'POST':
        plik = request.files['plik']
        file_name = plik.filename
        if ".csv" not in str(file_name):
            error = "Plik musi mieć rozszerzenie .csv!"
            return render_template("analysis.html", error=error, choose_data=None, select_1=None, file_name=None)
        if plik:
            filename = secure_filename(plik.filename)
            path = os.path.join(tempfile.gettempdir(), filename)
            plik.save(path)
        else:
            path = None
        if path:
            with open(path, 'r') as f:
                content = f.read()
        else:
            content = None
        session["path"] = path
        session["file_name"] = file_name
        L = []
        with open(path, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            count = []
            for element in data[0]:
                count.append(element)
            first_line = count
            count = len(count)
        ### w tym miejscu zostały już policzone kolumny (liczba elementów pierwszego wiersza)
        with open(path, newline='') as f:
            lines = f.readlines()
            table = []
            for k in range(count):
                table.append(k)
            for k in range(count):
                result = []
                for x in lines:
                    result.append(x.split(',')[k])
                table[k] = result
            f.close()
        ### w tym miejscu jest gotowa tabelka (pierwszy element - pierwsza kolumna, drugi - druga, ...)
        ### table[0] - pierwsza kolumna, table[1] - druga kolumna, ...
        ## teraz trzeba przekonwertować dane aby były odczytywane przez pythona:
        #####

        def check_categorical(table):
            commited_data = []
            for data in table:
                try:
                    data = float(data)
                except ValueError:
                    pass
                if isinstance(data, numbers.Real) == True:
                    break
                else:
                    commited_data.append(data)
            if len(commited_data) == len(table):
                print("Zatwierdzono dane jako kategoryczne")
                return True
            else:
                print("Odrzucono dane jako kategoryczne")
                return False

        #####
        for k in range(len(table)):
            if check_categorical(table[k]) == True:
                categorical_index = k
            else:
                continue
        ### Ujednolicenie table i data
        categorical_column = table[categorical_index]
        for k in range(len(categorical_column)):
            a = categorical_column[k]
            a = a.replace('"','')
            a = a.replace('\n','')
            a = a.replace('\r','')
            categorical_column[k] = a
        table[categorical_index] = categorical_column
        ####
        print('Indeks kolumny kategorycznej:', categorical_index)
        print('Wszystkie zmienne:',first_line) ### pierwsza linia - nazwy wszystkich zmiennych
        session["first_line"] = first_line
        print('Zmienne liczbowe:',first_line) ### pierwsza linia - nazwy zmiennych liczbowych
        choose_data = []
        for x in first_line:
            choose_data.append(x)
        choose_data.remove(choose_data[categorical_index])
        print(choose_data)
        print(first_line)
        M = []
        for element in table[categorical_index]: ### (GOTOWE) <---- do przerobienia na sprawdzanie czy jest to zmienna kategoryczna
            M.append(element)
        list_categorical_data = list(dict.fromkeys(M)) ### dane "kategoryczne"
        list_categorical_data_header = list_categorical_data[0]
        list_categorical_data.remove(list_categorical_data[0])
        session["choose_data"] = choose_data
        session["list_categorical_data"] = list_categorical_data
        session["list_categorical_data_header"] = list_categorical_data_header
        ### w tym miejscu gotowe jest już wybieranie z listy nazw wgranych danych (dwóch liczbowych i jednej kategorycznej)
        ### Pozostało:
        ####### [GOTOWE] odczytać daną 1,2,3
        ####### [GOTOWE] wybrać tylko dane 1,2 z "3" w trzeciej kolumnie (zmienna data gdzieś tam wysoko)
        ####### wyświetlić dane 1,2 w dwóch kolumnach tabelki
        ####### zamienić dane 1,2 ze stringów na floaty
        ####### cyk pyk średnia i gotowe
        session["categorical_index"] = categorical_index
        session["categorical_column"] = categorical_column
        select_1 = None
        select_2 = None
        return render_template("analysis.html", content=content, file_name=file_name, choose_data=choose_data, list_categorical_data_header=list_categorical_data_header, list_categorical_data=list_categorical_data, path=path, data=data, table=table,categorical_index=categorical_index,select_2=select_2, select_1=select_1)
    else:
        return redirect(url_for('analysis.html'))

@app.route("/save_data", methods=['POST', 'GET'])
def save_data():
    ##
    path = session["path"]
    categorical_column = session["categorical_column"]
    categorical_index = session["categorical_index"]
    with open(path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    count = []
    for element in data[0]:
        count.append(element)
    count = len(count)
### w tym miejscu zostały już policzone kolumny (liczba elementów pierwszego wiersza)
    with open(path, newline='') as f:
        lines = f.readlines()
        table = []
        for k in range(count):
            table.append(k)
        for k in range(count):
            result = []
            for x in lines:
                result.append(x.split(',')[k])
            table[k] = result
    f.close()
    table[categorical_index] = categorical_column
    ##
    choose_data = session["choose_data"]
    list_categorical_data_header = session["list_categorical_data_header"]
    select_1 = request.form.get('choose_data_1')
    select_2 = request.form.get('choose_data_2')
    select_categorical = request.form.get('choose_categorical_data')
    print(select_1,select_2,select_categorical)
    if select_1 == None:
        select_1 = None
        return render_template("analysis.html",file_name=session["file_name"], choose_data=session["choose_data"], list_categorical_data=session["list_categorical_data"], list_categorical_data_header=session["list_categorical_data_header"], select_1=None,select_2=None,select_categorical=None)
    elif select_2 == None:
        select_2 = None
        return render_template("analysis.html",file_name=session["file_name"], choose_data=session["choose_data"], list_categorical_data=session["list_categorical_data"], list_categorical_data_header=session["list_categorical_data_header"], select_1=None,select_2=None,select_categorical=None)
    elif select_categorical == None:
        select_categorical = None
        return render_template("analysis.html",file_name=session["file_name"], choose_data=session["choose_data"], list_categorical_data=session["list_categorical_data"], list_categorical_data_header=session["list_categorical_data_header"], select_1=None,select_2=None,select_categorical=None)
    session["select_1"] = select_1
    session["select_2"] = select_2
    session["select_categorical"] = select_categorical
    print('Pierwsza zmienna:', select_1)
    print('Druga zmienna:', select_2)
    print('Zmienna kategoryczna:', select_categorical)
    ###### table - dane kolumnowo |
    #print(table)
    #print(data)
    ###### data - dane wierszowo  -
    categorical_data = []
    for x in data:
        if (select_categorical) == (x[categorical_index]):
            categorical_data.append(x)
    print('Dane spełniające wymóg:', categorical_data)
    ### Wybieranie danych tylko z wybranych kolumn
    first_line = session["first_line"]
    print('Pierwsza linia:',first_line)
    for k in first_line:
        if k == select_1:
            select_1_index = first_line.index(k)
            if select_1 == select_2:
                select_2_index = select_1_index
        elif k == select_2:
            select_2_index = first_line.index(k)
    print('1:',select_1_index,'2:',select_2_index)
    ###
    X = []
    Y = []
    for x in categorical_data:
        X.append(float(x[select_1_index]))
        Y.append(float(x[select_2_index]))
    session["X"] = X
    session["Y"] = Y
    ### Liczenie średniej
    average_X = 0
    for x in X:
        average_X += float(x)
    if len(X) != 0:
        average_X = average_X/len(X)
        average_X = round(average_X,2)
    average_Y = 0
    for y in Y:
        average_Y += float(y)
    if len(Y) != 0:
        average_Y = average_Y/len(Y)
        average_Y = round(average_Y, 2)
    session["average_X"] = average_X
    session["average_Y"] = average_Y
    ### rysowanie tabelki w analysis.html
    zip_table = []
    for n in range(len(X)):
        temp = []
        temp.extend([X[n],Y[n]])
        zip_table.append(temp)
    print('Słownik do tabelki:',zip_table)
    session["zip_table"] = zip_table
    phi = (1 + 5 ** 0.5) / 2
    ### dobieranie kolorku dla każdego wyrazu
    def colorize(word):
        m = 1
        for k in word:
            m *= ord(k)
        m = m**2 / math.e / phi
        m = round(m,6)
        m = int(m)
        m=int(str(m)[:6])
        if len(str(m)) < 6:
            i = str(m) + (6-len(str(m)))*'0'
            m = int(i)
        return m
    color = "#"+str(colorize(select_categorical))
    session["color"] = color
#### Brighton Part
    def draw(X,Y,average_X,average_Y,color):
        img = io.BytesIO()
    ### Start Brigton Part ###

        plt.title("Wykres zależności "+select_1 + " od " + select_2 + " dla " + select_categorical)
        plt.plot(X, Y, 'o', color=color)
        plt.grid(color=color,linestyle='-',linewidth=1,alpha=0.3)
        plt.plot(average_X,average_Y,'ro')
        plt.axvline(average_X, 0, 1, label='Average for X',linestyle=':')
        plt.axhline(average_Y, 0, 1, label='Average for Y',linestyle=':')
        plt.xlabel(select_1)
        plt.ylabel(select_2)



    ### End Brigton Part ###
        plt.savefig(img, format='png')
        img.seek(0)
        url = base64.b64encode(img.getvalue()).decode()
        plt.close()
        return 'data:image/png;base64,{}'.format(url)
    graph = draw(X,Y,average_X,average_Y,color)
    return render_template("analysis.html",graph=graph, file_name=session["file_name"], choose_data=session["choose_data"], list_categorical_data=session["list_categorical_data"], list_categorical_data_header=session["list_categorical_data_header"], select_1=select_1,select_2=select_2,select_categorical=select_categorical, X=X, Y=Y, average_X=average_X, average_Y=average_Y, zip_table=zip_table,color=color)

@app.route("/remove_data", methods=['POST', 'GET'])
def remove_data():
        usun = request.form['usun']
        if usun:
            file_name = session["file_name"] = None
            select_1 = session["select_1"] = None
            select_2 = session["select_2"] = None
            select_categorical = session["select_categorical"] = None
            choose_data = session["choose_data"] = None
            
        return render_template("analysis.html", file_name=file_name, select_1=select_1, select_2=select_2, select_categorical=select_categorical, choose_data=choose_data)

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

def rysuj(liczba):
	img = io.BytesIO()

	plt.plot([0,0], [liczba,1], 'r')

	plt.savefig(img, format='png')
	img.seek(0)
	url = base64.b64encode(img.getvalue()).decode()
	plt.close()
	return 'data:image/png;base64,{}'.format(url)