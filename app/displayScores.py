import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns



def getScore(results):
    
    percent_score = results[0].get('SCORE')
    score = int(percent_score*100)
    return score
 
def plotnpo(npo_data):  
    
    years = [npo_data[i]['FYEAREND'] for i in range(len(npo_data))]
    assets_total = [npo_data[i]['ASSETS_TOTAL_EOY'] for i in range(len(npo_data))]
    expenses_total = [npo_data[i]['EXPENSES_TOTAL'] for i in range(len(npo_data))]
    gov_grants = [npo_data[i]['GOV_GRANTS'] for i in range(len(npo_data))]
    revenue_total = [npo_data[i]['REVENUE_TOTAL'] for i in range(len(npo_data))]
    other_liability = [npo_data[i]['LIABILITY_OTHER_EOY'] for i in range(len(npo_data))]
    wages_total = [npo_data[i]['WAGES_TOTAL'] for i in range(len(npo_data))]

    fig = plt.figure() 
    plt.plot(years, assets_total)
    plt.xlabel('Year', size=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.title('Total Assets', fontsize=20)
    plt.gca().set_ylim(ymin=0)
    fig.savefig('app/static/img/npo_total_assets.png')

    fig = plt.figure() 
    plt.plot(years, expenses_total)
    plt.xlabel('Year', size=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.title('Total Expenses', fontsize=20)
    plt.gca().set_ylim(ymin=0)
    fig.savefig('app/static/img/npo_total_expenses.png')

    fig = plt.figure() 
    plt.plot(years, gov_grants)
    plt.xlabel('Year', size=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.title('Government Grants', fontsize=20)
    plt.gca().set_ylim(ymin=0)
    fig.savefig('app/static/img/npo_gov_grants.png')

    fig = plt.figure() 
    plt.plot(years, revenue_total)
    plt.xlabel('Year', size=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.title('Total Revenue', fontsize=20)
    plt.gca().set_ylim(ymin=0)
    fig.savefig('app/static/img/npo_revenue_total.png')

    fig = plt.figure() 
    plt.plot(years, wages_total)
    plt.xlabel('Year', size=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.title('Wages', fontsize=20)
    plt.gca().set_ylim(ymin=0)
    fig.savefig('app/static/img/npo_wages_total.png')

    fig = plt.figure() 
    plt.plot(years, other_liability)
    plt.xlabel('Year', size=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.title('Other Liabilities', fontsize=20)
    plt.gca().set_ylim(ymin=0)
    fig.savefig('app/static/img/npo_other_liability.png')

    return
