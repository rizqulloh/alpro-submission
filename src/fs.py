import csv
import re
import os


class Filesystem:
    def __init__(self, path):
        if not os.path.exists(path):
            return print("File not found")
        self.path = path
        self.data = self.loadData()

    def loadData(self):
        results = []
        with open(self.path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=",")
            for row in csv_reader:
                rowData = {}
                for val in row:
                    key, value = val.strip().split(':')
                    if value.startswith("(") and value.endswith(")"):
                        valClean = re.compile(r'\(\s*\)|\s*\(|\s*\)|\(\s*')
                        rowData[key] = [
                            int(c) for c in valClean.sub("", value).split(',')]
                    else:
                        strippedValue = value.strip()
                        if strippedValue.isnumeric():
                            rowData[key] = int(strippedValue)
                        else:
                            rowData[key] = strippedValue

                results.append(rowData)
        return results

    def write(self, data: dict):
        with open(self.path, 'a') as csvFile:
            writer = csv.writer(
                csvFile,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )

            row = self.formatting(data)

            writer.writerow(row)

        self.data = self.loadData()

    def formatting(self, data: dict):
        row = []
        for key, value in data.items():
            if type(value) == list:
                val = "({})".format(",".join([str(id) for id in value]))
                row.append(f"{key}:{val}")
            else:
                row.append(f"{key}:{value}")
        return row

    def update(self, newData: dict, key, value):
        for index, data in enumerate(self.data):
            if data[key] == value:
                self.data[index] = newData
                break

        self.data = [self.formatting(data) for data in self.data]
        with open(self.path, 'w') as csvFile:
            writer = csv.writer(
                csvFile,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )

            row = self.data

            writer.writerows(row)

        self.data = self.loadData()

    def delete(self, key, value):
        for index, data in enumerate(self.data):
            if data[key] == value:
                del self.data[index]

        self.data = [self.formatting(data) for data in self.data]
        with open(self.path, 'w') as csvFile:
            writer = csv.writer(
                csvFile,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )

            row = self.data

            writer.writerows(row)

        self.data = self.loadData()
