import pickle
from datetime import datetime

import transaction


class Parser:
    def __init__(self):
        pass

    def parse(self, filename):
        file = open(filename, mode='r', encoding='iso-8859-1')
        data = file.read()
        print("Header")
        print("--------------")
        [print(l.split(';')) for l in data.split('\n')[:13]]
        print("CSV")
        print("--------------")
        [print(l.split(';')) for l in data.split('\n')[13:-1]]
        print("--------------")
        self.stats(data.split('\n')[14:-1])

    def stats(self, data):
        sum = 0
        transaction_list = []
        for l in data:
            l_split = l.split(';')
            transaction_list.append(
                transaction.Transaction(datetime.strptime(l_split[0], "%d.%m.%Y"), l_split[2], l_split[4],
                                        -float(l.split(';')[7].replace(".", "").replace(",", ".")), l_split[8],
                                        float(l.split(';')[5].replace(".", "").replace(",", ".")), l_split[4],
                                        l_split[3], l))
            if float(l.split(';')[7].replace(".", "").replace(",", ".")) < 0 and "VISA MCDONALDS" in l or "MCDONALDS;Lastschrift" in l:
                sum -= float(l.split(';')[7].replace(".", "").replace(",", "."))
                #print(l)
        pickle.dump(transaction_list, open('transaction_list.pkl', 'wb'))
        with open("sum.pkl", "w") as file:
            file.write(str(pickle.dumps(transaction_list)))
        print(transaction_list)
        print(sum)
        #[print(l) for l in data if float(l.split(';')[7].replace(".","").replace(",",".")) < 0 and "VISA MC" in l]