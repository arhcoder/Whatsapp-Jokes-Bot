import requests

#/ This is a gift for someone /#
def get_joke(programming: bool = False):

    #? Depending on the jokes type:
    if programming: jokes_url = "https://v2.jokeapi.dev/joke/Any"
    else: jokes_url = "https://v2.jokeapi.dev/joke/Miscellaneous,Dark,Pun,Spooky,Christmas"

    #? Get the jokes:
    response = requests.get(jokes_url)
    if response.status_code == 200:

        #? Correctly getted joke:
        joke_json = response.json()

        #? If it is a two part joke:
        if joke_json["type"] == "twopart":
            print("2")
        elif joke_json["type"] == "single":
            print("1")
    else:
        return False
    
#! Sabes qué? No tiene sentido utilizar esta API; las bromas son
#! en inglés; y al traducir muchas de estas no tienen sentido en
#! español. Dado que es un regalo para alguien que habla español,
#! no tiene sentido ;:T. Mejor busco un dataset con bromas :3

get_joke()