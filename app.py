import streamlit as st
import pycountry
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide", initial_sidebar_state="expanded" )
covid = pd.read_csv("data/covid_cases.csv")
def get_iso3(iso2):
    #Function takes in iso_alpha2 country codes and returns the iso_alpha 3 codes"""
    try:
        return pycountry.countries.get(alpha_2=iso2).alpha_3
    except:
        #In case we have errors that row of data will be left out.
        #Try except is a good way to handle possible errors that might occur while running a function"""
        pass
st.sidebar.image("who.PNG")
st.sidebar.title("WHO Coronavirus (COVID-19) Dashboard")
opt= st.sidebar.radio("Select the case to view", options=("Cumulative cases","New cases", "Cumulative deaths", "New deaths"))
covid['iso_alpha'] = covid.Country_code.apply(lambda x: get_iso3(x))
covid["Date_reported1"]=pd.to_datetime(covid["Date_reported"])
covid1 = covid.groupby (["Date_reported1"])["New_cases"].sum().reset_index()
covid2 = covid.groupby (["Date_reported1"])["Cumulative_cases"].sum().reset_index()
covid3 = covid.groupby (["Date_reported1"])["Cumulative_deaths"].sum().reset_index()
covid4 = covid.groupby (["Date_reported1"])["New_deaths"].sum().reset_index()
if opt == "Cumulative cases":
    st.title("WHO Coronavirus (COVID-19) Cumulative Cases")
    fig= px.choropleth(covid,
               locations="iso_alpha",
               color="Cumulative_cases", 
               hover_name="Country", # column to add to hover information
               color_continuous_scale=px.colors.sequential.Blues,
               animation_frame="Date_reported",
                title="Global COVID-19  Cumulative Cases")# animation based on the dates
    fig.update_layout(height=600) #Enlarge the figure
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
    st.markdown("This is Covid-19 Cumulative confirmed cases reported to WHO as at December, 2022. The cumulative cases can also be observed in the bar graph below")
    fig=px.bar(covid2, x="Date_reported1", y="Cumulative_cases", labels={"Date_reported1": "Date", "Cumulative_cases":"Cumulative Cases"}, title="Covid 19 cumulative cases")
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
   
#new cases
elif opt == "New cases":
    st.title("WHO Coronavirus (COVID-19) New Cases")
    fig= px.choropleth(covid,
               locations="iso_alpha",
               color="New_cases", 
               hover_name="Country", # column to add to hover information
               color_continuous_scale=px.colors.sequential.Turbo,
               animation_frame="Date_reported",# animation based on the dates
               title="Global COVID-19 Daily New Cases")
    fig.update_layout(height=600) #Enlarge the figure
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
    st.markdown("This is Covid-19 New confirmed cases reported to WHO as at December, 2022. The daily new cases can also be visualized in the bar graph below")
    fig=px.bar(covid1, x="Date_reported1", y="New_cases", labels={"Date_reported1": "Date", "New_cases":"New Covid Daily Cases"}, title="Daily Covid 19 new cases")
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')

#cumulative deaths
elif opt == "Cumulative deaths":
    st.title("WHO Coronavirus (COVID-19) Cumulative Deaths")
    fig= px.choropleth(covid,
               locations="iso_alpha",
               color="Cumulative_deaths", 
               hover_name="Country", # column to add to hover information
               color_continuous_scale=px.colors.sequential.Magenta,
               animation_frame="Date_reported")# animation based on the dates
    fig.update_layout(height=600) #Enlarge the figure
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
    st.markdown("This is Covid-19 Cumulative confirmed deaths reported to WHO as at December, 2022. The cumulative deaths can also be observed in the bar graph below")
    fig=px.bar(covid3, x="Date_reported1", y="Cumulative_deaths", labels={"Date_reported1": "Date", "Cumulative_deaths":"Daily Cumulative Cases"}, title="Daily Covid 19 Cumulative deaths")
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
#new deaths
else:
    st.title("WHO Coronavirus (COVID-19) New Deaths")
    fig= px.choropleth(covid,
               locations="iso_alpha",
               color="New_deaths", 
               hover_name="Country", # column to add to hover information
               color_continuous_scale=px.colors.sequential.Oranges,
               animation_frame="Date_reported")# animation based on the dates
    fig.update_layout(height=600) #Enlarge the figure
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
    st.markdown("This is Covid-19 new confirmed deaths reported to WHO as at December, 2022. The new deaths can also be observed in the bar graph below")
    fig=px.bar(covid4, x="Date_reported1", y="New_deaths",labels={"Date_reported1": "Date", "New_cases":"New deaths"}, title="Daily Covid 19 new deaths")
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
### TASKS
## 1. GENERATE THREE MORE ANIMATED GRAPHS i.e. new cases, cumulative deaths, new deaths
## 2. Give your graphs titles and if possible add explanative text after each graph
## 3. Use widgets in the sidebar to help the user chooose between the four animations: e.g. select box, button, radio 
## 4. create bar graphs to show the cumulative cases per day and cumulative daeaths per day 
## 5. deploy your app to streamlit cloud
## 6. submit the link to your streamlit app on dexvirtual


