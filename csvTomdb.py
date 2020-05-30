import pypyodbc
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
#Ruta ficheros
ruta_fichero_access='C:\\Users\\34637\\Documents\\BD_2019.accdb'
ruta_fichero_txt="C:\\Users\\34637\\Desktop\\fichero_txt_a_mdb\\fichero.TXT"

#Programa
dbname = ruta_fichero_access
constr = "DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={0};".format(dbname)
#Conectamos con bd access
dbconn = pypyodbc.connect(constr)
cur = dbconn.cursor()

#Preparamos SQL
sql = 'INSERT INTO BASE_DATOS_MAYOR VALUES ( ? , ?, ?, ?, ?, ?, ?, ?, ?)'
f = open(ruta_fichero_txt, "r")
lines = f.readlines()[1:-1]
for x in lines:
   params = (
    x[indice_inicial_campo_1:indice_final_campo_1],
   x[indice_inicial_campo_2:indice_final_campo_2],
   x[indice_inicial_campo_3:indice_final_campo_3],
   x[indice_inicial_campo_4:indice_final_campo_4],
   x[indice_inicial_campo_5:indice_final_campo_5],
   x[indice_inicial_campo_6:indice_final_campo_6],
   x[indice_inicial_campo_7:indice_final_campo_7],
   x[indice_inicial_campo_8:indice_final_campo_8],
   x[indice_inicial_campo_9:indice_final_campo_9]
   )
   cur.execute(sql, params)
   dbconn.commit()
f.close()
dbconn.close()
cur.close()