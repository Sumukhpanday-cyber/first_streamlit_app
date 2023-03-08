import streamlit;
streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Favourites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale,Spinach & Rocket Smoothiee')
streamlit.text('Hard Boiled Free Range Egg ')
streamlit.text('Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.dataframe(fruits_to_show)
streamlit.stop()
import snowflake.connector
from urllib.error import URLError
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert  into fruit_load_list values('from  streamlit')")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit list contains ")
streamlit.dataframe(my_data_rows)	





