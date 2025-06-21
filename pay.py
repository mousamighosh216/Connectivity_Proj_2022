def p():
    try:
        import mysql.connector
        from tabulate import tabulate
    #cursor =db.cursor()
        db=mysql.connector.connect(host="localhost",user ="root", password="mou216",
                               database="mou")
        cursor=db.cursor()
        ps=int(input("Again Type your FlightID:"))
        p=int(input("Again Type your PassID:"))
        cursor.execute("select TicketPrice from FlightDetails F,PassengerDetails P where F.FlightID=P.FlightID and P.FlightID ={} and P.PassID = {} and P.Class='Economy' ".format(ps,p))
        results=cursor.fetchall()
        h=['Payable Amount']
        print(tabulate(results,headers=h,tablefmt="psql"))
    except:
        print("Error!! Unable to fetch data")

def q():
    try:
        import mysql.connector
        from tabulate import tabulate
        db=mysql.connector.connect(host="localhost",user ="root", password="mou216",
                                         database="mou")
        cursor=db.cursor()
        ps=int(input("Again Type your FlightID:"))
        p=int(input("Again Type your PassID:"))
        cursor.execute("select (TicketPrice+0.4*TicketPrice) from FlightDetails F,PassengerDetails P where F.FlightID=P.FlightID and P.FlightID ={} and P.PassID = {} and P.Class='First' ".format(ps,p))
        results=cursor.fetchall()
        h=['Payable Amount']
        print(tabulate(results,headers=h,tablefmt="psql"))
    except:
        print("Error!! Unable to fetch data")
    
def r():
    try:
        import mysql.connector
        from tabulate import tabulate
        db=mysql.connector.connect(host="localhost",user ="root", password="mou216",
                                         database="mou")
        cursor=db.cursor()
        ps=int(input("Again Type your FlightID:"))
        p=int(input("Again Type your PassID:"))
        cursor.execute("select (TicketPrice+0.2*TicketPrice) from FlightDetails F,PassengerDetails P where F.FlightID=P.FlightID and P.FlightID ={} and P.PassID = {} and P.Class='Business' ".format(ps,p))
        results=cursor.fetchall()
        h=['Payable Amount']
        print(tabulate(results,headers=h,tablefmt="psql"))
    except:
        print("Error!! Unable to fetch data")

