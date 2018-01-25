# Simple script to convert the STATA dta file to a csv file.

import pandas as pd

hti_df = pd.read_stata('HTI_00-11_stata13.dta')

hti_df.to_csv('HTI_00-11_stata13.csv', index=False)
