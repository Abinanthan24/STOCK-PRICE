import yfinance as yf
import streamlit as st
import datetime



st.write("""
# Simple Stock Price App

stock **closing price** and ***volume price*** Of period '1d'

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = st.text_input('Enter the symbol')
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date', today)
end_date = st.date_input('End date', tomorrow)
if start_date < end_date:
    st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.error('Error: End date must fall after start date.')

tickerDf = tickerData.history( period='1d', start= start_date,end=end_date)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.bar_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
st.bar_chart(tickerDf.Volume)

