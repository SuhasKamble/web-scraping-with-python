from bs4 import BeautifulSoup

with open('index.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content,'lxml')
    all_cources = soup.find_all('div',class_="card")
    for cources in all_cources:
        cource_name = cources.h5.text 
        cources_cost = cources.a.text.split()[-1]

        print(f"{cource_name} costs {cources_cost}")
