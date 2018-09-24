#!C:/Python34/python.exe
print("Content-Type: text/html")

print("""
  """)
print("<html>");
print("<form action='resultstd.py'>");
print("<table>")
print("<caption><b><i>Data Entry Form</i></b></caption>")
print("<tr><td><b><i>Student Name:</i></b></td><td><input type='text' name='sn'></td></tr>");

print("<tr><td><b><i>Physics:</i></b></td><td><input type='text' name='p'></td></tr>");

print("<tr><td><b><i>Chemistry:</i></b></td><td><input type='text' name='c'></td></tr>");

print("<tr><td><b><i>Math:</i></b></td><td><input type='text' name='m'></td></tr>");


print("</table>");
print("<input type='submit'></form>");

print("</html>");
  