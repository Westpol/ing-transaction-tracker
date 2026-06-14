
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
        self.stats(data.split('\n')[14:-1])

    def stats(self, data):
        sum = 0
        for l in data:
            if float(l.split(';')[7].replace(".", "").replace(",", ".")) < 0 and "VISA MCDONALDS" in l or "MCDONALDS;Lastschrift" in l:
                sum -= float(l.split(';')[7].replace(".", "").replace(",", "."))
                print(l)
        print(sum)
        #[print(l) for l in data if float(l.split(';')[7].replace(".","").replace(",",".")) < 0 and "VISA MC" in l]