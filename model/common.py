import pyodbc

# server = '110.50.84.98,11114'
server = 'DESKTOP-1GP5JPT'
database = 'TradingView'
username = 'root'
password = 'root'
# username = 'Tradingview'
# password = 'tradingview123987#'

conn_str = 'DRIVER=SQL Server;'\
           f'SERVER={server};'\
           f'DATABASE={database};'\
           f'UID={username};'\
           f'PWD={password};'\
           'TrustServerCertificate=yes;'
