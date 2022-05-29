import requests
from requests.models import Response
# a function that get two dates as parameters and compares the rates from older date to the  newer date (reports the changes)

print("Hi this here uses the COVID 19 API to get information from it.")
print("Here are the available options of the program.")
print("1. Relevant information for a state at the current date.")
print("2. Compares 2 dates for a state of choice.")
print("3. Compares 2 states at the current date.")
print("4. Gets recent news for a state of choice.")
print("Now, what would you like to do? Choose a number 1-5.")
choice = int(input())

#CURRENT VALUES
def current_values():
    state = input("Choose a state. (abbreviation of state, California = ca):")
    r2 = requests.get(url = 'https://api.covidtracking.com/v1/states/' +state+ '/current.json')
    data_current = r2.json() #data_current is the state's current data 

    current_date = data_current['date']
    current_positive = data_current['positive']
    current_negative = data_current['negative']
    current_total = data_current['totalTestResults']
    current_hospitalized = data_current['hospitalizedCurrently']


    print("Here are current values for: " + state)
    print("Date: "+ str(current_date))
    print("Positive: "+ str(current_positive))
    print("Negative: "+ str(current_negative))
    print("Total Cases: "+ str(current_total))
    print("Currently Hospitalized: "+ str(current_hospitalized))


#COMPARES CURRENT VALUES AND SELECTED DATE VALUES
#THIS ONE IS NOT WORKING CORRECTLY YET
def compare_values():
    # compares 2 dates with rate of mortality, hospitalization, etc
    state = input("Choose a state. (abbreviation of state, California = ca):")
    date = input("Input the date you would like to compare to in (YYYYMMDD) format please, it's less work for me:")
    r_date = requests.get(url = "https://api.covidtracking.com/v1/states/"+state+"/"+str(date)+".json")
    date_hist = r_date.json()

    #DATE VALUES  
    print("Here are the values fot the date you entered:")
    compare_date = date_hist['date']
    compare_hospitalized = date_hist['hospitalizedCurrently']
    compare_positive = date_hist['positive']
    compare_negative = date_hist['negative']
    compare_total = date_hist['total'] 
    print("Values for the date & state you entered are:")
    print("Date: "+ str(compare_date))
    print("Positive: "+ str(compare_positive))
    print("Negative: "+ str(compare_negative))
    print("Total Cases: "+ str(compare_total))
    print("Currently Hospitalized: "+ str(compare_hospitalized))
    print("")
    
    #CURRENTVALUES
    r2 = requests.get(url = 'https://api.covidtracking.com/v1/states/' +state+ '/current.json')
    data_current = r2.json() #data_current is the state's current data 
    current_date = data_current['date']
    current_positive = data_current['positive']
    current_negative = data_current['negative']
    current_total = data_current['totalTestResults']
    current_hospitalized = data_current['hospitalizedCurrently']
    print("Here are current values for: " + state)
    print("Date: "+ str(current_date))
    print("Positive: "+ str(current_positive))
    print("Negative: "+ str(current_negative))
    print("Total Cases: "+ str(current_total))
    print("Currently Hospitalized: "+ str(current_hospitalized))
    print("")

    print("Here are the changes: " )
    print("Change in positive cases: " + str(current_positive - compare_positive))
    print("Change in negative cases: " + str(current_negative - compare_negative))
    print("Change in total cases: " + str(current_total - compare_total))
    print("Change in Hospitalized: " + str(current_hospitalized - compare_hospitalized))

    
#NEWS API KEY: 57da8752d51b46abab19fd86dbc70b3e, BUT ALSO THIS IS THE NEWS TITLES API OR SOMETHING
def titles():
    state_news = input("What state would you like to get headlines for? You can input the state's name. (California, Pennsylvania, New York, etc.)")
    r_news = requests.get(url = 'https://newsapi.org/v2/everything?q=%27'+state_news+'%27&language=en&apiKey=57da8752d51b46abab19fd86dbc70b3e')
    response = r_news.json()
    print("Here are some headlines for your state of choice!")
    for i in range(10):
        print (response['articles'][i]['title'])

def two_states():
    state1 = input("Choose a state. (abbreviation of state, California = ca):")
    r1 = requests.get(url = 'https://api.covidtracking.com/v1/states/'+state1+'/current.json')
    data_current1 = r1.json() #data_current is the state's current data 

    state2 = input("Choose another state. (abbreviation of state, California = ca):")
    r2 = requests.get(url = 'https://api.covidtracking.com/v1/states/'+state2+'/current.json')
    data_current2 = r2.json() #data_current is the state's current data

    #STATE 1
    print("Here's the data for State 1:")
    current_date1 = data_current1['date']
    current_positive1 = data_current1['positive']
    current_negative1 = data_current1['negative']
    current_total1 = data_current1['totalTestResults']
    current_hospitalized1 = data_current1['hospitalizedCurrently']
    print("Current values for: " + state1)
    print("Date: "+ str(current_date1))
    print("Positive: "+ str(current_positive1))
    print("Negative: "+ str(current_negative1))
    print("Total Cases: "+ str(current_total1))
    print("Currently Hospitalized: "+ str(current_hospitalized1))
    print("")

    #STATE 2
    print("Here's the data for State 2:")    
    current_date2 = data_current2['date']
    current_positive2 = data_current2['positive']
    current_negative2 = data_current2['negative']
    current_total2 = data_current2['totalTestResults']
    current_hospitalized2 = data_current2['hospitalizedCurrently']
    print("Current values for: " + state2)
    print("Date: "+ str(current_date2))
    print("Positive: "+ str(current_positive2))
    print("Negative: "+ str(current_negative2))
    print("Total Cases: "+ str(current_total2))
    print("Currently Hospitalized: "+ str(current_hospitalized2))

if choice == 1: #WORKING
    print(current_values())
elif choice == 2: #WORKING 
    print(compare_values())
elif choice == 3: #WORKING BUT NOT SURE IF HOW INTENDED
    print(two_states())
elif choice == 4: #WORKING 
    print(titles())

def double_link_append(self):
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        old_tail = self.tail
        self.tail.next = new_node
        new_node.previous = old_tail
        self.tail = new_node

def double_link_prepend(self):
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node