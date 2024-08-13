import pyodbc

server = '110.50.84.98,11114'
# server = 'localhost'
database = 'TradingView'
username = 'Tradingview'
password = 'tradingview123987#'

conn = pyodbc.connect(
    'DRIVER=SQL Server;'
    f'SERVER=DESKTOP-1GP5JPT;'
    f'DATABASE={database};'
    'UID=Tradingview;'
    'PWD=tradingview123987#;'
    'TrustServerCertificate=yes;'
)
