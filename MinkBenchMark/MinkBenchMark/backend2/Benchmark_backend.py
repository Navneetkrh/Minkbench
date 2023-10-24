import time
import psutil
import re
import sympy
# from pdfminer.high_level import extract_pages, extract_text
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

# ML
def ml_train():
    import numpy as np 
    import pandas as pd 
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import AdaBoostClassifier

    st1 = time.time()
    df = pd.read_csv('/home/soham/Coding_Adventures/OS/MinorProject/Minkbench/MinkBenchMark/MinkBenchMark/backend2/my_benchmark_data.csv')
    y_data = np.array(df['Class'])
    x_data = np.array(df.drop(columns=['Class']))
    x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,random_state = 100,stratify = y_data)
    Ada_clf = AdaBoostClassifier(random_state=42)
    Ada_clf.fit(x_test,y_test)
    st2 = time.time()
    return st2-st1


# Arith

def Arith_test():
    start_benchmark = 12000 
    start_benchmark = int(start_benchmark)

    start = time.time()

    for i in range(0,start_benchmark):
        for x in range(1,1000):
            3.141592 * 2**x
        for x in range(1,10000):
            float(x) / 3.141592
        for x in range(1,10000):
            float(3.141592) / x

    end = time.time()
    duration = (end - start)
    return duration 


# PDF Rendere

# def pdf_text_render():
#     start_time = time.time()
#     for page_layout in extract_pages('trial.pdf'):
#         for element in page_layout:
#             continue
#     end_time = time.time()
#     duration = end_time-start_time
#     return duration


# Tree Search Prime Finder

def Prime_calc():
    start_time = time.time()
    n = 20000000
    primes = list(sympy.primerange(1, n))
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed



def Main_benchmark():
    b_start = time.time()
    ml = ml_train()
    ar = Arith_test()
    # pd = pdf_text_render()
    dt = Prime_calc()
    total = ml + ar  + dt
    ml_score = (1000/ml)*10
    ar_score = (1000/ar)*10
    # pd_score = (1000/pd)*10
    dt_score = (1000/dt)*10


    b_score = ml_score + ar_score + dt_score
    return b_score, ml_score, ar_score, dt_score



if __name__ == "__main__":
    score,ml_score,ar_score,dt_score = Main_benchmark()
    # return score,ml_score,ar_score,dt_score
    print("b_score  :", score)
    print("ml_score :",ml_score)
    print("ar_score :",ar_score)
    print("dt_score :", dt_score)


