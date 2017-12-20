import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.corpus import wordnet
#This dictionairy was obtained from scraping the http://www.supercook.com/scripts/scripts.cabbb32a.js file.
ingredient_dictionairy={"Dairy":["butter","eggs","milk","whole milk","parmesan","cheddar","cream","sour cream","cream cheese","mozzarella","american cheese","yogurt","evaporated milk","condensed milk","whipped cream","half and half","monterey jack cheese","feta","cottage cheese","ice cream","goat cheese","frosting","swiss cheese","buttermilk","velveeta","ricotta","powdered milk","blue cheese","provolone","colby cheese","gouda","pepper jack","italian cheese","soft cheese","romano","brie","pepperjack cheese","custard","cheese soup","pizza cheese","ghee","pecorino cheese","gruyere","creme fraiche","neufchatel","muenster","asiago","queso fresco cheese","hard cheese","havarti cheese","mascarpone"],"Vegetables":["garlic","onion","olive","tomato","potato","salad greens","carrot","basil","parsley","rosemary","bell pepper","chili pepper","corn","ginger","mushroom","broccoli","spinach","green beans","celery","red onion","cilantro","cucumber","pickle","dill","avocado","sweet potato","zucchini","shallot","mixed vegetable","cabbage","asparagus","cauliflower","mint","pumpkin","kale","frozen vegetables","scallion","squash","sun dried tomato","horseradish","sweet corn","beet"],"Fruits":["lemon","banana","apple","coconut","mango","lime","orange","pineapple","strawberries","raisin","blueberries","grapefruit","honeydew","grape","prunes","nectarine","fig","peach","cranberries","raspberries","pear","cherry","apricot","blackberries","berries","date","watermelon","kiwi","craisins","mandarin","cantaloupe","plum","papaya","pomegranate","apple butter","clementine","rhubarb","tangerine","sultanas","currant","plantain","passion fruit","persimmons","quince","lychee","tangelos","lingonberry","kumquat","boysenberry","star fruit","guava"],"Spices":["red pepper flake","cinnamon","chive","vanilla","garlic powder","oregano","paprika","cayenne","chili powder","cumin","italian seasoning","thyme","peppercorn","nutmeg","onion powder","curry powder","bay leaf","taco seasoning","sage","ground nutmeg","chinese five spice","allspice","turmeric","ground coriander","coriander","cajun seasoning","steak seasoning","herbs","celery salt","vanilla essence","poultry seasoning","marjoram","tarragon","cardamom","celery seed","garam masala","mustard seed","chile powder","italian herbs","saffron","caraway","herbes de provence","italian spice","star anise","savory","dill seed","aniseed","cacao","tamarind"],"Meats":["chicken breast","ground beef","bacon","sausage","cooked chicken","ham","veal","beef steak","hot dog","pork chops","chicken thighs","ground turkey","pork","turkey","pepperoni","whole chicken","chicken leg","ground pork","chicken wings","chorizo","polish sausage","salami","pork roast","ground chicken","pork ribs","venison","spam","lamb","pork shoulder","beef roast","bratwurst","prosciutto","chicken roast","bologna","corned beef","lamb chops","ground lamb","beef ribs","duck","pancetta","beef liver","leg of lamb","chicken giblets","beef shank","pork belly","cornish hen","lamb shoulder","lamb shank"],"Fish":["canned tuna","salmon","fish fillets","tilapia","haddock","grouper","cod","flounder","anchovies","tuna steak","rockfish","sardines","smoked salmon","monkfish","canned salmon","whitefish","halibut","trout","mahi mahi","catfish","sea bass","mackerel","swordfish","sole","red snapper","pollock","herring","perch","caviar","pike","bluefish","lemon sole","eel","carp","cuttlefish","barramundi"],
"Baking & Grains":["wheat germ","flour","whole wheat flour","rice","pasta","bread","baking powder","bread flour","baking soda","bread crumbs","bran","cornstarch","semolina","noodle","rolled oats","yeast","cracker","quinoa","pancake mix","flour tortillas","cornmeal","chips","saltines","brown rice","popcorn","self rising flour","macaroni cheese mix","corn tortillas","stuffing mix","biscuits","couscous","pie crust","pita","bisquick","cereal","angel hair","croutons","lasagne","ramen","baguette","pizza dough","barley","puff pastry","cake mix","bagel","pretzel","cream of wheat","multigrain bread","crescent roll dough","pierogi","hot dog bun","filo dough","wheat","ravioli","muffin mix","gnocchi","bread dough","potato flakes","rye","croissants","matzo meal","shortcrust pastry","ciabatta","breadsticks","angel food","risotto","spelt"],"Oils":["vegetable oil","olive oil","peanut oil","cooking spray","shortening","lard","almond oil","grape seed oil"],"Seafood":["shrimp","crab","scallop","prawns","clam","lobster","octopus","calamari","squid","oyster","cockle","crawfish","mussel"],"Added Sweeteners":["sugar","honey","confectioners sugar","maple syrup","syrup","molasses","corn syrup"],"Seasonings":["cream of tartar","bouillon","ground ginger","sesame seed","apple cider","chili sauce","liquid smoke","balsamic glaze","hoisin sauce","vegetable bouillon","soy sauce","rice wine","rose water","fish stock","champagne vinegar"],"Nuts":["peanut butter","chestnut","almond","cashew","walnut","peanut","pecan","flax","pine nut","pistachio","almond meal","praline","hazelnut","macadamia","almond paste","macaroon"],"Condiments":["mayonnaise","mustard","ketchup","vinegar","balsamic vinegar","wine vinegar","cider vinegar","rice vinegar","mirin","apple cider vinegar","fish sauce","blue cheese dressing"],"Desserts & Snacks":["chocolate","white chocolate","apple sauce","graham cracker","marshmallow","potato chips","pudding mix","chocolate morsels","bittersweet chocolate","cookie dough","chocolate syrup","nutella"],"Beverages":["apple juice","coffee","orange juice","tea","espresso","tomato juice","green tea","cranberry juice","coke","lemonade","ginger ale","pineapple juice","fruit juice","club soda","sprite","grenadine","margarita mix"],"Soup":["chicken broth","mushroom soup","beef broth","tomato soup","vegetable stock","chicken soup","celery soup","onion soup","vegetable soup","dashi"],"Dairy Alternatives":["soy milk","almond milk","coconut milk","hemp milk"],"Legumes":["peas","black beans","chickpea","lentil","hummus","soybeans","pinto beans","cannellini beans","navy beans","kidney beans","lima beans","green beans","french beans"],"Sauces":["tomato sauce","tomato paste","chicken gravy","pesto","beef gravy","alfredo sauce","curry paste"],"Alcohol":["liqueur","whiskey","beer","white wine","red wine","champagne","rum","frangelico","brandy","vodka","tequila","sherry","bitters","cooking wine","bourbon","kahlua","gin","whisky","irish cream","sake","amaretto","vermouth","triple sec","grappa","masala","grand marnier","cabernet sauvignon","dessert wine","schnapps","port wine","burgundy wine","sparkling wine","cognac","chocolate liqueur","curacao","creme de menthe","limoncello","raspberry liquor","bloody mary","shaoxing wine","madeira wine","absinthe","ciclon","ouzo","anisette"]}
#Total list
totalList=[]
manuallyAddedIngredients=["plum tomatoes","water","red pepper","green pepper","yellow pepper","salt"]
for key,value in ingredient_dictionairy.items():
    totalList=totalList+value
totalList=totalList+manuallyAddedIngredients

print(len(totalList))


def returnTotalList():
    """
    Returns the total list with all the ingredients from the ingredient dictionairy and the manually added ingredients
    """
    return totalList

def load_tsv():
    #LOAD RECIPE DATA INTO DF
    INFOFOLDER="recipeInfo/"
    tsvDf=pd.read_csv(INFOFOLDER+"recipeInfo_WestWhiteHorvitz_WWW2013.tsv",sep="\t",encoding="UTF-8")
    return tsvDf


#----------------------------------------DATA CLEANING------------------------------------------#

def morphy_lower(s):
    """
    Returns the given string to lower case and morphed.
    """
    s=s.lower()
    splitteds=s.split(" ")
    temps=""
    for spls in splitteds:
        morphyCheck=wordnet.morphy(spls)
        if morphyCheck!=None:
            temps=temps+ wordnet.morphy(spls)+" "
        else:
            temps=temps+ spls+ " "
    return temps[0:-1] #Remove last space

def makeIngredientList(ingredientStr):
    """
    Returns a liste of ingredients spllitted according to |. 
    It removed the uneccesairy items from each ingredient.
    """
    #SPLIT with |
    splitted=ingredientStr.split("|")
    #print(splitted)
    #clean the string
    cleanedSplitted=[]
    for ingredient in splitted:
        cleanedSplitted.append(removeUnecessairyItems(ingredient))
     
    return cleanedSplitted


#IMPORTS AND META DATA USED TO REMOVE UNECESSAIRY WORDS
from nltk.corpus import stopwords
weightIndicators=["ounce","teaspoon","tablespoon","cup","small","big","half","peel"]
weightRE=[re.compile(el) for el in weightIndicators]
filteringOut=["-lrb-", "-rrb-","!","ripe","sliced"]
filterOutRE=[re.compile(el) for el in filteringOut]
uselessWords=stopwords.words("english")
from string import digits
remove_digits = str.maketrans('', '', digits)
RE_D = re.compile('\d')

def removeUnecessairyItems(ingredientBOW):
    words=ingredientBOW.split(' ')
    finalSentence=[]
    weightIndicString=" ".join(weightIndicators)
    for word in words:
        if containsMethod(word,RE_D):
            continue 
        if subStringInList(word,weightRE):
            continue
        if subStringInList(word,filterOutRE):
            continue
        if word in uselessWords:
            continue
        finalSentence.append(word)
    return " ".join(finalSentence) #make the list to a sentence agin

def containsMethod(string,RE):
    return bool(RE.search(string))
def subStringInList(string,RElst):
    for i in range(len(RElst)):
        if containsMethod(string,RElst[i]):
            return True        
    return False


#----------------------------------------MATCHING THE INGREDIENTS------------------------------------------#

#Usefull library function that returns the closest matches in a list of strings to a given string.
from difflib import get_close_matches
def findBestMatch(s):
    """
    Finds the best matches to the given string in the ingredient database (totalList)
    There can be multiple matches and if the strings are not similar enough an empty list is returned.
    """
    s = " ".join(re.findall(r"[\w']+", s))
    close_matches = get_close_matches(s,totalList,cutoff=0.7)
    if len(close_matches) == 0:
        #NO near perfect match is found
        #This could be because of an adjective like nonfat or because the string is not the same 
        #format as the other strings , let's try to find with sub words
        splitteds= s.split(" ")
        if len(splitteds) == 1:
            return []
        #Try a two word frame first (for stuff like blue cheese, ice cream, goat cheese) if the two words match we take them out
        ingredients2Words,splitteds = matchTwoWordFrame(splitteds)
        
        #After that we try to match the resting one word frames.
        ingredients1Word = matchOneWordFrame(splitteds)
        
        return ingredients2Words + ingredients1Word      
    elif len(close_matches) == 1:
        return [close_matches[0]]
    else:
        #print(s + "matches close with "+ str(close_matches))
        return [close_matches[0]]
def matchTwoWordFrame(splitteds):
    """
    Tries to match two consecutive words with the ingredient database.
    It returns the matches and the unmatched words. 
    """
    matches=[]
    unMatchedSplitteds=[]
    i=0
    while i<len(splitteds)-1:
        subMatches=get_close_matches(splitteds[i]+" "+splitteds[i+1],totalList,cutoff=0.91)
        
        if (len(subMatches)>=1):
            matches.append(subMatches[0])
            i=i+2
        else:
            unMatchedSplitteds.append(splitteds[i])
            if (i+1==len(splitteds)-1):
                unMatchedSplitteds.append(splitteds[i+1])
            i=i+1
    return matches,unMatchedSplitteds


def matchOneWordFrame(splitteds):
    """
    Tries to match single words with the ingredient database.
    """
    smallMatches={}
    for spls in splitteds:
        subMatches=get_close_matches(spls,totalList,cutoff=0.9)
        if len(subMatches)==0:
                #No match found for this word
                continue
        smallMatches[spls]=subMatches[0]
    if len(smallMatches.items())==0:
            #NO MATCH FOUND FOR THIS INGREDIENT
            return []
    return list(smallMatches.values())


def finalClean(s):
    """
    Cleans an ingredient string to a list of unique ingredients.
    """
    ingredientList=makeIngredientList(s)
    resultList=[]
    #print(ingredientList)
    for s in ingredientList:
        bestMatch=findBestMatch(s)
        resultList=resultList+bestMatch
    return str(set(resultList))#Remove duplicates and convert to a string.
