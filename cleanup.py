import pandas as pd
import numpy as np

na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('./data/311-service-requests.csv',
                       na_values=na_values,
                       dtype={'Incident Zip': str})


def fix_zip_codes(zips):
    # Truncate everything to length 5
    zips = zips.str.slice(0, 5)

    # Set 00000 zip codes to nan
    zero_zips = zips == '00000'
    zips[zero_zips] = np.nan

    return zips


requests['Incident Zip'] = fix_zip_codes(requests['Incident Zip'])

print(requests['Incident Zip'].unique())

