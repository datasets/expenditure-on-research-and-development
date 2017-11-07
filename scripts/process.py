import csv
import pandas as pd

def government():
    with open('archive/gerd.csv', 'r') as inp, open('archive/government.csv', 'w') as out:
        writer = csv.writer(out)
        writer.writerow(('LOCATION','Country','TIME','Government'))
        for row in csv.reader(inp):
            if row[1] == "GERD - financed by Government (in '000 current PPP$)":
                writer.writerow((row[2], row[3], row[4], row[6]))
                
def higher_education():
    with open('archive/gerd.csv', 'r') as inp, open('archive/higher_education.csv', 'w') as out:
        writer = csv.writer(out)
        writer.writerow(('LOCATION','Country','TIME','Higher Education'))
        for row in csv.reader(inp):
            if row[1] == "GERD - financed by Higher education (in '000 current PPP$)":
                writer.writerow((row[2], row[3], row[4], row[6]))
def private_non_profit():
    with open('archive/gerd.csv', 'r') as inp, open('archive/private_non_profit.csv', 'w') as out:
        writer = csv.writer(out)
        writer.writerow(('LOCATION','Country','TIME','Private non-profit'))
        for row in csv.reader(inp):
            if row[1] == "GERD - financed by Private non-profit (in '000 current PPP$)":
                writer.writerow((row[2], row[3], row[4], row[6]))
def business_enterprise():
    with open('archive/gerd.csv', 'r') as inp, open('archive/business_enterprise.csv', 'w') as out:
        writer = csv.writer(out)
        writer.writerow(('LOCATION','Country','TIME','Business enterprise'))
        for row in csv.reader(inp):
            if row[1] == "GERD - financed by Business enterprise (in '000 current PPP$)":
                writer.writerow((row[2], row[3], row[4], row[6]))
def rest_of_the_world():
    with open('archive/gerd.csv', 'r') as inp, open('archive/rest_of_the_world.csv', 'w') as out:
        writer = csv.writer(out)
        writer.writerow(('LOCATION','Country','TIME','Rest of the world'))
        for row in csv.reader(inp):
            if row[1] == "GERD - financed by Rest of the world (abroad) (in '000 current PPP$)":
                writer.writerow((row[2], row[3], row[4], row[6]))
def not_specified_source():
    with open('archive/gerd.csv', 'r') as inp, open('archive/not_specified_source.csv', 'w') as out:
        writer = csv.writer(out)
        writer.writerow(('LOCATION','Country','TIME','Not specified source'))
        for row in csv.reader(inp):
            if row[1] == "GERD - financed by Not specified source (in '000 current PPP$)":
                writer.writerow((row[2], row[3], row[4], row[6]))
def basic_research():
    with open('archive/gerd.csv', 'r') as inp, open('archive/basic_research.csv', 'w') as out:
        writer = csv.writer(out)
        writer.writerow(('LOCATION','Country','TIME','Basic research'))
        for row in csv.reader(inp):
            if row[1] == "GERD - Basic research (in '000 current PPP$)":
                writer.writerow((row[2], row[3], row[4], row[6]))
def applied_research():
    with open('archive/gerd.csv', 'r') as inp, open('archive/applied_research.csv', 'w') as out:
        writer = csv.writer(out)
        writer.writerow(('LOCATION','Country','TIME','Applied research'))
        for row in csv.reader(inp):
            if row[1] == "GERD - Applied research (in '000 current PPP$)":
                writer.writerow((row[2], row[3], row[4], row[6]))
def experimental_development():
    with open('archive/gerd.csv', 'r') as inp, open('archive/experimental_development.csv', 'w') as out:
        writer = csv.writer(out)
        writer.writerow(('LOCATION','Country','TIME','Experimental development'))
        for row in csv.reader(inp):
            if row[1] == "GERD - Experimental development (in '000 current PPP$)":
                writer.writerow((row[2], row[3], row[4], row[6]))
def not_specified_activities():
    with open('archive/gerd.csv', 'r') as inp, open('archive/not_specified_activities.csv', 'w') as out:
        writer = csv.writer(out)
        writer.writerow(('LOCATION','Country','TIME','Not specified activities'))
        for row in csv.reader(inp):
            if row[1] == "GERD - Not specified activities (in '000 current PPP$)":
                writer.writerow((row[2], row[3], row[4], row[6]))
def medical_and_health():
    with open('archive/gerd.csv', 'r') as inp, open('archive/medical_and_health.csv', 'w') as out:
        writer = csv.writer(out)
        writer.writerow(('LOCATION','Country','TIME','Medical and health sciences'))
        for row in csv.reader(inp):
            if row[1] == "GERD - Medical and health sciences (in '000 current PPP$)":
                writer.writerow((row[2], row[3], row[4], row[6]))

def merge():
    a = pd.read_csv("archive/business_enterprise.csv")
    b = pd.read_csv("archive/government.csv")
    c = pd.read_csv("archive/higher_education.csv")
    d = pd.read_csv("archive/private_non_profit.csv")
    e = pd.read_csv("archive/rest_of_the_world.csv")
    f = pd.read_csv("archive/not_specified_source.csv")
    g = pd.read_csv("archive/basic_research.csv")
    h = pd.read_csv("archive/applied_research.csv")
    i = pd.read_csv("archive/experimental_development.csv")
    j = pd.read_csv("archive/not_specified_activities.csv")
    k = pd.read_csv("archive/medical_and_health.csv")
    merged1 = pd.merge(a,b, on =['LOCATION', 'TIME', 'Country'], how='outer')
    merged2 = pd.merge(merged1,c, on =['LOCATION', 'TIME', 'Country'], how='outer')
    merged3 = pd.merge(merged2,d, on =['LOCATION', 'TIME', 'Country'], how='outer')
    merged4 = pd.merge(merged3,e, on =['LOCATION', 'TIME', 'Country'], how='outer')
    merged5 = pd.merge(merged4,f, on =['LOCATION', 'TIME', 'Country'], how='outer')
    merged6 = pd.merge(merged5,g, on =['LOCATION', 'TIME', 'Country'], how='outer')
    merged7 = pd.merge(merged6,h, on =['LOCATION', 'TIME', 'Country'], how='outer')
    merged8 = pd.merge(merged7,i, on =['LOCATION', 'TIME', 'Country'], how='outer')
    merged9 = pd.merge(merged8,j, on =['LOCATION', 'TIME', 'Country'], how='outer')
    merged10 = pd.merge(merged9,k, on =['LOCATION', 'TIME', 'Country'], how='outer').sort_values(by='LOCATION')
    merged10.to_csv("data/expenditure.csv", index=False)
    
government()
higher_education()
private_non_profit()
business_enterprise()
rest_of_the_world()
not_specified_source()
basic_research()
applied_research()
experimental_development()
not_specified_activities()
medical_and_health()
merge()