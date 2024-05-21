# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"3903.0","system":"readv2"},{"code":"44169.0","system":"readv2"},{"code":"39923.0","system":"readv2"},{"code":"37810.0","system":"readv2"},{"code":"34015.0","system":"readv2"},{"code":"10358.0","system":"readv2"},{"code":"2587.0","system":"readv2"},{"code":"18678.0","system":"readv2"},{"code":"16723.0","system":"readv2"},{"code":"13243.0","system":"readv2"},{"code":"12582.0","system":"readv2"},{"code":"103946.0","system":"readv2"},{"code":"17391.0","system":"readv2"},{"code":"33444.0","system":"readv2"},{"code":"36371.0","system":"readv2"},{"code":"41523.0","system":"readv2"},{"code":"21698.0","system":"readv2"},{"code":"31268.0","system":"readv2"},{"code":"57802.0","system":"readv2"},{"code":"38961.0","system":"readv2"},{"code":"36530.0","system":"readv2"},{"code":"25886.0","system":"readv2"},{"code":"15221.0","system":"readv2"},{"code":"31188.0","system":"readv2"},{"code":"42566.0","system":"readv2"},{"code":"40595.0","system":"readv2"},{"code":"54134.0","system":"readv2"},{"code":"31700.0","system":"readv2"},{"code":"20170.0","system":"readv2"},{"code":"12870.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_lung-and-trachea-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["lung---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["lung---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["lung---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
