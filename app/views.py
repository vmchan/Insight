from flask import render_template, request, make_response, flash, redirect
from app import app
from displayScores import getResults, getScore
import pandas as pd
import pymysql as mdb
from json import dumps

conxn = mdb.connect('localhost', 'root', 'passw0rd', 'alldata') #host, user, password, #database

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/contact')
def contact():
    return render_template("contact.html")
  
@app.route('/slides')
def about():
    return render_template("slides.html")

@app.route('/output')
def output():
    #pull "ID" from input field and store it
    npoid = request.args.get('ID', type = int)

    conxn = mdb.connect('localhost', 'root', '', 'alldata') #host, user, password, #database
    with conxn:
        cur = conxn.cursor(mdb.cursors.DictCursor) 
        cur.execute("SELECT logregresult.SCORE, alldata.FYEAREND, alldata.GOV_GRANTS, alldata.SERVICE_REVENUE, alldata.REVENUE_TOTAL, \
            alldata.LIABILITY_OTHER_EOY, alldata.ASSETS_TOTAL_EOY, alldata.WAGES_TOTAL, alldata.EXPENSES_TOTAL \
            FROM logregresult LEFT JOIN alldata ON logregresult.NPO_ID=alldata.NPO_ID WHERE logregresult.NPO_ID = '%s' ", (npoid)) 

    results = cur.fetchall()

    conxn.close()

    if not results:
        #flash('Sorry, NPO %s does not have data in the current year yet. Please enter a new NPO ID.')
        return redirect('/index')
    else:
        score = getScore(results)
        years, assets_total, expenses_total, gov_grants, revenue_total, other_liability, wages_total = getResults(results)
        return render_template("output.html", npoid = npoid, score = score, years=years, assets_total=assets_total, expenses_total=expenses_total, gov_grants=gov_grants, revenue_total=revenue_total, other_liability=other_liability, wages_total=wages_total)
    

@app.route('/mapimages/<path:filename>')
def return_image (filename):
    response = make_response(app.send_static_file(filename))
    response.cache_control.max_age = 0
    return response

@app.route('/data/npos')
def npos_ids():
    conxn = mdb.connect('localhost', 'root', '', 'alldata') #host, user, password, #database
    with conxn:
        cur = conxn.cursor(mdb.cursors.DictCursor) 
        cur.execute("SELECT NPO_ID from logregresult") 
    results = cur.fetchall()
    conxn.close()

    return dumps([int(r['NPO_ID']) for r in results])
