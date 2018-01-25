# Script to help wrangle all the date strings into one uniform format

import pandas as pd

hti_df = pd.read_csv('./data/HTI_00-11_stata13.csv')


# Let's remove all unwanted characters (ex: 'Ê' and ' a') from the 
def remove_unwanted_chars (s):
    #if type(s) is str:
    if isinstance(s, str):
        new_s = s
        new_s = s.replace('Ê','')
        if new_s[-2:] == ' a': #taking care of this weird case
            new_s = new_s[:-2]
        return new_s

date_cols = ['UNP_sign', 'UNP_rat', 'ILO182', 'ILO29',
       'ILO105', 'CEDAW_sign', 'CEDAW_rat', 'UNCRC_sign', 'UNCRC_rat',
       'conflict_sign', 'conflict_rat']

for col in date_cols:
    hti_df[col] = hti_df[col].apply(remove_unwanted_chars)


# Let's now convert all the dates to one uniform format
def convert_datetime(s, in_fmt, out_fmt):
    if s is not None:
        return datetime.datetime.strptime(s, in_fmt).strftime(out_fmt)


