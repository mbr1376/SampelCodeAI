# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:57:09 2020

@author: mohamad
"""


import pandas as pd
import matplotlib.pyplot as plt

def func_p(thresh,list1,list2):
    tp,fp=0,0;
    for i in range(0,len(list2)):
        if list2[i]>=thresh and list1[i]==1 :
            tp=tp+1
        elif list2[i]>=thresh and list1[i]==0:
            fp=fp+1
    return tp ,fp

def func_N(thresh,list1,list2):
    tN,fN=0,0;
    for i in range(0,len(list2)):
        if list2[i]<thresh and list1[i]==0 :
            tN=tN+1
        elif list2[i]<thresh and list1[i]==1:
            fN=fN+1
    return tN ,fN

if __name__== "__main__":
         col_list=["d0","d1"];
         Tp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
         Fp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
         Tn=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
         Fn=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
         accuracy=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
         Precision=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
         recall=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
         Specificity=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
         F1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
         
         df = pd.read_csv('input1.csv',usecols=col_list)
         list_th=[1,0.95,0.90,0.85,0.80,0.75,0.70,0.65,0.60,0.55,0.50,0.45,0.40,0.35,0.30,0.25,0.20,0.15,0.10,0.05,0]
         for i in range(0,len(list_th)) :
             Tp[i],Fp[i]=func_p(list_th[i],df['d0'],df['d1'])
             Tn[i],Fn[i]=func_N(list_th[i],df['d0'],df['d1'])
          
         for i in range(0,len(list_th)) :
             accuracy[i]=(Tp[i]+Tn[i])/len(list_th)
             recall[i]=Tp[i]/(Tp[i]+Fn[i])
             Specificity[i]=Tn[i]/(Tn[i]+Fp[i])
             if Tp[i]+Fp[i]!=0:
                 Precision[i]=Tp[i]/(Tp[i]+Fp[i])
             else:
                 Precision[i]=1
         for i in range(0,len(list_th)) :
            F1[i]=(2*Precision[i]*recall[i])/(Precision[i]+recall[i])
        
        
         dic_file={'th':list_th,'Tp':Tp,'Fp':Fp,'Tn':Tn,'Fn':Fn,'accuracy':accuracy,'Precision':Precision,'recall':recall,'Specificity':Specificity,'F1':F1}
         df_save = pd.DataFrame(dic_file, columns= ['th', 'Tp' ,'Fp','Tn','Fn','accuracy','Precision','recall','Specificity','F1']) 
         df_save.to_csv (r'out.csv', index = False, header=True)
         plt.plot(recall,Specificity)
         plt.xlabel('recall')
         plt.ylabel('Specificity')
         plt.show()
         
         
         
         
         
         
         