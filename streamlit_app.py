import streamlit;
streamlit.title("My parent new healthy dinner");
streamlit.header("Breakfast menu");
streamlit.text("chicken");
streamlit.text("manchurian");
streamlit.text("eating food ");
import pandas;
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list);


