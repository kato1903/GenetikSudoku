# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 22:23:49 2019

@author: Toprak
"""
import random
import time
# define sudoku problem. 0's have to be filled
    
def initialize(sudoku):
    tmp = []
    for i in range(0,80):
        if sudoku[i]==0:
            tmp.append = random.randint(1,9)
        else:
            tmp.append = sudoku[i]
    return tmp

def fitness(sudoku):
    sum = 0
    for i in range(0,9):
        m = i * 9
        for j in range(m,m+8):
            n = int (j / 9)
            n+=1
            n*=9
            for k in range(j+1,n):
                if(sudoku[j] == sudoku[k]):
                    sum += 1
                    
                    
    for i in range(0,9):
        for j in range(0,8):
            n = int (j / 9)
            n+=1
            n*=9
            for k in range(j+1,n):
                if(sudoku[j*9+i]==sudoku[k*9+i]):
                    sum += 1
                    
    box = [1,2,9,10,11,18,19,20]
    boxi= [0,3,6,27,30,33,54,57,60]
    for i in range(0,9):
        m = boxi[i]        
        for j in range(0,8):
            n = int (j / 9)
            n+=1
            n*=9
            if(j!=0):
                t = m + box[j-1]
            else:
                t = m
            for k in range(j+1,n): 
                p = m + box[k-1]
                if(sudoku[t]==sudoku[p]):
                    sum += 1
                    
    #print(sum)        
    return sum;

def initialize(K,Su):                   # ilk durum için rasgele kromozomlu bireylerin popülasyonunu
    population = []                     # oluşturur
    path = []
    individual = []
    for j in range(K):
        for i in range(0,81):
            if(Su[i]==0):
                path.append(random.randint(1, 9))
            else:
                path.append(Su[i])
        individual.append(path)
        individual.append(fitness(path))
        population.append(individual)
        individual = []
        path = []
    return population

def reproduce(individual1, individual2):
    l = list(range(81))
    random.shuffle(l)
    child = []
    tmp = [0] * 81
    #print(l)
    #print(tmp)
    k = 0
    for i in range(0, 27):
        tmp[l[i]] = individual1[0][l[i]]
    for i in range(27, 81):
        tmp[l[i]] = individual2[0][l[i]]
    child.append(tmp)
    child.append(fitness(tmp))
    return child



def mutation(child,sabit):                    # Mutasyona uğratıp birey döndürüyor
    count = random.randint(1,9)
    
    i = 0;
    while(i < 1):        
        value = random.randint(0,80)
        #print(value)
        if(value in sabit):
            pass
        else:
            child[0][value] = random.randint(1,9)
            i += 1
    child[1] = fitness(child[0])    
    return child

def bestindividual(population):                 # Popülasyondaki En iyi bireyi döndürür
    min = population[0][1]
    best = population[0]
    for i in population:
        if (i[1] < min):
            min = i[1]
            best = i
    return best

def worstindividual(population):                 # Popülasyondaki En iyi bireyi döndürür
    min = population[0][1]
    worst = population[0]
    for i in population:
        if (i[1] > min):
            min = i[1]
            worst = i
    return worst

def selection(population):  # Olasılığa göre birey döndüren fonksiyon
    sum = 0		            # Rulet Tekeri mantığına göre
    pr = []
    p = 0
    for i in population:
        sum += int((200 - i[1]))
        pr.append(sum)

    p = random.randint(1, sum)
    c = 0
    #print(p)
    while pr[c] < p:
        c += 1
        
    return population[c]

def check(population):                    # Tüm yiyecekleri yiyen bulundu mu
    a = True
    for individual in population:
        if individual[1] == 0:
            a = individual
            print("Found")
            return a

    return False

def genetic_algorithm(population,sabit,c,p):        # Genetik Algoritma
    found = False	# Bulunca whiledan çıkmak için
    k = 0		# jenerasyon sayısını tutuyor 100000 e kadar deniyor
    bestindividuals = []# her 100 jenerasyonda bir örnek eklemek için    
    start_time = time.time()
    timeout = 120   # [seconds]
    timeout_start = time.time()
    while (found == False and time.time() < timeout_start + timeout):
        
        k += 1
        print("Generation Count : " + str(k) + " Best Fitness " + str((200-bestindividual(population)[1]) / 2) + " Worst Fitness " + str((200-worstindividual(population)[1]) / 2 ) + " Gecen Sn: " + str((time.time() - start_time)))
                            
        new_population = []
        
        for i in range(4):    
            worst = worstindividual(population)
            population.remove(worst)
        Ran = initialize(4,sudoku)
        for j in Ran:
            population.append(j)                     
        for i in range(c):
            x = selection(population)	# Olasılığa göre birey seçimi
            y = selection(population)
            while(y==x):
               y = selection(population)  	
            child = reproduce(x, y)	# 2 bireyi crossover
            if (random.randint(1, 100) < 5):	 
                child = mutation(child,sabit)
            new_population.append(child)	# yeni bireyin yeni popülasyona eklenmesi        
        for i in range(p-c):    
            best = bestindividual(population)
            population.remove(best)
            new_population.append(best)                   
        population = new_population        
        found = check(population)	# bulunup bulunmadığının kontrolü
    print("Generation Count : " + str(k) + " Best Fitness " + str((200-bestindividual(population)[1]) / 2) + " Worst Fitness " + str((200-worstindividual(population)[1]) / 2 ) + " Gecen Sure: " + str((time.time() - start_time)))     
    end_time = time.time() 
    return end_time-start_time,bestindividual(population)

def compare(a,b):
    sum = 0
    for i in range(0,81):
        if a[i] != b[i]:
            sum += 1
    return sum

def yazdir(s):
    for j in range(0,9):
        for i in range (0,1):
            print(str(s[i+j*9]) + " " + str(s[i+j*9 + 1]) + " " + str(s[i+j*9 + 2]) + " "+ str(s[i+j*9 + 3]) + " "+ str(s[i+j*9 + 4]) + " "+ str(s[i+j*9 + 5]) + " "+ str(s[i+j*9 + 6]) + " "+ str(s[i+j*9 + 7]) + " "+ str(s[i+j*9 + 8]))
            
        
    
sudoku=[
0,0,0,0,5,2,8,0,0,
5,0,0,0,0,0,0,6,2,
8,0,6,4,7,0,0,0,5,
1,0,0,2,0,0,0,5,0,
0,0,9,0,1,0,7,0,0,
0,5,0,0,0,6,0,0,1,
4,0,0,0,2,5,3,0,7,
9,1,0,0,0,0,0,0,4,
0,0,2,1,4,0,0,0,0]

sudoku=[
3,4,0,0,5,2,8,0,0,
5,0,7,8,0,0,0,6,2,
8,0,6,4,7,9,0,0,5,
1,0,0,2,0,0,6,5,0,
0,0,9,0,1,0,7,0,3,
2,5,0,0,0,6,0,0,1,
4,0,8,9,2,5,3,0,7,
9,1,0,3,6,0,0,0,4,
0,0,2,1,4,8,0,0,0]

sudokuGercek=[
3,4,1,6,5,2,8,7,9,
5,9,7,8,3,1,4,6,2,
8,2,6,4,7,9,1,3,5,
1,7,4,2,9,3,6,5,8,
6,8,9,5,1,4,7,2,3,
2,5,3,7,8,6,9,4,1,
4,6,8,9,2,5,3,1,7,
9,1,5,3,6,7,2,8,4,
7,3,2,1,4,8,5,9,6]


sudoku = []

file_handle = open('sudoku.txt', 'r')
lines_list = file_handle.readlines()
for j in range(0,9):
    cols = lines_list[j].split()
    for i in range(0,9):
        sudoku.append(int(cols[i]))
sabit = []

for i in range(0,81):
    if sudoku[i]!=0:
        sabit.append(i)

populasyonSayisi = 1000
SabitKalan = 250
Populasyon = initialize(populasyonSayisi,sudoku)

#yazdir(Populasyon[0])

Test = []



sure,last = genetic_algorithm(Populasyon,sabit,SabitKalan,populasyonSayisi)


print("Time: " + str(sure)); 
yazdir(last[0])

text = input("Çıkmak için esc tuşuna basın")
