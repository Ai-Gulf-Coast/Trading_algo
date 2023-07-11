import random 
import csv 
import sys 
import statistics 
import numpy as np 
 
def main(): 
   with open("BITSTAMP_BTCUSD, 5.csv", "r") as infile: 
       data = list(csv.reader(infile))[1:2016] 
   period = int(sys.argv[1]) if len(sys.argv) > 1 else len(data) 
   trials = int(sys.argv[2]) if len(sys.argv) > 2 else 100 
   data = data[:period] 
   print(f"for {((period*5)/60)/24} days:") 
   rates = np.arange(0.5, 0.65, 0.01) 
   [print(f"\t{r:0.2f}% accuracy : {p}% profit") for r, p in list(zip(rates,[statistics.mean(trial(rate, data) for i in range(trials)) for rate in rates]))] 
 
def trial(rate, data): 
   choices = [1 if random.random() < rate else 0 for i in data] 
   initial = 1000000 
   value = [initial] 
   delta = [(d if d > 1 else 1) if choices[i] else (d if d < 1 else 1) for i, d in enumerate([1+((float(row[2])-float(row[1]))/float(row[1])) for row in data])] 
   for i, d in enumerate(delta): 
       value.append(d*value[i]) 
   return value[-1]/value[0] 
 
if __name__ == '__main__': 
   main()