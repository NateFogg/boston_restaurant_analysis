import requests
import pandas as pd
import time
from config import TOKEN

ZIPS = {'East Boston':['02128'], 'Charlestown': ['02129'], 'Allston': ['02163','02134'], 'Brighton':['02135'], 'Beacon Hill': ['02108'], 
        'Back Bay': ['02116', '02199'],'Chinatown': ['02111'], 'Dorchester': ['02121', '02122', '02124', '02125'], 'Fenway': ['02115', '02215'],
          'Hyde Park': ['02136'], 'Jamaica Plain': ['02130'], 'Mattapan': ['02126'], 'Mission Hill': ['02120'],'North End': ['02113', '02109'], 'Roslindale': ['02131'], 
          'Roxbury': ['02119'], 'South Boston': ['02127', '02210'], 'South End': ['02118'], 'West End': ['02114'], 'West Roxbury': ['02132'], 'Wharf District': ['02110'],
           'Downtown': ['02203', '02201']}
VALID_CUISINES = [
    "afghan", "african", "senegalese", "southafrican", "newamerican", "tradamerican", "andalusian", "arabian",
    "arabpizza", "argentine", "armenian", "asianfusion", "asturian", "australian", "austrian", "baguettes",
    "bangladeshi", "bbq", "basque", "bavarian", "beergarden", "beerhall", "beisl", "belgian", "flemish", "bistros",
    "blacksea", "brasseries", "brazilian", "brazilianempanadas", "centralbrazilian", "northeasternbrazilian",
    "northernbrazilian", "rodizios", "breakfast_brunch", "pancakes", "british", "buffets", "bulgarian", "burgers",
    "burmese", "cafes", "themedcafes", "cafeteria", "cajun", "cambodian", "newcanadian", "canteen", "caribbean",
    "dominican", "haitian", "puertorican", "trinidadian", "catalan", "cheesesteaks", "chickenshop", "chicken_wings",
    "chilean", "chinese", "cantonese", "congee", "dimsum", "fuzhou", "hainan", "hakka", "henghwa", "hokkien", "hunan",
    "pekinese", "shanghainese", "szechuan", "teochew", "comfortfood", "corsican", "creperies", "cuban", "currysausage",
    "cypriot", "czech", "czechslovakian", "danish", "delis", "diners", "dinnertheater", "dumplings", "eastern_european",
    "eritrean", "ethiopian", "hotdogs", "filipino", "fischbroetchen", "fishnchips", "flatbread", "fondue", "food_court",
    "foodstands", "freiduria", "french", "alsatian", "auvergnat", "berrichon", "bourguignon", "mauritius", "nicois",
    "provencal", "reunion", "sud_ouest", "galician", "gamemeat", "gastropubs", "georgian", "german", "baden",
    "easterngerman", "franconian", "hessian", "northerngerman", "palatine", "rhinelandian", "giblets", "gluten_free",
    "greek", "guamanian", "halal", "hawaiian", "heuriger", "himalayan", "honduran", "hkcafe", "hotdog", "hotpot",
    "hungarian", "iberian", "indpak", "indonesian", "international", "irish", "island_pub", "israeli", "italian",
    "abruzzese", "altoatesine", "apulian", "calabrian", "cucinacampana", "emilian", "friulan", "ligurian", "lumbard",
    "napoletana", "piemonte", "roman", "sardinian", "sicilian", "tuscan", "venetian", "japanese", "blowfish",
    "conveyorsushi", "donburi", "gyudon", "oyakodon", "handrolls", "horumon", "izakaya", "japacurry", "kaiseki",
    "kushikatsu", "oden", "okinawan", "okonomiyaki", "onigiri", "ramen", "robatayaki", "soba", "sukiyaki", "takoyaki",
    "tempura", "teppanyaki", "tonkatsu", "udon", "unagi", "westernjapanese", "yakiniku", "yakitori", "jewish", "kebab",
    "kopitiam", "korean", "kosher", "kurdish", "laos", "laotian", "latin", "colombian", "salvadoran", "venezuelan",
    "raw_food", "lyonnais", "malaysian", "mamak", "nyonya", "meatballs", "mediterranean", "falafel", "mexican",
    "easternmexican", "jaliscan", "northernmexican", "oaxacan", "pueblan", "tacos", "tamales", "yucatan",
    "mideastern", "egyptian", "lebanese", "milkbars", "modern_australian", "modern_european", "mongolian",
    "moroccan", "newmexican", "newzealand", "nicaraguan", "nightfood", "nikkei", "noodles", "norcinerie",
    "opensandwiches", "oriental", "pfcomercial", "pakistani", "panasian", "eltern_cafes", "parma", "persian",
    "peruvian", "pita", "pizza", "polish", "pierogis", "polynesian", "popuprestaurants", "portuguese", "alentejo",
    "algarve", "azores", "beira", "fado_houses", "madeira", "minho", "ribatejo", "tras_os_montes", "potatoes",
    "poutineries", "pubfood", "riceshop", "romanian", "rotisserie_chicken", "russian", "salad", "sandwiches",
    "scandinavian", "schnitzel", "scottish", "seafood", "serbocroatian", "signature_cuisine", "singaporean",
    "slovakian", "somali", "soulfood", "soup", "southern", "spanish", "arroceria_paella", "sri_lankan",
    "steakhouses", "swabian", "swedish", "swiss", "syrian", "tabernas", "taiwanese", "teaparlor", "teppanyaki",
    "tex-mex", "thai", "traditional", "tradamerican", "turkish", "doner", "gokuniku", "homemade", "lahmacun", "oygur",
    "pide", "trinidadian", "turkishravioli", "uyghur", "uzbek", "vegan", "vegetarian", "venison", "vietnamese",
    "waffles", "wok", "wraps", "yugoslav"
]

businesses = pd.DataFrame()
final_json_data = []

calls = 0
invalid_count = 0

for neighborhood, zip_codes in ZIPS.items():
    for code in zip_codes:

        offset = 0
        add_count = 1

        while add_count > 0 and offset < 1000:
            add_count = 0
            # grab data from the api
            url = 'https://api.yelp.com/v3/businesses/search?location=Boston%2C%20MA%2C%20' + code + '&term=restaurants&sort_by=distance&limit=50&offset=' + str(offset)
            headers = {
                        'accept': 'application/json',
                        'Authorization': 'Bearer ' + TOKEN
                    }

            response = requests.get(url, headers=headers)

            # Handle the API request error here
            if response.status_code == 200:
                json_data = response.json()
            else:
                print('Failed to retrieve data from the API.')
                json_data = None

            # if businesses - location - zip_code not in the list of neighborhood do not add
            # may need to use a loop to drop the index within json data
            business_list = json_data['businesses']
            for bus in business_list:
                # each new business set false
                valid_alias = False

                # verify that yelp has indeed returned a valid restaurant category
                for tag_dict in bus['categories']: 
                    if tag_dict['alias'] in VALID_CUISINES:
                        valid_alias = True
                        break
                # verify that the business is located within the target neighborhood as well
                if valid_alias and bus['location']['zip_code'] == code:
                    bus['neighborhood'] = neighborhood
                    final_json_data.append(bus)
                    add_count += 1
                else:
                    # curious to see how many invalid businesses the yelp api returns under the search terms 
                    invalid_count += 1


            # increase the offset
            offset += 50
            if offset > 950:
                print('EXCEEDED OFFSET LIMIT!')

            # do not call from the api too fast
            time.sleep(1)
            calls += 1