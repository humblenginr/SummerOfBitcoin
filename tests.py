import unittest
import solution

class Test(unittest.TestCase):
    
    def test_createTransaction(self):
        fee = 5000
        weight = 100
        parents = ""
        txid = '123asdfasdsdf23423'

        transaction = solution.Transaction(txid,fee,weight,parents)
        self.assertEqual(transaction.txid, txid)
        self.assertEqual(transaction.weight, weight)
        self.assertEqual(transaction.fee, fee)
        self.assertEqual(transaction.parents, parents)
    
    def test_csv_parser(self):
       parsed_array =  solution.csv_parser('mempool.csv')
       self.assertEqual(type(parsed_array), list)
       self.assertEqual(isinstance(parsed_array[0], solution.Transaction), True)
       self.assertEqual(parsed_array[0].get_fee(), 452)
       self.assertEqual(parsed_array[9].get_weight(), 1136)
       self.assertEqual(parsed_array[0].get_score(), 0.0172)

    def get_sorted_array(self):
       parsed_array =  solution.csv_parser('mempool.csv')
       sorted_array = solution.sort_transactions(parsed_array)
       return sorted_array

    def test_sorted_list_of_transactions(self):
        self.assertEqual(type(self.get_sorted_array()), list) 

    def test_transaction_list_with_limit(self):
        limited_array = solution.find_limited_array(self.get_sorted_array())
        total_weight = 0
        for i in limited_array:
            total_weight = total_weight + i.get_weight()
        self.assertLessEqual(total_weight, 4000000)

    def test_final_list_of_txids(self):
        limited_array = solution.find_limited_array(self.get_sorted_array())
        final_list = solution.final_list_of_txids(limited_array)
        self.assertEqual(type(final_list), list)
    
    


        

    


if __name__ == "__main__":
    unittest.main()
