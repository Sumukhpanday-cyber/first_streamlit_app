import streamlit;
streamlit.title("My parent new healthy dinner");
streamlit.header("Breakfast menu");
streamlit.text("chicken");
streamlit.text("manchurian");
streamlit.text("eating food ");
import pandas;
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruit_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected];
streamlit.dataframe(fruits_to_show);
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json()) #just writes the data to the screen
# take the json version of the response and normalize it
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
streamlit.dataframe(fruityvice_normalized)


