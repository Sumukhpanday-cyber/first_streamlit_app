import streamlit;
streamlit.title("My parent new healthy dinner");
streamlit.header("Breakfast menu");
streamlit.text("chicken");
streamlit.text("manchurian");
streamlit.text("eating food ");
import pandas;
myfruitlist=pandas.read_csv("uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
streamlit.dataframe(myfruitlist);
