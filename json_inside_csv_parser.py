#!/usr/bin/env python
# coding: utf-8
#csv kolonundaki json verisi, pandas ile okurken problem olusturuyor. Bunun icin oncelikle kolonlar arasinda |
#koyuluyor ve daha sonra read_csv ile okunabiliyor. (delimiter vererek.)
import re
from pathlib import Path

p = Path('/home/skocer/csv_files') / 'value.csv'
p2 = Path('/home/skocer/csv_files') / 'value_fix.csv'

with p.open('r') as f:
    with p2.open('w') as f2:
        for cnt, line in enumerate(f):
            if cnt == 0:
                line = line.replace(',', '|')
            else:
                line = re.sub(r',(?=(((?!\}).)*\{)|[^\{\}]*$)', '|', line)
            f2.write(line)

ais_data = pd.read_csv('/home/skocer/csv_files/fix.csv', sep='|')
# In[ ]:

