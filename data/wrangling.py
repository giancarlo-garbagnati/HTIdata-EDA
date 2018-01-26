# Script to help wrangle all the date strings into one uniform format

import pandas as pd
import datetime

hti_df = pd.read_csv('HTI_00-11_stata13.csv')


# Let's remove all unwanted characters (ex: 'Ê' and ' a') from the 
def remove_unwanted_chars (s):
    #if type(s) is str:
    if isinstance(s, str):
        if len(s) < 10: # check len to see if it's not a valid date
            print(s)
            return '?'
        else:
            new_s = s
            new_s = s.replace('Ê','')
            # taking care of weird cases
            weird_cases = [' a', ' A', ' d']
            if new_s[-2:] in weird_cases: #taking care of this weird case
                new_s = new_s[:-2]
                
            return new_s

date_cols = ['UNP_sign', 'UNP_rat', 'ILO182', 'ILO29',
       'ILO105', 'CEDAW_sign', 'CEDAW_rat', 'UNCRC_sign', 'UNCRC_rat',
       'conflict_sign', 'conflict_rat']

for col in date_cols:
    hti_df[col] = hti_df[col].apply(remove_unwanted_chars)


# Let's now convert all the dates to one uniform format
def convert_datetime(s, in_fmt, out_fmt):
    if (s is not None) and (s is not '?'):
        return datetime.datetime.strptime(s, in_fmt).strftime(out_fmt)

"""
Each date column and an example of original format
'UNP_sign' - 13 Dec 2000
'UNP_rat' - 3 Nov 2005
'ILO182' - 1999-12-02
'ILO29' - 2011-06-13
'ILO105' - 1991-09-25
'CEDAW_sign' - 17 Jul 1980
'CEDAW_rat' - 10 Dec 1981
'UNCRC_sign' - 10 Nov 2001
'UNCRC_rat' - 23 Dec 2002
'conflict_sign' - 5 Jul 2000
'conflict_rat' - 23 Dec 2002
"""

in_fmt = '%d %b %Y'
out_fmt = '%Y-%m-%d'

date_change_cols = ['UNP_sign', 'UNP_rat', 'CEDAW_sign', 'CEDAW_rat', 
       'UNCRC_sign', 'UNCRC_rat', 'conflict_sign', 'conflict_rat']

for col in date_change_cols:
    hti_df[col] = hti_df[col].apply(lambda s: convert_datetime(s, in_fmt, out_fmt))

hti_df.to_csv('HTI_00-11_stata13_unifdate.csv', index=False)
