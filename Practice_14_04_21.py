import random
list_1 = ['ball','мессенджер', 'triangle']
empty_list=[]
list_2=list(list_1[random.randint(0,len(list_1)-1)])
word=(''.join(list_2))
#print(word)
i=0
while i<10 and list_2!=empty_list:
    a=input()
    if a in list_2:
        #print("yes")
        while a in list_2:
        	list_2.remove(a)
    else:
        #print("no")
        i+=1
        if i==1:
            print("│\n"*7+"┴")
        elif i==2:
            print("┌─────┐\n"+"|\n"*6+"┴")
        elif i==3:
            print("┌─┬───┐\n"+"|/\n"+"|\n"*5+"┴")
        elif i==4:
            print("┌─┬───┐\n"+"|/    |\n"+"|     |\n"+"|\n"*4+"┴")
        elif i==5:
            print("┌─┬───┐\n"+"|/    |\n"+"|     |\n"+"|     0\n"+"|\n"*3+"┴")
        elif i==6:
            print("┌─┬───┐\n"+"|/    |\n"+"|     |\n"+"|     0\n"+"|     |\n"+"|\n"*2+"┴")
        elif i==7:
            print("┌─┬───┐\n"+"|/    |\n"+"|     |\n"+"|     0\n"+"|    /| \n"+"|\n"*2+"┴")
        elif i==8:
            print("┌─┬───┐\n"+"|/    |\n"+"|     |\n"+"|     0\n"+"|    /|\ \n"+"|\n"*2+"┴")
        elif i==9:
            print("┌─┬───┐\n"+"|/    |\n"+"|     |\n"+"|     0\n"+"|    /|\ \n"+"|     | \n"+"|\n"+"┴")
        elif i==10:
            print("┌─┬───┐\n"+"|/    |\n"+"|     |\n"+"|     0\n"+"|    /|\ \n"+"|     ║ \n"+"|\n"+"┴\n"+"\nВы проиграли!\n")
if i<10 and list_2==empty_list:
    print("\nВы угадали слово: "+word)
