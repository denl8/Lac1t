##1
#spisok=[1,2,4,6,7,8,85,8,5,4,42,False,25,686,9]
#i=0
#while i<len(spisok):
#    if spisok[i]%2==0 :
#        print(spisok[i])
#    i+=1



##2
#spisok=[1,2,4,6,7,8,'Lacit',85,8,5,4,42,False,25,686,9]
#i=0
#while i<len(spisok):
#    print(spisok[i*2])
#    i+=1



##3
#spisok=[1,2,-4,6,-7,8,-85,8,5,4,-42,False,25,-686,9]
#i=0
#while i<len(spisok):
#    if spisok[i]>0 :
#        print(spisok[i])
#    i+=1



##4
# input_list=[1,3,4,7,23,42,765,45,9]
# m=int(input())
# i=0
# mod_list=list({input_list[i]%m for i in range(len(input_list))})
# result_list=[]
# for i in range(len(mod_list)):
    # result_list.append(set())
# for i in range(len(input_list)):
    # result_list[mod_list.index(input_list[i]%m)].add(input_list[i])
# print(result_list)



##5
# dict1={1:12,3.3:43,2:'lacit',5:7.32, 'lacit':123}
# keys_list=list(dict1.keys())
# values_list=list(dict1.values())
# i=0
# summ=0
# summ2=0
# for i in range(len(dict1)):
    # if (type(keys_list[i]) == int) or (type(keys_list[i]) == float) :
        # summ+=keys_list[i]
        # i+=1
# i=0
# for i in range(len(dict1)):
    # if type(values_list[i]) == int or (type(values_list[i]) == float):
        # summ2+=values_list[i]
        # i+=1
# print([summ, summ2])



##6
# list1=[1,3,5,7,7,5,3,8]
# set1=set(list1)
# list1=list(set1)
# list1.sort()
# list2=[]
# i=0
# while i < (len(list1)-1):
    # j=1+i
    # while j < (len(list1)):
        # list2.append(tuple([list1[i],list1[j]]))
        # j+=1
    # i+=1
# print(list2)



##7
# list1=[1,12,3.3,43,2,'lacit',5,7.32,'lacit',123]
# i=0
# dictionary={}
# while i<len(list1):
    # dictionary[list1[i]]=list1[i+1]
    # i+=2
# print(dictionary)
