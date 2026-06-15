import pickle

macces_list = pickle.load(open("transaction_list.pkl", "rb"))

for t in macces_list:
    print(t.print_object())
