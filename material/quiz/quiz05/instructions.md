# SD212 Quiz 05: Counting Unauthorized Web Accesses

## Scenario

You are running a website and want to access the "server logs" to know
how many times code 401 appears, which indicates an attempt to load an
unauthorized page.

## The data

You have a file `access.log` which contains lines like this:

    192.168.1.99 - - [05/Feb/2026:12:00:00] "GET /downloads/internet-backup.zip HTTP/1.1" 200 9690
    10.0.0.45 - - [05/Feb/2026:12:00:40] "GET /cat-memes-collection-2026.zip HTTP/1.1" 404 18972
    172.16.0.5 - - [05/Feb/2026:12:00:44] "POST /middle-earth-tours/mordor/gate HTTP/1.1" 401 10116
    10.0.0.45 - - [05/Feb/2026:12:00:46] "GET /downloads/internet-backup.zip HTTP/1.1" 200 16091

These represent accesses to a web server, like the web servers
you made for your surveys in the previous lab.

Each line contains an IP address, a timestamp, an HTTP request, and then
the response code and the total file size transferred.

## Your task

Write a **bash script** in the file `unauth.sh` that prints out a single
number for the number lines in `access.log` with code 401.

You just write bash commands directly into the `unauth.sh` file, and
then you can test what you did by running

    bash unauth.sh

If it works, for the sample file given, it should just print out a
single line

    13

## Commands to submit

    club -csd212 -pquiz05 unauth.sh

    submit -c=sd212 -p=quiz05 unauth.sh
