import requests
from bs4 import BeautifulSoup
import pandas

r = requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div", {"class": "propertyRow"})
page_no = soup.find_all("a",{"class":"Page"})[-1].text


l = []
base_url = "http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0, int(page_no)*10, 10):
    print(base_url+ str(page)+".html")
    r = requests.get(base_url+ str(page)+".html")
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    all = soup.find_all("div",{"class":"propertyRow"})

    for item in all:
        d = {}
        d["Address"] = item.find_all("span",{"class":"propAddressCollapse"})[0].text
        d["Locality"] = item.find_all("span", {"class": "propAddressCollapse"})[1].text
        d["Price"] = item.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", "")
        try:
            d["Beds"] = item.find("span",{"class":"infoBed"}).find("b").text
        except:
            d["Beds"] = None
        try:
            d["Area"] = item.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            d["Area"] = None
        try:
            d["Full Bath"] = item.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Bath"] = None
        try:
            d["Half Bath"] = item.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Bath"] = None
        for colgroup in item.find_all("div",{"class":"columnGroup"}):
            for fg, fn in zip(colgroup.find_all("span",{"class":"featureGroup"}),colgroup.find_all("span",{"class":"featureName"}) ):
                if "Lot Size" in fg.text:
                    d["Lot Size"] = fn.text
        l.append(d)




import pandas as pd
df = pd.DataFrame(l)
print(df)

df.to_csv("Output.csv")


