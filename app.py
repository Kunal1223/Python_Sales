# Core Pkgs
import streamlit as st
from home_page import run_home_page
from eda_app import run_eda
from ml_app import run_ml

html_temp = """
		<div style="background-color:#E8E8AB;padding:10px;border-radius:10px">
		<h1 style="color:Blue;text-align:center;">Welcome to NITTE Prediction</h1>
		<h4 style="color:Red;text-align:center;">Happy to see you..</h4>
		</div>
		"""

def main():
	st.markdown(html_temp, unsafe_allow_html=True)
	menu = ["Home", "EDA", "Predict", "About"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice == "Home":
		run_home_page()
	elif choice == "EDA":
		run_eda()    
	elif choice == "Predict":
		run_ml()
	else:
		st.subheader("About")
		st.info("Built with Streamlit")
		st.text("Made with ❤️ by NITTE ")
		

if __name__ == '__main__':
	main()
