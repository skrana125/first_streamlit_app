import streamlit
import pandas
import requests
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

streamlit.header("🍓🍎🍒Fruityvice Fruit Advice!🍏🍐🍈")

# This will not only  show only but it show the value i tabluar format of what user are search in search tab
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)

# take the jason file data and shows into normalize form which shows in tabular format 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# show output in the screen as in RDBMS like tabular format
streamlit.dataframe(fruityvice_normalized)


import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The Fruit load list contain:")
streamlit.text(my_data_row)
