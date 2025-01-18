import streamlit as st
from utils.brochure_func import Website 
from utils.brochure_func import link_system_prompt 
from utils.brochure_func import get_links_user_prompt 
from utils.brochure_func import get_links 
from utils.brochure_func import get_all_details
from utils.brochure_func import system_prompt 
from utils.brochure_func import get_brochure_user_prompt 
from utils.brochure_func import stream_brochure


st.title('Company Brochure Generator')
st.sidebar.header('Input Details')

company_name = st.sidebar.text_input('Company Name', placeholder = 'Enter the company name')
url = st.sidebar.text_input('Website URL', placeholder = 'Enter the company website URL')

if st.sidebar.button('Generate Brochure'):
    if company_name and url:
        st.write(f'### Generating Brochure for {company_name}')
        with st.spinner('Fetching and processing data...'):
            try:
                stream_brochure(company_name, url)
            except Exception as e:
                st.write(f"An error occurred: {e}")
    else:
        st.error("Please provide both the company name and the website URL.")
        
        
st.write('---')
st.write('Created by [Kamil Stachurski](https://www.linkedin.com/in/kamroki/)')
