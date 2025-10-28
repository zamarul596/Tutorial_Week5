import streamlit as st

# Set the title and icon for the page
st.set_page_config(
    page_title="Program Apprentice 3u1i@FHPK",
    page_icon="🎓", 
)

analysis = st.Page('PLO_sum.py', title='Pencapaian Akademik', icon=":material/school:")
#overall = st.Page('Overall_PLO.py', title="Overall PLO")
industri = st.Page('Industry_List.py', title='Pencapaian Industri', icon=":material/business:")
home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home, analysis, industri]
        }
    )

pg.run()
