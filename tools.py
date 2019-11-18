import os
import pandas as pd
import glob


class CombineCsv:

    def combine_csv(self, output):
        extension = 'csv'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
        
        # combine all files in the list
        combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
        
        # export to csv
        combined_csv.to_csv(f"{output}.csv", index=False, encoding='utf-8-sig')