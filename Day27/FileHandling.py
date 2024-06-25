"""
File handling:
 f=open(filename, mode)
 where mode is RAWX >
 where R- read
       A- append
       W- write
       X- Delete

       read: is the read the date from the file
       f = open(filename, "rt")
       print(f.read())


      write is write the data on previous date
       ex: hi write abc output: abc
       f = open(filename, "wt")
       f.write("hi")  #hi

       append is write the data next to previous data
       ex: hi  append abc output: hiabc
       f = open(filename, "at")
       f.write(" abc") #hi abc


      write is write the data on previous date
       ex: hi write abc output: abc
       f = open(filename, "wt")
       f.write("saichand")  NO#hiabc  output: saichand

       X- Delete the file
       import OS
       f.remove("filename")

     f.close

"""