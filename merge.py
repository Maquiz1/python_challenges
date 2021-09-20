import csv


def merge_file(csv_list, output_path):
    fieldnames = list()
    for file in csv_list:
        with open(file, 'r') as input_csv:
            fn = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(x for x in fn if x not in fieldnames)

    with open(output_path, 'w', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file, 'r') as csv_list:
                reader = csv.DictReader(csv_list)
                for row in reader:
                    writer.writerow(row)


merge_file(['file1.csv', 'file2.csv'], 'all.csv')