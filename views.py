from flask import render_template, request, make_response
from app import app
from displayScores import getScore, plotnpo
import pandas as pd
import pymysql as mdb
from json import dumps

conxn = mdb.connect('localhost', 'root', '', 'alldata') #host, user, password, #database

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/contact')
def contact():
    return render_template("contact.html")
  
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/output')
def output():
    #pull "ID" from input field and store it
    npoid = request.args.get('ID', type = int)

    with conxn:
        cur = conxn.cursor(mdb.cursors.DictCursor) 
        cur.execute("SELECT SCORE from logregresult where NPO_ID = %s limit 1", (npoid)) 
    results = cur.fetchall()
    
    score = getScore(results)

    with conxn: 
        cur.execute("SELECT FYEAREND, GOV_GRANTS, SERVICE_REVENUE, REVENUE_TOTAL, \
            LIABILITY_OTHER_EOY, ASSETS_TOTAL_EOY,WAGES_TOTAL, EXPENSES_TOTAL \
            from alldata where NPO_ID = %s", (npoid)) 
    npo_data = cur.fetchall()

    plotnpo(npo_data)


    return render_template("output.html", npoid = npoid, score = score)

@app.route('/mapimages/<path:filename>')
def return_image (filename):
    response = make_response(app.send_static_file(filename))
    response.cache_control.max_age = 0
    return response

@app.route('/data/npos')
def npos_ids():
    with conxn:
        cur = conxn.cursor(mdb.cursors.DictCursor) 
        cur.execute("SELECT NPO_ID from logregresult") 
    results = cur.fetchall()

    return dumps([int(r['NPO_ID']) for r in results])
