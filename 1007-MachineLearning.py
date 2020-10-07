import pandas as pd

dataset = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/pythonTutorial/online_raw.csv')
print(dataset.info())
print('\nStatistik deskriptif:\n', dataset.describe())

dataset_corr = dataset.corr()
print('Korelasi dataset:\n', dataset.corr())
print('Distribusi Label (Revenue):\n', dataset['Revenue'].value_counts())

# Tugas praktek
print('Korelasi BounceRates-ExitRates: ', dataset_corr.loc['BounceRates','ExitRates'])
print('Korelasi Revenue-PageValues: ', dataset_corr.loc['PageValues','Revenue'])
print('Korelasi TrafficType-Weekend: ', dataset_corr.loc['Weekend','TrafficType'])