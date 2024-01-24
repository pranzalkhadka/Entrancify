import streamlit as st


from src.overview import Overview
from src.ascol import Ascol
from src.patan import Patan
from src.bhaktapur import Bhaktapur
from src.stxavier import StXavier


program_overview = Overview.program_overview
ascol_analysis = Ascol.ascol_analysis
patan_analysis = Patan.patan_analysis
bhaktapur_analysis = Bhaktapur.bhaktapur_analysis
stxavier_analysis = StXavier.stxavier_analysis


st.sidebar.title("Merit List Analysis")

csit_img_path = "/home/pranjal/Downloads/Entrancify/Images/csit.jpg"

st.sidebar.image(csit_img_path, use_column_width=True)


user_menu = st.sidebar.radio(
    'Select an Option',
    ('Program Overview','Amrit Science Campus', 'Patan Multiple Campus', 'Bhaktapur Multiple Campus', 'St.Xavier')
)

if user_menu == 'Program Overview':
    program_overview()

if user_menu == 'Amrit Science Campus':
    ascol_analysis()

if user_menu == 'Patan Multiple Campus':    
    patan_analysis()

if user_menu == 'Bhaktapur Multiple Campus':
    bhaktapur_analysis()

if user_menu == 'St.Xavier':
    stxavier_analysis()