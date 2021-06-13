class Transaction():
    def __init__(self,txid,fee,weight,parents = ""):
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parents = parents
        self.score = round((self.fee/pow(self.weight,1)*100), 4)

    def get_fee(self):
        return self.fee

    def get_weight(self):
        return self.weight

    def get_score(self):
        return self.score

    def get_txid(self):
        return self.txid

def csv_parser(path=""):
    parsed_list = []
    with open(path) as csv_file:
        parsed_list = [Transaction(*line.strip().split(',')) for line in csv_file.readlines() if line.strip().split(',')[1] != "fee"]
    return parsed_list

def sort_transactions(transactions):
    return sorted(transactions,key= lambda e: e.get_score(),reverse=True)

def find_limited_array(sorted_array):
    total_weight = 0
    limited_array = []

    for i in sorted_array:
        total_weight += i.get_weight()
        if total_weight < 4000000:
            limited_array.append(i)
        else:
            break

    return limited_array

def final_list_of_txids(limited_array):
    return [tx.get_txid() for tx in limited_array]

def write_to_file(final_list_of_txids):
    file = open("block.txt","a")
    final_list_of_txids = [id+"\n" for id in final_list_of_txids]
    file.writelines(final_list_of_txids)
    file.close()

def get_total_fee(limited_array):
    total_fee = 0
    for i in limited_array:
        total_fee  += i.get_fee()
    return total_fee




if __name__ == "__main__":
    parsed_list = csv_parser('mempool.csv')
    sorted_list = sort_transactions(parsed_list)
    limited_array = find_limited_array(sorted_list)
    final_list = final_list_of_txids(limited_array)
    print(get_total_fee(limited_array))
    write_to_file(final_list)
