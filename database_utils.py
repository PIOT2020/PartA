import MySQLdb
import MySQLdb.cursors
from datetime import date


#Handles the SQL queries needed for each API request.
class DatabaseUtils:
    HOST = "35.244.78.82"
    USER = "root"
    PASSWORD = 'z.s?5[BD3)"WaHDd'
    DATABASE = "CarShare"

    def __init__(self, connection = None):
        if(connection == None):
            connection = MySQLdb.connect(DatabaseUtils.HOST, DatabaseUtils.USER,
                DatabaseUtils.PASSWORD, DatabaseUtils.DATABASE)
        self.connection = connection

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def checkBooking(self,prams):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from bookings where userid = %s && carid = %s && status = 'active'", ([prams[2]],[prams[3]]))
            return cursor.fetchone()[0] >= 1

    def returnCar(self,prams):
        with self.connection.cursor() as cursor:
            cursor.execute("Update bookings set status = 'completed' where userid = %s && carid = %s && status = 'active'", ([prams[2]],[prams[3]]))
            cursor.execute("Update cars set available = 1 where carid = %s", [prams[3]])
            self.connection.commit()
        return True

    def findBooking(self,prams):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from bookings where userid = %s && carid = %s && status = 'active'", ([prams[2]],[prams[3]]))
            return cursor.fetchone()[0] >= 1

    def registerUser(self,prams):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into users (type,username,password,firstname,lastname, email) values (%s,%s,%s,%s,%s,%s)", 
            (prams[0],prams[1],prams[2],prams[3],prams[4],prams[5]))
            self.connection.commit()
        return cursor.rowcount == 1

    def getUser2(self,prams):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from users where username = %s", ([prams[0]]))
            return cursor.fetchone()[0] >= 1
    
    def getUser(self,prams):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from users where username = %s && password = %s", (prams[0],prams[1]))
            return cursor.fetchone()[0] >= 1

    def getUserID(self,prams):
        with self.connection.cursor() as cursor:
            cursor.execute("select userid from users where username = %s && password = %s", (prams[0],prams[1]))
            return str(cursor.fetchone()[0])

    def getUserID2(self,prams):
        with self.connection.cursor() as cursor:
            cursor.execute("select userid from users where username = %s", ([prams[0]]))
            return str(cursor.fetchone()[0])

    def addVehicle(self,prams):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into cars (make,bodytype,colour,seats,cost,available,latitude,longitude) values (%s,%s,%s,%s,%s,%s,%s,%s)", 
            (prams[0],prams[1],prams[2],prams[3],prams[4],prams[5],prams[6],prams[7]))
            self.connection.commit()
        return cursor.rowcount == 1

    def availableVehicles(self):
        with self.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("select * from cars where available = 1")
            return cursor.fetchall()

    def getVehicle(self,prams):
        with self.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("select * from cars where carid = %s",prams[0])
            return cursor.fetchall()

    def bookVehicle(self,prams):
        with self.connection.cursor() as cursor:
            cursor.execute("Update cars set available = 0 where carid = %s",[prams[3]])
            cursor.execute("insert into bookings (userid,carid,status,date) values (%s,%s,%s,%s)", 
            (prams[2],prams[3],"active",date.today()))
            self.connection.commit()
        #To Do: Validation Check
        return "Successful"

    def bookingHistory(self,prams):
        with self.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("select * from bookings where userid = %s",[prams])
            return cursor.fetchall()

    def cancelBooking(self,prams):
        with self.connection.cursor() as cursor:
            cursor.execute("select carid from bookings where bookingid = %s",[prams[2]])
            carid = str(cursor.fetchone()[0])
            cursor.execute("Update cars set available = 1 where carid = %s", [carid])
            cursor.execute("Update bookings set status = 'cancelled' where bookingid = %s",[prams[2]])
            self.connection.commit()
        #To Do: Validation Check
        return "Successful"

    def createDatabase(self):
        print("testingggggg")
        with self.connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE if not exists users (
                    userid    bigint NOT NULL AUTO_INCREMENT ,
                    type      varchar(45) NOT NULL ,
                    username  varchar(45) NOT NULL ,
                    password  char(64) NOT NULL ,
                    firstname varchar(45) NOT NULL ,
                    lastname  varchar(45) NOT NULL ,
                    email     varchar(320) NOT NULL ,
                    PRIMARY KEY (userid)
                )""")
            cursor.execute("""
                CREATE TABLE if not exists cars (
                    carid     bigint NOT NULL ,
                    make      varchar(45) NOT NULL ,
                    bodytype  varchar(45) NOT NULL ,
                    colour    varchar(45) NOT NULL ,
                    seats     smallint NOT NULL ,
                    latitude  decimal(10,8) NULL ,
                    longitude decimal(11,8) NULL ,
                    cost      smallint NOT NULL ,
                    available tinyint(1) NOT NULL ,
                    PRIMARY KEY (carid)
                )""")
            cursor.execute("""
                CREATE TABLE if not exists bookings (
                    bookingid bigint NOT NULL AUTO_INCREMENT ,
                    userid bigint NOT NULL ,
                    carid  bigint NOT NULL ,
                    status varchar(45) NOT NULL ,
                    date date NOT NULL ,
                    PRIMARY KEY (bookingid),
                    KEY fkIdx_23 (userid),
                    CONSTRAINT FK_23 FOREIGN KEY fkIdx_23 (userid) REFERENCES users (userid),
                    KEY fkIdx_27 (carid),
                    CONSTRAINT FK_27 FOREIGN KEY fkIdx_27 (carid) REFERENCES cars (carid)
                )""")
        self.connection.commit()