import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Parent Healthy Diner")
streamlit.header("Breakfast Favorites")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Raged Egg") 
streamlit.text("🥑🍞 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# Lets  give option to pick fruit list, So that they can choose what fruit they wanted
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick Some Fruits :", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display fruit table on the page
streamlit.dataframe(fruits_to_show)

# organize now into function for more sutable way so that it can create repetabel block
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
    # take the jason file data and shows into normalize form which shows in tabular format
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# new section to displt fruityvice api response
streamlit.header("🍓🍎🍒Fruityvice Fruit Advice!🍏🍐🍈")
# This will not only  show only but it show the value i tabluar format of what user are search in search tab
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error('Please select a fruit to get information')
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
        
except URLError as e:
    stremlit.error()

streamlit.header("The fruit load list contains:")

#snowflake related function
# first creat function to load fruit into the table which with help of function we can execute time and again
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute('Select * from fruit_load_list')
        return my_cur.fetchall()

# add button to load fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlist.dataframe(my_data_rows)
