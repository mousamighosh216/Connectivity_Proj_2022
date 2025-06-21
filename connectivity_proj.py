#download 1.matplotlib.pyplot (py -m pip install matplotlib)
#2.tabulate (pip install tabulate)
#3.insert required tables in sql
#4.Admin password =2116
#5.playsound (pip install playsound==1.2.2)


def ch():
    print("x"*167)
    print("*****WELCOME TO AIRPORT MANAGEMENT SYSTEM*****".center(167))
    print("x"*167)
    print("*****Branch Madhya Pradesh*****".center(167))
    print("1.Admin".center(167))
    print("2.Passenger".center(167))
    print("3.Exit".center(167))
    choice=int(input("Enter your choice:"))
    if choice==1:
        from datetime import datetime 
        file=open("Name.txt","a+")
        admin=input("Enter Username:")
        name=str(admin)
        me=str(datetime.now())
        file.write(name+","+me+'\n')
        file.close()
        passwd=str(input("Enter your password:"))
        if passwd in [ '2116' ]:
            print("\nWelcome",admin,"To The Management System!!\n")
            airwaymenu()
        else:
            print("\nSorry!!! Wrong Password\n")
    elif choice==2:
        pass_det()
    elif choice==3:
        return
    else:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nInvalid Entry!!!\n")




def airwaymenu():
    print("x"*167)
    print("*****Plane/Flight Details*****".center(167))
    print("x"*167)
    print("1.Plane Details".center(167))
    print("2.Flight Details".center(167))
    print("3.Exit(For Back)".center(167))
    choice = int(input("Enter your choice:"))
    if choice == 1:
        pln_det()
    elif choice == 2:
        flt_det()
    elif choice == 3:
        print("\nExit...\n")
        ch()
    else:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nWrong Input!!!\n")
        airwaymenu()




def pln_det():
    print("="*167)
    print("*****Plane Details*****".center(167))
    print("="*167)
    print("1.Insert Plane Details".center(167))
    print("2.Update Plane Details".center(167))
    print("3.Delete Details".center(167))
    print("4.Analysis".center(167))
    print("5.Exit(For Back)".center(167))
    choice = int(input("Enter your choice:"))
    if choice == 1:
        inst_det()
    elif choice == 2:
        update_det()
    elif choice == 3:
        del_det()
    elif choice == 4:
        ana_ly()
    elif choice == 5:
        print("\nExit...\n")
        airwaymenu()
    else:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nWrong Input!!!\n")
        pln_det()




def ana_ly():
    print("*"*167)
    print("*****Analysis*****".center(167))
    print("*"*167)
    print("1.Graphical Representation of Distinct Manufacturers".center(167))
    print("2.Display Plane Details".center(167))
    print("3.Exit(For Back)".center(167))
    choice=int(input("Enter your choice:"))
    if choice == 1:
        gr_rp()
    elif choice == 2:
        tab_pln()
    elif choice == 3:
        print("\nExit...\n")
        pln_det()
    else:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nWrong Input!!!\n")
        ana_ly()



        
def inst_det():
    import mysql.connector
    try:
        mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
        mycursor = mydb.cursor()
        plid=int(input("Enter PlaneID:"))
        maf=input("Enter the Manufacturer:")
        modnm=str(input("Enter Model Name:"))
        pdt=str(input("Enter Purchase Date(YYYY-MM-DD):"))
        lst=str(input("Enter Last Service Date(YYYY-MM-DD):"))
        anm=input("Enter Airline Name:")
        query="insert into PlaneDetails values({},'{}','{}','{}','{}','{}')".format(plid,maf,modnm,pdt,lst,anm)
        mycursor.execute(query)
        mydb.commit()
        print('\n')
        print("Insertion Successful!!!")
        print('\n')
        pln_det()
    except:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nInvalid Input!!!\n")
        pln_det()



        
def update_det():
    import mysql.connector
    print("*"*167)
    print("*****Update Details*****".center(167))
    print("*"*167)
    print("1.Update Manufacturer".center(167))
    print("2.Update Model Name".center(167))
    print("3.Update Purchase Date".center(167))
    print("4.Update Last Service Date".center(167))
    print("5.Update Airline Name".center(167))
    print("6.Exit(For Back)".center(167))
    choice=int(input("Enter your choice:"))
   
    if choice == 1:
        try:
            mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
            mycursor = mydb.cursor()
            plid=int(input("Enter PlaneID:"))
            maf=input("Enter the Manufacturer:")
            query="update PlaneDetails set manufacturer='{}' where PlaneID={}".format(maf,plid)
            mycursor.execute(query)
            mydb.commit()
            mydb.close()
            mycursor.close()
            print('\n')
            print("Table Updated!!!")
            print('\n')
            pln_det()
        except:
            import winsound
            freq=2500
            time=1000
            winsound.Beep(freq,time)
            print("\nWrong Input!!!\n")
            update_det()
                
    elif choice == 2:
        try:
            mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
            mycursor = mydb.cursor()
            plid=int(input("Enter PlaneID:"))
            modnm=str(input("Enter Model Name:"))
            query="update PlaneDetails set modelname='{}' where PlaneID={}".format(modnm,plid)
            mycursor.execute(query)
            mydb.commit()
            mydb.close()
            mycursor.close()
            print('\n')
            print("Table Updated!!!")
            print('\n')
            pln_det()
        except:
            import winsound
            freq=2500
            time=1000
            winsound.Beep(freq,time)
            print("\nWrong Input!!!\n")
            update_det()
       
    elif choice == 3:
        try:
            mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
            mycursor = mydb.cursor()
            plid=int(input("Enter PlaneID:"))
            pdt=str(input("Enter Purchase Date(YYYY-MM-DD):"))
            query="update PlaneDetails set OriginalPurchaseDate='{}' where PlaneID={}".format(pdt,plid)
            mycursor.execute(query)
            mydb.commit()
            mydb.close()
            mycursor.close()
            print('\n')
            print("Table Updated!!!")
            print('\n')
            pln_det()
        except:
            import winsound
            freq=2500
            time=1000
            winsound.Beep(freq,time)
            print("\nWrong Input!!!\n")
            update_det()
            
    elif choice == 4:
        try:
            mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
            mycursor = mydb.cursor()
            plid=int(input("Enter PlaneID:"))
            lst=str(input("Enter Last Service Date(YYYY-MM-DD):"))
            query="update PlaneDetails set LastServiceDate='{}' where PlaneID={}".format(lst,plid)
            mycursor.execute(query)
            mydb.commit()
            mydb.close()
            mycursor.close()
            print('\n')
            print("Table Updated!!!")
            print('\n')
            pln_det()
        except:
            import winsound
            freq=2500
            time=1000
            winsound.Beep(freq,time)
            print("\nWrong Input!!!\n")
            update_det()
    elif choice == 5:
        try:
            mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
            mycursor = mydb.cursor()
            anm=input("Enter Airline Name:")
            plid=int(input("Enter PlaneID:"))
            query="update PlaneDetails set AirlineName='{}' where PlaneID={}".format(anm,plid)
            mycursor.execute(query)
            mydb.commit()
            mydb.close()
            mycursor.close()
            print('\n')
            print("Table Updated!!!")
            print('\n')
            pln_det()
        except:
            import winsound
            freq=2500
            time=1000
            winsound.Beep(freq,time)
            print("\nWrong Input!!!\n")
            update_det()
    elif choice == 6:
        print("\nExit...\n")
        pln_det()
    else:
        print("\nInvalid Input!!!\n")
        update_det()



        
def del_det():
    try:
        import mysql.connector
        mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
        mycursor = mydb.cursor()
        plid=int(input("Enter PlaneID:"))
        query="delete from PlaneDetails where PlaneID={}".format(plid)
        mycursor.execute(query)
        mydb.commit()
        mydb.close()
        mycursor.close()
        print('\n')
        print("Details Deleted!!!")
        print('\n')
        pln_det()
    except:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nWrong Input!!!\n")
        pln_det()




def gr_rp():
    import mysql.connector
    import matplotlib.pyplot
    mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
    mycursor = mydb.cursor()
    mycursor.execute("select Distinct Manufacturer from PlaneDetails")
    dat=mycursor.fetchall()
    cl=[]
    for row in dat:
        cl.extend(row)
    print("Distinct Manufacturers:",cl)
    mycursor.execute("select count(Manufacturer) from PlaneDetails group by Manufacturer")
    dat=mycursor.fetchall()
    nos=[]
    for row in dat:
        nos.extend(row)
    print("No. of Distinct Manufacturers:",nos)

    print(matplotlib.pyplot.pie(nos,labels=cl,autopct="%1.1f%%"))
    matplotlib.pyplot.show()
    ana_ly()




def tab_pln():
    import mysql.connector
    from tabulate import tabulate
    db=mysql.connector.connect(host="localhost",user ="root", password="mou216",
                                         database="mou")
   
    if db.is_connected():
        cursor=db.cursor()
        cursor.execute("select * from PlaneDetails")
        results=cursor.fetchall()
      
        h=['PlaneID','Manufacturer','ModelName','OriginalPurchaseDate','LastServiceDate','AirlineName']
        print(tabulate(results,headers=h,tablefmt="fancy_grid"))
        ana_ly()
    else:
        print("\nError!! Unable to fetch data\n")
        ana_ly()




def flt_det():
    print("="*167)
    print("*****Flight Details*****".center(167))
    print("="*167)
    print("1.Insert Flight Details".center(167))
    print("2.Update Flight Details".center(167))
    print("3.Delete Details".center(167))
    print("4.Analysis".center(167))
    print("5.Exit(For Back)".center(167))
    
    choice = int(input("Enter your choice:"))
    if choice == 1:
        ins_det()
    elif choice == 2:
        upt_det()
    elif choice == 3:
        dl_det()
   
    elif choice == 4:
        analy()
    elif choice == 5:
        print("\nExit...\n")
        airwaymenu()
    else:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nInvalid Input!!!\n")
        flt_det()




def analy():
    print("*"*167)
    print("*****Analysis*****".center(167))
    print("*"*167)
    print("1.Graphical Representation of Distinct Airline".center(167))
    print("2.Display FlightDetails".center(167))
    print("3.Display PassengerDetails".center(167))
    print("4.Exit(For Back)".center(167))
    choice=int(input("Enter your choice:"))
    if choice == 1:
        grp_rep()
    elif choice == 2:
        tab_fli()
    elif choice == 3:
        dis_det()
    elif choice == 4:
        print("\nExit...\n")
        flt_det()
    else:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nWrong Input!!!\n")
        analy()


    

def ins_det():
    import mysql.connector
    try:
        mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
        mycursor = mydb.cursor()
        
        fid=int(input("Enter FlightID:"))
        pid=int(input("Enter PlaneID:"))
        anm=input("Enter Airline Name:")
        cd=input("Enter AirportCodeOfDeparture:")
        aar=input("Enter AirportCodeOfArrival:")
        dd=str(input("Enter DepartureDateTime(YYYY-MM-DD HH:MM:SS):"))
        at=str(input("Enter ArrivalDateTime(YYYY-MM-DD HH:MM:SS):"))
        yt=int(input("Enter TicketPrice(in Rupees):"))
        query="insert into FlightDetails values({},{},'{}','{}','{}','{}','{}',{})".format(fid,pid,anm,cd,aar,dd,at,yt)
        mycursor.execute(query)
        mydb.commit()
        print('\n')
        print("Insertion Successful!!!")
        print('\n')
        flt_det()
    except:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nInvalid Entry!!!\n")
        flt_det()




def upt_det():
    import mysql.connector
    print("*"*167)
    print("*****Update Details*****".center(167))
    print("*"*167)
    print("1.Update PlaneID".center(167))
    print("2.Update AirlineName".center(167))
    print("3.Update AirportCodeOfDeparture".center(167))
    print("4.Update AirportCodeOfArrival".center(167))
    print("5.Update DepartureDateTime".center(167))
    print("6.Update ArrivalDateTime".center(167))
    print("7.Update TicketPrice".center(167))
    print("8.Exit(For Back)".center(167))
   
    choice=int(input("Enter your choice:"))
    if choice == 1:
        try:
            mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
            mycursor = mydb.cursor()
            fid=int(input("Enter FlightID:"))
            pid=int(input("Enter PlaneID:"))
            query="update FlightDetails set PlaneID={} where FlightID={}".format(fid,pid)
            mycursor.execute(query)
            mydb.commit()
            mydb.close()
            mycursor.close()
            print('\n')
            print("Table Updated!!!")
            print('\n')
            flt_det()
        except:
            import winsound
            freq=2500
            time=1000
            winsound.Beep(freq,time)
            print("\nWrong Input!!!\n")
            flt_det()
    elif choice == 2:
        try:
            mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
            mycursor = mydb.cursor()
            anm=input("Enter Airline Name:")
            fid=int(input("Enter FlightID:"))
            query="update FlightDetails set AirlineName='{}' where FlightID={}".format(anm,fid)
            mycursor.execute(query)
            mydb.commit()
            mydb.close()
            mycursor.close()
            print('\n')
            print("Table Updated!!!")
            print('\n')
            flt_det()
        except:
            import winsound
            freq=2500
            time=1000
            winsound.Beep(freq,time)
            print("\nWrong Input!!!\n")
            flt_det()
    elif choice == 3:
        try:
            mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
            mycursor = mydb.cursor()
            cd=input("Enter AirportCodeOfDeparture:")
            fid=int(input("Enter FlightID:"))
            query="update FlightDetails set AirportCodeOfDeparture='{}' where FlightID={}".format(cd,fid)
            mycursor.execute(query)
            mydb.commit()
            mydb.close()
            mycursor.close()
            print('\n')
            print("Table Updated!!!")
            print('\n')
            flt_det()
        except:
            import winsound
            freq=2500
            time=1000
            winsound.Beep(freq,time)
            print("\nWrong Input!!!\n")
            flt_det()
    elif choice == 4:
        try:
            mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
            mycursor = mydb.cursor()
            cd=input("Enter AirportCodeOfArrival:")
            fid=int(input("Enter FlightID:"))
            query="update FlightDetails set AirportCodeOfArrival='{}' where FlightID={}".format(cd,fid)
            mycursor.execute(query)
            mydb.commit()
            mydb.close()
            mycursor.close()
            print('\n')
            print("Table Updated!!!")
            print('\n')
            flt_det()
        except:
            import winsound
            freq=2500
            time=1000
            winsound.Beep(freq,time)
            print("\nWrong Input!!!\n")
            flt_det()
    elif choice == 5:
        try:
            mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
            mycursor = mydb.cursor()
            cd=input("Enter DepartureDateTime(YYYY-MM-DD HH:MM:SS):")
            fid=int(input("Enter FlightID:"))
            query="update FlightDetails set DepartureDateTime='{}' where FlightID={}".format(cd,fid)
            mycursor.execute(query)
            mydb.commit()
            mydb.close()
            mycursor.close()
            print('\n')
            print("Table Updated!!!")
            print('\n')
            flt_det()
        except:
            import winsound
            freq=2500
            time=1000
            winsound.Beep(freq,time)
            print("\nWrong Input!!!\n")
            flt_det()
    elif choice == 6:
        try:
            mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
            mycursor = mydb.cursor()
            cd=input("Enter ArrivalDateTime(YYYY-MM-DD HH:MM:SS):")
            fid=int(input("Enter FlightID:"))
            query="update FlightDetails set ArrivalDateTime='{}' where FlightID={}".format(cd,fid)
            mycursor.execute(query)
            mydb.commit()
            mydb.close()
            mycursor.close()
            print('\n')
            print("Table Updated!!!")
            print('\n')
            flt_det()
        except:
            import winsound
            freq=2500
            time=1000
            winsound.Beep(freq,time)
            print("\nWrong Input!!!\n")
            flt_det()
    elif choice == 7:
        try:
            mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
            mycursor = mydb.cursor()
            cd=input("Enter TicketPrice(in Rupees):")
            fid=int(input("Enter FlightID:"))
            query="update FlightDetails set TicketPrice={} where FlightID={}".format(cd,fid)
            mycursor.execute(query)
            mydb.commit()
            mydb.close()
            mycursor.close()
            print('\n')
            print("Table Updated!!!")
            print('\n')
            flt_det()
        except:
            import winsound
            freq=2500
            time=1000
            winsound.Beep(freq,time)
            print("\nWrong Input!!!\n")
            flt_det()
    elif choice == 8:
        print("\nExit...\n")
        flt_det()
    else:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nInvalid Input!!!\n")
        upt_det()





def dl_det():
    try:
        import mysql.connector
        mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
        mycursor = mydb.cursor()
        plid=int(input("Enter FlightID:"))
        query="delete from FlightDetails where FlightID={}".format(plid)
        mycursor.execute(query)
        mydb.commit()
        mydb.close()
        mycursor.close()
        print('\n')
        print("Details Deleted!!!")
        print('\n')
        flt_det()
    except:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nWrong Input!!!\n")
        flt_det()




        
def grp_rep():
    import mysql.connector
    import matplotlib.pyplot
    mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
    mycursor = mydb.cursor()
    mycursor.execute("select Distinct AirlineName from FlightDetails")
    dat=mycursor.fetchall()
    cl=[]
    for row in dat:
        cl.extend(row)
    print("Distinct AirlineName:",cl)
    mycursor.execute("select count(AirlineName) from FlightDetails group by AirlineName")
    dat=mycursor.fetchall()
    nos=[]
    for row in dat:
        nos.extend(row)
    print("No. of Distinct Manufacturers:",nos)

    print(matplotlib.pyplot.pie(nos,labels=cl,autopct="%1.3f%%"))
    matplotlib.pyplot.show()
    analy()




def dis_det():
    import mysql.connector
    from tabulate import tabulate
    db=mysql.connector.connect(host="localhost",user ="root", password="mou216",
                                         database="mou")
    
    if db.is_connected():
        cursor=db.cursor()
        cursor.execute("select p.passid,p.flightid,f.planeid,p.name,p.age,p.sex,f.airlinename,f.AirportCodeOfDeparture,f.AirportCodeOfArrival,f.DepartureDateTime,f.ArrivalDateTime from PassengerDetails P,FlightDetails F where P.FlightID = F.FlightID")
        results=cursor.fetchall()
        
        h=['PassID','FlightID','PlaneID','Name','Age','Sex','AirlineName','Departure','Arrival','DepartureDateTime','ArrivalDateTime']
        print(tabulate(results,headers=h,tablefmt="fancy_grid"))
        analy()
    else:
        print("\nError!! Unable to fetch data\n")
        analy()




def tab_fli():
    import mysql.connector
    from tabulate import tabulate
    db=mysql.connector.connect(host="localhost",user ="root", password="mou216",
                                         database="mou")
    
    if db.is_connected():
        cursor=db.cursor()
        cursor.execute("select * from FlightDetails")
        results=cursor.fetchall()
        
        h=['FlightID','PlaneID','AirlineName','AirportCodeOfDeparture','AirportCodeOfArrival','DepartureDateTime','ArrivalDateTime','TicketPrice']
        print(tabulate(results,headers=h,tablefmt="fancy_grid"))
        analy()
    else:
        print("\nError!! Unable to fetch data\n")
        analy()




def pass_det():
    
    print("x"*167)
    print("*****Flight Booking*****".center(167))
    print("x"*167)
    print("1.Know about Flight Details".center(167))
    print("2.Reservation of Ticket".center(167))
    print("3.Cancellation of Ticket".center(167))
    print("4.Display ticket Details".center(167))
    print("5.Exit(For Back)".center(167))
    
    choice=int(input("Enter your choice:"))
    if choice == 1:
        tabf()
    elif choice == 2:
        res_tic()
    elif choice == 3:
        can_tic()
    elif choice == 4:
        disp_det()
    elif choice == 5:
        print("\nExit...\n")
        ch()
    else:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nWrong Input!!!\n")
        pass_det()





def tabf():
    import mysql.connector
    from tabulate import tabulate
    db=mysql.connector.connect(host="localhost",user ="root", password="mou216",
                                         database="mou")
  
    print("\n NOTICE!!! \n ~Economy Class (TicketPrice) \n ~Business Class (TicketPrice + 20%) \n ~First Class (TicketPrice + 40%)\n")
    if db.is_connected():
        cursor=db.cursor()
        cursor.execute("select * from FlightDetails")
        results=cursor.fetchall()
       
        h=['FlightID','PlaneID','AirlineName','AirportCodeOfDeparture','AirportCodeOfArrival','DepartureDateTime','ArrivalDateTime','TicketPrice']
        print(tabulate(results,headers=h,tablefmt="fancy_grid"))
        pass_det()
    else:
        print("\nError!! Unable to fetch data\n")
        pass_det()



        
def res_tic():
    import mysql.connector
    from pay import p
    from pay import q
    from pay import r
    from datetime import datetime
    try:
        mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
        mycursor = mydb.cursor()
        sn=int(input("Enter PassID:"))
        fid=int(input("Enter FlightID:"))
        pid=input("Enter Name of the Passenger:")
        anm=input("Enter Age:")
        cd=input("Enter Gender(F/M):")
        pp=input("Enter Class:")
        query="insert into PassengerDetails values({},{},'{}','{}','{}','{}')".format(sn,fid,pid,anm,cd,pp)
        mycursor.execute(query)
        mydb.commit()
        print('\n')
        print("*"*167)
        print("*****Amount Payable*****".center(167))
        print("*"*167)
        if pp in ["Economy","ECONOMY","economy"] :
            p()
        elif pp in ["Business","BUSINESS","business"] :
            r()
        elif pp in ["First","FIRST","first"] :
            q()
        else:
            import winsound
            freq=2500
            time=1000
            winsound.Beep(freq,time)
            print("Wrong Input!!!")
        print('\n')
        paym() 
        pass_det() 
    except:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nInvalid Entry!!!\n")
        pass_det()



    
def paym():
    import random
    from datetime import datetime
    print("*"*21)
    print("*****Transaction*****")
    print("*"*21)
    print("1.Manually \nNote!!!\nCan be done only by the admin.\n")
    print("2.Online\n")
    print("3.Exit(For Back)")
    ch=int(input("Enter your choice:"))
    if ch ==1:
        pas=str(input("Enter Admin Password:"))
        if pas == '2116':
            print('\n')
            print("Entry Accepted. \nTransaction Procceded!!")
            print('\n')
            print("Booking Successful!!! at",datetime.now())
            print("~~~THANK-YOU FOR USING OUR MANAGEMENT SYSTEM~~~".center(167))
            from playsound import playsound
            playsound("C:\\Users\\Mousami Ghosh\\Downloads\\audio.mp3")
            print('\n')
            pass_det()
        else:
            import winsound
            freq=2500
            time=1000
            winsound.Beep(freq,time)
            print("\nEntry Denied.\n")
            paym()
    elif ch == 2:
        print("Where do want to receive your OTP?")
        print("1.At your email")
        print("2.On your linked Bank Account No.")
        print("3.Exit")
        t=int(input("Enter your choice:"))
        
        if t == 1.:
            import random
            import smtplib
            from datetime import datetime
            y = random.randrange(10000,100000)
            r= "Your OTP is "+str(y)
            ser=smtplib.SMTP("smtp.gmail.com",587)
            ser.starttls()
            ser.login('satakshion@gmail.com','zmonukxuupltmnup')
            g=str(input("Enter you mail:"))
            ser.sendmail("satakshion@gmail.com",str(g),r)
            ser.quit()
            typeOTP= int(input("Type Your Otp:"))
            if y == typeOTP: 
                print("\nPayment Received. \nTransaction Successfull!!!\n")
                print("\nBooking Successful!!! at",datetime.now())
                print("~~~THANK-YOU FOR USING OUR MANAGEMENT SYSTEM~~~".center(167))
                from playsound import playsound
                playsound("C:\\Users\\Mousami Ghosh\\Downloads\\audio.mp3")
            else:
                import winsound
                freq=2500
                time=1000
                winsound.Beep(freq,time)
                print("\nWrong OTP Entered!!!\n")
                print('\n')
        elif t == 2:
            ty=str(input("Type your Bank Account No.(Ex: xxxx-xxxx-xxxx):"))
            y=random.randrange(100000,1000000)
            print("------------------------------------------------")
            print("\nYour OTP is:",y)
            print("OTP has been sent!!\n")
            print("------------------------------------------------")
            typeOTP= int(input("Type Your Otp:"))
            if y==typeOTP:
                print("\nPayment Received. \nTransaction Successfull!!!\n")
                print("\nBooking Successful!!! at",datetime.now())
                print("~~~THANK-YOU FOR USING OUR MANAGEMENT SYSTEM~~~".center(167))
                from playsound import playsound
                playsound("C:\\Users\\Mousami Ghosh\\Downloads\\audio.mp3")
            
                print('\n')
            else:
                import winsound
                freq=2500
                time=1000
                winsound.Beep(freq,time)
                print("\nWrong OTP Entered!!!\n")
        elif t==3:
            print("\nExit..\n")
            print("Reservation Unsuccessful!!")
            paym()
    elif ch ==3:
        print("\nExit..\n")
        pass_det()
    else:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nWrong Input!!!\n")
        pass_det()



                
def can_tic():
    try:
        import mysql.connector
        from datetime import datetime
        mydb = mysql.connector.connect(host = "LocalHost",
                                 user = "root",
                                passwd = "mou216",
                                 database = "mou")
        mycursor = mydb.cursor()
        plid=int(input("Enter PassID:"))
        query="delete from PassengerDetails where PassID={}".format(plid)
        mycursor.execute(query)
        mydb.commit()
        mydb.close()
        mycursor.close()
        print('\n')
        print("Booking Cancelled!!! at",datetime.now())
        print("\nNote!!\nIt may take 1-2 working days to generate refund....")
        print('\n')
        pass_det()
    except:
        import winsound
        freq=2500
        time=1000
        winsound.Beep(freq,time)
        print("\nWrong Input!!!\n")
        pass_det()




def disp_det():
    import mysql.connector
    from tabulate import tabulate
    db=mysql.connector.connect(host="localhost",user ="root", password="mou216",
                                         database="mou")
    #cursor =db.cursor()
    if db.is_connected():
        con= mysql.connector.connect(host="localhost",user="root",passwd="mou216",database="mou")
        cursor=con.cursor()
        fid=str(input("Enter PassID:"))
        query="select p.passid,p.flightid,f.planeid,p.name,f.airlinename,p.class,f.AirportCodeOfDeparture,f.AirportCodeOfArrival,f.DepartureDateTime,f.ArrivalDateTime from PassengerDetails P,FlightDetails F where P.FlightID = F.FlightID and p.PassId={}".format(fid)
        cursor.execute(query)
        dat=cursor.fetchall()
        h=['PassID','FlightID','PlaneID','Name','AirlineName','Class','Departure','Arrival','Departure D&T','Arrival D&T']
        data=tabulate(dat,headers=h,tablefmt="fancy_grid")
        print('\n')
        print(data)
        print('\n')
        pass_det()
    else:
        print("\nError!! Unable to fetch data\n")
        pass_det()
    
    

ch()
