import pandas as pd
import numpy as np
# import pyperclip, re # Importing the libraries(this case: regex and pyperclip)

# Create phone regex
import pandas as pd

uni=pd.DataFrame(pd.read_csv(r"E:\Waseem\extraViz\KnowledgeBase\world_universities.csv"))
uni.head()

city=pd.DataFrame(pd.read_excel(r"E:\Waseem\extraViz\KnowledgeBase\cities500.xlsx"))
city.head()

def module_1_entities(data):

    #   urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    def _urls(g):
        urls=[]
    #     print(data.head())
        url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    #     for g in data['Resumes']:
        url_matches = url_pattern.finditer(str(g))
    #     print(url_matches)
        for match in url_matches:
            urls.append(match.group(0))
        return urls


    import re
    def _email(g):
        email=[]
    #     y=""
        
    #     print(data.head())
    #     email_pattern = re.compile(r'[a-zA-Z0-9-\.]+@[a-zA-Z-\.]*\.(com|edu|net)')
        email_pattern = re.compile(r'[a-zA-Z0-9-\.]+@[a-zA-Z-\.]*\.(com|edu|net)')

    #     for g in data['Resumes']:
        email_matches = email_pattern.finditer(g)
    #     print(email_matches)
        for match in email_matches:
            email.append(match.group(0))
    #         print(match.group(1))
        return email
        


    def _contact(g):
        y=""
        cont=[]
        contact_pattern = re.compile(r'(?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    #     for g in data['Resumes']:
        contact_matches = contact_pattern.finditer(str(g))
        for match in contact_matches:
            cont.append(match.group(0))
        return cont


    def _university(g):
        univ=[]
    #     for g in data['cleaned']:
        uni=pd.DataFrame(pd.read_csv(r"E:\Waseem\extraViz\KnowledgeBase\world_universities.csv"))

        g=str(g).lower()
        for x in uni['University of Andorra']:
            x=str(x).lower()
            if x in g:
                univ.append(x)
        return univ



    from fuzzywuzzy import fuzz
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    stop=stopwords.words("english")

    def _city(g):
        citi=[]
        city=pd.DataFrame(pd.read_excel(r"E:\Waseem\extraViz\KnowledgeBase\cities500.xlsx"))

        g=str(g).lower()
        g=word_tokenize(g)
        for x in city['City']:
    #         print(x)
            x=str(x).lower()
            if x in g:
                citi.append(x)
        return citi

    def _country(g):
        countri=[]
        country=pd.DataFrame(pd.read_excel(r"E:\Waseem\extraViz\KnowledgeBase\cities500.xlsx"))

        g=str(g).lower()
        g=word_tokenize(g)
        for x in country['GEOGRAPHY']:
    #         print(x)
            x=str(x).lower()
            if x in g:
                countri.append(x)
        return countri
        # col=['Skill','Date','Location','Organization','NORP','Languages','Name','City','University','Country','Email','Contact']
    col=['City','Location','University','Contact','Email','URLS']

    new_data2=pd.DataFrame(columns=col)


    

    # uni.head()

    # city.head()

    for g in range(len(data)):
    #     print(g)
        city=_city(data['cleaned'][g])
        location=_country(data['cleaned'][g])
    #     print(city)
        uni=_university(data['cleaned'][g])
    #     print(uni)
        cont=_contact(data['Resumes'][g])   
    #     print(cont)
        email=_email(data['Resumes'][g])
    #     print(email)
        urls=_urls(data['Resumes'][g])
        new_data2=new_data2.append({'City':city,'Location':location,'University':uni,'Contact':cont,'Email':email,'URLS':urls}, ignore_index=True)


    return new_data2
