import streamlit as st
import pandas as pd
import yfinance as yf

# Set the page title
st.title("French CAC 40 Stock Price Viewer")

# Define a list of CAC 40 stocks
cac40_stocks = ["AIR.PA", 
                "SAN.PA", 
                "TOT.PA", 
                "BNP.PA", 
                "OR.PA",
                "RI.PA",
                "ATO.PA",
                "WLN.PA",
                "ORA.PA",
                "CA.PA",
                "ACA.PA",
                "VIE.PA",
                "SGO.PA",
                "CAP.PA",
                "ML.PA",
                "KER.PA",
                "MC.PA",
                "UG.PA",
                "ENGI.PA",
                "BN.PA",
                "FP.PA",
                "SW.PA",
                "GLE.PA",
                "AC.PA",
                "VIV.PA",
                "HO.PA",
                "SU.PA",
                "DG.PA",
                "AI.PA",
                "EN.PA",
                "LR.PA"]

# Create a dropdown menu for stock selection
selected_stock = st.selectbox("Select a CAC 40 Stock:", cac40_stocks)

# Function to get the last closing price
def get_last_closing_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        if not data.empty:
            return data["Close"].iloc[0]
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    return None

# Display the last closing price if a stock is selected
if selected_stock:
    last_closing_price = get_last_closing_price(selected_stock)
    if last_closing_price is not None:
        st.success(f"Last Closing Price for {selected_stock}: {last_closing_price} USD")
    else:
        st.error(f"Failed to retrieve data for {selected_stock}.")