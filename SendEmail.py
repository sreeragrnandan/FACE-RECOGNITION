import pymysql
import smtplib

while 1:
        connection = pymysql.connect(host="localhost",port=3307, user="root", passwd="", database="face_recognition")
        cursor = connection.cursor()

        # queries for retrievint observation made
        retriveID = "SELECT max(id) FROM contacts_contact;"
        #executing the quires
        cursor.execute(retriveID)
        Featched_id = cursor.fetchall()
        print(Featched_id[0][0])
        obsID = Featched_id[0][0]

        retriveMAIL = "SELECT contact_id FROM email WHERE id=(SELECT max(id) FROM email);"
        cursor.execute(retriveMAIL)
        Featched_email = cursor.fetchall()
        print(Featched_email[0][0])
        obsEmailId = Featched_email[0][0]

        if obsEmailId != obsID:
            # queries for retrievint observation made
            retriveNAME = "SELECT name FROM contacts_contact WHERE id=(SELECT max(id) FROM contacts_contact);"
            retriveCAM = "SELECT cam FROM contacts_contact WHERE id=(SELECT max(id) FROM contacts_contact);"
            #executing the quires
            cursor.execute(retriveNAME)

            Featched_name = cursor.fetchall()
            obsName = ','.join(map(','.join,Featched_name))
            cursor.execute(retriveCAM)
            Featched_cam = cursor.fetchall()
            cam = ','.join(map(','.join,Featched_cam))
            
            TO = 'recivers id'
            SUBJECT = 'CENTRAL MONITORING SYSTEM'
            TEXT =  obsName +' spoted at '+cam
            print(TEXT)
            # Gmail Sign In
            gmail_sender = 'your gmail address'
            gmail_passwd = 'your password'

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_sender, gmail_passwd)

            BODY = '\r\n'.join(['To: %s' % TO,
                                'From: %s' % gmail_sender,
                                'Subject: %s' % SUBJECT,
                                '', TEXT])

            try:
                server.sendmail(gmail_sender, [TO], BODY)
                print ('email sent')
            except:
                print ('error sending mail')

            server.quit()
            cursor.execute("INSERT INTO email (contact_id) VALUES( %s );",(obsID))

        else:
            print ('email already sent')
        connection.commit()
        connection.close()
