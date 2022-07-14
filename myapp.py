import pandas as pd
import re
from urllib.parse import urlparse
import urllib
import sys
import datetime

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)
pd.set_option('display.max_colwidth',None)


#with open("data.tsv") as inp:
#    print( list(zip(*(line.strip().split('\t') for line in inp))) )

def calfile(filename,outname):

    df1=pd.read_csv (filename, sep='\t',header='infer')
    #print(df1)
    urls = df1.referrer.to_list()
    pro_list = df1.product_list[3]
    #print(pro_list)
    df = pd.DataFrame()
    l = len(urls)
    i=0
    for url in urls:
        parse = urlparse(url)
        df.loc[i, 'domain'] = parse.netloc.split(".", 1)[1]
        df.loc[i, 'query'] = parse.query
        i+=1

    
    df3 = pd.DataFrame(df1.pop('product_list').str.split(';', expand=True))
    df3.columns = ['Category' ,'Product_Name' ,'Number_of_Items' ,'Total_Revenue' ,'Custom_Event']

    df4=df3['Total_Revenue'].fillna(0).apply(pd.to_numeric)
    #print(df4)

    result = pd.concat([df, df4], axis=1, ignore_index=True)
    result.columns = ['Search_Engine_Domain','Search_Keyword','Revenue']
    #result=result.sort_values(by='Revenue', inplace=True, ascending=False)

    result=result.sort_values('Revenue', ascending=False)
    print(result)
    

    result.to_csv(outname,sep ='\t')


try:
    filename=sys.argv[1]
except:
    if len(sys.argv)==1:
        print("atleast two args is expected")
else:
    x = datetime.datetime.today().strftime("%Y-%m-%d")
    outname=x+'_SearchKeywordPerformance.tab'
    calfile(filename,outname)

"""


def calfile(filename,outname):
#    filename='data.tsv'
    df1=pd.read_csv (filename, sep='\t',header='infer')
    urls = df1.referrer.to_list()
    df = pd.DataFrame()
    df= df1['referrer']
    df.to_csv(outname)


#print(df)
#print(urls)

#urls = ['https://www.google.com/something','https://mail.google.com/anohtersomething', 'https://www.amazon.com/yetanotherthing']
#df['protocol'],df['domain'],df['path'],df['query'],df['fragment'] = zip(*[urllib.parse.urlsplit(x) for x in urls])

l = len(urls)
i=0
for url in urls:
    i+=1
    parse = urlparse(url)
    #df.loc[i, 'domain'] = parse.netloc
    df.loc[i, 'domain'] = parse.netloc.split(".", 1)[1]
    df.loc[i, 'query'] = parse.query
    
print(df)
#print(df[['hit_time_gmt','date_time']])
#print(df[['user_agent','ip']])
#print(df[['event_list','geo_city']])
#print(df[['geo_region','geo_country']])
#print(df[['pagename','page_url']])
#print(df[['product_list','referrer']])
#print(df[['referrer']])

#for x in urls:
#    df['fragments'],df['fragment'] = zip([urllib.parse.urlsplit(x).netloc,urllib.parse.urlsplit(x).query])
#df['fragments'] = [urllib.parse.urlsplit(x).query for x in urls]


#for col in df.columns:
#    print(col)
#print(list(df.columns))
#print(df.keys())
#print(df.columns.values)

#'hit_time_gmt' 'date_time' 'user_agent' 'ip' 'event_list' 'geo_city'  'geo_region' 'geo_country' 'pagename' 'page_url' 'product_list'  'referrer'



#ful = urlparse('http://www.example.test/foo/bar')
#print(ful)
domain = urlparse('http://www.example.test/foo/bar').netloc
#print(domain) # --> www.example.test

query = urlparse('http://search.yahoo.com/search?p=cd+player&toggle=1&cop=mss&ei=UTF-8&fr=yfp-t-701').query
#print(query) # --> www.example.test
#def domain_name(url):
#    pattern = re.compile(r'(https?://|www\.)?(www\.)?([a-z0-9-]+)(\..+)?')
#    subbed_url = pattern.sub(r'\3', url)
#    return subbed_url

#print(domain_name('https://www.gale.com'))
"""

