import csv
import os
import time 
def readdata():
  with open(r"D:\CS\python\usthack\usthack2021\usthackcsv.csv", newline='', encoding="utf-8") as csvfile:
      rows = csv.reader(csvfile)
      l0 = list(rows)
      l1 = []
      for i in range(5, len(l0[1]), 2):
          if l0[1][i] != "":
              l1.append(l0[1][i])
      print(l1)
      l2 = []
      for i in range(5, len(l0[4]), 2):
          if l0[4][i] != "":
              l2.append(l0[4][i])
      print(l2)
      print(set(l1) & set(l2))

def inputmeun():
  global time
  id1 = input("ID:")
  dido = input("Dine-in?(y/n):")
  t = time.localtime()
  time = time.strftime("%H%M",t)
  return "abc"

def mainmeun():
  print("***Main meun***\n1. Ordering\n2. Food availible today\n3. Quene\n4. Ordering history\n5. Back")
mainmeun()
