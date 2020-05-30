#indices campo 1
indice_inicial_campo_1=0
indice_final_campo_1=13
#indices campo 2
indice_inicial_campo_2=13
indice_final_campo_2=17
#indices campo 3
indice_inicial_campo_3=17
indice_final_campo_3=41
#indices campo 4
indice_inicial_campo_4=41
indice_final_campo_4=85
#indices campo 5
indice_inicial_campo_5=85
indice_final_campo_5=130
#indices campo 6
indice_inicial_campo_6=130
indice_final_campo_6=150
#indices campo 7
indice_inicial_campo_7=150
indice_final_campo_7=170
#indices campo 8
indice_inicial_campo_8=170
indice_final_campo_8=190
#indices campo 9
indice_inicial_campo_9=190
indice_final_campo_9=210


f = open("C:\\Users\\34637\\Desktop\\fichero_txt_a_mdb\\fichero1.TXT", "r")
lines = f.readlines()[1:-1]
for x in lines:

  print(len(x[indice_inicial_campo_1:indice_final_campo_1]))
  print(len(x[indice_inicial_campo_2:indice_final_campo_2]))
  print(len(x[indice_inicial_campo_3:indice_final_campo_3]))
  print(len(x[indice_inicial_campo_4:indice_final_campo_4]))
  print(len(x[indice_inicial_campo_5:indice_final_campo_5]))
  print(len(x[indice_inicial_campo_6:indice_final_campo_6]))
  print(len(x[indice_inicial_campo_7:indice_final_campo_7]))
  print(len(x[indice_inicial_campo_8:indice_final_campo_8]))
  print(len(x[indice_inicial_campo_9:indice_final_campo_9]))
f.close()



f.close()

