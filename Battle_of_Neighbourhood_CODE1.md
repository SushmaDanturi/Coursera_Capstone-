```python

```


```python
import requests
import pandas as pd 
import numpy as np 
```


```python
CLIENT_ID = 'X5DC02PSOJVYTXTIHFY2PGAGVOQZRAUZK3LLRJLWR3IBLLCP' 
CLIENT_SECRET = 'M0QER4RYNVWEFMV3CC3N0VAV4KSAPU5E5FE33QIBGJLGCANR' 

VERSION = '20180604'
LIMIT = 30

print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)
```

    Your credentails:
    CLIENT_ID: X5DC02PSOJVYTXTIHFY2PGAGVOQZRAUZK3LLRJLWR3IBLLCP
    CLIENT_SECRET:M0QER4RYNVWEFMV3CC3N0VAV4KSAPU5E5FE33QIBGJLGCANR



```python
df = pd.read_csv("NYPD_Crime_Data.csv")
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CMPLNT_NUM</th>
      <th>CMPLNT_FR_DT</th>
      <th>RPT_DT</th>
      <th>KY_CD</th>
      <th>OFNS_DESC</th>
      <th>PD_CD</th>
      <th>LAW_CAT_CD</th>
      <th>BORO_NM</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Lat_Lon</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>574970069</td>
      <td>1/1/19</td>
      <td>1/1/19</td>
      <td>341</td>
      <td>PETIT LARCENY</td>
      <td>338.0</td>
      <td>MISDEMEANOR</td>
      <td>BRONX</td>
      <td>40.890285</td>
      <td>-73.859106</td>
      <td>(40.89028471600005, -73.85910627199996)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>695390287</td>
      <td>1/1/19</td>
      <td>1/1/19</td>
      <td>109</td>
      <td>GRAND LARCENY</td>
      <td>411.0</td>
      <td>FELONY</td>
      <td>MANHATTAN</td>
      <td>40.851404</td>
      <td>-73.932216</td>
      <td>(40.851403574000074, -73.93221569599996)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>553237569</td>
      <td>11/25/18</td>
      <td>1/1/19</td>
      <td>114</td>
      <td>ARSON</td>
      <td>264.0</td>
      <td>FELONY</td>
      <td>QUEENS</td>
      <td>40.680003</td>
      <td>-73.764022</td>
      <td>(40.68000300400007, -73.76402239699996)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>320312402</td>
      <td>1/1/19</td>
      <td>1/1/19</td>
      <td>344</td>
      <td>ASSAULT 3 &amp; RELATED OFFENSES</td>
      <td>101.0</td>
      <td>MISDEMEANOR</td>
      <td>BROOKLYN</td>
      <td>40.596940</td>
      <td>-73.973665</td>
      <td>(40.59694042900003, -73.97366455699995)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>936158061</td>
      <td>1/1/19</td>
      <td>1/1/19</td>
      <td>578</td>
      <td>HARRASSMENT 2</td>
      <td>637.0</td>
      <td>VIOLATION</td>
      <td>MANHATTAN</td>
      <td>40.856200</td>
      <td>-73.934015</td>
      <td>(40.85619961300006, -73.93401465599999)</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['value']=1
```


```python
df.shape
```




    (482337, 12)




```python
df.columns = ['Crime_No', 'Crime_DT','Crime_Reported_DT','Classification_Code','Offence_Desc','Internal_Code','Level','Borough','Latitude','Longitude','Lat_Lon','No_of_crimes']

```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Crime_No</th>
      <th>Crime_DT</th>
      <th>Crime_Reported_DT</th>
      <th>Classification_Code</th>
      <th>Offence_Desc</th>
      <th>Internal_Code</th>
      <th>Level</th>
      <th>Borough</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Lat_Lon</th>
      <th>No_of_crimes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>574970069</td>
      <td>1/1/19</td>
      <td>1/1/19</td>
      <td>341</td>
      <td>PETIT LARCENY</td>
      <td>338.0</td>
      <td>MISDEMEANOR</td>
      <td>BRONX</td>
      <td>40.890285</td>
      <td>-73.859106</td>
      <td>(40.89028471600005, -73.85910627199996)</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>695390287</td>
      <td>1/1/19</td>
      <td>1/1/19</td>
      <td>109</td>
      <td>GRAND LARCENY</td>
      <td>411.0</td>
      <td>FELONY</td>
      <td>MANHATTAN</td>
      <td>40.851404</td>
      <td>-73.932216</td>
      <td>(40.851403574000074, -73.93221569599996)</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>553237569</td>
      <td>11/25/18</td>
      <td>1/1/19</td>
      <td>114</td>
      <td>ARSON</td>
      <td>264.0</td>
      <td>FELONY</td>
      <td>QUEENS</td>
      <td>40.680003</td>
      <td>-73.764022</td>
      <td>(40.68000300400007, -73.76402239699996)</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>320312402</td>
      <td>1/1/19</td>
      <td>1/1/19</td>
      <td>344</td>
      <td>ASSAULT 3 &amp; RELATED OFFENSES</td>
      <td>101.0</td>
      <td>MISDEMEANOR</td>
      <td>BROOKLYN</td>
      <td>40.596940</td>
      <td>-73.973665</td>
      <td>(40.59694042900003, -73.97366455699995)</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>936158061</td>
      <td>1/1/19</td>
      <td>1/1/19</td>
      <td>578</td>
      <td>HARRASSMENT 2</td>
      <td>637.0</td>
      <td>VIOLATION</td>
      <td>MANHATTAN</td>
      <td>40.856200</td>
      <td>-73.934015</td>
      <td>(40.85619961300006, -73.93401465599999)</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 482337 entries, 0 to 482336
    Data columns (total 12 columns):
     #   Column               Non-Null Count   Dtype  
    ---  ------               --------------   -----  
     0   Crime_No             482337 non-null  int64  
     1   Crime_DT             482337 non-null  object 
     2   Crime_Reported_DT    482337 non-null  object 
     3   Classification_Code  482337 non-null  int64  
     4   Offence_Desc         482317 non-null  object 
     5   Internal_Code        481968 non-null  float64
     6   Level                482337 non-null  object 
     7   Borough              481961 non-null  object 
     8   Latitude             475612 non-null  float64
     9   Longitude            475612 non-null  float64
     10  Lat_Lon              475612 non-null  object 
     11  No_of_crimes         482337 non-null  int64  
    dtypes: float64(3), int64(3), object(6)
    memory usage: 44.2+ MB



```python
df['Borough'].value_counts()
```




    BROOKLYN         138382
    MANHATTAN        121550
    BRONX            104825
    QUEENS            97201
    STATEN ISLAND     20003
    Name: Borough, dtype: int64




```python
df['Level'].value_counts()
```




    MISDEMEANOR    254977
    FELONY         152691
    VIOLATION       74669
    Name: Level, dtype: int64




```python
NYPD_crime = pd.pivot_table(df,values=['No_of_crimes'],
                               index=['Borough'],
                               columns=['Level'],
                               aggfunc=np.sum,fill_value=0)
NYPD_crime.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">No_of_crimes</th>
    </tr>
    <tr>
      <th>Level</th>
      <th>FELONY</th>
      <th>MISDEMEANOR</th>
      <th>VIOLATION</th>
    </tr>
    <tr>
      <th>Borough</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BRONX</th>
      <td>30356</td>
      <td>57102</td>
      <td>17367</td>
    </tr>
    <tr>
      <th>BROOKLYN</th>
      <td>46631</td>
      <td>70504</td>
      <td>21247</td>
    </tr>
    <tr>
      <th>MANHATTAN</th>
      <td>38903</td>
      <td>66785</td>
      <td>15862</td>
    </tr>
    <tr>
      <th>QUEENS</th>
      <td>31369</td>
      <td>49857</td>
      <td>15975</td>
    </tr>
    <tr>
      <th>STATEN ISLAND</th>
      <td>5059</td>
      <td>10727</td>
      <td>4217</td>
    </tr>
  </tbody>
</table>
</div>




```python
NYPD_crime.reset_index(inplace = True)

```


```python
NYPD_crime['Total'] = NYPD_crime.sum(axis=1)
NYPD_crime.head(33)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>Borough</th>
      <th colspan="3" halign="left">No_of_crimes</th>
      <th>Total</th>
    </tr>
    <tr>
      <th>Level</th>
      <th></th>
      <th>FELONY</th>
      <th>MISDEMEANOR</th>
      <th>VIOLATION</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BRONX</td>
      <td>30356</td>
      <td>57102</td>
      <td>17367</td>
      <td>104825</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BROOKLYN</td>
      <td>46631</td>
      <td>70504</td>
      <td>21247</td>
      <td>138382</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MANHATTAN</td>
      <td>38903</td>
      <td>66785</td>
      <td>15862</td>
      <td>121550</td>
    </tr>
    <tr>
      <th>3</th>
      <td>QUEENS</td>
      <td>31369</td>
      <td>49857</td>
      <td>15975</td>
      <td>97201</td>
    </tr>
    <tr>
      <th>4</th>
      <td>STATEN ISLAND</td>
      <td>5059</td>
      <td>10727</td>
      <td>4217</td>
      <td>20003</td>
    </tr>
  </tbody>
</table>
</div>




```python
NYPD_crime.columns = NYPD_crime.columns.map(''.join)
NYPD_crime.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>No_of_crimesFELONY</th>
      <th>No_of_crimesMISDEMEANOR</th>
      <th>No_of_crimesVIOLATION</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BRONX</td>
      <td>30356</td>
      <td>57102</td>
      <td>17367</td>
      <td>104825</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BROOKLYN</td>
      <td>46631</td>
      <td>70504</td>
      <td>21247</td>
      <td>138382</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MANHATTAN</td>
      <td>38903</td>
      <td>66785</td>
      <td>15862</td>
      <td>121550</td>
    </tr>
    <tr>
      <th>3</th>
      <td>QUEENS</td>
      <td>31369</td>
      <td>49857</td>
      <td>15975</td>
      <td>97201</td>
    </tr>
    <tr>
      <th>4</th>
      <td>STATEN ISLAND</td>
      <td>5059</td>
      <td>10727</td>
      <td>4217</td>
      <td>20003</td>
    </tr>
  </tbody>
</table>
</div>




```python
NYPD_crime.columns = ['Borough','Felony', 'Misdemeanor','Violation','Total']
NYPD_crime.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Felony</th>
      <th>Misdemeanor</th>
      <th>Violation</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BRONX</td>
      <td>30356</td>
      <td>57102</td>
      <td>17367</td>
      <td>104825</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BROOKLYN</td>
      <td>46631</td>
      <td>70504</td>
      <td>21247</td>
      <td>138382</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MANHATTAN</td>
      <td>38903</td>
      <td>66785</td>
      <td>15862</td>
      <td>121550</td>
    </tr>
    <tr>
      <th>3</th>
      <td>QUEENS</td>
      <td>31369</td>
      <td>49857</td>
      <td>15975</td>
      <td>97201</td>
    </tr>
    <tr>
      <th>4</th>
      <td>STATEN ISLAND</td>
      <td>5059</td>
      <td>10727</td>
      <td>4217</td>
      <td>20003</td>
    </tr>
  </tbody>
</table>
</div>




```python
!conda install -c anaconda lxml --yes
!conda install -c anaconda beautifulsoup4 --yes
#from bs4 import BeautifulSoup 
import requests
from bs4 import BeautifulSoup
import xml
```

    Collecting package metadata (current_repodata.json): done
    Solving environment: done
    
    ## Package Plan ##
    
      environment location: /home/jupyterlab/conda/envs/python
    
      added / updated specs:
        - lxml
    
    
    The following packages will be downloaded:
    
        package                    |            build
        ---------------------------|-----------------
        ca-certificates-2020.6.24  |                0         133 KB  anaconda
        certifi-2020.6.20          |           py36_0         160 KB  anaconda
        libxml2-2.9.10             |       he19cac6_1         1.3 MB  anaconda
        libxslt-1.1.34             |       hc22bd24_0         573 KB  anaconda
        lxml-4.5.2                 |   py36hefd8a0e_0         1.4 MB  anaconda
        openssl-1.1.1g             |       h7b6447c_0         3.8 MB  anaconda
        ------------------------------------------------------------
                                               Total:         7.3 MB
    
    The following NEW packages will be INSTALLED:
    
      libxslt            anaconda/linux-64::libxslt-1.1.34-hc22bd24_0
      lxml               anaconda/linux-64::lxml-4.5.2-py36hefd8a0e_0
    
    The following packages will be UPDATED:
    
      ca-certificates    conda-forge::ca-certificates-2020.6.2~ --> anaconda::ca-certificates-2020.6.24-0
      libxml2             conda-forge::libxml2-2.9.9-h13577e0_2 --> anaconda::libxml2-2.9.10-he19cac6_1
    
    The following packages will be SUPERSEDED by a higher-priority channel:
    
      certifi            conda-forge::certifi-2020.6.20-py36h9~ --> anaconda::certifi-2020.6.20-py36_0
      openssl            conda-forge::openssl-1.1.1g-h516909a_0 --> anaconda::openssl-1.1.1g-h7b6447c_0
    
    
    
    Downloading and Extracting Packages
    openssl-1.1.1g       | 3.8 MB    | ##################################### | 100% 
    libxml2-2.9.10       | 1.3 MB    | ##################################### | 100% 
    ca-certificates-2020 | 133 KB    | ##################################### | 100% 
    certifi-2020.6.20    | 160 KB    | ##################################### | 100% 
    lxml-4.5.2           | 1.4 MB    | ##################################### | 100% 
    libxslt-1.1.34       | 573 KB    | ##################################### | 100% 
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    Collecting package metadata (current_repodata.json): done
    Solving environment: done
    
    ## Package Plan ##
    
      environment location: /home/jupyterlab/conda/envs/python
    
      added / updated specs:
        - beautifulsoup4
    
    
    The following packages will be downloaded:
    
        package                    |            build
        ---------------------------|-----------------
        beautifulsoup4-4.9.1       |           py36_0         168 KB  anaconda
        soupsieve-2.0.1            |             py_0          33 KB  anaconda
        ------------------------------------------------------------
                                               Total:         201 KB
    
    The following NEW packages will be INSTALLED:
    
      beautifulsoup4     anaconda/linux-64::beautifulsoup4-4.9.1-py36_0
      soupsieve          anaconda/noarch::soupsieve-2.0.1-py_0
    
    
    
    Downloading and Extracting Packages
    soupsieve-2.0.1      | 33 KB     | ##################################### | 100% 
    beautifulsoup4-4.9.1 | 168 KB    | ##################################### | 100% 
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done



```python
wikipedia_link='https://www.citypopulation.de/en/usa/newyorkcity/'
raw_wikipedia_page= requests.get(wikipedia_link).text

# using beautiful soup to parse the HTML/XML codes.
soup = BeautifulSoup(raw_wikipedia_page,'xml')
table=soup.find('table')
print(soup.prettify())

#     https://en.wikipedia.org/wiki/List_of_London_boroughs
```

    <?xml version="1.0" encoding="utf-8"?>
    <!DOCTYPE html>
    <html lang="en">
     <head>
      <meta charset="utf-8">
       <meta content="New York City Boroughs (USA): Boroughs with population statistics, charts and maps." name="description">
        <title>
         New York City Boroughs (USA): Boroughs - Population Statistics, Charts and Map
        </title>
        <link href="/favicon.ico" rel="shortcut icon">
         <script>
          var pagemode = 'adminpage'; var pagecat = 'admin_city'; var isAdmin = false; var pageid = 'usa-newyorkcity'; var pagelang = 'en'; var pagelabel = "New York City Boroughs"; var popDate = 'E 2019-07-01'; var popcolnum  = 4; var start_x = -73.975; var start_y = 40.705; var start_level = 10; var swap_width = 1132; var hor_percent = 40; var vert_percent = 42; var swap = 'true'; var mapcopyright = 'U.S. Census Bureau.'; var objid = ''; var objtype = ''; var startmap = 'street'; var lev_num = 1; var edit_mode = ''; var placeLocale = 'en'; var nativeName = false; var wikiFromWD = false
         </script>
         <script src="/js/countries/usa.js"/>
         <script src="/jquery/jquery-3.1.1.min.js"/>
         <script src="/js/cp_data_m.js"/>
         <script src="/js/cp_phpbase_v3.js"/>
         <script>
          load_resources()
         </script>
         <script src="/js/cp_menu.js"/>
         <style>
          article#admtable { top: 42%; }
    div#admmap { height: 42%; }
    @media all and (min-width: 1132px) {
    	article#admtable { top: 26px; left: calc(180px + 40%); }
    	div#admmap { height: auto; bottom: -1px; width: 40% }
    	header.admpage { left: calc(180px + 40%) }
    	div#headline { left: calc(162px + 40%) }
    }
         </style>
        </link>
        <body itemscope="" itemtype="http://schema.org/City" onload="init_data(); start_maps()">
         <script>
          writeMenu('en')
         </script>
         <div class="mobiadv">
          <script>
           show_mobiadv();
          </script>
         </div>
         <div class="hor" id="headline">
          <div id="orient">
           <a href="/">
            Home
           </a>
           →
           <span itemprop="containedIn" itemscope="" itemtype="http://schema.org/Continent">
            <a href="/America.html" itemprop="url">
             <span itemprop="name">
              America
             </span>
            </a>
           </span>
           →
           <span itemprop="containedIn" itemscope="" itemtype="http://schema.org/Country">
            <a href="/en/usa/" itemprop="url">
             <span itemprop="name">
              USA
             </span>
            </a>
           </span>
          </div>
          <div id="social">
           <div class="changelang">
            <a href="javascript:cp.changePageLang('en','de')">
             <img alt="" src="/images/icons/de.svg" title="Deutsch"/>
            </a>
           </div>
          </div>
          <div class="info" id="inforowdiv" style="display:none"/>
          <article class="cpage swapped" id="admtable">
           <header class="admpage">
            <a href="javascript:openMap()">
             <img alt="Show Map" id="smap" src="/images/smaps/usa-cities.png" title="Show Map"/>
             <h1>
              <a href="/en/usa/">
               USA
              </a>
              :
              <span class="smalltext" itemprop="name">
               New York City Boroughs
              </span>
             </h1>
            </a>
            <script>
             handleArticleResize()
            </script>
            <h2>
             <span class="noviz">
              Contents:
             </span>
             Boroughs
            </h2>
            <p>
             The population of the boroughs of New York City according to census results and latest official estimates.
            </p>
            <p class="small noprint">
             The
             <img alt="Details" class="infoicon" src="/images/icons/separate_wb.svg">
              icon links to further information about a selected division including its population structure (gender, age groups, age distribution, »race«, ethnicity).
             </img>
             <table class="data" id="ts">
              <thead>
               <tr>
                <th class="rname" data-coltype="name" onclick="javascript:sort('ts',0,false)">
                 <a href="javascript:sort('ts',0,false)">
                  Name
                 </a>
                </th>
                <th class="rstatus" data-coltype="status" onclick="javascript:sort('ts',1,false)">
                 <a href="javascript:sort('ts',1,false)">
                  Status
                 </a>
                </th>
                <th class="rpop prio4" data-coldate="1990-04-01" data-colhead="C 1990-04-01" data-coltype="pop" onclick="javascript:sort('ts',2,true)">
                 <a href="javascript:sort('ts',2,true)">
                  Population
                 </a>
                 <br>
                  <span class="unit">
                   Census
                   <br>
                    1990-04-01
                   </br>
                  </span>
                  <th class="rpop prio3" data-coldate="2000-04-01" data-colhead="C 2000-04-01" data-coltype="pop" onclick="javascript:sort('ts',3,true)">
                   <a href="javascript:sort('ts',3,true)">
                    Population
                   </a>
                   <br>
                    <span class="unit">
                     Census
                     <br>
                      2000-04-01
                     </br>
                    </span>
                    <th class="rpop prio2" data-coldate="2010-04-01" data-colhead="C 2010-04-01" data-coltype="pop" onclick="javascript:sort('ts',4,true)">
                     <a href="javascript:sort('ts',4,true)">
                      Population
                     </a>
                     <br>
                      <span class="unit">
                       Census
                       <br>
                        2010-04-01
                       </br>
                      </span>
                      <th class="rpop prio1" data-coldate="2019-07-01" data-colhead="E 2019-07-01" data-coltype="pop" onclick="javascript:sort('ts',5,true)">
                       <a href="javascript:sort('ts',5,true)">
                        Population
                       </a>
                       <br>
                        <span class="unit">
                         Estimate
                         <br>
                          2019-07-01
                         </br>
                        </span>
                        <th class="sc" data-coltype="other"/>
                       </br>
                      </th>
                      <tbody>
                       <tr class="rname" itemscope="" itemtype="http://schema.org/Place" onclick="javascript:sym('36005')">
                        <td class="rname" data-area="108.91" data-density="13021.75" data-wd="Q18426" data-wiki="The Bronx" id="i36005">
                         <a href="javascript:sym('36005')">
                          <span itemprop="name">
                           Bronx
                          </span>
                         </a>
                        </td>
                        <td class="rstatus">
                         Borough
                        </td>
                        <td class="rpop prio4">
                         1,203,789
                        </td>
                        <td class="rpop prio3">
                         1,332,244
                        </td>
                        <td class="rpop prio2">
                         1,384,580
                        </td>
                        <td class="rpop prio1">
                         1,418,207
                        </td>
                        <td class="sc">
                         <a href="/en/usa/newyorkcity/36005__bronx/" itemprop="url">
                          →
                         </a>
                        </td>
                       </tr>
                       <tr class="rname" itemscope="" itemtype="http://schema.org/Place" onclick="javascript:sym('36047')">
                        <td class="rname" data-area="180.81" data-density="14157.68" data-wd="Q18419" data-wiki="Brooklyn" id="i36047">
                         <a href="javascript:sym('36047')">
                          <span itemprop="name">
                           Brooklyn
                          </span>
                         </a>
                         (
                         <span itemprop="name">
                          Kings County
                         </span>
                         )
                        </td>
                        <td class="rstatus">
                         Borough
                        </td>
                        <td class="rpop prio4">
                         2,300,664
                        </td>
                        <td class="rpop prio3">
                         2,465,689
                        </td>
                        <td class="rpop prio2">
                         2,504,721
                        </td>
                        <td class="rpop prio1">
                         2,559,903
                        </td>
                        <td class="sc">
                         <a href="/en/usa/newyorkcity/36047__brooklyn/" itemprop="url">
                          →
                         </a>
                        </td>
                       </tr>
                       <tr class="rname" itemscope="" itemtype="http://schema.org/Place" onclick="javascript:sym('36061')">
                        <td class="rname" data-area="58.68" data-density="27756.53" data-wd="Q11299" data-wiki="Manhattan" id="i36061">
                         <a href="javascript:sym('36061')">
                          <span itemprop="name">
                           Manhattan
                          </span>
                         </a>
                         (
                         <span itemprop="name">
                          New York County
                         </span>
                         )
                        </td>
                        <td class="rstatus">
                         Borough
                        </td>
                        <td class="rpop prio4">
                         1,487,536
                        </td>
                        <td class="rpop prio3">
                         1,538,096
                        </td>
                        <td class="rpop prio2">
                         1,586,381
                        </td>
                        <td class="rpop prio1">
                         1,628,706
                        </td>
                        <td class="sc">
                         <a href="/en/usa/newyorkcity/36061__manhattan/" itemprop="url">
                          →
                         </a>
                        </td>
                       </tr>
                       <tr class="rname" itemscope="" itemtype="http://schema.org/Place" onclick="javascript:sym('36081')">
                        <td class="rname" data-area="281.71" data-density="8000.69" data-wd="Q18424" data-wiki="Queens" id="i36081">
                         <a href="javascript:sym('36081')">
                          <span itemprop="name">
                           Queens
                          </span>
                         </a>
                        </td>
                        <td class="rstatus">
                         Borough
                        </td>
                        <td class="rpop prio4">
                         1,951,598
                        </td>
                        <td class="rpop prio3">
                         2,229,394
                        </td>
                        <td class="rpop prio2">
                         2,230,619
                        </td>
                        <td class="rpop prio1">
                         2,253,858
                        </td>
                        <td class="sc">
                         <a href="/en/usa/newyorkcity/36081__queens/" itemprop="url">
                          →
                         </a>
                        </td>
                       </tr>
                       <tr class="rname" itemscope="" itemtype="http://schema.org/Place" onclick="javascript:sym('36085')">
                        <td class="rname" data-area="150.68" data-density="3159.96" data-wd="Q18432" data-wiki="Staten Island" id="i36085">
                         <a href="javascript:sym('36085')">
                          <span itemprop="name">
                           Staten Island
                          </span>
                         </a>
                         (
                         <span itemprop="name">
                          Richmond County
                         </span>
                         )
                        </td>
                        <td class="rstatus">
                         Borough
                        </td>
                        <td class="rpop prio4">
                         378,977
                        </td>
                        <td class="rpop prio3">
                         443,762
                        </td>
                        <td class="rpop prio2">
                         468,730
                        </td>
                        <td class="rpop prio1">
                         476,143
                        </td>
                        <td class="sc">
                         <a href="/en/usa/newyorkcity/36085__staten_island/" itemprop="url">
                          →
                         </a>
                        </td>
                       </tr>
                      </tbody>
                      <tbody class="admin0">
                       <tr>
                        <td class="rname">
                         New York City
                        </td>
                        <td class="rstatus">
                         City
                        </td>
                        <td class="rpop prio4">
                         7,322,564
                        </td>
                        <td class="rpop prio3">
                         8,009,185
                        </td>
                        <td class="rpop prio2">
                         8,175,031
                        </td>
                        <td class="rpop prio1">
                         8,336,817
                        </td>
                        <td class="sc"/>
                       </tr>
                      </tbody>
                     </br>
                     <section id="sourcesection">
                      <p class="source">
                       <strong>
                        Source:
                       </strong>
                       U.S. Census Bureau (web).
                      </p>
                     </section>
                     <hr id="hraddinfo">
                      <h3>
                       Further information about the population structure:
                      </h3>
                      <div id="chartgrid">
                       <section class="addinfo">
                        <div class="addchart" id="addchart0"/>
                        <table class="data">
                         <thead>
                          <tr>
                           <th colspan="2">
                            Gender (E 2019)
                           </th>
                          </tr>
                         </thead>
                         <tbody>
                          <tr>
                           <td>
                            Males
                           </td>
                           <td class="rpop">
                            3,978,439
                           </td>
                          </tr>
                          <tr>
                           <td>
                            Females
                           </td>
                           <td class="rpop">
                            4,358,378
                           </td>
                          </tr>
                         </tbody>
                        </table>
                       </section>
                       <section class="addinfo">
                        <div class="addchart" id="addchart1"/>
                        <table class="data">
                         <thead>
                          <tr>
                           <th colspan="2">
                            Age Groups (E 2019)
                           </th>
                          </tr>
                         </thead>
                         <tbody>
                          <tr>
                           <td>
                            0-14 years
                           </td>
                           <td class="rpop">
                            1,451,817
                           </td>
                          </tr>
                          <tr>
                           <td>
                            15-64 years
                           </td>
                           <td class="rpop">
                            5,604,595
                           </td>
                          </tr>
                          <tr>
                           <td>
                            65+ years
                           </td>
                           <td class="rpop">
                            1,280,405
                           </td>
                          </tr>
                         </tbody>
                        </table>
                       </section>
                       <section class="addinfo">
                        <div class="addchart" id="addchart2"/>
                        <table class="data">
                         <thead>
                          <tr>
                           <th colspan="2">
                            Age Distribution (E 2019)
                           </th>
                          </tr>
                         </thead>
                         <tbody>
                          <tr>
                           <td>
                            0-9 years
                           </td>
                           <td class="rpop">
                            1,008,031
                           </td>
                          </tr>
                          <tr>
                           <td>
                            10-19 years
                           </td>
                           <td class="rpop">
                            883,550
                           </td>
                          </tr>
                          <tr>
                           <td>
                            20-29 years
                           </td>
                           <td class="rpop">
                            1,273,671
                           </td>
                          </tr>
                          <tr>
                           <td>
                            30-39 years
                           </td>
                           <td class="rpop">
                            1,335,563
                           </td>
                          </tr>
                          <tr>
                           <td>
                            40-49 years
                           </td>
                           <td class="rpop">
                            1,043,319
                           </td>
                          </tr>
                          <tr>
                           <td>
                            50-59 years
                           </td>
                           <td class="rpop">
                            1,033,138
                           </td>
                          </tr>
                          <tr>
                           <td>
                            60-69 years
                           </td>
                           <td class="rpop">
                            878,204
                           </td>
                          </tr>
                          <tr>
                           <td>
                            70-79 years
                           </td>
                           <td class="rpop">
                            543,337
                           </td>
                          </tr>
                          <tr>
                           <td>
                            80+ years
                           </td>
                           <td class="rpop">
                            338,004
                           </td>
                          </tr>
                         </tbody>
                        </table>
                       </section>
                       <section class="addinfo">
                        <div class="addchart" id="addchart3"/>
                        <table class="data">
                         <thead>
                          <tr>
                           <th colspan="2">
                            »Race« (E 2019)
                           </th>
                          </tr>
                         </thead>
                         <tbody>
                          <tr>
                           <td>
                            White
                           </td>
                           <td class="rpop">
                            4,393,042
                           </td>
                          </tr>
                          <tr>
                           <td>
                            Black/African American
                           </td>
                           <td class="rpop">
                            2,093,874
                           </td>
                          </tr>
                          <tr>
                           <td>
                            Indigenous
                           </td>
                           <td class="rpop">
                            116,497
                           </td>
                          </tr>
                          <tr>
                           <td>
                            Asian
                           </td>
                           <td class="rpop">
                            1,256,584
                           </td>
                          </tr>
                          <tr>
                           <td>
                            Pacific Islander
                           </td>
                           <td class="rpop">
                            17,682
                           </td>
                          </tr>
                          <tr>
                           <td>
                            2 or more
                           </td>
                           <td class="rpop">
                            258,314
                           </td>
                          </tr>
                         </tbody>
                        </table>
                       </section>
                       <section class="addinfo">
                        <div class="addchart" id="addchart4"/>
                        <table class="data">
                         <thead>
                          <tr>
                           <th colspan="2">
                            Ethnicity (E 2019)
                           </th>
                          </tr>
                         </thead>
                         <tbody>
                          <tr>
                           <td>
                            Hispanic or Latino
                           </td>
                           <td class="rpop">
                            2,423,590
                           </td>
                          </tr>
                          <tr>
                           <td>
                            Other
                           </td>
                           <td class="rpop">
                            5,913,227
                           </td>
                          </tr>
                         </tbody>
                        </table>
                       </section>
                      </div>
                      <script>
                       var addChartData = [{"name":"Gender","type":"pie","data":[["Gender","Persons"],["Males",3978439],["Females",4358378]]},
    {"name":"Age Groups","type":"pie","data":[["Age Groups","Persons"],["0-14 years",1451817],["15-64 years",5604595],["65+ years",1280405]]},
    {"name":"Age Distribution","type":"column","data":[["Age Distribution","Persons"],["0-9 years",1008031],["10-19 years",883550],["20-29 years",1273671],["30-39 years",1335563],["40-49 years",1043319],["50-59 years",1033138],["60-69 years",878204],["70-79 years",543337],["80+ years",338004]]},
    {"name":"»Race«","type":"pie","data":[["»Race«","Persons"],["White",4393042],["Black/African American",2093874],["Indigenous",116497],["Asian",1256584],["Pacific Islander",17682],["2 or more",258314]]},
    {"name":"Ethnicity","type":"pie","data":[["Ethnicity","Persons"],["Hispanic or Latino",2423590],["Other",5913227]]}]
                      </script>
                      <script>
                       var addMapData = ["genderM","genderF","ageX","ageX","ageO"]; var addMapMetadata = [{ "maptype":"genderM", "date":"E 2019-07-01" },{ "maptype":"ageX", "date":"E 2019-07-01" }]
                      </script>
                      <div class="mobiadv">
                       <script>
                        show_mobiadv()
                       </script>
                      </div>
                      <div id="advhor">
                       <script>
                        show_adv('h');
                       </script>
                      </div>
                      <hr>
                       <section class="ytvideosec">
                        <h2>
                         Greater New York: COVID-19 cases, incidence rates and growth by counties
                        </h2>
                        <iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" class="ytvideo" src="https://www.youtube.com/embed/mKAGHkMhlXU"/>
                       </section>
                       <script>
                        writeFooter('2020-07-11')
                       </script>
                      </hr>
                      <div id="admmap" itemprop="geo" itemscope="" itemtype="http://schema.org/GeoCoordinates">
                       <meta content="40.705" itemprop="latitude">
                        <meta content="-73.975" itemprop="longitude">
                         <div id="mapcontainer">
                          <div id="mapdiv">
                           <div id="maplconrl"/>
                           <div id="maprconrl"/>
                          </div>
                         </div>
                        </meta>
                        <div id="alert"/>
                        <div id="helpdiv"/>
                        <div id="adv">
                         <script>
                          show_adv();
                         </script>
                        </div>
                        <script>
                         var startChartID = "NYC"; var startChartType = "adm1";
    	var minlat = 40.49; var minlng = -74.26; var maxlat = 40.92; var maxlng = -73.69;
    	var admCount = { "adm1": 5, "adm2": 0 };
    	if (cp.getVizMode() == cp.VIZMODE_DESKTOP) cp.social.addSocial(false);
                        </script>
                       </meta>
                      </div>
                      <!-- create time: 0.0037448406219482 countries -->
                      <!-- cache time: 0.00016903877258301 -->
                     </hr>
                    </th>
                   </br>
                  </th>
                 </br>
                </th>
               </tr>
              </thead>
             </table>
            </p>
           </header>
          </article>
         </div>
        </body>
       </meta>
      </meta>
     </head>
    </html>



```python
NYC_table = pd.read_html('https://www.citypopulation.de/en/usa/newyorkcity/')
NYC=NYC_table[0]
NYC.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Status</th>
      <th>PopulationCensus1990-04-01</th>
      <th>PopulationCensus2000-04-01</th>
      <th>PopulationCensus2010-04-01</th>
      <th>PopulationEstimate2019-07-01</th>
      <th>Unnamed: 6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bronx</td>
      <td>Borough</td>
      <td>1203789</td>
      <td>1332244</td>
      <td>1384580</td>
      <td>1418207</td>
      <td>→</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Brooklyn (Kings County)</td>
      <td>Borough</td>
      <td>2300664</td>
      <td>2465689</td>
      <td>2504721</td>
      <td>2559903</td>
      <td>→</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Manhattan (New York County)</td>
      <td>Borough</td>
      <td>1487536</td>
      <td>1538096</td>
      <td>1586381</td>
      <td>1628706</td>
      <td>→</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Queens</td>
      <td>Borough</td>
      <td>1951598</td>
      <td>2229394</td>
      <td>2230619</td>
      <td>2253858</td>
      <td>→</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Staten Island (Richmond County)</td>
      <td>Borough</td>
      <td>378977</td>
      <td>443762</td>
      <td>468730</td>
      <td>476143</td>
      <td>→</td>
    </tr>
  </tbody>
</table>
</div>




```python
NYC.columns = ['Borough', 'Status','Population-1990','Population-2000','Population-2010','Population-2019','Unnamed']
NYC.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Status</th>
      <th>Population-1990</th>
      <th>Population-2000</th>
      <th>Population-2010</th>
      <th>Population-2019</th>
      <th>Unnamed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bronx</td>
      <td>Borough</td>
      <td>1203789</td>
      <td>1332244</td>
      <td>1384580</td>
      <td>1418207</td>
      <td>→</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Brooklyn (Kings County)</td>
      <td>Borough</td>
      <td>2300664</td>
      <td>2465689</td>
      <td>2504721</td>
      <td>2559903</td>
      <td>→</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Manhattan (New York County)</td>
      <td>Borough</td>
      <td>1487536</td>
      <td>1538096</td>
      <td>1586381</td>
      <td>1628706</td>
      <td>→</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Queens</td>
      <td>Borough</td>
      <td>1951598</td>
      <td>2229394</td>
      <td>2230619</td>
      <td>2253858</td>
      <td>→</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Staten Island (Richmond County)</td>
      <td>Borough</td>
      <td>378977</td>
      <td>443762</td>
      <td>468730</td>
      <td>476143</td>
      <td>→</td>
    </tr>
  </tbody>
</table>
</div>




```python
NYC_Census=NYC.drop(['Unnamed','Population-1990','Population-2000','Population-2010'], axis=1)
NYC_Census.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Status</th>
      <th>Population-2019</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bronx</td>
      <td>Borough</td>
      <td>1418207</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Brooklyn (Kings County)</td>
      <td>Borough</td>
      <td>2559903</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Manhattan (New York County)</td>
      <td>Borough</td>
      <td>1628706</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Queens</td>
      <td>Borough</td>
      <td>2253858</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Staten Island (Richmond County)</td>
      <td>Borough</td>
      <td>476143</td>
    </tr>
  </tbody>
</table>
</div>




```python
NYC_Census=NYC_Census.rename(columns={'B':'Borough'})
```


```python
NYC_Census.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Status</th>
      <th>Population-2019</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bronx</td>
      <td>Borough</td>
      <td>1418207</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Brooklyn (Kings County)</td>
      <td>Borough</td>
      <td>2559903</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Manhattan (New York County)</td>
      <td>Borough</td>
      <td>1628706</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Queens</td>
      <td>Borough</td>
      <td>2253858</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Staten Island (Richmond County)</td>
      <td>Borough</td>
      <td>476143</td>
    </tr>
  </tbody>
</table>
</div>




```python
NYC_Census["Borough"].replace({"Bronx":"BRONX",
                               "Brooklyn (Kings County)":"BROOKLYN",
                               "Manhattan (New York County)":"MANHATTAN",
                               "Queens":"QUEENS",
                               "Staten Island (Richmond County)":"STATEN ISLAND",
                               "New York City":"NYC"},inplace=True)
```


```python
print(NYC_Census)
```

             Borough   Status  Population-2019
    0          BRONX  Borough          1418207
    1       BROOKLYN  Borough          2559903
    2      MANHATTAN  Borough          1628706
    3         QUEENS  Borough          2253858
    4  STATEN ISLAND  Borough           476143
    5            NYC     City          8336817



```python
NYC_Crime_Table = pd.merge(NYPD_crime, NYC_Census, on='Borough')
NYC_Crime_Table.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Felony</th>
      <th>Misdemeanor</th>
      <th>Violation</th>
      <th>Total</th>
      <th>Status</th>
      <th>Population-2019</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BRONX</td>
      <td>30356</td>
      <td>57102</td>
      <td>17367</td>
      <td>104825</td>
      <td>Borough</td>
      <td>1418207</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BROOKLYN</td>
      <td>46631</td>
      <td>70504</td>
      <td>21247</td>
      <td>138382</td>
      <td>Borough</td>
      <td>2559903</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MANHATTAN</td>
      <td>38903</td>
      <td>66785</td>
      <td>15862</td>
      <td>121550</td>
      <td>Borough</td>
      <td>1628706</td>
    </tr>
    <tr>
      <th>3</th>
      <td>QUEENS</td>
      <td>31369</td>
      <td>49857</td>
      <td>15975</td>
      <td>97201</td>
      <td>Borough</td>
      <td>2253858</td>
    </tr>
    <tr>
      <th>4</th>
      <td>STATEN ISLAND</td>
      <td>5059</td>
      <td>10727</td>
      <td>4217</td>
      <td>20003</td>
      <td>Borough</td>
      <td>476143</td>
    </tr>
  </tbody>
</table>
</div>




```python
NYC_Crime_Table = NYC_Crime_Table[['Borough','Felony','Misdemeanor','Violation',
                 'Status','Population-2019','Total']]
NYC_Crime_Table
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Felony</th>
      <th>Misdemeanor</th>
      <th>Violation</th>
      <th>Status</th>
      <th>Population-2019</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>BROOKLYN</td>
      <td>46631</td>
      <td>70504</td>
      <td>21247</td>
      <td>Borough</td>
      <td>2559903</td>
      <td>138382</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MANHATTAN</td>
      <td>38903</td>
      <td>66785</td>
      <td>15862</td>
      <td>Borough</td>
      <td>1628706</td>
      <td>121550</td>
    </tr>
    <tr>
      <th>0</th>
      <td>BRONX</td>
      <td>30356</td>
      <td>57102</td>
      <td>17367</td>
      <td>Borough</td>
      <td>1418207</td>
      <td>104825</td>
    </tr>
    <tr>
      <th>3</th>
      <td>QUEENS</td>
      <td>31369</td>
      <td>49857</td>
      <td>15975</td>
      <td>Borough</td>
      <td>2253858</td>
      <td>97201</td>
    </tr>
    <tr>
      <th>4</th>
      <td>STATEN ISLAND</td>
      <td>5059</td>
      <td>10727</td>
      <td>4217</td>
      <td>Borough</td>
      <td>476143</td>
      <td>20003</td>
    </tr>
  </tbody>
</table>
</div>




```python
NYC_Crime_Table.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Felony</th>
      <th>Misdemeanor</th>
      <th>Violation</th>
      <th>Population-2019</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000e+00</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>30463.600000</td>
      <td>50995.000000</td>
      <td>14933.600000</td>
      <td>1.667363e+06</td>
      <td>96392.200000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>15643.156037</td>
      <td>23927.115883</td>
      <td>6375.194334</td>
      <td>8.098120e+05</td>
      <td>45560.768087</td>
    </tr>
    <tr>
      <th>min</th>
      <td>5059.000000</td>
      <td>10727.000000</td>
      <td>4217.000000</td>
      <td>4.761430e+05</td>
      <td>20003.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>30356.000000</td>
      <td>49857.000000</td>
      <td>15862.000000</td>
      <td>1.418207e+06</td>
      <td>97201.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>31369.000000</td>
      <td>57102.000000</td>
      <td>15975.000000</td>
      <td>1.628706e+06</td>
      <td>104825.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>38903.000000</td>
      <td>66785.000000</td>
      <td>17367.000000</td>
      <td>2.253858e+06</td>
      <td>121550.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>46631.000000</td>
      <td>70504.000000</td>
      <td>21247.000000</td>
      <td>2.559903e+06</td>
      <td>138382.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
NYC_Crime_Table.sort_values(['Total'], ascending = False, axis = 0, inplace = True )
NYC_Crime_Table
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Felony</th>
      <th>Misdemeanor</th>
      <th>Violation</th>
      <th>Status</th>
      <th>Population-2019</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>BROOKLYN</td>
      <td>46631</td>
      <td>70504</td>
      <td>21247</td>
      <td>Borough</td>
      <td>2559903</td>
      <td>138382</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MANHATTAN</td>
      <td>38903</td>
      <td>66785</td>
      <td>15862</td>
      <td>Borough</td>
      <td>1628706</td>
      <td>121550</td>
    </tr>
    <tr>
      <th>0</th>
      <td>BRONX</td>
      <td>30356</td>
      <td>57102</td>
      <td>17367</td>
      <td>Borough</td>
      <td>1418207</td>
      <td>104825</td>
    </tr>
    <tr>
      <th>3</th>
      <td>QUEENS</td>
      <td>31369</td>
      <td>49857</td>
      <td>15975</td>
      <td>Borough</td>
      <td>2253858</td>
      <td>97201</td>
    </tr>
    <tr>
      <th>4</th>
      <td>STATEN ISLAND</td>
      <td>5059</td>
      <td>10727</td>
      <td>4217</td>
      <td>Borough</td>
      <td>476143</td>
      <td>20003</td>
    </tr>
  </tbody>
</table>
</div>




```python
import matplotlib.pyplot as plt
NYC_V = NYC_Crime_Table[['Borough','Total']]

NYC_V.set_index('Borough',inplace = True)

a = NYC_V.plot(kind='bar', figsize=(10, 6), rot=0)

a.set_ylabel('Number of Crimes') 
a.set_xlabel('Borough') 
a.set_title('NYC Borough with least crimes') 

for p in a.patches:
    a.annotate(np.round(p.get_height(),decimals=2), 
                (p.get_x()+p.get_width()/2., p.get_height()), 
                ha='center', 
                va='center', 
                xytext=(0, 10), 
                textcoords='offset points',
                fontsize = 11
               )

plt.show()
```


![png](output_30_0.png)



```python
NYC_V1 =  NYC_Crime_Table[NYC_Crime_Table['Borough'] == 'STATEN ISLAND']

NYC = NYC_V1[['Borough','Felony','Misdemeanor','Violation',
                 'Status','Total']]


NYC.set_index('Borough',inplace = True)

a = NYC.plot(kind='bar', figsize=(10, 6), rot=0)

a.set_ylabel('Number of Crimes')
a.set_xlabel('Borough') 
a.set_title('NYC Boroughs with the least Crimes') 



for p in a.patches:
    a.annotate(np.round(p.get_height(),decimals=2), 
                (p.get_x()+p.get_width()/2., p.get_height()), 
                ha='center', 
                va='center', 
                xytext=(0, 10), 
                textcoords='offset points',
                fontsize = 11
               )

plt.show()
```


![png](output_31_0.png)



```python

```


```python

```


```python

```
