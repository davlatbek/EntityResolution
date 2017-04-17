import mysql.connector
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

cnx = mysql.connector.connect(user='root', password='1',
                              host='127.0.0.1',
                              database='er')

print(cnx.is_connected())
cursor = cnx.cursor()

flickr = open('../data/flickrdata.txt', 'w')
query = ("SELECT id, name, location, hometown, gender, status, occupation, links, connections, aboutme FROM multiple_flickr ")
cursor.execute(query)

for (id, name, location, hometown, gender, status,
     occupation, links, connections, aboutme) in cursor:

    name = name if name != "" else "-"
    location = location if location != "" else "-"
    hometown = hometown if hometown != "" else "-"
    gender = gender if gender != "" else "-"
    status = status if status != "" else "-"
    occupation = occupation if occupation != "" else "-"
    links = links if links != "" else "-"
    connections = connections if connections != "" else "-"
    aboutme = aboutme if aboutme != "" else "-"
    flickr.write(id + "%"
                 + name + "%"
                 + location + "%"
                 + hometown + "%"
                 + gender + "%"
                 + status + "%"
                 + occupation + "%"
                 + links + "%"
                 + connections + "%"
                 + aboutme + "\n")

myspace = open('../data/myspacedata.txt', 'w')
query = ("SELECT id, name, hometown, hometown, gender, status, occupation, links, connections, aboutme FROM multiple_myspace ")
cursor.execute(query)

for (id, name, hometown, hometown, gender, status, occupation, links, connections, aboutme) in cursor:

    name = name if name != "" else "-"
    location = location if location != "" else "-"
    hometown = hometown if hometown != "" else "-"
    gender = gender if gender != "" else "-"
    status = status if status != "" else "-"
    occupation = occupation if occupation != "" else "-"
    links = links if links != "" else "-"
    connections = connections if connections != "" else "-"
    aboutme = aboutme if aboutme != "" else "-"
    myspace.write(id + "%"
                  + name + "%"
                  + hometown + "%"
                  + hometown + "%"
                  + gender + "%"
                  + status + "%"
                  + occupation + "%"
                  + links + "%"
                  + connections + "%"
                  + aboutme + "\n")