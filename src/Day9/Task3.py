
import pandas as pd
names = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

print(names.str.lower())
print(names.str.strip())
print(names.str.contains('a'))