import csv

import newline


def load_data(filename):
    rows = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            if row:
                rows.append(tuple(row))

        return rows

