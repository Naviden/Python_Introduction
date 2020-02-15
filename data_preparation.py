import pandas as pd

data = pd.read_csv('./Data/Daily_Demand_Forecasting_Orders.csv', sep=';')

data.columns = ['week_num',
                'week_day', 'non_urgent_order',
                'urgent_order', 'order_A', 'order_B', 'Order_C',
                'fiscal_sect_ord', 'traffict_sect_ord',
                'bank_ord_1', 'bank_ord_2', 'bank_ord_3',
                'total_ord']

data_urg = data[['week_num',
                 'week_day', 'non_urgent_order',
                 'urgent_order']]

data_urg_1 = data_urg.iloc[:, :30]
data_urg_2 = data_urg.iloc[:, 30:]

data_urg_1.to_csv('./data/urg_1.csv')
data_urg_1.to_csv('./data/urg_2.csv')

data_type = data[['week_num',
                  'week_day', 'order_A', 'order_B', 'Order_C']]

data_type_1 = data_type.iloc[:, :30]
data_type_2 = data_type.iloc[:, 30:]

data_type_1.to_csv('./data/type_1.csv')
data_type_1.to_csv('./data/type_2.csv')

data_bank = data[['week_num',
                  'week_day', 'bank_ord_1', 'bank_ord_2', 'bank_ord_3']]

data_bank_1 = data_bank.iloc[:, :30]
data_bank_2 = data_bank.iloc[:, 30:]

data_bank_1.to_csv('./data/bank_1.csv')
data_bank_1.to_csv('./data/bank_2.csv')
