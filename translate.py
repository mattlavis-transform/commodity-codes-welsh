from googletrans import Translator
from commodity import Commodity
import csv
import os
import sys


main_folder = os.getcwd()
src_folder = os.path.join(main_folder, "src")
source_file = os.path.join(src_folder, "eu_commodities_2021-02-15.csv")
dest_folder = os.path.join(main_folder, "dest")
dest_file = os.path.join(dest_folder, "welsh_commodities.csv")

f = open(dest_file, "w+")
with open(source_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            pass
        else:
            c = Commodity(row[0], row[1], row[2], row[7])
            c.translate()
            f.write(c.extract)

        line_count += 1

        # if line_count > 10:
        #     sys.exit()

f.close()