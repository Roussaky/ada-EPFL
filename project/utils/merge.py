#Imports
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#File loading
panama_entity = pd.read_csv('./Data/panama_papers.nodes.entity.csv')
panama_adress = pd.read_csv('./Data/panama_papers.nodes.address.csv')
panama_edges = pd.read_csv('./Data/panama_papers.edges.csv')
panama_intermediary = pd.read_csv('./Data/panama_papers.nodes.intermediary.csv')
panama_officer = pd.read_csv('./Data/panama_papers.nodes.officer.csv')

# Duplicated row: 8
panama_edges.drop(panama_edges[panama_edges.duplicated()==True].index,inplace=True)

weird_date  = panama_edges['r.start_date'].dropna().apply(lambda x: x.split('-')[2]).astype(int) < 1900
index_weird_date = weird_date [weird_date  == True].index
panama_edges.ix[index_weird_date].head()

panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0012','2012')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0014','2014')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0003','2003')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0082','1982')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0200','2000')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0202','2002')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0203','2003')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('2500','2005')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('1194','1994')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0199','1999')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0015','2015')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0009','2009')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0006','2006')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0201','2001')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0095','1995')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0004','2004')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0213','2013')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0096','1996')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0214','2014')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0011','2011')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('0206','2006')

# We also checked the incoherence between start_date and end_date,
#for exp: 'r.start_date': 18-MAR-2019 & 'r.end_date': 06-OCT-2009 
#         means that start_date was probably in year 2009 instead of 2019
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('2088','2008')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('2019','2009')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('2020','2002')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('2099','2009')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('2201','2001')
panama_edges['r.start_date']  = panama_edges['r.start_date'].str.replace('2205','2005')

weird_date  = panama_edges['r.end_date'].dropna().apply(lambda x: x.split('-')[2]).astype(int) < 1900
index_weird_date = weird_date [weird_date  == True].index
panama_edges.ix[index_weird_date].head()

panama_edges['r.end_date']  = panama_edges['r.end_date'].str.replace('0213','2013')
panama_edges['r.end_date']  = panama_edges['r.end_date'].str.replace('0206','2006')
panama_edges['r.end_date']  = panama_edges['r.end_date'].str.replace('0012','2012')
panama_edges['r.end_date']  = panama_edges['r.end_date'].str.replace('0200','2000')
panama_edges['r.end_date']  = panama_edges['r.end_date'].str.replace('0201','2001')
panama_edges['r.end_date']  = panama_edges['r.end_date'].str.replace('0015','2015')
panama_edges['r.end_date']  = panama_edges['r.end_date'].str.replace('0199','1999')
panama_edges['r.end_date']  = panama_edges['r.end_date'].str.replace('0208','2008')
panama_edges['r.end_date']  = panama_edges['r.end_date'].str.replace('0006','2006')
panama_edges['r.end_date']  = panama_edges['r.end_date'].str.replace('0009','2009')
panama_edges['r.end_date']  = panama_edges['r.end_date'].str.replace('0213','2013')

panama_edges['r.end_date']  = panama_edges['r.end_date'].str.replace('2209','2009')

## Convert feature:'r.start_date' & 'r.end_date' to type date
panama_edges['r.start_date'] = pd.to_datetime(panama_edges['r.start_date'])
panama_edges['r.end_date'] = pd.to_datetime(panama_edges['r.end_date'])

#Merging the data
panama_nodes = pd.concat([panama_entity,panama_intermediary,panama_officer,panama_adress])
panama_nodes.to_csv('./Data/merged_data.csv')