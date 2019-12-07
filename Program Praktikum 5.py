Data = {}
while True:
    print("")  
    enter = input("[ (L)ook, (A)dd, (E)dit, (D)elete, (S)earch , (Q)uit ]: ")
    if enter.lower() == 'q' :
        break
    elif enter.lower() == 'l' :
        print ("===========================Data Nilai Mahasiswa=========================")
        print ("========================================================================")
        print (" | No |   Nama   |    NIM    |    Kelas   |Tugas| UTS | UAS  |  Akhir  |")
        print ("========================================================================")
        i=0
        for x in Data.items():
            i+=1
            print (" | {7:2} |  {0:7s} | {1:9} | {2:10} | {3:3d} | {4:3d} | {5:4d} | {6:7.2f} |"\
                   .format(x[0],x[1][0],x[1][1],x[1][2],x[1][3],x[1][4],x[1][5],i))
        print ("========================================================================")
    elif enter.lower() == 'a':
        print ()
        print ("==========Tambahkan Data==========")
        print ()
        Nama        = input ("Nama        : ")
        NIM         = input ("NIM         : ")
        Kelas       = input ("Kelas       : ")
        Nilai_Tugas = int(input ("Nilai Tugas : "))
        Nilai_UTS   = int(input ("Nilai UTS   : "))
        Nilai_UAS   = int(input ("Nilai UAS   : "))
        Nilai_Akhir = float(((Nilai_Tugas)*30/100 + (Nilai_UTS)*35/100 + (Nilai_UAS)*35/100))
        Data[Nama] = NIM,Kelas,Nilai_Tugas,Nilai_UTS,Nilai_UAS,Nilai_Akhir
        print ("==================================")
    elif enter.lower() == 'e':
        print ()
        print ("=====Edit Data Nilai Mahasiswa=====")
        print ()
        Nama = input ("Nama        : ")
        if  Nama in Data.keys():
            NIM         = input ("NIM         : ") 
            Kelas       = input ("Kelas       : ")
            Nilai_Tugas = int(input ("Nilai Tugas : "))
            Nilai_UTS   = int(input ("Nilai UTS   : "))
            Nilai_UAS   = int(input ("Nilai UAS   : "))
            Nilai_Akhir = float(((Nilai_Tugas)*30/100 + (Nilai_UTS)*35/100 + (Nilai_UAS)*35/100))
            Data[Nama] = NIM,Kelas,Nilai_Tugas,Nilai_UTS,Nilai_UAS,Nilai_Akhir
        else:
                print ("Data Nilai Mahasiswa {0} TIDAK ADA". format(Nama))
        print ("===================================")
    elif enter.lower() == 'd':
        print ()
        print ("=====Hapus Data Nilai Mahasiswa=====")
        print ()
        Nama = input ("Nama : ")
        if Nama in Data.keys():
            del Data[Nama]
        else:
                print ("Data Mahasiswa {0} TIDAK ADA".format(Nama))
        print ("====================================")
    elif enter.lower() == 's':
        print ()
        print ("====Mencari Data Nilai Mahasiswa====")
        print ()
        Nama = input ("Nama : ")
        if Nama in Data.keys():
            print (" Data Mahasiswa {0} adalah {1}"\
                   .format(Nama, Data [Nama]))
        else:
                print ("Data Mahasiswa {0} TIDAK ADA".format(Nama))
        print ("===================================")
    else:
            print("Pilih Menu yang Tersedia")
                    
                           
