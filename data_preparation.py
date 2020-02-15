import pandas as pd

data = pd.read_csv('./Data/Daily_Demand_Forecasting_Orders.csv', sep=';')

data.columns = ['week_num',
                'week_day', 'non_urgent_order',
                'urgent_order', 'order_A', 'order_B', 'order_C',
                'fiscal_sect_ord', 'traffict_sect_ord',
                'bank_ord_1', 'bank_ord_2', 'bank_ord_3',
                'total_ord']

data = data.sort_values(['week_num', 'week_day']).reset_index(drop=True)

total = data[['week_num',
              'week_day',
              'total_ord']].to_csv('./data/totals.csv', index=False)

# urgency
data_urg = data[['week_num',
                 'week_day', 'non_urgent_order',
                 'urgent_order']]

data_urg_1 = data_urg[data_urg.week_num <= 2]
data_urg_2 = data_urg[data_urg.week_num > 2]

data_urg_1.to_csv('./data/urg_1.csv', index=False)
data_urg_2.to_csv('./data/urg_2.csv', index=False)


# bank
data_bank = data[['week_num',
                  'week_day', 'bank_ord_1', 'bank_ord_2', 'bank_ord_3']]

data_bank_1 = data_bank[data_bank.week_num <= 2]
data_bank_2 = data_bank[data_bank.week_num > 2]

data_bank_1.to_csv('./data/bank_1.csv', index=False)
data_bank_2.to_csv('./data/bank_2.csv', index=False)

# data type
data_type = data[['week_num',
                  'week_day', 'order_A', 'order_B', 'order_C']]

data_type_1 = data_type[data_type.week_num <= 2]
data_type_2 = data_type[data_type.week_num > 2]

data_type_1.to_csv('./data/type_1.csv', index=False)
data_type_2.to_csv('./data/type_2.csv', index=False)
