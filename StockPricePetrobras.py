import yfinance as yf
import streamlit as st
import pytz


st.write("""
# Simples App de Ações
Mostra os preços de **Fechamento** e ***Volume*** da Petrobras
 entre 2010 e 2020.
""")

# Definir o simbolo da ação
tickerSymbol = 'PETR3.SA'
# Pegar os dados desse simbolo
tickerData = yf.Ticker(tickerSymbol)
# Pegar os dados históricos desse simbolo
tickerDf = tickerData.history(
    start="2010-02-22", end="2020-02-20")

# Conversor de unidades temporais
trans = pytz.timezone('US/Eastern')
tickerDf.index = tickerDf.index.tz_localize(trans).tz_convert(pytz.utc)

st.write('''
Fechamento das ações da Petrobras''')
st.line_chart(tickerDf.Close)


st.write('''
Volume das ações da Petrobras''')
st.line_chart(tickerDf.Volume)
