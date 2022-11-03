# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 18:02:49 2021

@author: User
"""




import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import torch
result = []
n = 1
ran_ratio = np.zeros((1,n))
ffd_ratio = np.zeros((1,n))
pro_ratio = np.zeros((1,n))
for k in range(n):
# name = input("please write file name to open: ")
    if k == 0:
        name = 'ep_1000_item_50_knap_3_R_10_R2_80_data.pickle_221103_12_34'
        result.append('ffh_mul_end_1103_19_12_item_50_knap_3_data.pickle_')
        result.append('random_sol_knap_end_1103_19_09_item_50_knap_3_data.pickle_')
        result.append('test_1103_19_28_item_50_knap_3_data.pickle')

    with open(name,'rb') as f:
        data = pickle.load(f)
    # with open('./ep_10_item_10_knap_2_R_30_div_10_mul_3_data.pickle_210907_16_55','rb') as f:
    #     data = pickle.load(f)
        
    # print(data)
    # print(data.get('item'))
    # print(data.get('knapsack'))
    overall_item_value = np.array(data.get('value'))
    overall_item_weight = np.array(data.get('weight'))
    overall_knap_capa = np.array(data.get('knapsack'))
    item_size = overall_item_value.shape[1]
    epi_len = 1000
    epi_ratio_sum = np.zeros((3,epi_len))
    last_state = np.zeros((3,item_size))
    result_data = []
    # result = input("please write file name to open: ")
    for j in range(3):
        with open(result[j],'rb') as f:
            result_data = pickle.load(f)
         #overall_knap_capa.shape[0]  
        
        t_state = np.array(result_data.get('last_state'))
        t_state = np.squeeze(t_state)
        isItem_map = np.zeros((epi_len,item_size))
        isItem_unmap = np.zeros((epi_len,item_size))
        epi_sum = np.zeros((1,epi_len))
        
        for i in range(epi_len):
        
            isItem_map[i,:] = np.add(isItem_map[i,:], t_state[i])
            unSelected = np.nonzero(isItem_map[i] == 0 )[0]
            isItem_unmap[i,unSelected] = 1
             # print(unSelected)
            epi_sum[0,i] = sum(np.squeeze(np.multiply(isItem_map[i].reshape(1, len(isItem_map[i])), overall_item_value[i].reshape(1,len(overall_item_value[i])))))
            epi_ratio_sum[j,i] = epi_sum[0,i]/sum(overall_item_value[i])
            # print(np.multiply(isItem_map[i].reshape(1, len(isItem_map[i])), overall_item_value[i].reshape(1,len(overall_item_value[i]))))        
    
    # result2 = input("please write file name to open: ")
    # with open(result2,'rb') as f:
    #     result_data2 = pickle.load(f)
    # last_state2 = np.array(result_data2.get('last_state'))
    # last_state2 = np.squeeze(last_state2)
    # isItem_map2 = np.zeros((epi_len,item_size))
    # isItem_unmap2 = np.zeros((epi_len,item_size))
    # epi_sum2 = np.zeros((1,epi_len))
    # for i in range(epi_len):
    
    #     isItem_map2[i,:] = np.add(isItem_map2[i,:], last_state2[i])
    #     unSelected = np.nonzero(isItem_map2[i] == 0 )[0]
    #     isItem_unmap2[i,unSelected] = 1
     
    #     # print(unSelected)
    #     epi_sum2[0,i] = sum(np.squeeze(np.multiply(isItem_map2[i].reshape(1, len(isItem_map2[i])), overall_item_value[i].reshape(1,len(overall_item_value[i])))))
    #     epi_ratio_sum[1,i] = epi_sum2[0,i]/sum(overall_item_value[i])
    #     # print(np.multiply(isItem_map[i].reshape(1, len(isItem_map[i])), overall_item_value[i].reshape(1,len(overall_item_value[i]))))        

    # with open(result3,'rb') as f:
    #     result_data3 = pickle.load(f)
    # last_state3 = np.array(result_data3.get('last_state'))
    # last_state3 = np.squeeze(last_state3)
    # isItem_map3 = np.zeros((epi_len,item_size))
    # isItem_unmap3 = np.zeros((epi_len,item_size))
    # epi_sum3 = np.zeros((1,epi_len))
    # for i in range(epi_len):
    
    #     isItem_map3[i,:] = np.add(isItem_map3[i,:], last_state3[i])
    #     unSelected = np.nonzero(isItem_map3[i] == 0 )[0]
    #     isItem_unmap2[i,unSelected] = 1
    
    #     # print(unSelected)
    #     epi_sum3[0,i] = sum(np.squeeze(np.multiply(isItem_map3[i].reshape(1, len(isItem_map3[i])), overall_item_value[i].reshape(1,len(overall_item_value[i])))))
    #     epi_ratio_sum[2,i] = epi_sum3[0,i]/sum(overall_item_value[i])
        # print(np.multiply(isItem_map[i].reshape(1, len(isItem_map[i])), overall_item_value[i].reshape(1,len(overall_item_value[i]))))        
    x = np.arange(n)
    x = x*1 + 1
    print(epi_ratio_sum[1].mean())
    ran_ratio[0,k] = epi_ratio_sum[1].mean()
    ffd_ratio[0,k] = epi_ratio_sum[0].mean()
    pro_ratio[0,k] = epi_ratio_sum[2].mean()
# plt.bar(x, np.squeeze(epi_sum), color='blue')
# plt.bar(x,np.squeeze(epi_sum2), color='red')
# print("random", ran_ratio.mean())
# print("greedy", ffd_ratio.mean())
# print("proposed_0*10~99*10",dqn_ratio.mean())
plt.plot(x,np.squeeze(ran_ratio), color='red', marker= 'o', label='random')
plt.plot(x,np.squeeze(ffd_ratio), color='orange',  marker= 'o',label='ffd')
plt.plot(x,np.squeeze(pro_ratio), color='blue',  marker= 'o',label='a3c (0.0001)')
# plt.plot(x,np.squeeze(dqn_ratio), color='sky',  marker= 'o',label='a2c_agregated aggre_test(0.0001)')
plt.title('50 items RI')
plt.xlabel('Number of knapsacks')
plt.ylabel('Averate map ratio of values')
plt.ylim(0.0,1)
plt.xlim(0.5,5.5)
plt.xticks(np.arange(0, 6, step=1))
plt.legend(loc=0)
plt.savefig('50_RI.eps', format='eps')
# plt.xticks(x, years)

plt.show