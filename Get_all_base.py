import requests
import json
import jsonpath
import pymysql as mysql  # ładowanie biblioteki

url = "https://api.covid19api.com/dayone/country/poland"
response = requests.get(url)
json_response = json.loads(response.text)

date_tab = []
za_ra = []
za_dn = []
zg_ra = []
zg_dn = []
oz_ra = []
oz_dn = []
ak_ra = []
ak_dn = []

for i in range(455):
    try:
        json_date = jsonpath.jsonpath(json_response[i], 'Date')
        date = str(json_date)
        date_tab.append(date[2:12])

        json_za_ra = jsonpath.jsonpath(json_response[i], 'Confirmed')
        str_za_ra = str(json_za_ra)
        int_za_ra = int(str_za_ra[1:-1])
        za_ra.append(int_za_ra)

        json_zg_ra = jsonpath.jsonpath(json_response[i], 'Deaths')
        str_zg_ra = str(json_zg_ra)
        int_zg_ra = int(str_zg_ra[1:-1])
        zg_ra.append(int_zg_ra)

        json_oz_ra = jsonpath.jsonpath(json_response[i], 'Recovered')
        str_oz_ra = str(json_oz_ra)
        int_oz_ra = int(str_oz_ra[1:-1])
        oz_ra.append(int_oz_ra)

        json_ak_ra = jsonpath.jsonpath(json_response[i], 'Active')
        str_ak_ra = str(json_ak_ra)
        int_ak_ra = int(str_ak_ra[1:-1])
        ak_ra.append(int_ak_ra)

        if i > 0:
            za_dn.append(za_ra[i] - za_ra[i-1])
            zg_dn.append(zg_ra[i] - zg_ra[i-1])
            oz_dn.append(oz_ra[i] - oz_ra[i-1])
            ak_dn.append(ak_ra[i] - ak_ra[i-1])
        else:
            za_dn.append(za_ra[i])
            zg_dn.append(zg_ra[i])
            oz_dn.append(oz_ra[i])
            ak_dn.append(ak_ra[i])

    except IndexError:
        break

con = mysql.Connect(host='127.0.0.1', unix_socket='', user='krzys2', passwd='kijwoko',
                    db='corona_pl')  # łączenie się z bazą danych
cur = con.cursor()  # tworzy obiekt, dzięki któremu będzie można wysyłać zapytania do bazy danych
cur.execute("USE corona_pl")  # wybranie istniejącej bazy danych
cur.execute("TRUNCATE TABLE zarazenia")

zdate = date_tab
zplZar = za_ra
zplPrz = za_dn
zplZgo = zg_ra
zplZP = zg_dn
zwlZar = oz_ra
zwlPrz = oz_dn
zwlZgo = ak_ra
zwlZP = ak_dn

loggit = """INSERT INTO zarazenia(date, plZar, plPrz, plZgo, plZP, wlZar, wlPrz, wlZgo, wlZP) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

for i in range(0, len(date_tab)):
    date = zdate[i]
    plZar = zplZar[i]
    plPrz = zplPrz[i]
    plZgo = zplZgo[i]
    plZP = zplZP[i]
    wlZar = zwlZar[i]
    wlPrz = zwlPrz[i]
    wlZgo = zwlZgo[i]
    wlZP = zwlZP[i]

    cur.execute(loggit, (date, plZar, plPrz, plZgo, plZP, wlZar, wlPrz, wlZgo, wlZP))
cur.close()












