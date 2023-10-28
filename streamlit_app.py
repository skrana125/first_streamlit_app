import streamlit
import pandas
streamlit.title("My Parent Healthy Diner")
streamlit.header("Breakfast Favorites")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Raged Egg") 
streamlit.text("🥑🍞 Avacado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# Lets  give option to pick fruit list, So that they can choose what fruit they wanted
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick Some Fruits :", list(my_fruit_list.index))

# Display fruit table on the page
streamlit.dataframe(my_fruit_list)
