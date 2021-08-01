import streamlit as st

import numpy as np
import pandas as pd
import yfinance as yf
import datetime

st.title('Enter a Stock Symbol')

with st.form(key='my_form'):
    text_input = st.text_input("Enter Stock Symbol")
    submit = st.form_submit_button(label='Submit')
    if submit:
        ticket = yf.Ticker(text_input)  #
        ticket_info = ticket.info  # dictionary

        if not ticket_info["regularMarketPrice"]:
            st.write("Sorry, there is no data for the symbol you entered")

        lower_bound = datetime.date.today() - datetime.timedelta(365)
        upper_bound = datetime.date.today()

        ticket_range = ticket.history(period="max")  #(interval='1d', start=lower_bound.isoformat(), end=upper_bound.isoformat())
        st.line_chart(ticket_range)
        st.subheader("Business Summary")
        st.write(ticket_info["longBusinessSummary"])