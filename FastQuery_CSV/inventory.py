import re
import csv

with open('csv_and_dataproc/output_laptops.csv') as f:
    reader = csv.reader(f)
    rows = list(reader)
    header = rows[0]
    rows = rows[1:]
    
def row_price(row):
    return row[-1]

class Inventory():                    
    
    def __init__(self, csv_filename):
        with open(csv_filename) as f: 
            reader = csv.reader(f)
            rows = list(reader)
        self.header = rows[0]        
        self.rows = rows[1:]

        for row in self.rows:              
            row[-1] = int(row[-1])
        
        self.id_to_row = {}                        
        for row in self.rows:                       
            self.id_to_row[row[0]] = row
        
        self.prices = set()                          
        for row in self.rows:                        
            self.prices.add(row[-1])
        
        self.rows_by_price = sorted(self.rows, key=row_price)
    
    def get_laptop_from_id(self, laptop_id):
        for row in self.rows:                 
            if row[0] == laptop_id:
                return row
        return None   
    
    def get_laptop_from_id_fast(self, laptop_id):  
        if laptop_id in self.id_to_row:           
            return self.id_to_row[laptop_id]
        return None

    def check_promotion_dollars(self, dollars):    
        for row in self.rows:                   
            if row[-1] == dollars:
                return True
        for row1 in self.rows:                  
            for row2 in self.rows:
                if row1[-1] + row2[-1] == dollars:
                    return True
        return False                        
    
    def check_promotion_dollars_fast(self, dollars):
        if dollars in self.prices:                   
            return True
        for price in self.prices:                    
            if dollars - price in self.prices:
                return True
        return False                                
    
    def find_laptop_with_price(self, target_price):
        range_start = 0                                   
        range_end = len(self.rows_by_price) - 1                       
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2  
            value = self.rows_by_price[range_middle][-1]
            if value == target_price:                            
                return range_middle                        
            elif value < target_price:                           
                range_start = range_middle + 1             
            else:                                          
                range_end = range_middle - 1 
        if self.rows_by_price[range_start][-1] != target_price:                  
            return -1                                      
        return range_start
    
    def find_first_laptop_more_expensive(self, target_price): # Step 2
        range_start = 0                                   
        range_end = len(self.rows_by_price) - 1                   
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2  
            price = self.rows_by_price[range_middle][-1]
            if price > target_price:
                range_end = range_middle
            else:
                range_start = range_middle + 1
        if self.rows_by_price[range_start][-1] <= target_price:                  
            return -1                                   
        return range_start
    
    def find_last_laptop_cheaper(self, target_price):
        range_start = 0
        range_end = len(self.rows_by_price) - 1
        last_cheaper = -1  # Inicialmente, nenhum laptop mais barato é encontrado
    
        while range_start <= range_end:
            range_middle = (range_end + range_start) // 2
            price = self.rows_by_price[range_middle][-1]

            if price < target_price:
                last_cheaper = range_middle  # Atualiza o último laptop mais barato
                range_start = range_middle + 1
            else:
                range_end = range_middle - 1

        return last_cheaper

    
    def find_laptops_in_range(self, min_price, max_price):
        if (min_price > max_price):
            return -1
        min = self.find_first_laptop_more_expensive(min_price)
        max = self.find_last_laptop_cheaper(max_price)
        laptops_in_range = []
        for i in range(min,max):
            laptops_in_range.append(self.rows_by_price[i])

        return laptops_in_range
    
    def find_cheapest_laptop_with_ram_memory(self, target_ram, target_memory):
        for i in range(len(self.rows_by_price)):
            row = self.rows_by_price[i]
            if row[7] == target_ram and row[8] == target_memory:
                return row
        return -1
        
        
    